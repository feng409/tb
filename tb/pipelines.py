# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from tb.items import TbCommentItem, TMallCommentItem, Comment
from scrapy.exceptions import DropItem


class ParsePipeline(object):
    """
    转换提取爬虫信息
    """

    def process_item(self, item, spider):
        values = {}
        if isinstance(item, TbCommentItem):
            values['nickname'] = item['user']['nick']
            values['content'] = item['content']
            values['append_comment'] = ''
            values['photos'] = [photo['url'] for photo in item['photos']]
            values['videos'] = item['video']
        elif isinstance(item, TMallCommentItem):
            values['nickname'] = item['displayUserNick']
            values['content'] = item['rateContent']
            values['photos'] = item['pics']
            if item['append_comment']:
                values['append_comment'] = item['appendComment']['content']
                if item['append_comment']['pics']:
                    values['photos'] += item['append_comment']['pics']
        return Comment(values)


class ContentPipeline(object):
    """过滤默认评论"""
    def process_item(self, item, spider):
        if item['content'] is '评价方未及时做出评价,系统默认好评!' \
                or item['content'] is '此用户没有填写评论!':
            raise DropItem(item)
        else:
            return item


class LengthPipeline(object):
    """长度过滤"""
    def process_item(self, item, spider):
        if len(item['content']) < 15:
            raise DropItem(item)
        return item


class GoodPipeline(object):
    """淘宝好评过滤"""
    def process_item(self, item, spider):
        if isinstance(item, TbCommentItem) and item['rate'] is not '1':
            raise DropItem(item)
        return item
