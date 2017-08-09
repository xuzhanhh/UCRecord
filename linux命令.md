123321hello
## python linux 结束占用端口的进程
```python
def kill_process(port):
    ret = os.popen(''' netstat -nlp | grep :''' + str(port) + ''' | awk '{print $7}' | awk -F"/" '{ print $1 }' ''')
    str_list = ret.read().strip()
    if str_list:
        cmd = "kill -9 " + str_list
        os.system(cmd)
```
### netstat

1. -n  禁用反向域名解析，加快查询速度  如果你觉得 IP 地址已经足够，而没有必要知道主机名，就使用 -n 选项禁用域名解析功能。  

2. -l 只列出监听中的连接  
任何网络服务的后台进程都会打开一个端口，用于监听接入的请求。这些正在监听的套接字也和连接的套接字一样，也能被 netstat 列出来。使用 -l 选项列出正在监听的套接字。  

3. -p  获取进程名、进程号以及用户 ID  
查看端口和连接的信息时，能查看到它们对应的进程名和
默认情况下 netstat 会通过反向域名解析技术查找每个 IP 地址对应的主机名。这会降低查找速度。进程号对系统管理员来说是非常有帮助的。举个栗子，Apache 的 httpd 服务开启80端口，如果你要查看 http 服务是否已经启动，或者 http 服务是由 apache 还是 nginx 启动的，这时候你可以看看进程名。  


### awk
1.  -F"/" 以/作为分隔符，默认为空格 
2. '{print $7}' 输出第7列


### 例子 找到端口号or进程名所在的PID
```shell
netstat -nlp | grep 'node'
//result
tcp        0      0 0.0.0.0:8003            0.0.0.0:*               LISTEN      32265/node          
tcp6      43      0 :::8001                 :::*                    LISTEN      32265/node          
tcp6       0      0 :::8002                 :::*                    LISTEN      32265/node          
tcp6       0      0 :::7891                 :::*                    LISTEN      2881/node           
tcp6       0      0 :::9075                 :::*                    LISTEN      22279/node          
tcp6       0      0 :::7999                 :::*                    LISTEN      1478/node
  
netstat -nlp | grep 'node' | awk '{print $7}'  
//result  
32265/node
32265/node
32265/node
2881/node
22279/node
1478/node  
  

netstat -nlp | grep 'node' | awk '{print $7}'| awk -F"/" '{ print $1 }'  
//result  
32265
32265
32265
2881
22279
1478

```

## find

基本用法：
1. find . -name "*" -exec rm -rf {} \;
2. 避开某个文件夹不搜索  find /home/student -path /home/student/sep -prune -o -name "tmp.txt" -print

## scp 通过ssh传输文件
1. 从服务器上下载文件 scp -r xzh@100.84.72.201:/home/xzh/weifan ~/test
2. 上传本地文件到服务器   
```
~ scp ./Untitled-5.sh xzh@100.84.72.201:~
xzh@100.84.72.201's password:
Untitled-5.sh                                 100%   77     6.6KB/s   00:00 
```

## nohup
### 场景：
如果只是临时有一个命令需要长时间运行，什么方法能最简便的保证它在后台稳定运行呢？
### hangup 名称的来由
在 Unix 的早期版本中，每个终端都会通过 modem 和系统通讯。当用户 logout 时，modem 就会挂断（hang up）电话。 同理，当 modem 断开连接时，就会给终端发送 hangup 信号来通知其关闭所有子进程。
### 解决方法：
我们知道，当用户注销（logout）或者网络断开时，终端会收到 HUP（hangup）信号从而关闭其所有子进程。因此，我们的解决办法就有两种途径：要么让进程忽略 HUP 信号，要么让进程运行在新的会话里从而成为不属于此终端的子进程。
### 1. nohup
nohup 无疑是我们首先想到的办法。顾名思义，nohup 的用途就是让提交的命令忽略 hangup 信号。
nohup 的使用是十分方便的，只需在要处理的命令前加上 nohup 即可，标准输出和标准错误缺省会被重定向到 nohup.out 文件中。一般我们可在结尾加上"&"来将命令同时放入后台运行，也可用">filename 2>&1"来更改缺省的重定向文件名。
```
nohup anyproxy -p  '+anyproxy_port+' -w '+anyproxy_if_port+ '  --intercept --file=' + spu_log_file + ' >/home/xzh/log/xzh1.log 2>&1 &
```