# -*- coding: GBK -*-
import socket
import argparse

def banner():
    usage = '''
    #######################################���ʵ����###################################
    ##################################################################################
    ##################################################################################
    '''
    print(usage)



# ��д��������ʾ
def bind_server():
    banner()
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--ip', dest='ip', help='���Ӽ�����������ַ', type=str)
    parser.add_argument('-p', '--port', dest='port', help='���Ӽ����������˿�', type=int)
    return parser.parse_args().ip, parser.parse_args().port

def sock(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    while True:
        sent_data = input("������ִ�е����")
        if sent_data == 'quit':
            break
        s.sendall(sent_data.encode())
        recv_data = s.recv(10240).decode()   # ���ܷ���˻�������ִ�н��
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
    #     print('�����������Ϣ:-h')

