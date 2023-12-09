from flask import Flask, request
from slackeventsapi import SlackEventAdapter

app = Flask("WhatToday")

slack_event_adapter = SlackEventAdapter()

@slack_event_adapter.on("block_actions")