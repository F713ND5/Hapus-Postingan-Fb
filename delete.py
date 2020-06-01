'''
File: Penghapus postingan Facebook
Author: Pandas ID
Date: 31-05-2020

Description: Script ini open source jadi bisa kalian pelajari
meskipun begitu saya tidak rela jika script ini di upload ke github kalian tanpa
mencantumkan sumber nya (github saya).

Untuk yang suka recode karya orang, ingat!!! Recode tidak akan menjadikan kalian 
hebat.

Tolong hargai script orang meskipun kalian menganggap ituhanya script sampah
semoga bermanfaat...

'''

import requests
from headerz import headerz
import re
import os
import time
import html

class Bot:
    
    banner = '''
             Pandas ID
    <------------------------->
      Bot Penghapus Postingan
            Facebook
    <------------------------->
    '''
    
    def __init__(self):
        self.banner = Bot.banner
        self.head = 'https://mbasic.facebook.com'
        self.req = requests.Session()
        self.count = 0
        
        os.system('clear')
        print(self.banner)
        file = []
        for c in os.listdir('.'):
            if '.log' in c:
                file.append(c)
        if len(file) != 0:
            for s in file:
                print(f'     [{file.index(s)+1}] '+s)
        print()
        try:
            select_file = int(input('     -•> '))
        except ValueError:
            exit('     -!> Pilihan tidak tersedia')
        try:
            open_file = open(file[select_file-1], 'r').read()
        except IndexError:
            exit('     -!> Pilihan tidak tersedia')

        header = headerz().parser(open_file)
        cookie = headerz().cookie_builder(header["cookie"])
        self.kuki = {'Cookies':cookie}
        test_cookie = self.req.get(self.head+'/me', cookies=self.kuki).text
        self.username = re.search(r'<title>(.*?)</title>', test_cookie).group(1)
        if 'Masuk ke Facebook' in test_cookie:
            os.system('rm -rf '+file[select_file-1])
            exit('     -!> Invalid Cookies')
        self.menu()
        
    def menu(self):
        os.system('clear')
        print(self.banner)
        print('     <user> '+self.username)
        print()
        print('     <1> Mulai menghapus semua postingan')
        print('     <2> Info')
        print('     <0> Exit')
        print()
        pilihan = input('     -•> ')
        if pilihan == '1':
            print('     <!> CTRL + C untuk berhenti')
            self.getPost()
        elif pilihan == '2':
            self.info()
        elif pilihan == '0':
            exit('     -!> Exit')
        else:
            print('     -!> Pilihan tidak tersedia')
            time.sleep(1)
            self.menu()
            
    def getPost(self):
        try:
            get_post = self.req.get(self.head+'/me', cookies=self.kuki).text
            all_post = re.findall(r'\<a\ href\=\"\/nfx\/basic\/direct_actions(.*?)\"\>Lainnya\<\/a\>', get_post)
            for d in all_post:
                self.delete(d)
                print(f'\r     --> Postingan terhapus: {str(self.count)}', end="", flush=True)
            self.getPost()
        except KeyboardInterrupt:
            exit('     --> Silahkan cek beranda Anda')
            
    def delete(self, url):
        mature_url = self.head+'/nfx/basic/direct_actions'+html.unescape(url)
        get_url = self.req.get(mature_url, cookies=self.kuki).text
        raw_action = re.search(r'\<form\ method\=\"post\"\ action\=\"(.*?)\"\ id\=\"actions\-form\"\>', get_url).group(1)
        mature_action = self.head+html.unescape(raw_action)
        fb_dtsg = re.search(r'\<input\ type\=\"hidden\"\ name\=\"fb_dtsg\"\ value\=\"(.*?)\"\ autocomplete\=\"off\"\ \/\>', get_url).group(1)
        jazoest = re.search(r'\<input\ type\=\"hidden\"\ name\=\"jazoest\"\ value\=\"(.*?)\"\ autocomplete\=\"off\"\ \/\>', get_url).group(1)
        data = {
            'fb_dtsg':fb_dtsg,
            'jazoest':jazoest,
            'action_key':'DELETE',
            'submit':'Kirim'
        }
        delete_post = self.req.post(mature_action, data=data, cookies=self.kuki).text
        self.count += 1
        
    def info(self):
        print('    <------------------------->')
        print('     Author: Pandas ID')
        print('     WA: 082250223147')
        print('     FB: Pandas ID')
        print('     Blog: https://pandasid.blogspot.com')
        print('    <------------------------->')
        print('     silahkan hubungi saya jika program tidak')
        print('     berjalan dengan baik')
        print()
        input('    < Kembali >')
        self.menu()
try:
    Bot()
except KeyboardInterrupt:
    exit('     -!> Exit')
except requests.ConnectionError:
    exit('     -!> Koneksi Error')
except AttributeError:
    exit('     -!> Postingan sudah tidak tersedia')