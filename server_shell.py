# -*- coding: GBK -*-
import os
import argparse
import socket
import subprocess

def banner():
    usage = '''
    #######################################风哥实验室###################################
    ##################################################################################
    ##################################################################################
    '''
    print(usage)


# 编写命令行提示
def listen_port():
    banner()
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', dest='Port', help='本地监听的端口', type=int)
    return parser.parse_args().Port

def sock(port):
    print('listenning......')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', port))      # 监听端口
    s.listen(1)             # 设置最大客户端连接数量
    client_conn,addr = s.accept()      # 被动接受客户端连接，阻塞，等待连接
    while True:
        recv_data = client_conn.recv(1024).decode()     # 接受TCP数据，1024表示为一次数据接收的大小
        print(">>", recv_data)
        if recv_data == 'quit':
            break

        # os_data = os.popen(recv_data)       # 将接受的数据执行系统命令
        # os_result = os_data.read()          # 读出执行命令后得出的结果
        # print(os_result)                    # 打印命令结果
        # client_conn.sendall(os_result.encode())     # 将命令执行的结果同时也发送给客户端
        popen = subprocess.Popen(recv_data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        sout, serr = popen.communicate()
        sout = sout.decode('gbk')
        print(sout)
        client_conn.sendall(sout.encode())
    client_conn.close()
    s.close()


if __name__=='__main__':
    try:
        sock(listen_port())
    except TypeError:
        print('请查看帮助信息：-h')



