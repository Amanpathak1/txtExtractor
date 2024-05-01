#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6863049418:AAHru5Bk-_6fIUAskKxURQdinYt8y31usUg")
    API_ID = int(os.environ.get("API_ID", "27184026"))
    API_HASH = os.environ.get("API_HASH", "4c26e2cb6c6d9d57841b3c5ab6bb7605")
    AUTH_USERS = os.environ.get("AUTH_USERS", "7183515722")
