import json
import datetime
import os

utils = __import__('utils')

def config_to_xml(show):
    utils.create_folder(show["general"]["name"])
    utils.create_channel_file(show, show["general"]["name"] + "/" + show["general"]["name"] + "_channel.xml")
