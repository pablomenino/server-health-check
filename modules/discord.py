#!/usr/bin/env python3

#----------------------------------------------------------------------------------------
# server-health-check
# Version: 0.1
# 
# WebSite:
# https://github.com/pablomenino/server-health-check/
# 
# Copyright © 2017 - Pablo Meniño <pablo.menino@gmail.com>
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
# Include modules
import json
import time
import datetime
from collections import defaultdict
import requests

#----------------------------------------------------------------------------------------
# Include modules

class discord_webhook:
    def __init__(self, url, **kwargs):
        # Initialise a Webhook Embed Object
        self.url = url
        self.msg = kwargs.get('msg')
        self.color = kwargs.get('color')
        self.title = kwargs.get('title')
        self.title_url = kwargs.get('title_url')
        self.author = kwargs.get('author')
        self.author_icon = kwargs.get('author_icon')
        self.author_url = kwargs.get('author_url')
        self.desc = kwargs.get('desc')
        self.fields = kwargs.get('fields', [])
        self.image = kwargs.get('image')
        self.thumbnail = kwargs.get('thumbnail')
        self.footer = kwargs.get('footer')
        self.footer_icon = kwargs.get('footer_icon')
        self.timestamp = kwargs.get('timestamp')

    def add_field(self, **kwargs):
        # Adds a field to self.fields
        name = kwargs.get('name')
        value = kwargs.get('value')
        inline = kwargs.get('inline', True)
        field = {
            'name' : name,
            'value' : value,
            'inline' : inline
        }
        self.fields.append(field)

    def set_desc(self, desc):
        self.desc = desc

    def set_color(self, color):
        if color == "red":
            self.color = 16711680
        elif color == "yellow":
            self.color = 16776960
        elif color == "blue":
            self.color = 255
        elif color == "green":
            self.color = 65280
        else:
            self.color = color

    def set_title(self, **kwargs):
        self.title = kwargs.get('title')
        self.title_url = kwargs.get('url')

    def set_thumbnail(self, url):
        self.thumbnail = url

    def set_image(self, url):
        self.image = url

    def set_footer(self, **kwargs):
        self.footer = kwargs.get('text')
        self.footer_icon = kwargs.get('icon')
        timestamp = kwargs.get('timestamp')
        if timestamp:
            self.timestamp = str(datetime.datetime.utcfromtimestamp(time.time()))
        else:
            self.timestamp = ""

    def del_field(self, index):
        self.fields.pop(index)

    @property
    def json(self):
        # Formats the data into a payload
        data = {}
        data["embeds"] = []
        embed = defaultdict(dict)
        if self.msg:
            data["content"] = self.msg
        if self.color:
            embed["color"] = self.color
        if self.desc:
            embed["description"] = self.desc
        if self.title:
            embed["title"] = self.title
        if self.title_url:
            embed["url"] = self.title_url
        if self.image:
            embed["image"]['url'] = self.image
        if self.thumbnail:
            embed["thumbnail"]['url'] = self.thumbnail
        if self.footer:
            embed["footer"]['text'] = self.footer
        if self.footer_icon:
            embed['footer']['icon_url'] = self.footer_icon
        if self.timestamp:
            embed["timestamp"] = self.timestamp

        if self.fields:
            embed["fields"] = []
            for field in self.fields:
                field_tmp = {}
                field_tmp["name"] = field['name']
                field_tmp["value"] = field['value']
                field_tmp["inline"] = field['inline']
                embed["fields"].append(field_tmp)

        data["embeds"].append(dict(embed))

        empty = all(not d for d in data["embeds"])

        if empty and 'content' not in data:
            print('You cant post an empty payload.')
        if empty:
            data['embeds'] = []

        return json.dumps(data, indent=4)

    def post(self):
        # Send the JSON formated object to the specified `self.url`.
        headers = {'Content-Type': 'application/json'}
        result = requests.post(self.url, data=self.json, headers=headers)
        print(self.json);
        if result.status_code == 400:
            print("Post Failed, Error 400")
        else:
            print("Message delivered successfuly.");
            print("Result code: "+str(result.status_code));
