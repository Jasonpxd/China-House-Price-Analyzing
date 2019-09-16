# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

import requests
import scrapy
from scrapy import signals
from settings import USER_AGENT_LIST
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class HousepricespiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class HousepricespiderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        rand_use = random.choice(USER_AGENT_LIST)
        # if rand_use:
        #     request.headers.setdefault('User-Agent', rand_use)
        #     request.cookies = {'_ga':'GA1.2.624411560.1567089317',
        #                        'yfx_c_g_u_id_10000001':'_ck19082922351617009275132107617',
        #                        'yfx_mr_f_n_10000001':'baidu%3A%3Amarket_type_cpc%3A%3A%3A%3Abaidu_ppc%3A%3A%25e4%25b8%258a%25e6%25b5%25b7%25e6%2588%25bf%25e4%25bb%25b7%25e8%25b5%25b0%25e5%258a%25bf%3A%3A%3A%3A%25E4%25B8%258A%25E6%25B5%25B7%25E6%2588%2591%25E7%2588%25B1%25E6%2588%2591%25E5%25AE%25B6%3A%3Awww.baidu.com%3A%3A92661210024%3A%3A%3A%3A%25E5%2593%2581%25E7%2589%258C%25E8%25AF%258D%3A%3A%25E5%259C%25B0%25E5%259F%259F-%25E5%2593%2581%25E7%2589%258C%3A%3A41%3A%3Apmf_from_adv%3A%3Ash.5i5j.com%2F',
        #                        'smidV2':'2019082922352813247bc49628311fc574767ea01dcb4b009bc46036bed0a00',
        #                        'PHPSESSID':'dj6eqdi62go7n0fipnc8m93mbk',
        #                        '_gid':'GA1.2.1365559642.1567824004',
        #                        'yfx_mr_n_10000001':'baidu%3A%3Amarket_type_ppzq%3A%3A%3A%3Abaidu_ppc%3A%3A%25e6%2588%2591%25e7%2588%25b1%25e6%2588%2591%25e5%25ae%25b6%3A%3A%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3Asp0.baidu.com%3A%3A%3A%3A%3A%3A%25E5%25B7%25A6%25E4%25BE%25A7%25E6%25A0%2587%25E9%25A2%2598%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3A179%3A%3Apmf_from_adv%3A%3Ash.5i5j.com%2F',
        #                        'yfx_key_10000001':'%25e6%2588%2591%25e7%2588%25b1%25e6%2588%2591%25e5%25ae%25b6',
        #                        'Hm_lvt_94ed3d23572054a86ed341d64b267ec6':'1567089319,1567824004',
        #                        'ershoufang_BROWSES':'37730441%2C35163429%2C43189292%2C43340944%2C43303768',
        #                        'domain':'sh',
        #                        '_Jo0OQK':'1537439BE95C29482F036F1F9D214019F1E85FE74C07B55AADBA2476A20F250BD7C013E27E2769292462D4C7086AE418C31C811E632B84AB6B9A6D6E64324227639A3A6B6373DCEA275A28E4E02FA79F6B8A28E4E02FA79F6B8B773E863E48C8F2A20D2F0A621A51499GJ1Z1Kg==',
        #                        'yfx_f_l_v_t_10000001':'f_t_1567089316687__r_t_1567914603646__v_t_1567935074986__r_c_2',
        #                        '_gat':'1',
        #                        'Hm_lpvt_94ed3d23572054a86ed341d64b267ec6':'1567936419'
        #                        }
        # return None
        cookies = '_ga=GA1.2.624411560.1567089317; yfx_c_g_u_id_10000001=_ck19082922351617009275132107617; yfx_mr_f_n_10000001=baidu%3A%3Amarket_type_cpc%3A%3A%3A%3Abaidu_ppc%3A%3A%25e4%25b8%258a%25e6%25b5%25b7%25e6%2588%25bf%25e4%25bb%25b7%25e8%25b5%25b0%25e5%258a%25bf%3A%3A%3A%3A%25E4%25B8%258A%25E6%25B5%25B7%25E6%2588%2591%25E7%2588%25B1%25E6%2588%2591%25E5%25AE%25B6%3A%3Awww.baidu.com%3A%3A92661210024%3A%3A%3A%3A%25E5%2593%2581%25E7%2589%258C%25E8%25AF%258D%3A%3A%25E5%259C%25B0%25E5%259F%259F-%25E5%2593%2581%25E7%2589%258C%3A%3A41%3A%3Apmf_from_adv%3A%3Ash.5i5j.com%2F; smidV2=2019082922352813247bc49628311fc574767ea01dcb4b009bc46036bed0a00; PHPSESSID=dj6eqdi62go7n0fipnc8m93mbk; _gid=GA1.2.1365559642.1567824004; yfx_mr_n_10000001=baidu%3A%3Amarket_type_ppzq%3A%3A%3A%3Abaidu_ppc%3A%3A%25e6%2588%2591%25e7%2588%25b1%25e6%2588%2591%25e5%25ae%25b6%3A%3A%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3Asp0.baidu.com%3A%3A%3A%3A%3A%3A%25E5%25B7%25A6%25E4%25BE%25A7%25E6%25A0%2587%25E9%25A2%2598%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3A179%3A%3Apmf_from_adv%3A%3Ash.5i5j.com%2F; yfx_key_10000001=%25e6%2588%2591%25e7%2588%25b1%25e6%2588%2591%25e5%25ae%25b6; Hm_lvt_94ed3d23572054a86ed341d64b267ec6=1567089319,1567824004; ershoufang_BROWSES=37730441%2C35163429%2C43189292%2C43340944%2C43303768; domain=sh; _Jo0OQK=1537439BE95C29482F036F1F9D214019F1E85FE74C07B55AADBA2476A20F250BD7C013E27E2769292462D4C7086AE418C31C811E632B84AB6B9A6D6E64324227639A3A6B6373DCEA275A28E4E02FA79F6B8A28E4E02FA79F6B8B773E863E48C8F2A20D2F0A621A51499GJ1Z1Kg==; yfx_f_l_v_t_10000001=f_t_1567089316687__r_t_1567914603646__v_t_1567935074986__r_c_2; _gat=1; Hm_lpvt_94ed3d23572054a86ed341d64b267ec6=1567936419'
        headers = {
            'User-Agent':rand_use,
            'Cookie':cookies
        }
        res = requests.get(request.url,headers=headers)
        html = res.content
        return scrapy.http.HtmlResponse(request.url, encoding='utf-8', status=200, body=html)

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
