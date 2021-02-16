import socket

input = '''
naver.com:123
naver.com:80
'''

def chk_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((host, port))
        b_conn = 'O'
    except:
        b_conn = 'X'

    return '%s %s %s' % (b_conn, host, port)

if __name__ == '__main__':
    for line in input.split():
        sline = line.strip()
        host, port = sline.split(':')
        print (chk_port(host, int(port)))
