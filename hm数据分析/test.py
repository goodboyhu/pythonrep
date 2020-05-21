# from mpl_toolkits.basemap import Basemap
from matplotlib import pyplot as plt
from matplotlib import font_manager
import time, json, requests, urllib.request


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
        heal = d['total']['heal']
        infos = (confirm, name, dead, heal)
        # print(infos)
        data2.append(infos)
    # print(data2)
    # print(len(data2))
    new_data = sorted(data2, reverse=True)
    # print(new_data[:50])
    # print(len(new_data[:50]))

    my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")

    # a1=new_data[:50][0][1]
    a1 = list()
    b1 = list()
    b2 = list()
    b3 = list()
    for item in new_data[:20]:
        a1.append(item[1])
        b1.append(item[0])
        b2.append(item[2])
        b3.append(item[3])
    # print(a1)
    # print(b1)
    # print(b2)

    bar_width = 0.3

    confirm = list(range(len(a1)))
    dead = [i + bar_width * 2 for i in confirm]
    heal = [i + bar_width for i in confirm]

    # x_16 = [i + bar_width * 2 for i in confirm]

    plt.figure(figsize=(25, 10), dpi=80)  # 设置图形大小和清晰度

    plt.bar(range(len(a1)), b1, width=bar_width, color="red", label="累计确诊人数")
    plt.bar(dead, b2, width=bar_width, color="#696969", label="死亡人数")
    plt.bar(heal, b3, width=bar_width, color="#7CFC00", label="治愈人数")
    # plt.bar(x_16, b_16, width=bar_width, label="9月16日")

    plt.legend(loc="upper right", prop=my_font)
    # 调整x轴的刻度
    plt.xticks(heal, a1, fontproperties=my_font)

    for a, b in zip(confirm, b1):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)
    for a, b in zip(dead, b2):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)
    for a, b in zip(heal, b3):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)

    plt.show()
    '''
    a = ["猩球崛起3：终极之战", "敦刻尔克", "蜘蛛侠：英雄归来", "战狼2"]
    b_16 = [15746, 312, 4497, 319]
    b_15 = [12357, 156, 2045, 168]
    b_14 = [2358, 399, 2358, 362]

    # 线条宽度
    bar_width = 0.01

    x_14 = list(range(len(a)))
    x_15 = [i + bar_width for i in x_14]
    x_16 = [i + bar_width * 2 for i in x_14]
    
    plt.figure(figsize=(20, 8), dpi=80)  # 设置图形大小和清晰度
    
    plt.bar(range(len(a)), b_14, width=bar_width, label="9月14日")
    plt.bar(x_15, b_15, width=bar_width, label="9月15日")
    plt.bar(x_16, b_16, width=bar_width, label="9月16日")
    
    # 图例
    plt.legend(loc="upper left", prop=my_font)
    # 调整x轴的刻度
    plt.xticks(x_15, a, fontproperties=my_font)

# plt.grid(alpha=0.3)
# 添加描述信息
# plt.xlabel("时间", fontproperties=my_font)
# plt.ylabel("温度", fontproperties=my_font)
# plt.title("3月和10月的气温", fontproperties=my_font)
#


    plt.show()'''


if __name__ == "__main__":
    test2()
