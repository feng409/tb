# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from tb.items import TbCommentItem, TMallCommentItem, Comment, ShopItem
from scrapy.exceptions import DropItem
import pymysql


class ShopPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, ShopItem):
            raise DropItem('shop item')
        else:
            return item


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
            values['photos'] = ['http:' + photo['url'] for photo in item['photos']]
            values['videos'] = 'http:' + item['video']['cloudVideoUrl'] if item['video'] else ''
        elif isinstance(item, TMallCommentItem):
            values['nickname'] = item['displayUserNick']
            values['content'] = item['rateContent']
            values['photos'] = ['http:' + pic for pic in item['pics']]
            if item.get('appendComment', None):
                values['append_comment'] = item['appendComment']['content']
                if item['appendComment'].get('pics', None):
                    values['photos'] += item['appendComment']['pics']
        if values['photos']:
            values['photos'] = '\n'.join(values['photos'])

        # 妈的直通车链接自带https开头
        values['goods_url'] = 'https:' + item['shop']['detail_url'] if item['shop']['detail_url'][:2] == '//' else item['shop']['detail_url']
        values['goods_title'] = item['shop']['raw_title']
        values['shop_id'] = item['shop']['nid']
        return Comment(values)


class ContentPipeline(object):
    """过滤默认评论"""
    def process_item(self, item, spider):
        _filter = ('此用户没有填写评价。',
                   '评价方未及时做出评价,系统默认好评!')
        if item['content'] in _filter:
            raise DropItem('默认好评')
        else:
            return item


class LengthPipeline(object):
    """长度过滤"""
    def process_item(self, item, spider):
        if len(item['content']) < 15:
            raise DropItem('长度太低')
        return item


class GoodPipeline(object):
    """淘宝好评过滤"""
    def process_item(self, item, spider):
        if isinstance(item, TbCommentItem) and item['rate'] is not '1':
            if item['rate'] == 0:
                raise DropItem('中评')
            else:
                raise DropItem('差评')
        return item


class MysqlPipeline(object):
    def process_item(self, item, spider):
        sql = """
        INSERT INTO `comments` (`nid`, `goods_url` , `goods_title`, `nickname`, `content`, `append_comment`, `videos`, `photos`) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        
        """
        self.cursor.execute(sql, [item.get(key, '') for key in ('shop_id,goods_url,goods_title,nickname,content,append_comment,videos,photos'.split(','))])
        self.db.commit()

    def open_spider(self, spider):
        print('''
        ##########################打开数据库###################
        ''')
        from .settings import MYSQL_HOST, MYSQL_DB, MYSQL_USER, MYSQL_CHARSET, MYSQL_PASS
        self.db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASS, db=MYSQL_DB, charset=MYSQL_CHARSET)
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        print('''
        ########################关闭数据库##################
        ''')
        self.db.close()

