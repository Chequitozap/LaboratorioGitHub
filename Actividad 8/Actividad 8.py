#El siguiente script funciona de manera manual
#Elija cualquier ftp y cambie los comentarios que le  aparezcan en terminal
#Create by Chequito
#!/usr/bin/env python3

from ftplib import FTP, FTP_PORT
from typing import List

def save_file(con: FTP, remote_file_path:str, local_file_path:str):
    with open(local_file_path,'wb') as local_file:
        con.retrbinary(f'RETR {remote_file_path}', local_file.write)

 

def get_txt_file(con: FTP, file_path:str):
    listado = []
    con.retrlines(f'RETR {file_path}', listado.append)
    return listado

 

def list_folder(con: FTP, directory:str):
    print(directory)
    listado = []
    con.retrlines(f'LIST {directory}', listado.append)
    return listado


def get_file_dir(con: FTP, directory:str):
    listado = list_folder(con,directory)
    return [file_info for file_info in listado if file_info.startswith('-')],  \
        [file_info for file_info in listado if not file_info.startswith('-')]
 

def get_file_name(file_info:str) -> str:
    return ''.join(file_info.split()[8:])

 
def connect_ftp(host:str, port:int = FTP_PORT, usr:str = '', pwd:str = '', save_path:str = ''):
    connection = FTP()
    connection.connect(host=host, port=port, timeout=3)
    connection.login(usr,pwd)
    actual_path = ''
    l_file, l_dir = get_file_dir(connection, actual_path)
    print(f'files:\n{l_file}\ndirs:\n{l_dir}')
    print(get_txt_file(connection, 'robots.txt'))
    save_file(connection, 'robots.txt', f'{save_path}/robots.txt')
    for file_info in l_file:
        file_name = get_file_name(file_info)
        print(file_name)
        save_file(connection, f'{actual_path}/{file_name}', f'{save_path}/{file_name}')
    print(list_folder(connection, 'debian'))
    ftp = FTP('ftp.mirror.nl')
    ftp.login()
    ftp.cwd('debian')
    ftp.retrlines('LIST')
    ftp.retrbinary('RETR README', open('README', 'wb').write)
    connection.close()

if __name__ == '__main__':
    # connect_ftp('192.168.11.3', 8022)
    connect_ftp('ftp.mirror.nl', save_path='/users/zm_se/desktop')
