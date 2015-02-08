#coding:utf-8
from email.mine.text import MINEText

msg = MINEText('hello, send by Python...', 'plain', 'utf-8')

from_addr = raw_input('From: ') # 输入Email地址和口令
password = raw_input('Password: ')
smtp_server = raw_input('SMTP server: ') # 输入SMTP服务器地址
to_addr = raw_input('To: ') # 输入收件人地址

'''
import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
'''
