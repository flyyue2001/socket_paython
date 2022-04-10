# server_shell.py

usege:

```
server_shell.py [-h] [-p PORT]
  -h, --help            show this help message and exit
  -p PORT, --port PORT  本地监听的端口
```

eg：

```
python server_shell.py -p 5000
```



# client_shell.py

usege:

```
client_shell.py [-h] [-u IP] [-p PORT]
  -h, --help            show this help message and exit
  -u IP, --ip IP        连接监听服务器地址
  -p PORT, --port PORT  连接监听服务器端口
```

eg：

```
python client_shell.py -u 127.0.0.1 -p 5000
```

