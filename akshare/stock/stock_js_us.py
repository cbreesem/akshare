# -*- coding:utf-8 -*-
# /usr/bin/env python
"""
Date: 2020/6/26 13:30
Desc: 美股目标价 or 港股目标价
https://www.ushknews.com/report.html
"""
import requests
import pandas as pd


def stock_js_price(category="us"):
    """
    美股目标价 or 港股目标价
    :param category: choice of ["us", "hk"]
    :type category: str
    :return: 美股目标价 or 港股目标价
    :rtype: pandas.DataFrame
    """
    url = "https://calendar-api.ushknews.com/getWebTargetPriceList"
    params = {
        "limit": "10000",
        "category": category
    }
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "cookie": "UM_distinctid=1721157a7ea9b-07ab7d5af65271-d373666-1fa400-1721157a7ebb94",
        "origin": "https://www.ushknews.com",
        "pragma": "no-cache",
        "referer": "https://www.ushknews.com/report.html",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        "x-app-id": "BNsiR9uq7yfW0LVz",
        "x-version": "1.0.0"
    }
    r = requests.get(url, params=params, headers=headers)
    json_data = r.json()
    temp_df = pd.DataFrame(json_data["data"]["list"])
    return temp_df


if __name__ == '__main__':
    stock_js_price_us_df = stock_js_price(category="us")
    print(stock_js_price_us_df)

    stock_js_price_hk_df = stock_js_price(category="hk")
    print(stock_js_price_hk_df)
