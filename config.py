# Configure your podcasts using this file.
# If a config line does not have a comment, don't touch it.
podcasts = {
    "matinale": {
        # General config
        "general": {
            "name": "matinale",
            "user_name": "Yann",  # The name botoz will use to salute you
            "script_name": "BOTOZ 3000",  # The name of the script
            "main_xml_url": "http://gautozf.cluster030.hosting.ovh.net/matinale-podcast/podcast_la-matinale-jv.xml",
            "youtube-dl_quiet": False,  # True or False
            "ffmpeg_quiet": False,  # True or False
            "date_format": "EU",  # ISO or EU
            "xml_file_name": "podcast_la-matinale-jv"
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
            "title": "La Matinale Jeu Vidéo",  # Main title of the podcasts
            "itunes_author": "Gautoz",  # Author or owner of the podcasts
            "itunes_owner_email": "gauthier.andres@gmail.com",  # Email of the owner
            "itunes_category_main": "Leisure",  # Main category asked by itunes
            "itunes_cageroy_sub": "Video Games",  # Sub category asked by itunes
            "link": "https://www.twitch.tv/Gautoz/",  # Website of the owner
            "itunes_summary": "Du lundi au vendredi de 9h à 11h30 sur Twitch, Gautoz passe en revue les actus brûlantes du monde du jeu vidéo. Envie de rattraper tout ça en podcast audio ? C'est ici !",  # Summary for itunes
            "itunes_description": "Du lundi au vendredi de 9h à 11h30 sur Twitch, Gautoz passe en revue les actus brûlantes du monde du jeu vidéo. Envie de rattraper tout ça en podcast audio ? C'est ici !",  # Description for itunes
            "itunes_type": "episodic",  # episodic or serial
            "language": "fr-fr",  # Language of the podcast
            "last_build_date": "",
            "copyright": "Gautoz — 2021",  # Copyright
            "image_url": "http://gautozf.cluster030.hosting.ovh.net/matinale-podcast/LaMatinaleJV.jpg",  # Image URL
            "image_text": "La Matinale Jeu Vidéo",  # Image Text
            "image_link": "https://www.twitch.tv/Gautoz/",  # Link for image
            "itunes_image": "http://gautozf.cluster030.hosting.ovh.net/matinale-podcast/LaMatinaleJV.jpg",  # Itunes image
            "itunes_explicit": "no",  # yes or no
        },

        # Xml config and data for the <item>
        "item": {
            "title": "",
            "link": "",
            "itunes_author": "Gautoz",  # Author of the episode
            "enclosure_url": "http://www.podtrac.com/pts/redirect.mp3/gautozf.cluster030.hosting.ovh.net/matinale-podcast/",  # MP3 files folder
            "guid": "",
            "guid_permalink": "false",  # true or false
            "pub_date": "",
            "pub_date_hour": "09:00:00",  # Fixed publication hour if needed
            "itunes_episode": "",
            "itunes_episode_type": "full",  # full, trailer, bonus
            "itunes_duration": "",
            "itunes_image": "http://gautozf.cluster030.hosting.ovh.net/matinale-podcast/LaMatinaleJV.jpg",
            "itunes_subtitle": "",
            "itunes_description": "",
            "content_encoded_header": "<img src='http://gautozf.cluster030.hosting.ovh.net/matinale-podcast/LaMatinaleJV_short.jpg' /><br /><p style='text-align: justify;'>'C'est pas Trotauz !', votre matinale jeux vidéo du lundi au vendredi de 9h à 11h30 sur Twitch !</p><ul style='text-align: justify;'><li style='text-align: justify;'><a href='https://twitch.tv/gautoz​'>https://twitch.tv/gautoz​</a></li><li style='text-align: justify;'><a href='https://gautoz.cool/matinales/'>Sources articles</a></li><li style='text-align: justify;'><a href='https://www.youtube.com/playlist?list=PLyh2wbBeYS9izB0S6JUiwq4cYdXcR_tjg'>Toutes les matinales sur YouTube </a></li></ul>",  # In HTML
            "content_encoded_timestamps": "",
            "content_encoded_main": "",
            "content_encoded_footer": "",  # in HTML
        },
    },
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
