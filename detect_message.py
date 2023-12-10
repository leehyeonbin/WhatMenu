from slack_sdk.rtm_v2 import RTMClient
from dotenv import load_dotenv
import ssl
import os

ssl._create_default_https_context = ssl._create_unverified_context

load_dotenv()
bot_id = os.getenv('BOT_ID')
rtm = RTMClient(token=bot_id)

@rtm.on("message")
def detect_message(client: RTMClient, event: dict):
    print(event['text'])
    if 'hello' in event['text']:
        channel_id = event['channel']
        thread_ts = event['ts']
        user = event['user']

        client.web_client.chat_postMessage(
            channel=channel_id,
            text="Let's go {}".foramt(user),
            thread_ts=thread_ts
        )

rtm.start()