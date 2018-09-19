# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import CsvItemExporter

class NbastatsPipeline(object):
    def open_spider(self, spider):
        self.file = open('nba_stat.csv', 'w+b')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

'''
from scrapy.exporters import JsonItemExporter

class JsonExporterPipeline(object):
    # 调用Scrapy提供的JsonExporter导出Json文件。
    def __init__(self):
        self.file = open('nba_stat.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding="utf-8", ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def start_exporting(self):
        self.file.write(b"[\n")

    def finish_exporting(self):
        self.file.write(b"\n]")

'''