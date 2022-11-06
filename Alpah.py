import time
import pyperclip
import getpass
import warnings
import os
warnings.filterwarnings('ignore')
print('֍֍֍֍֍      /| |     |^^^^^|     /| |     | ® ֍֍֍֍֍')
print('֍֍֍֍֍     / | |     | ۝ ۝ |    / | |     |   ֍֍֍֍֍')
print('֍֍֍֍֍    /__| |     |_____|   /__| |_____|   ֍֍֍֍֍')
print('֍֍֍֍֍   /   | |     |        /   | |     |   ֍֍֍֍֍')
print('֍֍֍֍֍  /    | |____ |       /    | |     |   ֍֍֍֍֍\n')


try:
    with open('profile.txt', 'x'):
        profile = open('profile.txt').read()
except FileExistsError:
    profile = open('profile.txt').read()
if profile == '':
    print('Please create an account')
    username = input('Username: ')
    f = open('profile.txt', 'w')
    print(username, file=f)
    f.close()
    
else:
    encprofile = profile.strip()
    enc_profile = encprofile[:-3]
    enc_profile2 = encprofile[4:]
    print('Please Enter The Password to '+ enc_profile + '******'+enc_profile2)
    

try:
    with open('conf.txt', 'x'):
        conf = open('conf.txt').read()
except FileExistsError:
    conf = open('conf.txt').read()
if conf == '':
    try:
        p_word = getpass.getpass()
    except Exception as error:
        print('ERROR', error)
    else:
        fp = open('conf.txt', 'w')
        print(p_word, file=fp)
        print('User Registered Sucsessfully')
        fp.close()
else:
    try:
        p = getpass.getpass()
    except Exception as error:
        print('ERROR', error)
    else:
        if p == conf.strip():
            print('Hello'+ ' ' +profile.strip())
        else:
            while True:
                try:
                    p = getpass.getpass()
                except Exception as error:
                    print('ERROR', error)
                else:
                    if p == conf.strip():
                        print('Hello'+ ' ' +profile.strip())
                
kv_autorization = input('Do you want to add your own encryption keys (y or n): ')


if kv_autorization == 'y':
    try:
        os.remove("mykey.txt")
    except FileNotFoundError:
        pass
    print('keys and values should be in this formart \'key:value\' \nexample \'a:1\' enter should be pressed after each key value pairs\ntype in exit when done')
    while True:
        kv = input('enter your key value pairs: ')

        with open("mykey.txt", "a") as fa:
            if kv != 'exit':
                fa.writelines(kv+'\n')
            fa.close()
        with open("mykeyd.txt", "a") as fd:
            if kv != 'exit':
                fd.writelines(kv[::-1]+'\n')
            fd.close()
        if kv == 'exit':
            break
else:
    pass

my_dict = {}
with open("mykey.txt") as f:
    for line in f:
        key_value = line.rstrip('\n').split(":")
        if len(key_value) == 2:
            my_dict[key_value[0]]=key_value[1]
#print(my_dict)

encrypt = str.maketrans(my_dict)

my_dictd = {}
with open("mykeyd.txt") as fr:
    for line in fr:
        key_value = line.rstrip('\n').split(":")
        if len(key_value) == 2:
            my_dictd[key_value[0]]=key_value[1]
#print(my_dict)

decrypt = str.maketrans(my_dictd)



mode = input('Enter "e" to encrypt and "d" to decrypt or press "doc" for Documentation: ')

if mode == 'e':
    print('Entering Encrypthion Mode...')
    time.sleep(2)
    print('Encryption Mode Activated\n')
    print('"|" to exit')
    while True:
        text = input('Enter Text: ')
        text_lower = text.lower()
        print(text_lower.translate(encrypt))
        txtenc = str(text_lower.translate(encrypt))
        pyperclip.copy(txtenc)
        print('.................................................................\n')
        if text == '|':
            print('The loop is now quiting...')
            break

        elif text =='d':
            print('Entering Decrypthion Mode...')
            time.sleep(2)
            print('Decryption Mode Activated\nNOTE: YOU CAN NOT SWITCH TO ENCRYPTION MODE')
            while True:
                
                text = input('Enter Text: ')
                print(text.translate(decrypt))
                txtenc = str(text_lower.translate(decrypt))
                pyperclip.copy(txtenc)
                print('.................................................................\n')
                if text == '|':
                    print('The loop is now quiting...')
                    
            
        
                    break
                break
            
            
            

elif mode == 'd':
    print('Entering Decrypthion Mode...')
    time.sleep(2)
    print('Decryption Mode Activated\n')
    while True:
        text = input('Enter Text: ')
        text_lower = text.lower()
        print(text.translate(decrypt))
        txtenc = str(text_lower.translate(decrypt))
        pyperclip.copy(txtenc)
        print('.................................................................\n')
        if text == '|':
            print('The loop is now quiting...')
            break

        elif text =='e':
            print('Entering Encrypthion Mode...')
            time.sleep(2)
            print('Encryption Mode Activated\nNOTE: YOU CAN NOT SWITCH TO DECRYPTION MODE')
            while True:
                text = input('Enter Text: ')
                text_lower = text.lower()
                print(text_lower.translate(encrypt))
                txtenc = str(text_lower.translate(encrypt))
                pyperclip.copy(txtenc)
                print('.................................................................\n')
                if text == '|':
                    print('The loop is now quiting...')
            
        
                    break
                break
            
        
            

elif mode == 'doc':
    print('Alpah 0.0.1 Documentation \nAlpah is a text encryption tool and the most secured \nCreated July,20 2022 \nCreated by Red_X \nAssisted By Moxemrabs(Red)\n  ')
    print('version 0.0.1\n')
    print('Press "e" to enter Encryption Mode \nPress "doc" for Documentations')
    print('Press "d" to enter Decryption mode \nNOTE: THE "d" OR "e" OR "doc" SOULD BE LOWERCASE')
    print('Exit by pressing "|" .\nTo exit in encryption mode you have to first switch to decryption mode\n')
    exit_doc = input('Press "|" to exit Documentation: ' )
else:
    print(profile.strip()+ ' '+ 'You Most Be Drunk ')

time.sleep(3)





"""
a:1
b:2
c:3
d:4
e:5
f:6

"""
