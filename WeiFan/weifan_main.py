# coding: utf-8
import requests, time, json, re, os, datetime, subprocess
from macaca import WebDriver

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

macaca_port = '7999'
anyproxy_port = '8666'
anyproxy_if_port = '8766'
desired_caps = {
    'platformName': 'Android',
    'reuse': 3,
    'package': 'com.hy.wefans',
    # 'activity': '.FSMain',
    'udid': '100.84.228.26:5555'
}

server_url = {
    'hostname': 'localhost',
    'port': int(macaca_port)
}

spu_log_file="~/log/log.log"



def getTypeIDMap():
    url = 'http://fanshuapp.com/api?f=tagcategorys&d=868024027226449&v=a3.9.0&s=&t=0fc7333d88fd2ff57abb8e8630b61545&c=meizu'
    response = requests.get(url)
    raw_type_list = json.loads(response.text)
    type_list = raw_type_list['data']
    for item in type_list:
        typeID_map[item['type']] = item['name']
    print json.dumps(typeID_map, ensure_ascii=False)

def kill_adb():
    ret = os.popen("ps ux | grep adb | grep -v grep")
    str_list = ret.read()
    if str_list:
        os.system("taskkill /im adb.exe -f")


def kill_process(port):
    ret = os.popen(''' netstat -nlp | grep :''' + str(port) + ''' | awk '{print $7}' | awk -F"/" '{ print $1 }' ''')
    str_list = ret.read().strip()
    if str_list:
        cmd = "kill -9 " + str_list
        os.system(cmd)


def runMacaca():
    # 开始前的一些准备工作
    kill_process(macaca_port)
    #os.system("adb connect " + desired_caps['udid'])
    p = subprocess.Popen('macaca server -p ' + macaca_port, shell=True)
    time.sleep(4)
    kill_process(anyproxy_port)
    print 'nohup anyproxy -p  '+anyproxy_port+' -w '+anyproxy_if_port+ ' --intercept --file=' + spu_log_file + ' >/dev/null 2>&1 '
    p_spu = subprocess.Popen('nohup anyproxy -p  '+anyproxy_port+' -w '+anyproxy_if_port+ '  --intercept --file=' + spu_log_file + ' >/home/xzh/xzh1.log 2>&1 &', shell=True)
    driver = WebDriver(desired_caps, server_url)
    driver.init()
    time.sleep(9)
#从这里开始

    # 进入话题分类页
    driver.element_by_xpath('//*[@resource-id="com.hy.wefans:id/star_focus_list"]/android.widget.LinearLayout[2]/android.widget.ImageView[1]').click()
    time.sleep(5)
    driver.element_by_xpath('//*[@resource-id="com.hy.wefans:id/all_star_listview"]/android.widget.LinearLayout[1]').click()
    time.sleep(5)
    driver.touch('drag', {'fromX': 100, 'fromY': 600, 'toX': 700, 'toY': 600, 'duration': 0.2})
    time.sleep(2)
    driver.touch('drag', {'fromX': 100, 'fromY': 600, 'toX': 700, 'toY': 600, 'duration': 0.2})
    time.sleep(2)
    driver.touch('drag', {'fromX': 100, 'fromY': 600, 'toX': 700, 'toY': 600, 'duration': 0.2})
    time.sleep(2)
    driver.touch('drag', {'fromX': 100, 'fromY': 600, 'toX': 700, 'toY': 600, 'duration': 0.2})
    time.sleep(2)
    driver.touch('drag', {'fromX': 700, 'fromY': 600, 'toX': 100, 'toY': 600, 'duration': 0.2})
    time.sleep(2)
    driver.touch('drag', {'fromX': 700, 'fromY': 600, 'toX': 100, 'toY': 600, 'duration': 0.2})
    time.sleep(2)
    driver.touch('drag', {'fromX': 700, 'fromY': 600, 'toX': 100, 'toY': 600, 'duration': 0.2})
    time.sleep(2)
    driver.touch('drag', {'fromX': 700, 'fromY': 600, 'toX': 100, 'toY': 600, 'duration': 0.2})
    time.sleep(5)
    driver.element_by_xpath('//*[@resource-id="com.hy.wefans:id/titlebar"]/android.widget.ImageView[1]').click()
    time.sleep(6)
    driver.element_by_xpath('//*[@resource-id="com.hy.wefans:id/all_star_listview"]/android.widget.LinearLayout[2]').click()
    time.sleep(5)
    driver.touch('drag', {'fromX': 100, 'fromY': 600, 'toX': 700, 'toY': 600, 'duration': 0.2})
    time.sleep(2)
    driver.touch('drag', {'fromX': 100, 'fromY': 600, 'toX': 700, 'toY': 600, 'duration': 0.2})
    time.sleep(2)
    driver.touch('drag', {'fromX': 100, 'fromY': 600, 'toX': 700, 'toY': 600, 'duration': 0.2})
    time.sleep(2)
    driver.touch('drag', {'fromX': 100, 'fromY': 600, 'toX': 700, 'toY': 600, 'duration': 0.2})
    time.sleep(2)
    driver.touch('drag', {'fromX': 700, 'fromY': 600, 'toX': 100, 'toY': 600, 'duration': 0.2})
    time.sleep(2)
    driver.touch('drag', {'fromX': 700, 'fromY': 600, 'toX': 100, 'toY': 600, 'duration': 0.2})
    time.sleep(2)
    driver.touch('drag', {'fromX': 700, 'fromY': 600, 'toX': 100, 'toY': 600, 'duration': 0.2})
    time.sleep(2)
    driver.touch('drag', {'fromX': 700, 'fromY': 600, 'toX': 100, 'toY': 600, 'duration': 0.2})
    time.sleep(3)
    driver.element_by_xpath('//*[@resource-id="com.hy.wefans:id/titlebar"]/android.widget.ImageView[1]').click()
    time.sleep(6)
    driver.element_by_xpath('//*[@resource-id="com.hy.wefans:id/all_star_listview"]/android.widget.LinearLayout[3]').click()
    time.sleep(6)
    driver.touch('drag', {'fromX': 100, 'fromY': 600, 'toX': 700, 'toY': 600, 'duration': 0.2})
    time.sleep(2)
    driver.touch('drag', {'fromX': 100, 'fromY': 600, 'toX': 700, 'toY': 600, 'duration': 0.2})
    time.sleep(2)
    driver.touch('drag', {'fromX': 100, 'fromY': 600, 'toX': 700, 'toY': 600, 'duration': 0.2})
    time.sleep(2)
    driver.touch('drag', {'fromX': 100, 'fromY': 600, 'toX': 700, 'toY': 600, 'duration': 0.2})
    time.sleep(2)
    driver.touch('drag', {'fromX': 700, 'fromY': 600, 'toX': 100, 'toY': 600, 'duration': 0.2})
    time.sleep(2)
    driver.touch('drag', {'fromX': 700, 'fromY': 600, 'toX': 100, 'toY': 600, 'duration': 0.2})
    time.sleep(2)
    driver.touch('drag', {'fromX': 700, 'fromY': 600, 'toX': 100, 'toY': 600, 'duration': 0.2})
    time.sleep(2)
    driver.touch('drag', {'fromX': 700, 'fromY': 600, 'toX': 100, 'toY': 600, 'duration': 0.2})
    time.sleep(5)
    driver.element_by_xpath('//*[@resource-id="com.hy.wefans:id/titlebar"]/android.widget.ImageView[1]').click()
    time.sleep(6) 
    driver.element_by_xpath('//*[@resource-id="com.hy.wefans:id/all_star_listview"]/android.widget.LinearLayout[4]').click()
    time.sleep(6)
    driver.touch('drag', {'fromX': 100, 'fromY': 600, 'toX': 700, 'toY': 600, 'duration': 0.2})
    time.sleep(2)
    driver.touch('drag', {'fromX': 100, 'fromY': 600, 'toX': 700, 'toY': 600, 'duration': 0.2})
    time.sleep(2)
    driver.touch('drag', {'fromX': 100, 'fromY': 600, 'toX': 700, 'toY': 600, 'duration': 0.2})
    time.sleep(2)
    driver.touch('drag', {'fromX': 100, 'fromY': 600, 'toX': 700, 'toY': 600, 'duration': 0.2})
    time.sleep(2)
    driver.touch('drag', {'fromX': 700, 'fromY': 600, 'toX': 100, 'toY': 600, 'duration': 0.2})
    time.sleep(2)
    driver.touch('drag', {'fromX': 700, 'fromY': 600, 'toX': 100, 'toY': 600, 'duration': 0.2})
    time.sleep(2)
    driver.touch('drag', {'fromX': 700, 'fromY': 600, 'toX': 100, 'toY': 600, 'duration': 0.2})
    time.sleep(2)
    driver.touch('drag', {'fromX': 700, 'fromY': 600, 'toX': 100, 'toY': 600, 'duration': 0.2})
    time.sleep(5)
    driver.element_by_xpath('//*[@resource-id="com.hy.wefans:id/titlebar"]/android.widget.ImageView[1]').click()
    time.sleep(6)
    driver.touch('drag', {'fromX': 400, 'fromY': 400, 'toX': 400, 'toY': 1000, 'duration': 0.2})
    p_spu.kill()
    """
    for i in range(16): #16
        driver.touch('drag', {'fromX': 500, 'fromY': 1000, 'toX': 100, 'toY': 1000, 'duration': 0.2})

    # 进入搜索页
    driver.wait_for_element_by_id('com.fanshu.daily:id/right').click()
    # 进入到spu页，并滑动至底部，同时抓包
    f = open(spu_log_file)
    for line in f.readlines():
        raw_data = json.loads(line)
        url = raw_data['url']
        if ('api?f=tagcategoryslist' in url) and (url.split('=')[-1] in type_ids) and ('resBody' in raw_data):
            raw_resBody = json.loads(raw_data['resBody'])
            for raw_spu in raw_resBody['data']:
                try:
                    print raw_spu['name'] + ' typeid: ' + url.split('=')[-1] + ' time: ' + str(datetime.datetime.now().strftime("%H:%M:%S"))
                    driver.wait_for_element_by_id('com.fanshu.daily:id/search_edittext').send_keys(raw_spu['name'])
                    driver.wait_for_element_by_id('com.fanshu.daily:id/itemFunction').click()
                    flag = 1
                    while flag:
                        driver.touch('drag', {'fromX': 100, 'fromY': 1500, 'toX': 100, 'toY': 300, 'duration': 0.2})
                        for bottom_i in range(2, 5):
                            end = driver.element_by_xpath_or_none('//*[@resource-id="android:id/list"]/android.widget.RelativeLayout['+str(bottom_i)+']/android.widget.RelativeLayout[1]/android.widget.LinearLayout[3]')
                            if end and end.rect == {'y': 1890, 'x': 0, 'height': 30, 'width': 1080}:
                                flag = 0
                    driver.back()
                except Exception, e:
                    print 'failed: ' + raw_spu['name']
                    print 'repr(e):\t', repr(e)
                    print 'e.message:\t', e.message
        time.sleep(1)

    driver.quit()
    p_spu.kill()
    p.kill()
    """


if __name__ == '__main__':
    runMacaca()
    # time.sleep(2)
    # clean_to_db()
