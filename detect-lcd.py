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
import subprocess
import re
import time

import lcd.LCD1602 as LCD

p = subprocess.Popen(['i2cdetect', '-y', '1'], stdout=subprocess.PIPE)

for i in range(0, 9):
    line = str(p.stdout.readline())

    for match in re.finditer("[0-9][0-9]:.*[0-9][0-9]", line):
        print(match.group())
        LCD.init_lcd()
        process = os.popen("hostname -I")
        outputs = process.readlines()
        for output in outputs:
            ip = output.strip()
            break

        time.sleep(1)
        LCD.turn_light(1)
        LCD.print_lcd(2, 0, ip)

        now = time.strftime('%m/%d %H:%M:%S', time.localtime(time.time()))
        LCD.print_lcd(1, 1, now)
