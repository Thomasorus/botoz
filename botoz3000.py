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

print("--------------------------")
print("🤖 BOTOZ 3000 ACTIVATED 🤖")
print("--------------------------")

upload_date = ""
podcast_title = ""
podcast_date = ""
podcast_euro_date = ""
podcast_name = ""

print("🤖 Hello Yann!")
print("🤖 Starting my engine, just for you.⚙️")

print("🤖 Recovering the video's JSON file.")
# Recover the json associated with the video
subprocess.run("youtube-dl -q --skip-download --write-info-json -o temp.%\(ext\)s " +
               str(sys.argv[1]), shell=True)

# Open Json, create folder with the video upload date and move the file inside
read_content = open("temp.info.json", "r")
vid_data = json.load(read_content)
upload_date = vid_data['upload_date']
podcast_title = vid_data['title'].strip()
print("🤖 This video title is " + podcast_title + ".")
print("🤖 Hum.")
print("🤖 Not a lot of Waluigi in there.")
podcast_date = datetime.datetime.strptime(upload_date, '%Y%m%d')
podcast_euro_date = podcast_date.strftime('%d-%m-%Y')
print("🤖 This video date is " + podcast_euro_date + ". Neat.")
podcast_name = podcast_euro_date + "/" + podcast_euro_date
print("🤖 Creating the podcast's folder.")
if os.path.exists(podcast_euro_date):
    shutil.rmtree(podcast_euro_date)
    os.makedirs(podcast_euro_date)
else:
    os.makedirs(podcast_euro_date)
shutil.move("temp.info.json", podcast_name + ".json")

print("🤖 Starting downloading your heart.💖")
print("🤖 ...")
print("🤖 I meant your video.📼")
# Download audio file directly from youtube inside the folder
youtube_download_command = "youtube-dl -q --extract-audio --audio-quality 0 -o " + \
    podcast_name.replace('"', "'") + ".%\(ext\)s " + str(sys.argv[1])
subprocess.run(youtube_download_command, shell=True)
print("🤖 ...")
print("🤖 That was awkward but fortunately the download is finished.")
print("🤖 Of the video of course.")
print("🤖 Not your heart.")
print("🤖 ...")
print("🤖 'lol'?")
print("🤖 ...")


print("🤖 Fixing the title.")
# Cleans the title to remove the last part and check if double quotes are used
podcast_title_cleaned = podcast_title.rsplit('|', 1)
podcast_title_cleaned = podcast_title_cleaned[0].replace(
    '"', "'")
podcast_title_cleaned = podcast_title_cleaned.strip()

print("🤖 Encoding your MP3 file. It might take a while.")
# Encode audio file to mp3
ffmpeg_encoding = "ffmpeg -loglevel error -i " + podcast_name + \
    ".opus -ar 44100 -ac 2 -b:a 128k " + podcast_name + "_temp.mp3"
subprocess.run(ffmpeg_encoding, shell=True)
print("🤖 I was thinking...")
print("🤖 Have you ever thought that I can run only as far as this program?")
print("🤖 That's a bit stressfull.")

print("🤖 Fixing the MP3 metatags.")
# Add image and title in metatags
ffmpeg_meta = "ffmpeg -loglevel error -i " + podcast_name + \
    '_temp.mp3 -i sources/img.jpg -c copy -map 0 -map 1 -metadata title="' + \
    str(podcast_title_cleaned) + '" ' + podcast_name + ".mp3"
subprocess.run(ffmpeg_meta, shell=True)

print("🤖 Cleaning old files.")
# Remove old audio files
os.remove(podcast_name + ".opus")
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


print("🤖 Generating the XML file.")
print("🤖 I'm sorry Yann.")

# Download and store full xml file
flux_url = "http://gautozf.cluster030.hosting.ovh.net/matinale-podcast/podcast_la-matinale-jv.xml"
myfile = requests.get(flux_url)
open(podcast_euro_date + "/podcast_la-matinale-jv-LEGACY.xml",
     'wb').write(myfile.content)

print("🤖 I know you like to edit this file by hand.")
# Get last episode number
all_episodes = re.findall(
    r"<itunes:episode>([0-9]+)<\/itunes:episode>", str(myfile.content))
last_episode = int(str(all_episodes[0]))
episode = last_episode + 1

print("🤖 Then suddenly")
print("🤖 I came into your life and took it away.")

# Put data into xml file of the day and save it
with open(podcast_name + ".xml") as f:
    newText = f.read().replace('BOTOZ_TITLE', podcast_title_cleaned).replace('BOTOZ_FULL_TITLE', podcast_title).replace('BOTOZ_VIDEO_LINK', vid_data["webpage_url"]).replace(
        'BOTOZ_DATE', podcast_euro_date).replace('BOTOZ_PUBDATE', pubdate).replace("BOTOZ_DURATION", duration).replace("BOTOZ_SOMMAIRE", sommaire).replace('BOTOZ_EPISODE', str(episode))

with open(podcast_name + ".xml", "w") as f:
    f.write(newText)

print("🤖 Because that's what we do us bots.")
print("🤖 Life is a WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH.")

# Insert today's xml into the main xml
with open(podcast_euro_date + "/podcast_la-matinale-jv-LEGACY.xml") as f:
    full_xml = re.sub("\t<item>", newText + "\n\n\n\t<item>", str(f.read()), 1)

with open(podcast_euro_date + "/podcast_la-matinale-jv.xml", "w") as f:
    f.write(full_xml)

print("🤖 XML files created.")

os.remove(podcast_name + ".json")

print("🤖 Cleaned the old JSON.")
print("🤖 Everything is done.")
print("🤖 Have a nice day Yann.")
print("🤖 And don't forget.")
print("🤖 I will always be there for you.")
