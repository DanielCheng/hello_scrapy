A scrapy hello world project for runnable
===
Objectives
---
* Find All NFL Teams and their official site link from nfl.com
* Save all teams's logo to TeamName.png

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

* run the spider

        scrapy crawl nfl -o nfl.json -t json
        #You can see all nfl teams are saved to nfl.json
