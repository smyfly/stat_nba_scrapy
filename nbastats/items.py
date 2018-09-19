# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class NbastatsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    team=scrapy.Field()
    season=scrapy.Field()
    absent=scrapy.Field()
    first=scrapy.Field()
    time=scrapy.Field()
    shoot=scrapy.Field()
    hit=scrapy.Field()
    hand=scrapy.Field()
    shoot3=scrapy.Field()
    hit3=scrapy.Field()
    hand3=scrapy.Field()
    penalty=scrapy.Field()
    hit1=scrapy.Field()
    hand1=scrapy.Field()
    rebound=scrapy.Field()
    frontrebound=scrapy.Field()
    behindrebound=scrapy.Field()
    assist=scrapy.Field()
    steal=scrapy.Field()
    block=scrapy.Field()
    fault=scrapy.Field()
    foul=scrapy.Field()
    score=scrapy.Field()
    win=scrapy.Field()
    lose=scrapy.Field()

    rebound_rate=scrapy.Field()
    attackrebound_rate=scrapy.Field()
    defendrebound_rate=scrapy.Field()
    assist_rate=scrapy.Field()
    steal_rate=scrapy.Field()
    block_rate=scrapy.Field()
    fault_rate=scrapy.Field()
    use_rate=scrapy.Field()
    attack_efficient=scrapy.Field()
    defend_efficient=scrapy.Field()
    ws=scrapy.Field()
    attack_ws=scrapy.Field()
    defend_ws=scrapy.Field()
    per_value=scrapy.Field()
    dunk=scrapy.Field()
    foul_plus_one=scrapy.Field()

    hand_distance=scrapy.Field()
    bottom_hit_rate=scrapy.Field()
    bottom_hit=scrapy.Field()
    bottom_hand=scrapy.Field()
    bottom_part_rate=scrapy.Field()
    close_hit_rate=scrapy.Field()
    close_hit=scrapy.Field()
    close_hand=scrapy.Field()
    close_part_rate=scrapy.Field()
    middle_hit_rate=scrapy.Field()
    middle_hit=scrapy.Field()
    middle_hand=scrapy.Field()
    middle_part_rate=scrapy.Field()
    remote_hit_rate=scrapy.Field()
    remote_hit=scrapy.Field()
    remote_hand=scrapy.Field()
    remote_part_rate=scrapy.Field()
    real_hit=scrapy.Field()
    shoot_efficient=scrapy.Field()

    pass
