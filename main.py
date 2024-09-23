import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# URL of the webpage to scrape
url = 'https://mawazine.ma/en/edition-2024/programme/'  

# Your YouTube API key
youtube_api_key = 'AIzaSyCXeD9uEXIlXv4zf8f8U2rv1ayZDRznYXw'  

# Send a GET request to the webpage
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    data = []

    for slide in soup.find_all('div', class_='slide'):
        date = slide.find('div', class_='pageTitle').h3.text.strip() if slide.find('div', class_='pageTitle') else None
        table = slide.find('table')
        
        if table:
            rows = table.find_all('tr')[1:]  # Skip header row
            
            for row in rows:
                artist, theme, stage = None, None, None

                # Check if there are <td> elements in the row
                td_elements = row.find_all('td')
                if td_elements:
                    # Extract the artist name
                    artist_tag = td_elements[1].find('strong').find('a').get_text() if td_elements[1].find('strong') else None
                    if artist_tag:
                        artist = artist_tag.strip()

                    # Extract theme and stage
                    if len(td_elements) > 2:
                        theme = td_elements[2].text.strip()
                    if len(td_elements) > 3:
                        stage = td_elements[3].text.strip()

                if artist:  # Proceed only if an artist name is found
                    # Clean the artist name and remove (Français)
                    cleaned_artist_name = artist.replace('(Français)', '').strip()
                    
                    # Fetch subscriber count from YouTube API
                    search_url = f'https://www.googleapis.com/youtube/v3/search?part=id&q={cleaned_artist_name}&key={youtube_api_key}'
                    search_response = requests.get(search_url)
                    subscriber_count = "Not Found"

                    if search_response.status_code == 200:
                        search_data = search_response.json()
                        if search_data['items']:
                            # Loop through items to find a channel
                            channel_id = None
                            for item in search_data['items']:
                                if item['id']['kind'] == 'youtube#channel':
                                    channel_id = item['id']['channelId']
                                    break
                            
                            if channel_id:
                                channel_url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={youtube_api_key}'
                                channel_response = requests.get(channel_url)

                                if channel_response.status_code == 200:
                                    channel_data = channel_response.json()
                                    if channel_data['items']:
                                        subscriber_count = channel_data['items'][0]['statistics']['subscriberCount']
                    else:
                        print(f"Error fetching YouTube data for {cleaned_artist_name}: {search_response.status_code}")

                    # Add a short delay to avoid rate limiting
                    time.sleep(1)

                    # Append the data
                    data.append((cleaned_artist_name, date, theme, stage, subscriber_count))

    # Create DataFrame
    df = pd.DataFrame(data, columns=['Artist Name', 'Date', 'Theme', 'Stage', 'Subscribers Count'])
    
    # Remove rows with None as Artist Name
    df = df[df['Artist Name'].notnull()]
    
    # Save the DataFrame to a CSV file
    df.to_csv('Mawazine_2024_Artists.csv', index=False)

    # Print the DataFrame
    print(df)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
