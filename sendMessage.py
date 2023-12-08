from venv import logger
import requests


def sendMessage():
    try:
        url = secrets.PERSNAL_SLACK
        header = {'Content-type': 'application/json'}
        icon_emoji = ":slack:"
        username = "WhatMenu"
        attachments = [{
            "color": "good",
            "text": "😎😎😎\n TEST Message 전송"
        }]

        data = {"username": username, "attachments": attachments, "icon_emoji": icon_emoji}
        print(data)

        # 메세지 전송
        return requests.post(url, headers=header, json=data)
        
    except Exception as e:
        logger.error("Slack Message 전송에 실패했습니다.")
        logger.error("에러 내용 : " + e)

        exit(0)