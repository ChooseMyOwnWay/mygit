# -*- encoding: utf-8 -*-
import requests
import json
import random
import time
from prettytable import PrettyTable

from config import load_ua
from info import date, from_station, to_station, custom_train_no


class SelectTickets(object):

    def __init__(self):
        self.date = date
        self.train_no = custom_train_no
        self.from_station = from_station
        self.to_station = to_station
        self.FLAG = True
        self.headers = {
            'User-Agent': load_ua(),
        }
        self.url = "https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=%s&leftTicketDTO." \
                   "from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT" % (date, from_station, to_station)
        # 高级软卧、动卧、软座暂时没有找到相应的数据
        self.dict = {
            "swztdz_num": "商务座/特等座",
            "ydz_num": "一等座",
            "edz_num": "二等座",
            # "gjrw_num": "高级软卧",
            "rw_num": "软卧",
            # "dw_num": "动卧",
            "yw_num": "硬卧",
            # "rz_num": "软座",
            "yz_num": "硬座",
            "wz_num": "无座",
            "other": "其他",
            "train_code": "车次",
            "start_time": "出发时间",
            "arrive_time": "到达时间",
            "time": "历时",
        }

    def get_data(self):
        res = requests.get(self.url, verify=False, headers=self.headers)
        data_dict = json.loads(res.text)
        return data_dict.get('data').get('result')

    def parse_data(self, datas):
        """
        商务座 特等座	一等座 二等座	高级软卧 软卧	动卧	硬卧	软座	硬座	无座	其他
        """
        base_list = []
        for d in datas:
            base_dict = {}
            data = d.split('|')
            base_dict['train_code'] = data[3]
            base_dict['start_time'] = data[8]
            base_dict['arrive_time'] = data[9]
            base_dict['time'] = data[10]
            base_dict['swztdz_num'] = data[31]
            base_dict['ydz_num'] = data[32]
            base_dict['edz_num'] = data[30]
            base_dict['rw_num'] = data[23]
            base_dict['yw_num'] = data[28]
            base_dict['yz_num'] = data[29]
            base_dict['wz_num'] = data[26]
            if self.train_no and base_dict.get('train_code') in self.train_no:
                base_list.append(base_dict)
        return base_list

    def handle_result(self, base_list):
        """
        处理数据按照表格形式输出
        """
        for base_dict in base_list:
            keys_list = []
            values_list = []
            for key, value in base_dict.items():
                if key in self.dict.keys():
                    key_zh = self.dict[key]
                    keys_list.append(key_zh)
                value_zh = value if value != "" else "-"
                values_list.append(value_zh)
            table = PrettyTable(keys_list)
            table.padding_width = 1
            table.add_row(values_list)
            print table

    def run(self):
        # 1.获取数据
        datas = self.get_data()
        # 2.取值
        base_list = self.parse_data(datas)
        # 3.返回处理结果
        return self.handle_result(base_list)


if __name__ == '__main__':
    st = SelectTickets()
    try:
        seconds = random.randint(2, 5)
        time.sleep(seconds)
        st.run()
    except ValueError:
        raise ValueError("查询失败，请重新尝试>_<")
    except Exception as e:
        raise Exception(e)
