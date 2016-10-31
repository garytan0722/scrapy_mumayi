# -*- coding: utf-8 -*-

import json
import base64
from scrapy_splash import SplashRequest
import scrapy
from apk1.items import Apk1Item
class apkspider(scrapy.Spider):
    name = "mumayi"
    allowed_domains = ["down.mumayi.com","www.mumayi.com"]
    start_urls = ["http://www.mumayi.com/android-18.html"]

    def parse(self, response):
        res=response.xpath('//a[@class="download fl"]/@href').extract()
        #print (response.body)
        print (res)
        yield scrapy.Request(res[0], callback=self.download)
    def download(self, response):
        link=response.url
        print("APK FILE DST:"+link)
        myitem = Apk1Item()
        myitem["file_urls"]=[link]
        yield myitem

     