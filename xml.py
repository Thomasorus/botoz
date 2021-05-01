def get_full_xml(url, path):
    myfile = requests.get(url)
    open(path + "_LEGACY.xml", 'wb').write(myfile.content)
    return myfile.content

def get_episode_number(xml_content):
    all_episodes = xml_content.findall(
        r"<itunes:episode>([0-9]+)<\/itunes:episode>", str(xml_content))
    last_episode = int(str(all_episodes[0]))
    return last_episode + 1

def create_xml_item(show):
    item = '''<item>
        <title>{show["title"]}</title>
        <link>{show["link"]}</link>
        <itunes:author>{show["itunes_author"]}</itunes:author>
        <enclosure url="{show["enclosure_url"]}" type="audio/mpeg"/>
        <guid isPermaLink="{show["guid_permalink"]}">{show["guid"]}</guid>
        <pubDate>{show["pub_date"]} {show["pub_date_hour"]}</pubDate>
        <itunes:episode>{show["itunes_episode"]}</itunes:episode>
        <itunes:episodeType>{show["itunes_episode_type"]}</itunes:episodeType>
        <itunes:duration>{show["itunes_duration"]}</itunes:duration>
        <itunes:image href="{show["itunes_image"]}"/>
        <itunes:subtitle>{show["itunes_subtitle"]}</itunes:subtitle>
        <description>{show["itunes_description"]}</description>
        <content:encoded>
            {show["content_encoded_header"]}
            {show["content_encoded_timestamps"]}
            {show["content_encoded_footer"]}
        </content:encoded>
    </item>'''
    return item

