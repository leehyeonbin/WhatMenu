from venv import logger
from dotenv import load_dotenv
import requests
import os


def sendMessage():
    try:
        load_dotenv()
        slack_url = os.environ.get('PRESNAL_SLACK')
        print(slack_url)
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
        return requests.post(slack_url, headers=header, json=data)
        
    except Exception as e:
        logger.error("Slack Message 전송에 실패했습니다.")
        logger.error("에러 내용 : " + e.__str__)

        exit(0)