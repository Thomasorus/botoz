#!/bin/bash

echo "================================"
echo "== 🤖 BOTOZ 3000 ACTIVATED 🤖 =="
echo "================================"


TODAY=$(date +%d-%m-%Y)

echo "🤖 Hello Yann, did you sleep well?"
echo "🤖 Today date is $TODAY. You look sharp Yann."
echo "🤖 As always."
TZ=`date +"%z"`
TIME=`date +"%H:%M:%S"`
WEEKDAY=`date +"%a"`
DATE=`date +"%d"`
MONTH=`date +"%b"`
YEAR=`date +"%Y"`
ISO_DATE="$WEEKDAY, $DATE $MONTH $YEAR $TIME $TZ"

echo "🤖 Creating folder to store you yummy podcast, Yann."
mkdir $TODAY

echo "🤖 Downloading video and converting to mp3, please wait Yann, this might take a while."

youtube-dl -f 'bestaudio,worstvideo' -x -q --audio-format mp3 --audio-quality 0 --write-description -o $TODAY"/%(title)s.%(ext)s" $1

TITLE=$(basename $TODAY/*.description .description | sed -E 's/[_]+/|/' | sed -E 's/[_]+/-/')

echo "🤖 Today's video title will be: ${TITLE}."
echo "🤖 What a sweet title. Just like you, Yann."

for file in $TODAY/*.*
do
  mv "$file" "./${TODAY}/$TODAY.${file##*.}"
done

VIDEO_LINK=$1

echo "🤖 Recovering the timestamps, so you don't have to copy and paste in your browser adress bar, Yann."

SOMMAIRE=""
FILENAME=$TODAY"/"$TODAY'.description'
CHECK_SOMMAIRE=false
N=1
while read line; do
# echo $line
if [[ -n $line ]]; then
    if [[ $line == *"00:00"* ]]; then
    CHECK_SOMMAIRE=true
    fi
    if [[ $line == *"---"* ]]; then
    CHECK_SOMMAIRE=false
    fi
    if [ $CHECK_SOMMAIRE = true ]; then
        SOMMAIRE=$SOMMAIRE'<li style="text-align: justify;">'$line'</li>'
    fi
fi
N=$((N+1))
done < $FILENAME

DURATION=$(ffmpeg -i $TODAY/$TODAY.mp3 2>&1 | awk '/Duration/ { print substr($2,0,length($2)-1) }')
echo "🤖 Today's podcast lenght is: ${DURATION}, Yann."

echo "🤖 Creating the xml <item> file for you Yann, with love."
cp sources/item.xml $TODAY/$TODAY.xml
sed -i "" "s#GAUTOZ_TITRE#${TITLE}#g" $TODAY/$TODAY.xml
sed -i "" "s#GAUTOZ_VIDEO_LINK#${1}#g" $TODAY/$TODAY.xml
sed -i "" "s#GAUTOZ_PUBDATE#${ISO_DATE}#g" $TODAY/$TODAY.xml
sed -i "" "s#GAUTOZ_DATE#${TODAY}#g" $TODAY/$TODAY.xml
sed -i "" "s#GAUTOZ_SOMMAIRE#${SOMMAIRE}#g" $TODAY/$TODAY.xml
sed -i "" "s#GAUTOZ_DURATION#${DURATION}#g" $TODAY/$TODAY.xml

echo '🤖 Adding image to the mp3 Yann, just because I can.'
echo '🤖 And I like you.'
mv $TODAY/$TODAY.mp3 $TODAY/$TODAY.temp.mp3
ffmpeg -hide_banner -loglevel error -i $TODAY/$TODAY.temp.mp3 -i sources/LaMatinaleJV.jpg -map 1 -map 0 -c copy -disposition:0 attached_pic $TODAY/$TODAY.mp3
rm $TODAY/$TODAY.temp.mp3
rm $TODAY/$TODAY.description
rm $TODAY/$TODAY.webm

echo "🤖 Everything is done, Yann."
echo "🤖 Don't forget to review the XML and MP3 files, Yann."
echo "🤖 Enjoy you day, Yann."