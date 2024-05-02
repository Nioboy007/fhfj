from bs4 import BeautifulSoup
import requests

# Replace 'url' with the URL of the webpage containing the videos
url = 'https://www.pexels.com/video/times-in-the-desrt-20770858'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all video tags
video_tags = soup.find_all('video')

# Extract URLs
video_urls = [video['src'] for video in video_tags]

print(video_urls)
