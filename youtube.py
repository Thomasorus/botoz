import sys
import datetime
import json
import shutil
import subprocess

utils = __import__('utils')

# This function converts a youtube video to a mp3 file and creates the associated xml files


def video_to_show(show, video_url):

    print("🤖 Recovering the video's JSON file.")
    # Recover the json associated with the video
    utils.youtube_get_json(video_url)

    # Retrieve the needed informations from json
    with open("temp.info.json") as f:
        vid_data = json.load(f)
        ep_id = vid_data['id']
        ep_title = vid_data['title'].strip()
        ep_upload_date = vid_data['upload_date']

        show_date = utils.select_date_format(
            show["general"]["date_format"], ep_upload_date)

        path_date_id = show_date + "_" + ep_id
        path_episode_folder = show["general"]["name"] + "/" + path_date_id
        path_folder_file = show["general"]["name"] + \
            "/" + path_date_id + "/" + path_date_id

    print("🤖 This video title is " + ep_title + ".")
    print("🤖 This video date is " + show_date + ".")

    # Create needed folders if they don't exist
    utils.create_folder(show["general"]["name"])
    utils.create_folder(path_episode_folder)

    # Moving JSON to the show's folder
    print("🤖 Moving JSON file to " + path_episode_folder)
    shutil.move("temp.info.json", path_folder_file + ".json")

    print("🤖 Starting downloading your video.💖")
    # Download audio file directly from youtube inside the folder
    utils.download_audio(video_url, path_folder_file,
                         show["general"]["youtube-dl_quiet"])
    print("🤖 Download complete.")

    # Cleans the title to remove the last part and check if double quotes are used
    ep_title_shortened = ep_title.rsplit('|', 1)[0].replace('"', "'").strip()

    # Generates the FFMPEG command from the mp3 options
    ffmpeg_command = utils.get_ffmpeg_download_command(
        show["mp3"], path_folder_file, show["general"]["ffmpeg_quiet"])

    # Convert to mp3
    subprocess.run(ffmpeg_command, shell=True)

    # ffmpeg_meta = "ffmpeg -loglevel error -i " + podcast["episode"]["podcast_folder_file"] + \
    #     '_temp.mp3 -i sources/img.jpg -c copy -map 0 -map 1 -metadata title="' + \
    #     str(podcast["episode"]["short_title"]) + '" ' + \
    #     podcast["episode"]["podcast_folder_file"] + ".mp3"

    # subprocess.run(ffZmpeg_meta, shell=True)

    # NEXT : functions for adding image, metatag title, metatag chapters
    # NEXT : Fill in the item dictionnary and the channel dictionnary
    # NEXT : Create functions to generate item and channel
