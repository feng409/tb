# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request import Request
from tb.items import TMallCommentItem, TbCommentItem, ShopItem
import json
import re

URL_COMMENT_TAOBAO = 'https://rate.taobao.com/feedRateList.htm?auctionNumId={item_id}&userNumId={user_id}&currentPageNum={current_page}&pageSize=20'
URL_COMMENT_TMALL = 'https://rate.tmall.com/list_detail_rate.htm?itemId={item_id}&sellerId={user_id}&currentPage={current_page}'


class CommentSpider(scrapy.Spider):
    name = 'comment'

    def __init__(self, keyword=None):
        self.start_urls = [
            'https://s.taobao.com/search?q=%s&ie=utf8' % keyword
        ]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, cookies=self.settings['COOKIE'])

    def parse(self, response):
        _ = re.findall('g_page_config = (\{.*\});', response.text)[0]
        data = json.loads(_)
        limit = 3
        for shop in data['mods']['itemlist']['data']['auctions']:
            # yield ShopItem(shop)
            # todo 根据不同店面parse
            if limit:
                limit = limit - 1
                meta = {'shop': shop}
                if 'tmall.com' in shop['comment_url']:
                    yield scrapy.Request(
                        url=URL_COMMENT_TMALL.format(item_id=shop['nid'], user_id=shop['user_id'], current_page=1),
                        callback=self.parse_comment_tmall,
                        cookies=self.settings['COOKIE'],
                        meta=meta)
                else:
                    yield scrapy.Request(
                        URL_COMMENT_TAOBAO.format(item_id=shop['nid'], user_id=shop['user_id'], current_page=1),
                        callback=self.parse_comment_taobao,
                        meta=meta)

    def parse_comment_tmall(self, response):
        # 真特么有毒的返回，不是标准json的json
        data = json.loads('{%s}' % response.text.strip())
        # 过滤id关键字
        for _ in data['rateDetail']['rateList']:
            _['_id'] = _['id']
            del _['id']
            _['shop'] = response.meta['shop']
            item = TMallCommentItem(_)
            yield item

        # 抓取下一页
        current_page = int(data['rateDetail']['paginator']['page'])
        max_page = int(data['rateDetail']['paginator']['lastPage'])
        if current_page < max_page:
            item_id = response.meta['shop']['nid']
            user_id = response.meta['shop']['user_id']
            yield scrapy.Request(
                url=URL_COMMENT_TMALL.format(item_id=item_id, user_id=user_id, current_page=current_page + 1),
                callback=self.parse_comment_tmall,
                cookies=self.settings['COOKIE'],
                meta=response.meta)

    def parse_comment_taobao(self, response):
        data = json.loads(response.text.strip()[1:-1])
        comments = data['comments']
        for comment in comments:
            comment['_from'] = comment['from']
            comment['shop'] = response.meta['shop']
            del comment['from']
            item = TbCommentItem(comment)
            yield item
        # 抓取下一页
        current_page = int(data['currentPageNum'])
        max_page = int(data['maxPage'])
        if current_page < max_page and False:
            item_id = response.meta['shop']['nid']
            user_id = response.meta['shop']['user_id']
            yield scrapy.Request(
                url=URL_COMMENT_TAOBAO.format(item_id=item_id, user_id=user_id, current_page=current_page + 1),
                callback=self.parse_comment_taobao,
                cookies=self.settings['COOKIE'],
                meta=response.meta)

