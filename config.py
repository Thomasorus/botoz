# Configure your podcasts using this file.
# If a config line does not have a comment, don't touch it.
podcasts = {
    "default": {
        # General config
        "general": {
            "name": "default", #Must be the same as the one you choose before
            "user_name": " ",  # The name botoz will use to salute you
            "script_name": "BOTOZ",  # The name of the script if you want to change it
            "main_xml_url": "", # The existing XML URL 
            "youtube-dl_quiet": True,  # True or False
            "ffmpeg_quiet": True,  # True or False
            "date_format": "ISO",  # ISO or EU
            # Optionnal, for youtube playlist automation only
            "playlist_url": "", # Youtube RSS file when you want to automate the conversion from youtube using the youtube_automate file
            "xml_file_name": "podcast_la-matinale-jv", # The name of xml files you want
            "ftp_folder": "", # The folder in your server where you want to transfer the files
            "ftp_url": "", # FTP url/ip
            "ftp_login": "", # FTP login
            "ftp_password": "" # FTP password
        },

        # MP3 config
        "mp3": {
            "frequency": "44100",  # 44100, 48000
            "component": "stereo",  # stereo or mono
            "bitrate": "CBR",  # CBR or VBR
            "CBR_quality": "128",  # 64, 80, 96, 112, 128, 160, 192, 224, 256, or 320
            "VBR_quality": "9",  # 0 to 9, 0 is best, 9 is worse (see Readme)
        },

        # Xml config for the <channel> part of the RSS file
        "channel": {
            "title": " ",  # Main title of the podcasts
            "itunes_author": " ",  # Author or owner of the podcasts
            "itunes_owner_email": " ",  # Email of the owner
            "itunes_category_main": " ",  # Main category asked by itunes
            "itunes_cageroy_sub": " ",  # Sub category asked by itunes
            "link": " ",  # Website of the owner
            "itunes_summary": " ",  # Description for itunes
            "itunes_type": " ",  # episodic or serial
            "language": " ",  # Language of the podcast in format : en-en
            "last_build_date": "",
            "copyright": " ",  # Copyright
            "image_url": " ",  # Main image URL of your podcast
            "image_text": "",  # Image Text Description
            "image_link": " ",  # When image is clicked, link to this
            "itunes_image": " ",  # Itunes image, same as image_url
            "itunes_explicit": " ",  # yes or no, depending if you swear a lot of not
        },

        # Xml config and data for the <item>
        "item": {
            "title": "",
            "link": "",
            "itunes_author": " ",  # Author of the episode
            "enclosure_url": " ",  # MP3 files folder
            "guid": "",
            "guid_permalink": " ",  # true or false, if unsure use false
            "pub_date": "",
            "pub_date_hour": "09:00:00",  # Fixed publication hour if needed
            "itunes_episode": "",
            "itunes_episode_type": " ",  # full, trailer, bonus
            "itunes_duration": "",
            "itunes_image": " ", # Probably the same as in channel
            "itunes_subtitle": "",
            "itunes_description": "",
            "content_encoded_header": " ",  # In HTML, put the text that you want to see AT THE TOP of the description of each episode
            "content_encoded_timestamps": "",
            "content_encoded_main": "",
            "content_encoded_footer": "",  # In HTML, put the text that you want to see AT THE BOTTOM of the description of each episode
        },
    },
}
