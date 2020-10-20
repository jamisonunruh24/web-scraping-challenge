#import dependancies
import os
import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests

#URL for first site to scrape
url = 'https://mars.nasa.gov/'
response = requests.get(url)
soup = bs(response.text, 'html.parser')

nasa_title = soup.title.text

paragraphs = soup.find_all('p')
clean_paragraph = []
for paragraph in paragraphs:
    clean_paragraph.append(paragraph.text)
nasa_para = clean_paragraph[1]

#Using splinter to navagate the page for the feature image
executable_path = {'executable_path': 'C:\chromedriver\chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
find_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(find_image_url)
image_html = browser.html
image_soup = bs(image_html, 'html.parser')
image = image_soup.find_all('a', class_='button fancybox')
image = str(image)
image_link = image[330:-147]
main_url = 'https://www.jpl.nasa.gov'
image_url = main_url + image_link

browser.quit()

#Pulling mars facts table 
facts_url = 'https://space-facts.com/mars/'
tables = pd.read_html(facts_url)
facts_df = tables[0]
facts_table = facts_df.to_html()
facts_table = facts_table.replace('\n', '')

#using splinter to navigate between 4 pages to pull image URL's
hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
executable_path = {'executable_path': 'C:\chromedriver\chromedriver.exe'}
hemisphere_browser = Browser('chrome', **executable_path, headless=False)
hemisphere_browser.visit(hemisphere_url)
hemisphere_html = hemisphere_browser.html
hemisphere_soup = bs(hemisphere_html, 'html.parser')

hemisphere_browser.links.find_by_partial_text('Cerberus Hemisphere Enhanced').click()
hemisphere_browser.links.find_by_partial_text('Sample').click()
cerberus_browser = hemisphere_browser.html
cerberus_soup = bs(cerberus_browser, 'html.parser')
cerberus_img = cerberus_soup.find_all('a')[4]

hemisphere_browser.visit(hemisphere_url)
hemisphere_browser.links.find_by_partial_text('Schiaparelli Hemisphere Enhanced').click()
hemisphere_browser.links.find_by_partial_text('Sample').click()
schiaparelli_browser = hemisphere_browser.html
schiaparelli_soup = bs(schiaparelli_browser, 'html.parser')
schiaparelli_img = schiaparelli_soup.find_all('a')[4]

hemisphere_browser.visit(hemisphere_url)
hemisphere_browser.links.find_by_partial_text('Syrtis Major Hemisphere Enhanced').click()
hemisphere_browser.links.find_by_partial_text('Sample').click()
syrtis_browser = hemisphere_browser.html
syrtis_soup = bs(syrtis_browser, 'html.parser')
syrtis_img = syrtis_soup.find_all('a')[4]

hemisphere_browser.visit(hemisphere_url)
hemisphere_browser.links.find_by_partial_text('Valles Marineris Hemisphere Enhanced').click()
hemisphere_browser.links.find_by_partial_text('Sample').click()
valles_browser = hemisphere_browser.html
valles_soup = bs(valles_browser, 'html.parser')
valles_img = valles_soup.find_all('a')[4]

hemisphere_browser.quit()

#converting the beautiful soup elements to a string
cerberus = str(cerberus_img)
schiaparelli = str(schiaparelli_img)
syrtis = str(syrtis_img)
valles = str(valles_img)
#trimming the strings to only use the URL part
cerberus_link = cerberus[9:-28]
schiaparelli_link = schiaparelli[9:-28]
syrtis_link = syrtis[9:-28]
valles_link = valles[9:-28]