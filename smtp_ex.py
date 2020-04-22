import socket

PORT = 587
IP = '54.213.229.251'


def main():
    my_socket = socket.socket()
    my_socket.connect((IP, PORT))
    mail = raw_input('Enter your email: \n')
    password = raw_input('Enter your password: \n')
    list1 = ['EHLO\r\n', 'AUTH PLAIN ' + ('\x00' + mail + '\x00' + password).encode('base64') + '\r\n',
             'MAIL FROM:<' + mail + '>\r\n', 'RCPT TO: ' + mail + '\r\n',
             'DATA\r\n', 'Subject: \x00' + raw_input('Enter your subject: \n') + '\r\n\r\n' + raw_input(
            'Enter your message: \n') + '\r\n.\r\n', 'QUIT\r\n']
    i = 0
    ans = ''
    while '221' not in ans:
        if i < 7:
            my_socket.send(list1[i])
        ans = my_socket.recv(1024)
        i += 1
        print ans
    my_socket.close()


if __name__ == '__main__':
    main()
