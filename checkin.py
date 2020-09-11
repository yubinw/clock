# 8:30 每日打卡
# 8:30 12:30 20:30 打三次卡
import requests
import time
import json

one_url = 'https://newweixin.bjtu.edu.cn/ncov/wap/default/save'
three_url = 'https://newweixin.bjtu.edu.cn/xisuncov/wap/open-report/save'
bot_token = '98964309:AAHMRuqeOe7lOySG2k3n0MwktQzXMLkn6ik'
chat_id = '86415403'

cookies = {
    'UUkey': '2f71f9f2e1ec16f53f50690d67a0c2cd',
    'eai-sess': '7u2ga1uqnmha79cbn6dro9pc97',
}

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'DNT': '1',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent':
    'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://newweixin.bjtu.edu.cn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://newweixin.bjtu.edu.cn/site/ncov/xisudailyup',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6',
}

one_data = {
    'ismoved': '0',
    'jhfjrq': '',
    'jhfjjtgj': '',
    'jhfjhbcc': '',
    'sfxk': '0',
    'xkqq': '',
    'szgj': '',
    'szcs': '',
    'uid': '37386',
    'date': '20200905',
    'tw': '2',
    'sfcxtz': '0',
    'sfyyjc': '0',
    'jcjgqr': '0',
    'jcjg': '',
    'sfjcbh': '0',
    'sfcxzysx': '0',
    'qksm': '',
    'remark': '',
    'address':
    '\u5317\u4EAC\u5E02\u6D77\u6DC0\u533A\u5317\u4E0B\u5173\u8857\u9053\u4EA4\u5927\u4E1C\u8DEF10\u53F7\u5317\u4EAC\u4EA4\u901A\u5927\u5B66\u9644\u5C5E\u5C0F\u5B66(\u4E1C\u6821\u533A)',
    'area': '\u5317\u4EAC\u5E02  \u6D77\u6DC0\u533A',
    'province': '\u5317\u4EAC\u5E02',
    'city': '\u5317\u4EAC\u5E02',
    'geo_api_info':
    '{"type":"complete","position":{"Q":39.953412814671,"R":116.34808729383701,"lng":116.348087,"lat":39.953413},"location_type":"html5","message":"Get geolocation success.Convert Success.Get address success.","accuracy":33,"isConverted":true,"status":1,"addressComponent":{"citycode":"010","adcode":"110108","businessAreas":[{"name":"\u5317\u4E0B\u5173","id":"110108","location":{"Q":39.955976,"R":116.33873,"lng":116.33873,"lat":39.955976}},{"name":"\u897F\u76F4\u95E8","id":"110102","location":{"Q":39.942856,"R":116.34666099999998,"lng":116.346661,"lat":39.942856}},{"name":"\u7682\u541B\u5E99","id":"110108","location":{"Q":39.960782,"R":116.339629,"lng":116.339629,"lat":39.960782}}],"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"\u4EA4\u5927\u4E1C\u8DEF","streetNumber":"10\u53F7","country":"\u4E2D\u56FD","province":"\u5317\u4EAC\u5E02","city":"","district":"\u6D77\u6DC0\u533A","township":"\u5317\u4E0B\u5173\u8857\u9053"},"formattedAddress":"\u5317\u4EAC\u5E02\u6D77\u6DC0\u533A\u5317\u4E0B\u5173\u8857\u9053\u4EA4\u5927\u4E1C\u8DEF10\u53F7\u5317\u4EAC\u4EA4\u901A\u5927\u5B66\u9644\u5C5E\u5C0F\u5B66(\u4E1C\u6821\u533A)","roads":[],"crosses":[],"pois":[],"info":"SUCCESS"}',
    'created': '1599269518',
    'sfzx': '1',
    'sfjcwhry': '0',
    'sfcyglq': '0',
    'gllx': '',
    'glksrq': '',
    'jcbhlx': '',
    'jcbhrq': '',
    'sftjwh': '0',
    'sftjhb': '0',
    'fxyy': '\u6B63\u5E38\u8FD4\u6821',
    'bztcyy': '',
    'fjsj': '0',
    'sfjchbry': '0',
    'sfjcqz': '',
    'jcqzrq': '',
    'jcwhryfs': '',
    'jchbryfs': '',
    'xjzd': '',
    'sfsfbh': '0',
    'jhfjsftjwh': '0',
    'jhfjsftjhb': '0',
    'szsqsfybl': '0',
    'sfygtjzzfj': '0',
    'gtjzzfjsj': '',
    'sfsqhzjkk': '0',
    'sqhzjkkys': '',
    'id': '1171767',
    'gwszdd': '',
    'sfyqjzgc': '',
    'jrsfqzys': '',
    'jrsfqzfy': ''
}

three_data = {
    'sfzx': '1',
    'tw': '1',
    'area': '\u5317\u4EAC\u5E02 \u6D77\u6DC0\u533A',
    'city': '\u5317\u4EAC\u5E02',
    'province': '\u5317\u4EAC\u5E02',
    'address':
    '\u5317\u4EAC\u5E02\u6D77\u6DC0\u533A\u5317\u4E0B\u5173\u8857\u9053\u4EA4\u5927\u4E1C\u8DEF10\u53F7\u5317\u4EAC\u4EA4\u901A\u5927\u5B66\u9644\u5C5E\u5C0F\u5B66(\u4E1C\u6821\u533A)',
    'geo_api_info':
    '{"type":"complete","position":{"Q":39.953330349393,"R":116.34809895833399,"lng":116.348099,"lat":39.95333},"location_type":"html5","message":"Get geolocation success.Convert Success.Get address success.","accuracy":30,"isConverted":true,"status":1,"addressComponent":{"citycode":"010","adcode":"110108","businessAreas":[{"name":"\u5317\u4E0B\u5173","id":"110108","location":{"Q":39.955976,"R":116.33873,"lng":116.33873,"lat":39.955976}},{"name":"\u897F\u76F4\u95E8","id":"110102","location":{"Q":39.942856,"R":116.34666099999998,"lng":116.346661,"lat":39.942856}},{"name":"\u7682\u541B\u5E99","id":"110108","location":{"Q":39.960782,"R":116.339629,"lng":116.339629,"lat":39.960782}}],"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"\u4EA4\u5927\u4E1C\u8DEF","streetNumber":"10\u53F7","country":"\u4E2D\u56FD","province":"\u5317\u4EAC\u5E02","city":"","district":"\u6D77\u6DC0\u533A","township":"\u5317\u4E0B\u5173\u8857\u9053"},"formattedAddress":"\u5317\u4EAC\u5E02\u6D77\u6DC0\u533A\u5317\u4E0B\u5173\u8857\u9053\u4EA4\u5927\u4E1C\u8DEF10\u53F7\u5317\u4EAC\u4EA4\u901A\u5927\u5B66\u9644\u5C5E\u5C0F\u5B66(\u4E1C\u6821\u533A)","roads":[],"crosses":[],"pois":[],"info":"SUCCESS"}',
    'sfcyglq': '0',
    'sfyzz': '0',
    'qtqk': '',
    'askforleave': '0'
}

if time.localtime()[3] == 8:
    response = requests.post(url=three_url,headers=headers,cookies=cookies,data=three_data)
    text = '每日打卡:'+json.loads(response.text)['m']
    requests.get("https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s"%(bot_token,chat_id,text))
    response = requests.post(url=one_url,headers=headers,cookies=cookies,data=one_data)
    text = '早打卡:'+json.loads(response.text)['m']
    requests.get("https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s"%(bot_token,chat_id,text))
elif time.localtime()[3] == 12:
    response = requests.post(url=three_url,headers=headers,cookies=cookies,data=three_data)
    text = '午打卡:'+json.loads(response.text)['m']
    requests.get("https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s"%(bot_token,chat_id,text))
elif time.localtime()[3] == 20:
    response = requests.post(url=three_url,headers=headers,cookies=cookies,data=three_data)
    text = '晚打卡:'+json.loads(response.text)['m']
    requests.get("https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s"%(bot_token,chat_id,text))
else:
    text = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    requests.get("https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s"%(bot_token,chat_id,text))
