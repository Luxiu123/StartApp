# -*- coding:utf-8 -*-
import os
import json
import subprocess
import time
import sys
import threading

# pyinstaller -F -i exe.ico --uac-admin start.py
def main():
    try:
        apps = []
        with open("./app-config.json", encoding="utf-8") as f:
            config = json.loads(f.read())
            apps = config["apps"]
        for app in apps:
            # "name": "qq",
            # "path": "",
            # "args": ""
            # "delay": 1000
            if "args" not in app:
                app["args"] = ""
            if "delay" not in app:
                app["delay"] = 0
            command = "{} {}".format(app["path"], app["args"])
            threading.Thread(
                target=start, args=(app["name"], command, app["delay"])
            ).start()
        print("over")
    except Exception as e:
        print(e)


def start(app_name: str, command: str, delay: int) -> None:
    begin_time = time.time() * 1000
    while time.time() * 1000 - begin_time < delay:
        time.sleep(0.1)
    try:
        subprocess.Popen(command)
        print(
            "['{}'] started on {}".format(
                app_name,
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            )
        )
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
