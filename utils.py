import subprocess
import time
import datetime
import os
import yt_dlp
import requests
import re

def youtube_get_json(url):
    subprocess.run(
        "yt-dlp -q --skip-download --write-info-json -o temp.%\(ext\)s " + url, shell=True)

def create_folder(folder):
    if os.path.exists(folder):
        print("The folder for " + folder + " already exists.")
    else:
        print("Creating " + folder + " folder.")
        os.makedirs(folder)


def select_date_format(date_format, date):
    iso_date = datetime.datetime.strptime(date, '%Y%m%d')
    if date_format == "EU":
        return datetime.datetime.strftime(iso_date, '%d-%m-%Y')
    if date_format == "ISO":
        return datetime.datetime.strftime(iso_date, '%Y-%m-%d')


def download_audio(url, path, quiet):
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'postprocessors': [
            {'key': 'FFmpegExtractAudio', 'preferredcodec': 'm4a'},
            {'key': 'FFmpegMetadata'},
        ],
        "outtmpl": path + ".%(ext)s",
        "quiet": quiet,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(url)


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

    return "ffmpeg -threads 1 " + loglevel + input_file + frequency + component + bitrate + output_file


def get_ffmpeg_title_cmd(title, ffmpeg_quiet, input_file, output_file):
    if ffmpeg_quiet == True:
        loglevel = "-loglevel fatal -i "
    else:
        loglevel = "-loglevel info -i "
    return "ffmpeg -threads 1 " + loglevel + input_file + ' -c copy -metadata title="' + \
        title + '" ' + output_file


def get_ffmpeg_image_cmd(image_path, ffmpeg_quiet, input_file, output_file):
    if ffmpeg_quiet == True:
        loglevel = "-loglevel fatal -i "
    else:
        loglevel = "-loglevel info -i "
    return "ffmpeg -threads 1 " + loglevel + input_file + " -i " + image_path + " -c copy -map 0 -map 1 " + output_file


def get_duration(duration):
    ty_res = time.gmtime(duration)
    return time.strftime("%H:%M:%S", ty_res)


def get_pubdate(ep_upload_date, fixed_hour):
    iso_date = datetime.datetime.strptime(ep_upload_date, '%Y%m%d')

    if time.localtime().tm_isdst:
        return iso_date.strftime('%a, %d %b %Y ' + fixed_hour + ' +0200')
    else:
        return iso_date.strftime('%a, %d %b %Y ' + fixed_hour + ' +0100')


def get_last_build_Date():
    today = datetime.datetime.today()
    if time.localtime().tm_isdst:
        return today.strftime('%a, %d %b %Y %H:%M:%S +0200')
    else:
        return today.strftime('%a, %d %b %Y %H:%M:%S +0100')


def get_youtube_chapters(description):
    description_array = description.split("\n")
    is_chapter = False
    chapters = "\t<ul>"
    for line in description_array:
        if line != "":
            if "00:00" in line:
                is_chapter = True
            if "---" in line:
                is_chapter = False
            if is_chapter == True:
                chapters += "<li style ='text-align: justify;'> " + line + " </li>"
    chapters += "</ul>"
    return chapters


def create_content(header, chapters, footer):
    return header + "\n" + chapters + "\n" + footer


def get_full_xml(url, path):
    myfile = requests.get(url)
    open(path + ".xml", 'wb').write(myfile.content)
    return myfile.content

def get_episode_number(xml_content):
    all_episodes = re.findall(
        r"<itunes:episode>([0-9]+)<\/itunes:episode>", str(xml_content))
    last_episode = int(str(all_episodes[0]))
    return last_episode + 1

def create_xml_item(show, path):
    item = "<item>\n"
    item += "\t<title><![CDATA["+ show["title"] + "]]></title>\n"
    item += "\t<link>" + show["link"] + "</link>\n"
    item += "\t<itunes:author>" + show["itunes_author"] + "</itunes:author>\n"
    item += "\t<enclosure url='" + show["enclosure_url"] + show["guid"] + ".mp3' type='audio/mpeg'/>\n"
    item += "\t<guid isPermaLink='" + show["guid_permalink"] + "'>" + show["guid"] + "</guid>\n"
    item += "\t<pubDate>" + show["pub_date"] + "</pubDate>\n"
    item += "\t<itunes:episode>" + show["itunes_episode"] + "</itunes:episode>\n"
    item += "\t<itunes:episodeType>" + show["itunes_episode_type"] + "</itunes:episodeType>\n"
    item += "\t<itunes:duration>" + show["itunes_duration"] + "</itunes:duration>\n"
    item += "\t<itunes:image href='" + show["itunes_image"] + "'/>\n"
    item += "\t<itunes:subtitle><![CDATA[" + show["itunes_subtitle"] + "]]></itunes:subtitle>\n"
    item += "\t<description><![CDATA[" + show["itunes_description"] + "]]></description>\n"
    item += "\t<content:encoded>\n\t<![CDATA[" + show["content_encoded_header"] + show["content_encoded_main"] + show["content_encoded_timestamps"] + show["content_encoded_footer"] + "]]></content:encoded>\n"
    item += "</item>"
    if os.path.exists(path):
        os.remove(path)

    with open(path, "w") as f:
        f.write(item)
    
    return item


def get_metadatas(file, path):
    command = "ffprobe -print_format json -show_format -show_streams " + file + " > " + path + "/" + file + ".json"
    subprocess.run(command, shell=True)    

def insert_item(item, legacy_location, path):

    with open(legacy_location) as f:
        full_xml = re.sub("</itunes:explicit>", "</itunes:explicit>\n\n\n" + item + "\n", str(f.read()), 1)
        full_xml = re.sub("<lastBuildDate>.+<\/lastBuildDate>", "<lastBuildDate>" + get_last_build_Date() + "</lastBuildDate>", full_xml, 1)

    if os.path.exists(path + ".xml"):
        os.remove(path + ".xml")

    with open(path + ".xml", "w") as f:
        f.write(full_xml)


def create_channel_file(show, path):
    channel = "<?xml version='1.0' encoding='utf-8' ?>\n"
    channel += "<rss xmlns:itunes='http://www.itunes.com/dtds/podcast-1.0.dtd' version='2.0' xmlns:googleplay='http://www.google.com/schemas/play-podcasts/1.0' xmlns:content='http://purl.org/rss/1.0/modules/content/' xmlns:wfw='http://wellformedweb.org/CommentAPI/' xmlns:dc='http://purl.org/dc/elements/1.1/' xmlns:media='http://www.rssboard.org/media-rss'>\n"
    channel += "<channel>\n"
    channel += "\t<title>"+ show["channel"]["title"] + "</title>\n"
    channel += "\t<itunes:author>" + show["channel"]["itunes_author"] + "</itunes:author>\n"
    channel += "\t<itunes:owner><itunes:email>" + show["channel"]["itunes_owner_email"] + "</itunes:email></itunes:owner>\n"
    channel += "\t<itunes:category text='" + show["channel"]["itunes_category_main"] + "'></itunes:category>  \n"
    channel += "\t<link>" + show["channel"]["link"] + "</link>\n"
    channel += "\t<itunes:summary>" + show["channel"]["itunes_summary"] + "</itunes:summary>\n"
    channel += "\t<description>" + show["channel"]["itunes_description"] + "</description>\n"
    channel += "\t<itunes:type>" + show["channel"]["itunes_type"] + "</itunes:type>\n"
    channel += "\t<language>" + show["channel"]["language"] + "</language>\n"
    channel += "\t<lastBuildDate>" + get_last_build_Date()  + "</lastBuildDate>\n"
    channel += "\t<copyright>" + show["channel"]["copyright"] + "</copyright>\n"
    channel += "\t<image>\n"
    channel += "\t\t<url>" + show["channel"]["image_url"] + "</url>\n"
    channel += "\t\t<title>" + show["channel"]["image_text"] + "</title>\n" 
    channel += "\t\t<link>" + show["channel"]["image_link"] + "</link>\n" 
    channel += "\t</image>\n"
    channel += "\t<itunes:image>" + show["channel"]["itunes_image"] + "</itunes:image>\n"
    channel += "\t<itunes:explicit>" + show["channel"]["itunes_explicit"] + "</itunes:explicit>\n"
    channel += "\n"
    channel += "</channel>\n"
    if os.path.exists(path):
        os.remove(path)

    with open(path, "w") as f:
        f.write(channel)

def download_item_image(url, path):
    myfile = requests.get(url)
    open(path + ".jpg", 'wb').write(myfile.content)
    