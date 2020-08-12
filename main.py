import csv

from bs4 import BeautifulSoup
import requests

source = requests.get('https://coreyms.com/').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('output.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline', 'Summary', 'Youtube Link'])

for article in soup.find_all('article'):
    try:
        headline = article.h2.a.text
    except:
        headline = ""
    print(headline)

    try:
        summary = article.find('div', class_='entry-content').text
    except:
        summary = ""
    print(summary)

    try:
        video_source = article.find('iframe', class_='youtube-player')['src']
        video_id = video_source.split('/')[4]
        vid_id = video_id.split('?')[0]
        youtube_link = f'https://youtube.com/watch?v={vid_id}'
    except:
        video_source = ""
        video_id = ""
        vid_id = ""
        youtube_link = None

    print(youtube_link)

    print()

    csv_writer.writerow([headline, summary, youtube_link])

# close file
csv_file.close()

