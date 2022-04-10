# -*- coding: GBK -*-
import socket
import argparse

def banner():
    usage = '''
    #######################################风哥实验室###################################
    ##################################################################################
    ##################################################################################
    '''
    print(usage)



# 编写命令行提示
def bind_server():
    banner()
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--ip', dest='ip', help='连接监听服务器地址', type=str)
    parser.add_argument('-p', '--port', dest='port', help='连接监听服务器端口', type=int)
    return parser.parse_args().ip, parser.parse_args().port

def sock(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    while True:
        sent_data = input("请输入执行的命令：")
        if sent_data == 'quit':
            break
        s.sendall(sent_data.encode())
        recv_data = s.recv(10240).decode()   # 接受服务端回显命令执行结果
        if not recv_data:
            continue
        else:
            print(recv_data)
    s.close()

if __name__=='__main__':
    # try:
    addr,port = bind_server()
    sock(addr, port)
    # except TypeError:
    #     print('请输入帮助信息:-h')

