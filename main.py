from bs4 import BeautifulSoup
import requests

# Replace 'url' with the URL of the webpage containing the videos
url = 'https://file-to-link-bot-botiodevs-918c1f28643d.herokuapp.com/watch/662d17e370f796e2061f681f'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all video tags
video_tags = soup.find_all('video')

# Extract URLs
video_urls = [video['src'] for video in video_tags]

print(video_urls)
