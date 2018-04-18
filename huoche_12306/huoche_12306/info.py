# -*- coding: utf-8 -*-

from config import get_station_val

date = '2018-02-14'
from_ = '南京'
to_ = '郑州'
# 默认空为所有车次 大小写敏感 可写入多个值 exp：['K601', 'K602']
custom_train_no = ['K1102', 'G1898', 'G1890', 'G1940']

from_station = get_station_val(from_)
to_station = get_station_val(to_)
