import requests
from bs4 import BeautifulSoup
import zipfile
import os
from io import BytesIO
import configparser

# Base URLs
game_list_url_template = "https://awbw.amarriner.com/gamescompleted.php?start={}&type=std"
replay_download_url_template = "https://awbw.amarriner.com/replay_download.php?games_id={}"

# Directory to save ZIP files and unpack them
output_dir = r"C:\Users\alexm\.aaprojects\awbw\replays"

config = configparser.ConfigParser()
config.read(os.path.join('conf', 'auth.conf'))

# Extract credentials
username = config.get('credentials', 'username')
password = config.get('credentials', 'password')
php_session_id = config.get('credentials', 'sesssion')

# Define the cookies and headers for authentication
cookies = {
    'awbw_username': username,
    'awbw_password': password,
    'PHPSESSID': php_session_id
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0'
}

# Function to get all game URLs from a page
def get_game_urls(page_number):
    url = game_list_url_template.format(page_number)
    response = requests.get(url, headers=headers, cookies=cookies)
    
    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all game links
    game_urls = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if 'game.php?games_id=' in href:
            game_id = href.split('=')[1]
            game_urls.append(game_id)
    
    return game_urls

# Function to download and unpack ZIP files
def download_and_unpack(game_id):
    # Download the ZIP file for the given game_id
    replay_download_url = replay_download_url_template.format(game_id)
    response = requests.get(replay_download_url, headers=headers, cookies=cookies)

    if response.status_code == 200:
        # Save and unpack the ZIP
        with zipfile.ZipFile(BytesIO(response.content)) as zip_file:
            zip_file.extractall(output_dir)
            print(f"Unpacked game {game_id} to {output_dir}")
    else:
        print(f"Failed to download game {game_id}, Status code: {response.status_code}")

# Loop through the pages and process games
start = 1
step = 50
while True:
    print(f"Processing page with start={start}")
    
    # Get all game URLs for this page
    game_ids = get_game_urls(start)
    
    if not game_ids:
        print("No more games found.")
        break

    # Download and unpack each game's replay
    for game_id in game_ids:
        download_and_unpack(game_id)

    # Increment start to get the next page
    start += step
