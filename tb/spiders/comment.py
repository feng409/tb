# -*- coding: utf-8 -*-
import scrapy
from tb.items import CommentItem, ShopItem
from urllib.parse import urlencode
import json
import re

URL_COMMENT_TAOBAO = ''
URL_COMMENT_TMAIL = 'https://rate.tmall.com/list_detail_rate.htm?itemId=%s&sellerId=%s'

class CommentSpider(scrapy.Spider):
    name = 'comment'
    # start_urls = ['https://rate.tmall.com/list_detail_rate.htm?%s' % format(urlencode({
    #     'itemId': 520552957694,
    #     'sellerId': 877891455
    # }))]
    start_urls = ['https://s.taobao.com/search?q=蟹老板&ie=utf8']

    def parse(self, response):
        _ = re.findall('g_page_config = (\{.*\});', response.text)[0]
        data = json.loads(_)
        for shop in data['mods']['itemlist']['data']['auctions']:
            yield ShopItem(shop)
            # todo 根据不同店面parse
            yield scrapy.Request()

    def parse_comment_taobao(self, response):
        # 真特么有毒的返回，不是标准json的json
        data = json.loads('{%s}' % response.text.strip())
        # 过滤id关键字
        items = []
        for _ in data['ratedetail']['ratelist']:
            _['_id'] = _['id']
            del _['id']
            items.append(CommentItem(_))
        return items

    def parse_comment_tmail(self, response):
        pass
