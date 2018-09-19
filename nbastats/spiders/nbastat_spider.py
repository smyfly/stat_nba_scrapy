# -*- coding: utf-8 -*-
import scrapy
from nbastats.items import NbastatsItem

playerlist_url=["http://www.stat-nba.com/playerList.php"]
player_url="http://www.stat-nba.com/player/{url}"
split_url="./player/"
name_split="/"
detail_mapping={
    1:'season',
    2:'team',
    3:'absent',
    4:'first',
    5:'time',
    6:'shoot',
    7:'hit',
    8:'hand',
    9:'shoot3',
    10:'hit3',
    11:'hand3',
    12:'rebound',
    13:'frontrebound',
    14:'behindrebound',
    15:'penalty',
    16:'hit1',
    17:'hand1',
    18:'assist',
    19:'steal',
    20:'block',
    21:'fault',
    22:'foul',
    23:'score',
    24:'win',
    25:'lose'}
advanced_mapping={
    3:'rebound_rate',
    4:'attackrebound_rate',
    5:'defendrebound_rate',
    6:'assist_rate',
    7:'steal_rate',
    8:'block_rate',
    9:'fault_rate',
    10:'use_rate',
    11:'attack_efficient',
    12:'defend_efficient',
    13:'ws',
    14:'attack_ws',
    15:'defend_ws',
    16:'per_value',
    17:'dunk',
    18:'foul_plus_one'}
shooting_mapping={
    3:'hand_distance',
    4:'bottom_hit_rate',
    5:'bottom_hit',
    6:'bottom_hand',
    7:'bottom_part_rate',
    8:'close_hit_rate',
    9:'close_hit',
    10:'close_hand',
    11:'close_part_rate',
    12:'middle_hit_rate',
    13:'middle_hit',
    14:'middle_hand',
    15:'middle_part_rate',
    16:'remote_hit_rate',
    17:'remote_hit',
    18:'remote_hand',
    19:'remote_part_rate',
    20:'real_hit',
    21:'shoot_efficient'}


class NbastatSpiderSpider(scrapy.Spider):
    name = 'nbastat_spider'
    allowed_domains = ['www.stat-nba.com']
    start_urls = playerlist_url#['http://www.stat-nba.com/']
    
    def parse(self, response):
        playerlist=response.xpath('//*[@class="allstarplayer"]')
        for item in playerlist:
            detail_url=item.xpath(".//@href").extract()[0].split(split_url)[1].strip()
            player_detail_url = player_url.format(url=detail_url)
            
            request = scrapy.Request(player_detail_url, callback=self.parse_detail)
            yield request

    def parse_detail(self, response):
        detail_list=response.xpath('//*[@id="stat_box_avg"]/tbody/tr[@class="sort"]')
        advanced_list=response.xpath('//*[@id="stat_box_advanced_basic"]/tbody/tr[@class="sort"]')#进阶数据
        shooting_list=response.xpath('//*[@id="stat_box_advanced_shooting"]/tbody/tr[@class="sort"]')#进阶数据-投篮
        name=response.xpath('//*[@id="background"]/div[4]/div[2]/text()').extract()[0].split(name_split)[1].strip()
        
        for obj in zip(detail_list,advanced_list,shooting_list):#detail_tr,advanced_tr,shooting_tr
            nba_item = NbastatsItem()
            nba_item['name']=name

            detail_td=obj[0].xpath('.//td')
            advanced_td=obj[1].xpath('.//td')
            shooting_td=obj[2].xpath('.//td')
            for i,item_detail in enumerate(detail_td):
                try:
                    if detail_mapping[i]!='':
                        nba_item[detail_mapping[i]]=item_detail.xpath('.//text()').extract()[0]
                        print(detail_mapping[i]+":"+nba_item[detail_mapping[i]])
                except KeyError:
                    continue
            
            for j,item_advanced in enumerate(advanced_td):           
                try:
                    if advanced_mapping[j]!='':
                        nba_item[advanced_mapping[j]]=item_advanced.xpath('.//text()').extract()[0]
                except KeyError:
                    continue

            for k,item_shooting in enumerate(shooting_td):
                try:
                    if shooting_mapping[k]!='':
                        nba_item[shooting_mapping[k]]=item_shooting.xpath('.//text()').extract()[0]
                except KeyError:
                    continue
              
            yield nba_item
