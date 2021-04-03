import subprocess
import time
import datetime
import os
import youtube_dl
import requests


def youtube_get_json(url):
    subprocess.run(
        "youtube-dl -q --skip-download --write-info-json -o temp.%\(ext\)s " + url, shell=True)


def create_xml_item(data, file):
    return


def check_folder():
    return


def create_folder(folder):
    if os.path.exists(folder):
        print("🤖 The folder for " + folder + " already exists.")
    else:
        print("🤖 Creating " + folder + " folder.")
        os.makedirs(folder)


def select_date_format(date_format, date):
    iso_date = datetime.datetime.strptime(date, '%Y%m%d')
    if date_format == "EU":
        return datetime.datetime.strftime(iso_date, '%d-%m-%Y')
    if date_format == "ISO":
        return datetime.datetime.strftime(iso_date, '%Y-%m-%d')


def download_audio(url, path, quiet):
    ydl_opts = {
        'format': 'bestaudio',
        'postprocessors': [
            {'key': 'FFmpegExtractAudio', 'preferredcodec': 'm4a'},
            {'key': 'FFmpegMetadata'},
        ],
        "outtmpl": path + ".%(ext)s",
        "quiet": quiet,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def get_ffmpeg_download_command(options, ffmpeg_quiet, input_file, output_file):
    frequency = " -ar " + options["frequency"] + " "

    if ffmpeg_quiet == True:
        loglevel = "-loglevel fatal -i "
    else:
        loglevel = "-loglevel info -i "

    if options["component"] == "stereo":
        component = "-ac 2 "
    elif options["component"] == "mono":
        component = "-ac 1 "

    if options["bitrate"] == "VBR":
        bitrate = "-c:a libmp3lame -qscale:a " + \
            options["VBR_quality"] + " "
    elif options["bitrate"] == "CBR":
        bitrate = "-b:a " + options["CBR_quality"] + "k "

    return "ffmpeg " + loglevel + input_file + frequency + component + bitrate + output_file


def get_ffmpeg_title_cmd(title, ffmpeg_quiet, input_file, output_file):
    if ffmpeg_quiet == True:
        loglevel = "-loglevel fatal -i "
    else:
        loglevel = "-loglevel info -i "
    return "ffmpeg " + loglevel + input_file + ' -c copy -metadata title="' + \
        title + '" ' + output_file


def get_ffmpeg_image_cmd(image_path, ffmpeg_quiet, input_file, output_file):
    if ffmpeg_quiet == True:
        loglevel = "-loglevel fatal -i "
    else:
        loglevel = "-loglevel info -i "
    return "ffmpeg " + loglevel + input_file + " -i " + image_path + " -c copy -map 0 -map 1 " + output_file


def get_duration(duration):
    ty_res = time.gmtime(duration)
    return time.strftime("%H:%M:%S", ty_res)


def get_pubdate(ep_upload_date, fixed_hour):
    iso_date = datetime.datetime.strptime(ep_upload_date, '%Y%m%d')

    if time.localtime().tm_isdst:
        return iso_date.strftime('%a, %d %b %Y ' + fixed_hour + ' +0200')
    else:
        return iso_date.strftime('%a, %d %b %Y ' + fixed_hour + ' +0100')


def get_last_build_Date(today):
    if time.localtime().tm_isdst:
        return today.strftime('%a, %d %b %Y %H:%M:%S +0200')
    else:
        return today.strftime('%a, %d %b %Y %H:%M:%S +0100')


def get_youtube_chapters(description):
    description_array = description.split("\n")
    is_chapter = False
    chapters = ""
    for line in description_array:
        if line != "":
            if "00:00" in line:
                is_chapter = True
            if "---" in line:
                is_chapter = False
            if is_chapter == True:
                chapters += "<li style ='text-align: justify;'> " + line + " </li>"
    return chapters


def get_full_xml(url, path):
    myfile = requests.get(url)
    open(path + "_LEGACY.xml", 'wb').write(myfile.content)
    return myfile.content


def get_episode_number(xml_content):
    all_episodes = xml_content.findall(
        r"<itunes:episode>([0-9]+)<\/itunes:episode>", str(xml_content))
    last_episode = int(str(all_episodes[0]))
    return last_episode + 1


def create_content(header, chapters, footer):
    return header + "\n" + chapters + "\n" + footer
