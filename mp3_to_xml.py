import json
import datetime

utils = __import__('utils')

def mp3_to_item(show, file):
    print("🤖 Recovering the video's JSON file.")

    path_show_file = show["general"]["name"] + "/" + file
    utils.create_folder(path_show_file)
    utils.get_metadatas(file, path_show_file)
    today = str(datetime.datetime.today()).split(" ", 1) 
    today = today[0].replace("-", "")
    pubdate = utils.get_pubdate(today, show["item"]["pub_date_hour"])
    
    with open(path_show_file + "/" + file + ".json") as f:
        json_data = json.load(f)
        tags = json_data["format"]["tags"]
        formats = json_data["format"]
        show["item"]["title"] = tags["title"]
        show["item"]["link"] = "WAITING_FOR_URL"
        show["item"]["enclosure_url"] = show["item"]["enclosure_url"] + formats["filename"]
        show["item"]["guid"] = show["item"]["guid"]  + formats["filename"]
        show["item"]["pub_date"] = pubdate
        show["item"]["itunes_episode"] = tags["track"]
        show["item"]["itunes_duration"] = utils.get_duration(float(formats["duration"]))
        show["item"]["itunes_subtitle"] = tags["comment"]
        show["item"]["itunes_description"] = tags["comment"]
        show["item"]["content_encoded_main"] = tags["comment"]

        utils.create_xml_item(show["item"], path_show_file + "/" + file + ".xml")


            