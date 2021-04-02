import subprocess
import datetime
import os
import youtube_dl


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

    # def get_episode_number(xml):
    #     with open(podcast["episode"]["podcast_folder_file"] + ".xml") as f:
    #         all_episodes = re.findall(
    #             r"<itunes:episode>([0-9]+)<\/itunes:episode>", str(xml))
    #         last_episode = int(str(all_episodes[0]))
    #     return last_episode + 1
