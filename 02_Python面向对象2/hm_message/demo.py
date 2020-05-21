import time, json, requests, pymysql, urllib.request
# from mpl_toolkits.basemap import Basemap
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context


# def test():
#     data2 = list()
#     # url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign'#&callback=&_=%d' % int(time.time() * 1000)
#     url = 'https://api.yonyoucloud.com/apis/dst/ncov/country'
#     # print(url)
#     resp = urllib.request.urlopen(url)
#     da = resp.read()
#     print(json.loads(resp.read()))
#     data = json.loads(da)['data']
#     # print(data)
#     data_f = json.loads(data)['foreignList']
#     # print(data_f)
#     for d in data_f:
#         # print(round(100 * d['dead'] / d['confirm'], 2))
#         infos = (d['name'], d['date'], d['confirmAdd'], d['confirm'], d['heal'], d['dead'],
#                  round(100 * d['dead'] / d['confirm'], 2), d['nowConfirm'])
#         # print(infos)
#
#         data2.append(infos)
#     print(data2)


def test2():
    url = 'https://c.m.163.com/ug/api/wuhan/app/data/list-total'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=url, headers=headers)
    content = urllib.request.urlopen(req).read()
    # print(content)
    # print(json.loads(content))
    da = json.loads(content)
    # print(da)
    data_f = da['data']['areaTree']
    # print(data_f)
    data2 = list()

    for d in data_f:
        name = d['name']
        confirm = d['total']['confirm']
        dead = d['total']['dead']
        infos = (name, confirm, dead)
        # print(infos)
        data2.append(infos)
    print(data2)
    print(len(data2))


if __name__ == "__main__":
    test2()
