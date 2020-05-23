import requests
#Cookie自己获取
Cookie=''
Referer = 'https://film.qq.com/x/autovue/grade/'
Agent = 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
headers = {
    'Referer': Referer,
    'User-Agent': Agent,
    'Cookie': Cookie,
    'Referer': 'https://v.qq.com'
}

cout = 0
urls=[
        'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=7&_=1582364733058&callback=Zepto1582364712694',#下载签到请求
        'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=6&_=1582366326994&callback=Zepto1582366310545',#赠送签到请求
        'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=hierarchical_task_system&cmd=2&_=1555060502385&callback=Zepto1555060502385',#签到请求
        'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=3&_=1582368319252&callback=Zepto1582368297765 ',#弹幕签到请求
        'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=spp_MissionFaHuo&cmd=4&task_id=1&_=1582997048625&callback=Zepto1582997031843',#观看60分钟签到
        #'https://v.qq.com/x/bu/mobile_checkin'
]


for url in urls:
    cout += 1
    if (cout==1):
        print("发送下载签到请求")
    elif( cout==2):
        print("发送赠送签到请求")
    elif(cout==3):
        print("发送签到请求")
    elif(cout==4):
        print("发送弹幕签到请求")
    elif(cout==5):
        print("发送观看60分钟请求")
    response = requests.get(url=url, headers=headers)
    print(requests.utils.dict_from_cookiejar(response.cookies))
    print(response.content.decode("utf-8"))
cookies = requests.utils.dict_from_cookiejar(response.cookies)


