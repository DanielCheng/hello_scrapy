A scrapy hello world project for runnable
===
Objectives
---
* Find All NFL Teams and their official site link from nfl.com

Steps
---
* start the project
        
        scrapy startproject hello_scrapy

* create a spider
        
        cd hello_scrapy
        scrapy genspider nfl nfl.com 

* edit the spider
        
        vim hello_scrapy/spiders/nfl.py

* add parse function to class NflSpider

* edit pipelines.py to save scraped item

* modify ITEM_PIPELINES in setting.py to enable pipeline

* run the spider

        scrapy crawl nfl
        #You can see all nfl teams are saved to nfl.json
