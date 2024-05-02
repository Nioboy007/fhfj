from bs4 import BeautifulSoup
import requests

# Replace 'url' with the URL of the webpage containing the video
url = 'https://www.pexels.com/video/times-in-the-desrt-20770858/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the iframe tag
iframe_tag = soup.find('iframe')

# Extract the src attribute, which contains the video URL
video_url = iframe_tag['src']

print(video_url)
