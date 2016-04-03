# -*- coding: utf-8 -*-

import csv
#import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time 
import codecs
import os




#Build Dictionary from HelloFresh CSV Data. R
#emoves name duplicates in the process.
reader = csv.DictReader(open('ingredients.csv'))

ingredients_dictionary = {}

for row in reader:
    key = row.pop('name')
    if key in ingredients_dictionary:
        # implement your duplicate row handling here
        pass
    ingredients_dictionary[key] = row



def scrape():
    
        fp = webdriver.FirefoxProfile()
        driver = webdriver.Firefox(fp)
        
        for item in ingredients_dictionary:
            try:

                if os.path.isfile("scrape_mfp/" + str(item) + ".html"):
                    print "already found a scrape result HTML file for this query..."
                else:
                    print "Scraping ", str(item), "..."
                    
                    #Because Internet was flaky, selenium was more stable
                    #when loading this page each time, although it is overhead
                    driver.get("http://www.myfitnesspal.com/food/calorie-chart-nutrition-facts")
                    time.sleep(0.2)
                    
                    #find search field, send search string
                    search = driver.find_element_by_id("search")
                    search.send_keys(item.decode("utf-8"))
                    search.send_keys(Keys.RETURN)
                    time.sleep(random.uniform(1,2))
                    
                    #store data in dictionary.
                    ingredients_dictionary[item]["mfp_source"]=driver.page_source
                    time.sleep(0.2)
                    
                    #store .html files - pickle usually corrupted the HTML data
                    if "Search Results for" in driver.page_source:
                        #save html file with name
                        with codecs.open("scraped/" + str(item) + ".html", "w", "utf-8-sig") as temp:
                            temp.write(driver.page_source)
                            temp.close()
                        
                        time.sleep(0.2)
                    else:
                        print str(item), " failed..."
                        #no RETRY yet, you can just start the scraper again 
            except Exception as g:
                print g
        
scrape()