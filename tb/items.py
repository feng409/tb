# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CommentItem(scrapy.Item):
    displayUserNick = scrapy.Field()  # 用户昵称
    rateContent = scrapy.Field()  # 评论内容
    rateDate = scrapy.Field()  # 评论日期 2017-10-14 12:47:04
    aliMallSeller = scrapy.Field()
    anony = scrapy.Field()
    appendComment = scrapy.Field()
    attributes = scrapy.Field()
    attributesMap = scrapy.Field()
    aucNumId = scrapy.Field()
    auctionPicUrl = scrapy.Field()
    auctionPrice = scrapy.Field()
    auctionSku = scrapy.Field()
    auctionTitle = scrapy.Field()
    buyCount = scrapy.Field()
    carServiceLocation = scrapy.Field()
    cmsSource = scrapy.Field()
    displayRatePic = scrapy.Field()
    displayRateSum = scrapy.Field()
    displayUserLink = scrapy.Field()
    displayUserNumId = scrapy.Field()
    displayUserRateLink = scrapy.Field()
    dsr = scrapy.Field()
    fromMall = scrapy.Field()
    fromMemory = scrapy.Field()
    gmtCreateTime = scrapy.Field()
    goldUser = scrapy.Field()
    headExtraPic = scrapy.Field()
    _id = scrapy.Field()
    memberIcon = scrapy.Field()
    pics = scrapy.Field()
    picsSmall = scrapy.Field()
    position = scrapy.Field()
    reply = scrapy.Field()
    sellerId = scrapy.Field()
    serviceRateContent = scrapy.Field()
    structuredRateList = scrapy.Field()
    tamllSweetLevel = scrapy.Field()
    tmallSweetPic = scrapy.Field()
    tradeEndTime = scrapy.Field()
    tradeId = scrapy.Field()
    useful = scrapy.Field()
    userIdEncryption = scrapy.Field()
    userInfo = scrapy.Field()
    userVipLevel = scrapy.Field()
    userVipPic = scrapy.Field()


class ShopItem(scrapy.Item):
    i2iTags = scrapy.Field()
    p4pTags = scrapy.Field()
    nid = scrapy.Field()
    category = scrapy.Field()
    pid = scrapy.Field()
    title = scrapy.Field()
    raw_title = scrapy.Field()
    pic_url = scrapy.Field()
    detail_url = scrapy.Field()
    view_price = scrapy.Field()
    view_fee = scrapy.Field()
    item_loc = scrapy.Field()
    view_sales = scrapy.Field()
    comment_count = scrapy.Field()
    user_id = scrapy.Field()
    nick = scrapy.Field()
    shopcard = scrapy.Field()
    icon = scrapy.Field()
    comment_url = scrapy.Field()
    shopLink = scrapy.Field()
    risk = scrapy.Field()
