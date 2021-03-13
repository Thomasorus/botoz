import sys
import subprocess
import random
import json
import os
import shutil
import datetime
import time
import shutil
import requests
import re

upload_date = ""
podcast_title = ""
podcast_date = ""
podcast_euro_date = ""
podcast_name = ""

# Recover the json associated with the video
subprocess.run("youtube-dl -q --skip-download --write-info-json -o temp.%\(ext\)s " +
               str(sys.argv[1]), shell=True)

# Open Json, create folder with the video upload date and move the file inside
read_content = open("temp.info.json", "r")
vid_data = json.load(read_content)
upload_date = vid_data['upload_date']
podcast_title = vid_data['title']
podcast_date = datetime.datetime.strptime(upload_date, '%Y%m%d')
podcast_euro_date = podcast_date.strftime('%d-%m-%Y')
podcast_name = podcast_euro_date + "/" + podcast_euro_date
if os.path.exists(podcast_euro_date):
    shutil.rmtree(podcast_euro_date)
    os.makedirs(podcast_euro_date)
else:
    os.makedirs(podcast_euro_date)
shutil.move("temp.info.json", podcast_name + ".json")


# Download audio file directly from youtube inside the folder
youtube_download_command = "youtube-dl -q --extract-audio --audio-quality 0 -o " + \
    podcast_name.replace('"', "'") + ".%\(ext\)s " + str(sys.argv[1])
subprocess.run(youtube_download_command, shell=True)

# Cleans the title to remove the last part and check if double quotes are used
podcast_title_cleaned = podcast_title.rsplit('|', 1)
podcast_title_cleaned = podcast_title_cleaned[0].replace(
    '"', "'")

# Encode audio file to mp3
ffmpeg_encoding = "ffmpeg -i " + podcast_name + \
    ".m4a -ar 44100 -ac 2 -b:a 128k " + podcast_name + "_temp.mp3"
subprocess.run(ffmpeg_encoding, shell=True)

# Add image and title in metatags
ffmpeg_meta = "ffmpeg -i " + podcast_name + \
    '_temp.mp3 -i sources/img.jpg -c copy -map 0 -map 1 -metadata title="' + \
    str(podcast_title_cleaned) + '" ' + podcast_name + ".mp3"
subprocess.run(ffmpeg_meta, shell=True)

# Remove old audio files
os.remove(podcast_name + ".m4a")
os.remove(podcast_name + "_temp.mp3")

# Copy xml file
shutil.copyfile('sources/item.xml', podcast_name + ".xml")

# Prepare all data needed for XML
if time.localtime().tm_isdst:
    pubdate = podcast_date.strftime('%a, %d %b %Y 09:00:00 +0200')
else:
    pubdate = podcast_date.strftime('%a, %d %b %Y 09:00:00 +0100')

ty_res = time.gmtime(vid_data["duration"])
duration = time.strftime("%H:%M:%S", ty_res)

description_array = vid_data["description"].split("\n")

is_sommaire = False
sommaire = ""
for line in description_array:
    if line != "":
        if "00:00" in line:
            is_sommaire = True
        if "---" in line:
            is_sommaire = False
        if is_sommaire == True:
            sommaire += "<li style ='text-align: justify;'> " + line + " </li>"


# Download and store full xml file
flux_url = "http://gautozf.cluster030.hosting.ovh.net/matinale-podcast/podcast_la-matinale-jv.xml"
myfile = requests.get(flux_url)
open(podcast_euro_date + "/podcast_la-matinale-jv-LEGACY.xml",
     'wb').write(myfile.content)

# Get last episode number
all_episodes = re.findall(
    r"<itunes:episode>([0-9]+)<\/itunes:episode>", str(myfile.content))
last_episode = int(str(all_episodes[0]))
episode = last_episode + 1

# Put data into xml file of the day and save it
with open(podcast_name + ".xml") as f:
    newText = f.read().replace('BOTOZ_TITLE', podcast_title_cleaned).replace('BOTOZ_VIDEO_LINK', vid_data["webpage_url"]).replace(
        'BOTOZ_DATE', podcast_euro_date).replace('BOTOZ_PUBDATE', pubdate).replace("BOTOZ_DURATION", duration).replace("BOTOZ_SOMMAIRE", sommaire).replace('BOTOZ_EPISODE', str(episode))

with open(podcast_name + ".xml", "w") as f:
    f.write(newText)


# Insert today's xml into the main xml
with open(podcast_euro_date + "/podcast_la-matinale-jv-LEGACY.xml") as f:
    full_xml = re.sub("\t<item>", newText + "\n\n\n\t<item>", str(f.read()), 1)

with open(podcast_euro_date + "/podcast_la-matinale-jv.xml", "w") as f:
    f.write(full_xml)

os.remove(podcast_name + ".json")
