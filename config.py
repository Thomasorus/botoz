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
    "guidon": {
        # General config
        "general": {
            "name": "guidon",
            "user_name": "Yann",  # The name botoz will use to salute you
            "script_name": "BOTOZ 3000",  # The name of the script
            "main_xml_url": "https://shows.blueprint.pm/la-tete-dans-le-guidon/podcast_la-tete-dans-le-guidon.xml",
            "youtube-dl_quiet": False,  # True or False
            "ffmpeg_quiet": True,  # True or False
            "date_format": "EU",  # ISO or EU
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
            "title": "La Tête dans le Guidon",  # Main title of the podcasts
            "itunes_author": "CyclismeRevue / Blueprint",  # Author or owner of the podcasts
            "itunes_owner_email": "podcast@blueprint.pm",  # Email of the owner
            "itunes_category_main": "Sports",  # Main category asked by itunes
            "itunes_cageroy_sub": "",  # Sub category asked by itunes
            "link": "https://www.blueprint.pm/podcasts/la-tete-dans-le-guidon/",  # Website of the owner
            "itunes_summary": "Votre podcast mensuel qui questionne le cyclisme, les mains sur les cocottes. Présenté par Greg Ienco, en partenariat avec CyclismeRevue.be !",  # Summary for itunes
            "itunes_description": "Votre podcast mensuel qui questionne le cyclisme, les mains sur les cocottes. Présenté par Greg Ienco, en partenariat avec CyclismeRevue.be !",  # Description for itunes
            "itunes_type": "episodic",  # episodic or serial
            "language": "fr-fr",  # Language of the podcast
            "last_build_date": "",
            "copyright": "CyclismeRevue / Blueprint © 2021. Tous droits réservés.",  # Copyright
            "image_url": "https://shows.blueprint.pm/la-tete-dans-le-guidon/latetedanslejpeg.jpg",  # Image URL
            "image_text": "La Tête dans le Guidon",  # Image Text
            "image_link": "https://www.blueprint.pm/podcasts/la-tete-dans-le-guidon/",  # Link for image
            "itunes_image": "https://shows.blueprint.pm/la-tete-dans-le-guidon/latetedanslejpeg.jpg",  # Itunes image
            "itunes_explicit": "no",  # yes or no
        },

        # Xml config and data for the <item>
        "item": {
            "title": "",
            "link": "",
            "itunes_author": "CyclismeRevue / Blueprint",  # Author of the episode
            "enclosure_url": "https://www.podtrac.com/pts/redirect.mp3/shows.blueprint.pm/la-tete-dans-le-guidon/",  # MP3 files folder
            "guid": "https://shows.blueprint.pm/la-tete-dans-le-guidon/",
            "guid_permalink": "false",  # true or false
            "pub_date": "",
            "pub_date_hour": "09:00:00",  # Fixed publication hour if needed
            "itunes_episode": "",
            "itunes_episode_type": "full",  # full, trailer, bonus
            "itunes_duration": "",
            "itunes_image": "https://shows.blueprint.pm/la-tete-dans-le-guidon/latetedanslejpeg.jpg",
            "itunes_subtitle": "",
            "itunes_description": "",
            "content_encoded_header": '<img src="https://shows.blueprint.pm/la-tete-dans-le-guidon/latetedanslejpeg.jpg" /><br /><p style="text-align: justify;">Bienvenue dans La Tête dans le Guidon, le podcast qui questionne le cyclisme les mains sur les cocottes !',  # In HTML
            "content_encoded_timestamps": "",
            "content_encoded_main": "",
            "content_encoded_footer": '</p><h3 style="text-align: justify;">Encore plus de cyclisme ?</h3><p style="text-align: justify;"><em>Suivez La Tête dans le Guidon ainsi que l’ensemble de l’actualité cycliste sur <a href="https://CyclismeRevue.be">CyclismeRevue.be</a>, et poursuivez votre découverte des podcasts sur <a href="https://www.blueprint.pm/podcasts/">Blueprint.pm</a> !</em></p>',  # in HTML
        },
    },
}
