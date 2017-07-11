
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