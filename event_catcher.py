from flask import Flask, request
from slackeventsapi import SlackEventAdapter
from slack import WebClient
import os

app = Flask("WhatToday")


slack_bot_token = os.getenv("PERSONAL_SLACK")
slack_event_adapter = SlackEventAdapter(slack_bot_token, endpoint="slack/events")

@slack_event_adapter.on("block_actions")
def handle_button_click(payload):
    event = payload.get("evnet")
    user_id = event.get("user")
    button_click = event.get("actions")[0]

    if button_click['action_id'] == 'previous_button':
        index_change = -1
    elif button_click['action_id'] == 'next_button':
        index_change = 1
    else:
        index_change = 0