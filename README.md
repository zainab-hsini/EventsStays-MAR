# Mawazine Artist Analysis

## Project Overview

**Mawazine Artist Data Scraper** is a Python project that extracts data about artists who performed at the **Mawazine Festival 2024**, one of the largest music festivals in the world, which takes place in Morocco. This project scrapes artist information from the festival's official website and augments the data by fetching YouTube subscriber counts for each artist, giving insight into their online reach and the festival's. The dataset can be valuable for comparing the popularity of festival performers and analyzing trends in music influence.

### Features
- **Artist Name & Performance Details:** Scraped directly from the official Mawazine 2024 festival program.
- **YouTube Subscriber Count:** Fetched using the YouTube Data API v3 to reflect the digital footprint of each artist.
- **Dataset Output:** Compiled into a clean CSV file for further analysis.

## Purpose

The goal of this project is to provide a comprehensive dataset that combines **artist performance data** from a major cultural festival with **YouTube popularity metrics**, offering insight into:
- The digital influence of performers in various genres.
- Comparative popularity among artists based on their YouTube following.
- Trends in global and regional music tastes at major festivals like Mawazine.
- The festival's impact on artists
- The growing influence of Mawazine

This information can serve a variety of purposes:
- **Event Organizers:** To assess the popularity of artists for future line-ups.
- **Music Analysts:** To study the relationship between festival performances and digital reach.
- **Marketing Teams:** To identify potential collaboration opportunities with artists based on their audience size.
- **Music Fans:** To discover new artists by exploring those with the highest influence.

## Technical Details

### Data Scraping
The artist data is scraped from the [Mawazine Festival 2024 website](https://mawazine.ma/en/edition-2024/programme/) using **BeautifulSoup**, a Python library for parsing HTML content. The script loops through the festival's artist listings, extracting details such as:
- **Artist Name**
- **Performance Date**
- **Genre/Theme**
- **Stage Location**

### YouTube Data Integration
Once the artist names are scraped, the project uses the **YouTube Data API v3** to retrieve each artist's subscriber count. This API allows the program to:
- Search for YouTube channels based on artist names.
- Extract subscriber counts from the corresponding channels.
  
**Error Handling**: In cases where no valid channel is found or the API request fails, the program records "Not Found" for the subscriber count.

### Data Output
The final dataset is saved as a **CSV file** that includes:
- **Artist Name**
- **Performance Date**
- **Theme**
- **Stage**
- **YouTube Subscriber Count**

## Installation & Dependencies

This project requires the following Python libraries, listed in `requirements.txt`:

- `requests`: For sending HTTP requests to the festival's website and the YouTube API.
- `beautifulsoup4`: For parsing and scraping HTML content.
- `pandas`: For managing and saving the dataset as a CSV file.

To install these dependencies, run:

```bash
pip install -r requirements.txt
```

## Running the Project

To scrape the Mawazine 2024 data and generate the CSV file, use the following command:

```bash
python3 main.py
```

The CSV file will be saved in the project directory as `mawazine_artists_2024.csv`.

## Use Cases of Mawazine Artist Data Scraper

This dataset can benefit several types of users by providing data-driven insights into the festival’s artist lineup and their online influence:

- **Event Organizers:** Identify the most popular performers to inform future line-up decisions.
- **Music Industry Professionals:** Analyze digital influence and fan engagement of various performers.
- **Academics and Researchers:** Study how YouTube popularity correlates with festival performances and audience reach.
- **Media and Journalists:** Highlight artists with significant digital followings, especially those with unexpected or rising influence.
- **Marketing & Brands:** Leverage artist popularity to make strategic partnerships or sponsorship deals based on audience size.

This dataset can be used to perform analysis that will offer valuable insights into the world of music festivals, digital presence, and trends in audience engagement.