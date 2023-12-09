from venv import logger
from dotenv import load_dotenv
from post import Post
import requests
import os

def send_message(posts: [Post]):
    index = 0

    load_dotenv()
    slack_url = os.getenv('PERSONAL_SLACK')
    header = {'Content-type': 'application/json'}
    icon_emoji = ":rice:"
    username = "WhatMenu"
    if(len(posts) > 0): 
        try:
            attachments = [{
                "color": "good",
                "author_name": posts[index].title,
                "image_url": posts[index].content,
                "actions": [
                    {
                        "action_id": "action_id",
                        "text": "이전으로",
                        "type": "button",
                        "value": "before"
                    },
                    {
                        "action_id": "next",
                        "text": "다음으로",
                        "type": "button",
                        "value": "next"
                    },
                ]
            }]

            data = {"username": username, "attachments": attachments, "icon_emoji": icon_emoji}
            print(data)

            # 메세지 전송
            return requests.post(slack_url, headers=header, json=data)
        
        except Exception as e:
            logger.error("Slack Message 전송에 실패했습니다.")
            logger.error("에러 내용 : " + e.__str__)

            exit(0)

    else:
        try:
            attachments = [{
                "color": "good",
                "text": "오늘은 공지가 없네요"
            }]

            data = {"username": username, "attachments": attachments, "icon_emoji": icon_emoji}
            print(data)

            # 메세지 전송
            return requests.post(slack_url, headers=header, json=data)
        
        except Exception as e:
            logger.error("Slack Message 전송에 실패했습니다.")
            logger.error("에러 내용 : " + e.__str__)

            exit(0)