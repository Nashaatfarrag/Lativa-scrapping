import scrapy

class realstate(scrapy.Spider):
    name = "mainSpider"

    start_urls = ["https://www.ss.com/lv/real-estate/"]

    def parse(self,response):
        links = response.css('a.a_category::attr(href)').getall()
        ads_links = response.css('a.am::attr(href)').getall()

        # print(links)
        output = []
        if(links):
            hi = response.urljoin(links[0])
            yield scrapy.Request(hi,callback=self.parse)

        if(ads_links):
            for ad_link in ads_links :
                test = response.urljoin(ad_link)
                yield scrapy.Request(test,callback=self.addParse)

            # next_page = response.css('a[rel="next"]::attr(href)').get()
            # yield next_page
            # if(next_page[-1] == 'l'):
            #     test1 = response.urljoin(next_page)
            #     yield scrapy.Request(test1,callback=self.parse)


            # next_page = response.css(link::attr(href)).getall()

    def addParse(self,response):
        price = response.css("td.ads_price::text").get()
        keys = response.css("td.ads_opt_name::text").getall()
        values = response.css("td.ads_opt").getall()
        images = response.css('div.pic_dv_thumbnail a::attr(href)').getall()
        item = dict({
            "images" : images,
            "keys" : keys ,
            "values" : values

            # "len keys " : len(keys),
            # "len values " : len(values)
        })
        # for i in range(len(keys)) :

            # item[keys[i]] = "x"
        if(price):
            yield item

