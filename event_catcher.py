from flask import Flask, request
from slackeventsapi import SlackEventAdapter

app = Flask("WhatToday")

slack_event_adapter = SlackEventAdapter()