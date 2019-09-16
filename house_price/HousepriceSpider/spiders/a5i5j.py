# -*- coding: utf-8 -*-
import time

import scrapy
from HousepriceSpider.items import Woi5jItem

from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class A5i5jSpider(scrapy.Spider):
    name = '5i5j'
    start_urls = ['https://sh.5i5j.com/ershoufang/']

    def parse(self, response):
        soup = BeautifulSoup(response.body,'html.parser')
        house_ul = soup.find('ul',attrs={'class':'pList'})
        house_list = house_ul.find_all('li')
        for house in house_list:
            item = Woi5jItem()
            #解析title
            title_div = house.find('h3',attrs={'class':'listTit'})
            title = title_div.get_text()
            detail_url = 'https://sh.5i5j.com' + title_div.a.get('href').strip()

            #解析规格详情
            house_spec_list = house.find_all('p')
            spec_data_list = []
            for house_spec in house_spec_list:
                txt = house_spec.get_text().strip()
                spec_data_list.append(txt)
            price = spec_data_list[-2]
            price_per_area = spec_data_list[-1]

            #解析标签
            label_data_list = []
            label_div = house.find('div',attrs={'class':'listTag'})
            if label_div:
                label_list = label_div.find_all('span')
                for label in label_list:
                    label_txt = label.get_text().strip()
                    label_data_list.append(label_txt)

            item['title'] = title
            item['detail_url'] = detail_url
            item['price'] = price
            item['price_per_area'] = price_per_area.split(u'万')[0]
            item['label'] = ';'.join(label_data_list)
            yield scrapy.Request(url=detail_url,
                                  callback=self.parseDetail,
                                  meta={
                                      'item':item,
                                      'spec_data_list':spec_data_list
                                        }
                                  )
        next_page_div = soup.find('div',attrs={'class':'pageSty'})
        next_page_url = next_page_div.find('a',attrs={'class':'cPage'})
        if next_page_url:
            next_url = 'https://sh.5i5j.com' + next_page_url.get('href')
            yield scrapy.Request(url=next_url,callback=self.parse)


    def parseDetail(self,response):

        item = response.meta.get('item')
        spec_data_list = response.meta.get('spec_data_list')

        soup = BeautifulSoup(response.body.encode('utf-8'),'html.parser')

        # retry =

        # main_container = soup.find('div',attrs={'class':'main container'})
        wrapper = soup.find('div',attrs={'class':'wrapper'})
        house_id = wrapper.find('span',attrs={'class':'del-houseid'}).get_text()
        if house_id:
            house_id = house_id.split(':')[-1]
            item['house_id'] = house_id
        details_view = soup.find('div',attrs={'class':'details-view'})
        house_type = details_view.find('div',attrs={'class':'housesty'})
        house_spec = house_type.find('div',attrs={'class':'clear'})
        house_spec_list = house_spec.find_all('div',attrs={'class':'jlquannei'})
        for spec in house_spec_list:
            value = spec.find('p',attrs={'class':'jlinfo'}).get_text().strip()
            key = spec.find('p',attrs={'class':'cjname'}).get_text().strip()
            if key == '售价':
                item['price'] = value
            elif key == '单价':
                item['price_per_area'] = value
            elif key == '户型':
                item['house_type'] = value
            elif key == '建筑面积':
                item['area'] = value
        #列表页规格解析
        last_line = spec_data_list[2]
        if '发布' in last_line:
            release_date = last_line.split('.')[-1].split('发布')[0]
            item['release_date'] = release_date



        #详情列表解析
        more_spec = soup.find('div',attrs={'class':'zushous'})
        more_spec_list = more_spec.find_all('li')
        for li in more_spec_list:
            key = li.span.get_text().strip()
            value = li.get_text().strip()
            if key == '小区：':
                item['community'] = value
            elif key == '楼层：':
                item['floor_level'] = value
            elif key == '朝向：':
                item['orientation'] = value
            elif key =='装修：':
                item['decoration'] = value
            elif key == '规划用途：':
                item['usage'] = value
            elif key == '年代：':
                item['build_time'] = value
            elif key == '商圈：':
                item['commercial_zone'] = value
            elif key == '地铁：':
                item['transportation'] = value

        #看房记录解析
        watch_record = soup.find_all('div',attrs={'class':'daikanquan'})
        for record in watch_record:
            value = record.find('p',attrs={'class':'jlinfo'}).get_text().strip()
            key = record.find('p',attrs={'class':'cjname'}).get_text().strip()
            if key == '最近带看':
                item['latest_watch_time'] = value
            elif key == '近30天带看':
                item['watch_num'] = value
            elif key == '累计带看':
                item['total_watch'] = value

        #小区信息解析
        community_soup = soup.find('div',attrs={'class':'infomain'})
        community_info_list = community_soup.find_all('li')
        for community_info in community_info_list:
            try:
                key = community_info.span.get_text().strip()
                value = community_info.get_text().strip()
                if key == '小区均价':
                    item['community_average_price'] = value
                elif key == '建筑年代':
                    item['build_time'] = value
                elif key == '所在商圈':
                    item['commercial_zone'] = value
            except:
                key = community_info.a.get_text().strip()
                if '小区在售房源' in key:
                    value = key[5:-1]
                    item['community_selling_house_num'] = value
                elif '小区在租房源' in key:
                    value = key[5:-1]
                    item['community_renting_house_num'] = value
        yield item













