import feedparser
import requests
from os.path import exists
import json
import subprocess
import ftplib
import sys

config_file = __import__('config')
youtube = __import__('youtube')

show_name = sys.argv[1]
show_config = config_file.podcasts[show_name]

print("Checking for new entries")
cache_path = "./cache_" + show_config["general"]["name"] +".json"
file_exists = exists(cache_path)

playlist_url = show_config["general"]["playlist_url"]
Feed = feedparser.parse(playlist_url)
entries = Feed.entries
reversed_entries = Feed.entries[::-1]

differences = False

links = []
for entry in entries:
    links.append(entry.link)

reversed_links = []
for entry in reversed_entries:
    reversed_links.append(entry.link)

if file_exists is False:
    print('Cache does not exists')
    json_text = json.dumps(links)
    with open(cache_path, 'w') as f:
        f.write(json_text)
    file_exists = True

if file_exists is True:
    with open(cache_path, 'r') as f:
        json_list = json.loads(str(f.read()))
        json_list_reversed = json_list[::-1]
        if json_list_reversed == reversed_links:
            print("No changes since last try")
        else:
            first_set = set(json_list)
            sec_set = set(reversed_links)
            differences = (first_set - sec_set).union(sec_set - first_set)
            print("New links : " + str(differences))


if differences:
    for entry in differences:
        #nsubprocess.run("python3 botoz3000.py yt-mp3 matinale " + entry, shell=True)
        youtube.video_to_show(show_config, entry)
        path = show_config["item"]["guid"] + "_" + show_config["item"]["ep_id"]
        mp3 = show_config["general"]["name"] + "/" + path + "/" + show_config["item"]["guid"] + ".mp3"
        previous_xml = show_config["general"]["name"] + "/" + path + "/" + show_config["general"]["xml_file_name"] + "-previous.xml"
        new_xml = show_config["general"]["name"] + "/" + path + "/" + show_config["general"]["xml_file_name"] + ".xml"

        server = ftplib.FTP()
        server.connect(show_config["general"]["ftp_url"])
        server.login(show_config["general"]["ftp_login"],show_config["general"]["ftp_password"])
        server.storbinary("STOR " + "/" + show_config["general"]["ftp_folder"] + "/" + show_config["item"]["guid"] + ".mp3", open(mp3, 'rb'))
        server.storlines("STOR " + "/" + show_config["general"]["ftp_folder"] + "/" + show_config["general"]["xml_file_name"] + "-previous.xml", open(previous_xml, 'rb'))
        server.storlines("STOR " + "/" + show_config["general"]["ftp_folder"] + "/" + show_config["general"]["xml_file_name"] + ".xml", open(new_xml, 'rb'))
        server.close()

        json_text = json.dumps(links)
        with open(cache_path, 'w') as f:
            f.write(json_text)

