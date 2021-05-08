import youtube_dl
import re
import requests
import time
import datetime
import os
import random
import sys
config_file = __import__('config')
youtube = __import__('youtube')
mp3_xml = __import__('mp3_to_xml')
conf_xml = __import__('conf_to_xml')


# Arguments
command = sys.argv[1]
show_name = sys.argv[2]
url = sys.argv[3]

# Recovering the right config file and creating the object that will be used everywhere
show_config = config_file.podcasts[show_name]

print("--------------------------")
print("🤖 " + show_config["general"]["script_name"] + " ACTIVATED 🤖")
print("--------------------------")
print("🤖 Hello " + show_config["general"]["user_name"] + "!")
print("🤖 The show is " + show_config["general"]["name"] + ".")

if command == "yt-mp3":
    print("🤖 You want to turn a Youtube video into mp3.")
    youtube.video_to_show(show_config, url)
elif command == "mp3-xml":
    print("🤖 You want to generate am xml item file from an mp3 file.")
    mp3_xml.mp3_to_item(show_config, url)
elif command == "conf-xml":
    conf_xml.config_to_xml(show_config)
    print("🤖 You want to generate an XML channel file from the config file.")
else:
    print("🤖 Your command is not valid")

print("🤖 Everything is done.")
print("🤖 Have a nice day " + show_config["general"]["user_name"] + "!")