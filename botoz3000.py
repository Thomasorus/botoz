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
elif command == "ch-xml":
    print("🤖 You want to generate an XML channel file from the config file.")
elif command == "yt-pl":
    print("🤖 You want to turn an entire youtube playlist to a podcast.")
else:
    print("🤖 Your command is not valid")

print("🤖 Everything is done.")
print("🤖 Have a nice day " + show_config["general"]["user_name"] + "!")


# print("🤖 Fixing the MP3 metatags.")
# # Add image and title in metatags
# ffmpeg_meta = "ffmpeg -loglevel error -i " + podcast["episode"]["podcast_folder_file"] + \
#     '_temp.mp3 -i sources/img.jpg -c copy -map 0 -map 1 -metadata title="' + \
#     str(podcast["episode"]["short_title"]) + '" ' + \
#     podcast["episode"]["podcast_folder_file"] + ".mp3"
# subprocess.run(ffZmpeg_meta, shell=True)

print("🤖 Cleaning old files.")
# Remove old audio files
# os.remove(podcast["episode"]["podcast_folder_file"] + ".opus")
# os.remove(podcast["episode"]["podcast_folder_file"] + "_temp.mp3")

# Copy xml file
# shutil.copyfile('sources/item.xml',
#                 podcast["episode"]["podcast_folder_file"] + ".xml")

# # Prepare all data needed for XML
# today = datetime.datetime.today()
# if time.localtime().tm_isdst:
#     pubdate = podcast["episode"]["upload_date"].strftime(
#         '%a, %d %b %Y 09:00:00 +0200')
#     lastBuildDate = today.strftime('%a, %d %b %Y %H:%M:%S +0200')
# else:
#     pubdate = podcast["episode"]["upload_date"].strftime(
#         '%a, %d %b %Y 09:00:00 +0100')
#     lastBuildDate = today.strftime('%a, %d %b %Y %H:%M:%S +0100')

# ty_res = time.gmtime(vid_data["duration"])
# duration = time.strftime("%H:%M:%S", ty_res)

# description_array = vid_data["description"].split("\n")

# is_sommaire = False
# sommaire = ""
# for line in description_array:
#     if line != "":
#         if "00:00" in line:
#             is_sommaire = True
#         if "---" in line:
#             is_sommaire = False
#         if is_sommaire == True:
#             sommaire += "<li style ='text-align: justify;'> " + line + " </li>"


# print("🤖 Generating the XML file.")

# Download and store full xml file
podcast["item"]["main_xml_url"] = get_full_xml(podcast)

# Get episode
podcast["item"]["itunes_episode"] = get_episode_number(
    podcast["item"]["main_xml_url"])

print(podcast["item"]["itunes_episode"])

# Put data into xml file of the day and save it
with open(podcast["episode"]["podcast_folder_file"] + ".xml") as f:
    newText = f.read().replace('BOTOZ_TITLE', podcast_title_cleaned).replace('BOTOZ_FULL_TITLE', podcast_title).replace('BOTOZ_VIDEO_LINK', vid_data["webpage_url"]).replace(
        'BOTOZ_DATE', podcast_euro_date).replace('BOTOZ_PUBDATE', pubdate).replace("BOTOZ_DURATION", duration).replace("BOTOZ_SOMMAIRE", sommaire).replace('BOTOZ_EPISODE', str(episode))

with open(podcast_name + ".xml", "w") as f:
    f.write(newText)

# Insert today's xml into the main xml
with open(podcast_euro_date + "/podcast_la-matinale-jv-LEGACY.xml") as f:
    full_xml = re.sub("</itunes:explicit>",
                      "</itunes:explicit>\n\n\n" + newText + "\n", str(f.read()), 1)
    full_xml = re.sub("<lastBuildDate>.+<\/lastBuildDate>",
                      "<lastBuildDate>" + lastBuildDate + "</lastBuildDate>", full_xml, 1)

with open(podcast_euro_date + "/podcast_la-matinale-jv.xml", "w") as f:
    f.write(full_xml)

print("🤖 XML files created.")

os.remove(podcast_name + ".json")

print("🤖 Cleaned the old JSON.")


def fill_item(podcast):
    podcast[item]["title"] = podcast[episode]["short_title"]
    podcast[item]["link"] = podcast["episode"]["video_url"]
    podcast[item]["guid"] = podcast["episode"]["euro_date"]
    podcast[item]["pub_date"] = podcast["episode"]["video_url"]
    # TODO : Function to retrieve episodes
    podcast[item]["itunes_episode"] = ""
    podcast[item]["itunes_duration"] = ""
    podcast[item]["itunes_subtitle"] = podcast[episode]["title"]
    podcast[item]["itunes_description"] = podcast[episode]["title"]
    podcast[item]["content_encoded_timestamps"] = ""
    return podcast


def get_full_xml(podcast):
    myfile = requests.get(podcast["general"]["main_xml_url"])
    open(podcast["episode"]["podcast_folder"] +
         "/" + podcast["episode"]["podcast_folder"] + "_LEGACY.xml", 'wb').write(myfile.content)
    return myfile.content
