import sys
import subprocess
import random
import json
import os
import shutil
import datetime
import shutil


upload_date = ""
podcast_title = ""
podcast_euro_date = ""
podcast_name = ""
# Recover the json associated with the video
subprocess.run("youtube-dl -q --skip-download --write-info-json -o temp.%\(ext\)s " +
               str(sys.argv[1]), shell=True)

# Open Json, create folder with the video upload date and move the file inside
with open("temp.info.json", "r") as read_content:
    data = json.load(read_content)
    upload_date = data['upload_date']
    podcast_title = data['title']
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
    ".opus -ar 44100 -ac 2 -b:a 128k " + podcast_name + "_temp.mp3"
subprocess.run(ffmpeg_encoding, shell=True)

# Add image and title in metatags
ffmpeg_meta = "ffmpeg -i " + podcast_name + \
    '_temp.mp3 -i sources/img.jpg -c copy -map 0 -map 1 -metadata title="' + \
    str(podcast_title_cleaned) + '" ' + podcast_name + ".mp3"
subprocess.run(ffmpeg_meta, shell=True)

# Remove old audio files
os.remove(podcast_name + ".opus")
os.remove(podcast_name + "_temo.mp3")

# Copy and opens xml file
