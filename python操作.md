## 关于python里的时间
1. time.time()返回当前时间的时间戳
```
time.time()
1503393420.999197
```
2. time.localtime(timestamp=now)返回tuple对象
```
time.localtime()
time.struct_time(tm_year=2017, tm_mon=8, tm_mday=22, tm_hour=17, tm_min=18, tm_sec=23, tm_wday=1, tm_yday=234, tm_isdst=0)
```
3. time.striptime()根据指定的格式把一个时间字符串解析为时间元组
```
a = "2017-2-3 12:35"
time.strptime(a,"%Y-%m-%d %H:%M")
time.struct_time(tm_year=2017, tm_mon=2, tm_mday=3, tm_hour=12, tm_min=35, tm_sec=0, tm_wday=4, tm_yday=34, tm_isdst=-1)
```
%y 两位数的年份表示（00-99）  
%Y 四位数的年份表示（000-9999）  
%m 月份（01-12）   
%d 月内中的一天（0-31)       
%H 24小时制小时数（0-23)  
%I 12小时制小时数（01-12)  
%M 分钟数（00=59)  
%S 秒（00-59)  
%a 本地简化星期名称  
%A 本地完整星期名称  
%b 本地简化的月份名称  
%B 本地完整的月份名称  
%c 本地相应的日期表示和时间表示  
%j 年内的一天（001-366)  
%p 本地A.M.或P.M.的等价符  
%U 一年中的星期数（00-53）星期天为星期的开始  
%w 星期（0-6），星期天为星期的开始  
%W 一年中的星期数（00-53）星期一为星期的开始  
%x 本地相应的日期表示  
%X 本地相应的时间表示  
%Z 当前时区的名称  
%% %号本身 

4. time.strftime()接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数format决定。 
```
a = time.localtime()
a
time.struct_time(tm_year=2017, tm_mon=8, tm_mday=22, tm_hour=17, tm_min=26, tm_sec=31, tm_wday=1, tm_yday=234, tm_isdst=0)
time.strftime("%Y-%m-%d %H:%M",a)
'2017-08-22 17:26'
```
5. time.mktime()接收struct_time对象作为参数，返回时间戳。
```
time.mktime(a)
1503393991.0
```
6. time.gmtime()将一个时间戳转换为UTC时区（0时区）的struct_time