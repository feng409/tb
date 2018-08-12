# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Comment(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nickname = scrapy.Field()
    content = scrapy.Field()
    append_comment = scrapy.Field()
    photos = scrapy.Field()
    videos = scrapy.Field()
    # 店铺信息
    goods_url = scrapy.Field()
    goods_title = scrapy.Field()


class TbCommentItem(scrapy.Item):
    def __init__(self, values):
        kw = {key: value for key, value in values.items() if key in TbCommentItem.__dict__['fields'].keys()}
        super(TbCommentItem, self).__init__(kw)

    shop = scrapy.Field()
    date = scrapy.Field()
    shareInfo = scrapy.Field()
    showDepositIcon = scrapy.Field()
    o2oRate = scrapy.Field()
    mainTradeId = scrapy.Field()
    raterType = scrapy.Field()
    validscore = scrapy.Field()
    video = scrapy.Field()
    photos = scrapy.Field()
    content = scrapy.Field()
    rateId = scrapy.Field()
    spuRatting = scrapy.Field()
    auction = scrapy.Field()
    award = scrapy.Field()
    rate = scrapy.Field()
    creditFraudRule = scrapy.Field()
    appendCanExplainable = scrapy.Field()
    _from = scrapy.Field()
    tag = scrapy.Field()
    propertiesAvg = scrapy.Field()
    reply = scrapy.Field()
    dayAfterConfirm = scrapy.Field()
    lastModifyFrom = scrapy.Field()
    bidPriceMoney = scrapy.Field()
    noQna = scrapy.Field()
    promotionType = scrapy.Field()
    vicious = scrapy.Field()
    enableSNS = scrapy.Field()
    appendList = scrapy.Field()
    buyAmount = scrapy.Field()
    showCuIcon = scrapy.Field()
    serviceRate = scrapy.Field()
    useful = scrapy.Field()
    user = scrapy.Field()
    append = scrapy.Field()
    status = scrapy.Field()


class TMallCommentItem(scrapy.Item):
    def __init__(self, values):
        kw = {key: value for key, value in values.items() if key in TMallCommentItem.__dict__['fields'].keys()}
        super(TMallCommentItem, self).__init__(kw)

    shop = scrapy.Field()
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
    def __init__(self, values):
        kw = {key: value for key, value in values.items() if key in ShopItem.__dict__['fields'].keys()}
        super(ShopItem, self).__init__(kw)

    i2iTags = scrapy.Field()
    p4p = scrapy.Field()
    p4pSameHeight = scrapy.Field()
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

