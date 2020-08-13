#  !/usr/bin/env python
#  -*- encoding: utf-8 -*-
#
#  Copyright (c) 2020 anqi.huang@outlook.com
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


import os
import time

import requests

import utils
from im.dingding import DingDing

userConfig = utils.readUserConfig()
user = userConfig["auth"]["user"]
pwd = userConfig["auth"]["pwd"]
access_token = userConfig["dingding"]["access_token"]
secret = userConfig["dingding"]["secret"]

message = "Welcome to the world of raspberry pi, device info = http://{ip}/pi-dashboard/\n" \
          "ad blocked = http://{ad}/admin/\n"

host = "http://1.1.1.3"
endpoint = "/ac_portal/login.php"
url = ''.join([host, endpoint])
body = {
    "opr": "pwdLogin",
    "userName": "********",
    "pwd": "********",
    "rememberPwd": 1
}

if __name__ == '__main__':
    try:
        result = os.popen("iwgetid -r").readlines()[0].strip()
        print(result)
        if 'bskj-sh' == result:
            print("has connected bskj-sh wifi, need login user account")
            data = dict()
            data['opr'] = 'pwdLogin'
            data['rememberPwd'] = 1
            data['userName'] = user
            data['pwd'] = pwd
            r = requests.post(url, data)
            # r = requests.post(url, body)
            time.sleep(2)
    except:
        pass

    process = os.popen("hostname -I")
    outputs = process.readlines()
    for output in outputs:
        ip = output.strip()
        break

    print(ip)
    send_message = message.format(ip=ip, ad=ip)
    process.close()

    ding = DingDing(access_token)
    ding.set_secret(secret)
    ding.send_text(send_message)
