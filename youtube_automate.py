import feedparser
import requests
from os.path import exists
import json
import subprocess
import ftplib
import sys
import shutil
import pysftp

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
new_entry = None

# For dev purposes only
# with open("feed.xml", 'r') as f:
#     Feed = feedparser.parse(str(f.read()))
#     entries = Feed.entries

differences = False

links = []
for entry in entries:
    links.append(entry.link)

if file_exists is False:
    print('Cache does not exists')
    json_text = json.dumps(links)
    with open(cache_path, 'w') as f:
        f.write(json_text)
    file_exists = True

if file_exists is True:
    with open(cache_path, 'r') as f:
        json_list = json.loads(str(f.read()))
        json_list = json_list
        if json_list[0] == links[0]:
            print("No changes since last try")
        else:
            new_entry = links[0]
            print("New links : " + str(entry))


if new_entry is not None:
    #subprocess.run("python3 botoz3000.py yt-mp3 matinale " + new_entry, shell=True)
    youtube.video_to_show(show_config, new_entry)
    path = show_config["item"]["guid"] + "_" + show_config["item"]["ep_id"]
    mp3 = show_config["general"]["name"] + "/" + path + "/" + show_config["item"]["guid"] + ".mp3"
    previous_xml = show_config["general"]["name"] + "/" + path + "/" + show_config["general"]["xml_file_name"] + "-previous.xml"
    new_xml = show_config["general"]["name"] + "/" + path + "/" + show_config["general"]["xml_file_name"] + ".xml"

    if show_config["general"]["connection_type"] == "FTP":
        server = ftplib.FTP()
        server.connect(show_config["general"]["ftp_url"])
        server.login(show_config["general"]["ftp_login"],show_config["general"]["ftp_password"])
        server.storbinary("STOR " + "/" + show_config["general"]["ftp_folder"] + "/" + show_config["item"]["guid"] + ".mp3", open(mp3, 'rb'))
        server.storlines("STOR " + "/" + show_config["general"]["ftp_folder"] + "/" + show_config["general"]["xml_file_name"] + "-previous.xml", open(previous_xml, 'rb'))
        server.storlines("STOR " + "/" + show_config["general"]["ftp_folder"] + "/" + show_config["general"]["xml_file_name"] + ".xml", open(new_xml, 'rb'))
        server.close()

    if show_config["general"]["connection_type"] == "SFTP":
        server = pysftp.Connection(host=show_config["general"]["sftp_url"],username=show_config["general"]["sftp_user"], password=show_config["general"]["sftp_password"])
        server.put("/" + show_config["general"]["sftp_folder"] + "/" + show_config["item"]["guid"] + ".mp3")
        server.put("/" + show_config["general"]["sftp_folder"] + "/" + show_config["general"]["xml_file_name"] + "-previous.xml")
        server.put("/" + show_config["general"]["sftp_folder"] + "/" + show_config["general"]["xml_file_name"] + ".xml")
        server.close()

    json_text = json.dumps(links)
    with open(cache_path, 'w') as f:
        f.write(json_text)

    try:
        shutil.rmtree("./" + show_name)
    except OSError as e:
        print("Error: %s : %s" % (show_name, e.strerror))

