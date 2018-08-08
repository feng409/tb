# -*- coding: utf-8 -*-
import scrapy
from tb.items import CommentItem, ShopItem
from urllib.parse import urlencode
import json
import re

URL_COMMENT_TAOBAO = 'https://rate.taobao.com/feedRateList.htm?auctionNumId={item_id}&userNumId={user_id}&currentPageNum=1&pageSize=20'
URL_COMMENT_TMALL = 'https://rate.tmall.com/list_detail_rate.htm?itemId={item_id}&sellerId={user_id}&currentPage={current_page}'


class CommentSpider(scrapy.Spider):
    name = 'comment'
    # start_urls = ['https://rate.tmall.com/list_detail_rate.htm?%s' % format(urlencode({
    #     'itemId': 520552957694,
    #     'sellerId': 877891455
    # }))]
    # start_urls = ['https://s.taobao.com/search?q=蟹老板&ie=utf8']
    def start_requests(self):
        item_id = 40333487112
        user_id = 2081957625
        return [scrapy.Request(
                    url=URL_COMMENT_TMALL.format(item_id=item_id, user_id=user_id, current_page=1),
                    callback=self.parse_comment_tmall,
                    cookies=self.settings['COOKIE'],
                    meta={'item_id': item_id, 'user_id': user_id})]

    def parse(self, response):
        _ = re.findall('g_page_config = (\{.*\});', response.text)[0]
        data = json.loads(_)
        for shop in data['mods']['itemlist']['data']['auctions']:
            yield ShopItem(shop)
            # todo 根据不同店面parse
            if 'tmall.com' in shop['comment_url']:
                print(URL_COMMENT_TMALL.format(item_id=shop['nid'], user_id=shop['user_id']))
                yield scrapy.Request(
                    url=URL_COMMENT_TMALL.format(item_id=shop['nid'], user_id=shop['user_id'], current_page=1),
                    callback=self.parse_comment_tmall,
                    cookies=self.settings['COOKIE'],
                    meta={'item_id': shop['nid', 'user_id': shop['user_id']]})
            else:
                yield scrapy.Request(
                    URL_COMMENT_TAOBAO.format(item_id=shop['nid'], user_id=shop['user_id']),
                    callback=self.parse_comment_taobao,
                    meta={'item_id': shop['nid', 'user_id': shop['user_id']]})

    def parse_comment_tmall(self, response):
        # 真特么有毒的返回，不是标准json的json
        data = json.loads('{%s}' % response.text.strip())
        # 过滤id关键字
        for _ in data['rateDetail']['rateList']:
            _['_id'] = _['id']
            del _['id']
            item = CommentItem(_)
            print('tmail ->', _['rateContent'], end='\n\n')
            yield item

        # 抓取下一页
        current_page = int(data['rateDetail']['paginator']['page'])
        max_page = int(data['rateDetail']['paginator']['lastPage'])
        if current_page < max_page:
            item_id = response.meta['item_id']
            user_id = response.meta['user_id']
            yield scrapy.Request(
                url=URL_COMMENT_TMALL.format(item_id=item_id, user_id=user_id, current_page=current_page + 1),
                callback=self.parse_comment_tmall,
                cookies=self.settings['COOKIE'],
                meta={'item_id': item_id, 'user_id': user_id})

    def parse_comment_taobao(self, response):
        comments = json.loads(response.text.strip()[1:-1])['comments']
        for comment in comments:
            print('taobao -> ', comment['content'], end='\n\n')
