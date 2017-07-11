# coding=utf-8
import time, json, re, os, datetime, time, requests,urllib
import weaverbird
spu_log_file = '/home/xzh/log/weifan.log'
ses = requests.session()
def md5(str):
    import hashlib
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()

def get_real_url(url):
    print url
    resp = requests.get(url)
    real_url = re.search('var url = "(.*?)";', resp.text)
    return real_url.group(1)
def get_star_times(sid):
   url="http://mx.wefans.com/wefans-war-2.0.0/QueryStarJourneyCalendar/index.do?startRow=0&pageSize=999&starInfoId="
   rsp=urllib.urlopen(url+str(sid)).readlines()
   time_list=[]
   for i in range(0,len(eval(rsp[0])['datastr'])):
      time_list.append(eval(rsp[0])['datastr'][i]["holdTime"])
   return time_list

def get_star_xc(sid,times):
   url="http://mx.wefans.com/wefans-war-2.0.0/QueryStarJourney/index.do?se=37654d930d73510f85d9363e69566e3d&startRow=0&pageSize=15&starInfoId="
   rsp=urllib.urlopen(url+str(sid)+"&holdTime="+str(times)).readlines()
   return eval(rsp[0])['datastr']



def get_star_info(sid):
   url="http://mx.wefans.com/wefans-war-2.0.0/QueryIsFocusedStar/index.do?se=37654d930d73510f85d9363e69566e3d&starInfoId="
   rsp=urllib.urlopen(url+str(sid)).readlines()
   return eval(rsp[0])['datastr']


def clean():
    spu_list = []
    spu_ids = []
    sku_list = []
    f = open(spu_log_file)
    linse = f.readlines()
    f.close()
    tagm={"http://res.wefans.com/res/wefansapp/srv_tags/icon_schedule_fanmeeting.png":"见面会",\
          "http://res.wefans.com/res/wefansapp/srv_tags/icon_schedule_awards.png":"典礼",\
          "http://res.wefans.com/res/wefansapp/srv_tags/icon_schedule_record.png":"综艺",\
          "http://res.wefans.com/res/wefansapp/srv_tags/1472628439651.png":"直播",\
          "http://res.wefans.com/res/wefansapp/srv_tags/icon_schedule_flight.png":"机场",\
          "http://res.wefans.com/res/wefansapp/srv_tags/1472628484184.png":"电台",\
          "http://res.wefans.com/res/wefansapp/srv_tags/icon_schedule_presscon.png":"发布会",\
          "http://res.wefans.com/res/wefansapp/srv_tags/icon_schedule_other.png":"其他",\
          "http://res.wefans.com/res/wefansapp/srv_tags/icon_schedule_tour.png":"演出",\
          "http://res.wefans.com/res/wefansapp/srv_tags/icon_schedule_concert.png":"音乐会",\
          "http://res.wefans.com/res/wefansapp/srv_tags/icon_schedule_show.png":"活动",\
          "http://res.wefans.com/res/wefansapp/srv_tags/icon_schedule_salecd.png":"签名会",
           "http://res.wefans.com/res/wefansapp/srv_tags/1472628515364.png":"拍摄",
          "http://res.wefans.com/res/wefansapp/srv_tags/1472628543166.png":"拍摄",
           "http://res.wefans.com/res/wefansapp/srv_tags/1472628405689.png":"高铁",
           "http://res.wefans.com/res/wefansapp/srv_tags/1472628461014.png":"音乐舞台剧",
           "":" "}
    for line in linse:
        raw_data = json.loads(line)
        url = raw_data['url']
        
        # 处理spu
        spu_id = ""
        if ('QueryAllStarList/index.do' in url) and ('resBody' in raw_data):
          print url
          #print raw_data['resBody']
          raw_resBody = json.loads(raw_data['resBody'])
          
          for i in range(0,len(raw_resBody['datastr'])):
            meta_b={}
            spu_id = md5('clb$spu:' +'star'+ str(raw_resBody['datastr'][i]['starInfoId']) + ':weifan')
            spu_list.append({
                    "content": {
                        "content": {
                            "message_type": "spu_full",
                            "data": {
                                "spu_id": spu_id,
                                "spu_source_id":'star'+str(raw_resBody['datastr'][i]['starInfoId']),
                                "spu_source_title": raw_resBody['datastr'][i]['starName']+u"的行程",
                                "spu_source_intro": " ",
                                "spu_source_category":"娱乐" ,
                                "spu_source_sub_category": "明星",
                                "spu_cover_url": weaverbird.TransformImageAndSetMeta("demo", raw_resBody['datastr'][i]['headImg'], meta_b),    
                                "spu_cover_thumbnail": " ",
                                "spu_source": "weifan",
                                "spu_creator": " ",
                                "spu_source_url": " ",
                                "spu_tags": "",
                                "spu_source_pub_time": " ",
                                "spu_last_update_time":" ",
                                "spu_total_article_count": " ",
                                "spu_total_follower_count":" "
                            }
                    
                         },
                      "meta":meta_b
                     },
                     
                     "unique": spu_id
                   })
            
            spu_ids.append(raw_resBody['datastr'][i]['starInfoId'])
         
    """    
    for j in range(0,len(spu_ids)):
        sku_time_list= get_star_times(spu_ids[j])
        if( len(sku_time_list)>0):
           for k in range(0,len(sku_time_list)):
             star_xc=get_star_xc(spu_ids[j],sku_time_list[k])
             if( len(star_xc)>0):
                for y in range(0,len(star_xc)):
                  meta_a={}
                  sku_list.append({
                    "content": {
                        "content": {
                            "message_type": "sku_full",
                            "data": {
                                "spu_id": md5('clb$spu:' +'star'+ str(spu_ids[j]) + ':weifan'),
                                "sku_id": md5('clb$sku:' +str(star_xc[y]['starTrailInfoId']) + ':weifan'),
                                "sku_source_id": star_xc[y]['starTrailInfoId'],
                                "sku_score":time.mktime(time.strptime(star_xc[y]['holdTime'][0:-2],'%Y-%m-%d %H:%M:%S'))*1000,
                                "sku_source_title":tagm[star_xc[y]['tagImg'].replace("\\",'')]+"  "+star_xc[y]['title']+","+star_xc[y]['starIds'],
                                "sku_source": "weifan",
                                "sku_source_url": "http://mx.wefans.com/appshare/travelDetail.html?starTrailId="+ str(star_xc[y]['starTrailInfoId']), 
                                "sku_source_category":"娱乐",
                                "sku_tags":"明星",
                                "sku_content": {
                                    "pub_time":time.mktime(time.strptime(star_xc[y]['holdTime'][0:-2],'%Y-%m-%d %H:%M:%S'))*1000,
                                    "content": " ",#raw_sku['action'] + ';'+raw_sku['type_cn'],
                                    "location":star_xc[y]['city']+"  "+ star_xc[y]['address'],
                                    "forward_count": " ",
                                    "comment_count": " ",
                                    "likes": "",
                                    "videos|video": [],
                                    "imgs": [],
                                    "audios|audio": []
                                },
                            }
                        },

                            "meta":meta_a
                       },
                          "unique": md5('clb$sku:' +str(star_xc[y]['starTrailInfoId']) + ':weifan')
                            })
    
   
    for i in range(0,len(sku_list)):
        list_a=[]
        list_a.append(sku_list[i])
        items = {
          "items":list_a,
           "name": "weifan_online_new",
           "key": "WYAdUMjL442zpEGIx5cdxg==",
          "control": {
            "bnName": "bh_columbus",
            "cfg": {
            "ums": {
                "add": {
                    "appid": "bh_columbus",
                    "appkey": "MaJ85Hv3mKfC75He"
                },
                "query": {
                    "appid": "bh_columbus",
                    "appkey": "O2wPNv63Lu7JOk88"
                },
                "callback": {
                    "appid": "ums",
                    "appkey": "MiswKeH13HkKensv"
                }
             },
                "imgCloud": {
                "buzId": "blackhole",
                "uid": "columbus"
             }
            }
             }
             }
        print ses.post( "https://bhbase.ucweb.com"+ "/nebula/append_list_items", json.dumps(items))
    """
    for j in range(0,len(spu_list)):
        list_a=[]
        list_a.append(spu_list[j])
        items = {
          "items":list_a,
           "name": "weifan_online_new",
          "key": "WYAdUMjL442zpEGIx5cdxg==",
          "control": {
            "bnName": "bh_columbus",
            "cfg": {
            "ums": {
                "add": {
                    "appid": "bh_columbus",
                    "appkey": "MaJ85Hv3mKfC75He"
                },
                "query": {
                    "appid": "bh_columbus",
                    "appkey": "O2wPNv63Lu7JOk88"
                },
                "callback": {
                    "appid": "ums",
                    "appkey": "MiswKeH13HkKensv"
                }
             },
                "imgCloud": {
                "buzId": "blackhole",
                "uid": "columbus"
             }
            }
             }
             }
        print ses.post( "https://bhbase.ucweb.com"+ "/nebula/append_list_items", json.dumps(items))

    
if __name__ == '__main__':
    clean()
