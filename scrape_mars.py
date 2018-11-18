# ## Mission to Mars

# All dependencies
import requests
import os
from bs4 import BeautifulSoup 
from splinter import Browser
import time
import json
import tweepy 
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    browser = init_browser()
    mars_d = {}
# ## NASA Mars News

# URL of page to be scraped
url = 'https://mars.nasa.gov/news/'


# Retrieve page with the requests module
response = requests.get(url)


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# find the the title text
title = soup.title.text
title


# retrieve paragraph text
paragraphs = soup.find_all('p')
paragraphs


# ## JPL Mars Space Images - Featured Image

# scraping web url 
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

# Test for the existence of an attribute
print(soup.prettify())

# scraping web url to pull full image
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

# executing splinter
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path)
browser.visit(url)

# Moving through the pages
wait_time = 3
browser.click_link_by_partial_text('FULL IMAGE')
wait_time = 3
browser.click_link_by_partial_text('more info')
wait_time = 3

# Create BeautifulSoup object; parse with 'html.parser'
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

# Get featured image
results = soup.find('article')
ext = results.find('figure').a['href']
link = "https://www.jpl.nasa.gov"
featured_image_url = link + ext

# add to main dictionary
mars_d["featured_image_url"]= featured_image_url

# ## Mars Weather

# Import Twitter API Keys
from config import consumer_key, consumer_secret, access_token, access_token_secret

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Target User
target_user = "@MarsWxReport"

# Get user tweet
# def get_last_tweet(user_tweet):
tweet = api.user_timeline(target_user, count=1)[0]

# Save tweet to variable mars_weather
mars_weather = tweet['text']
mars_weather

# add to main dictionary
mars_d["mars_weather"]= mars_weather

#print tweet in json
print(json.dumps(tweet, sort_keys=True, indent=4))


# ## Mars Facts

# URL to scrape 
url = 'https://space-facts.com/mars/'


# View url data in a list of dataframes
tables = pd.read_html(url)
tables


type(tables)


# Create dataframe for web url data
data = tables[0]
df = data
df.head()


# Convert to html string
html_table = df.to_html()
html_table



# Strip and clean the html table
html_table.replace('\n', '')



# Save the html file
df.to_html('table.html')


# ## Mars Hemispheres

# Mars Hemispheres URL
url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

# Empty list of image urls
hemisphere_image_urls = []

# Print web contents
print(soup.prettify())


# Setting up splinter 
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=True)
browser.visit(url)

# Moving through pages
wait_time = 3
browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
wait_time = 3

# Create BeautifulSoup object; parse with 'html.parser'
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

# Store link
valles_link = soup.find('div', 'downloads').a['href']

# Create dictionary
valles_marineris = {
    "title": "Valles Marineris Hemisphere",
    "img_url": valles_link
}

# Appending dictionary
hemisphere_image_urls.append(valles_marineris)



# Setting up splinter 
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=True)
browser.visit(url)

# Moving through pages
wait_time = 3
browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
wait_time = 3

# Create BeautifulSoup object; parse with 'html.parser'
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

# Store link
cer_link = soup.find('div', 'downloads').a['href']

# Create dictionary
cerberus = {
    "title": "Cerberus Hemisphere",
    "img_url": cer_link
}

# Appending dictionary
hemisphere_image_urls.append(cerberus)


# Setting up splinter 
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=True)
browser.visit(url)

# Moving through pages
wait_time = 3
browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
wait_time = 3

# Create BeautifulSoup object; parse with 'html.parser'
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

# Store link
schip = soup.find('div', 'downloads').a['href']

# Create dictionary
schiparelli = {
    "title": "Schiaparelli Hemisphere",
    "img_url": schip
}

# Appending dictionary
hemisphere_image_urls.append(schiparelli)

# Setting up splinter 
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=True)
browser.visit(url)

# Moving through pages
wait_time = 3
browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
wait_time = 3

# Create BeautifulSoup object; parse with 'html.parser'
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

# Store link
syrtis = soup.find('div', 'downloads').a['href']

# Create dictionary
syrtis_m = {
    "title": "Syrtis Major Hemisphere",
    "img_url": syrtis
}

# Appending dictionary
hemisphere_image_urls.append(syrtis_m)


# Print dictionary of urls
print(hemisphere_image_urls)
# Adding to dictionary
mars_d["hemisphere_image_urls"] = hemisphere_image_urls

# Copied hemisphere urls to check output table 
#url1 = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
#url2 = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
#url3 = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
#url4 = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'

# Return results
return mars_d
