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
            hi = response.urljoin(links[1])
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



    def addParse(self,response):
        price = response.css("td.ads_price::text").get()
        keys = response.css("td.ads_opt_name::text").getall()
        values = response.css("td.ads_opt")
        images = response.css('div.pic_dv_thumbnail a::attr(href)').getall()
        item = dict({ })
        item["images"] = images

        for i in range(len(keys)) :
            value = values[i].css("b::text").get() if values[i].css("b::text").get() else values[i].css("td.ads_opt::text").get()
            item[keys[i]] = value

        if(price):
            yield item

