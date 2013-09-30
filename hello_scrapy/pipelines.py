# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import json

class HelloScrapyPipeline(object):
    def process_item(self, item, spider):
        return item
    
class NFLTeamPipeline(object):
    '''
        save nfl team information to nfl.json
    '''
    def __init__(self):
        self.file = open("nfl.json","w")
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

 

