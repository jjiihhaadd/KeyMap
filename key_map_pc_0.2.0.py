import keyboard
import keyboard.mouse
import time
import os
xykey = []
xpos = []
ypos = []
INTRO = '       < Developer > Tension_IDK [ Jihad ]\n# This Is a On screen Mouce Key Mapper.\n# Code in Python.\n# Convert To EXE with AUTO_PY_TP_EXE.\n# Press [ ESC + H ] For Help.\n   __It Use Mouse Pointer to move and Left click__'

HLP = '>> Toggle Key_Mapper            [ CAPSLOCK ]\n>> Add A New Key_Map            [ ESC + N ]\n>> Set New Position For A Key   [ ESC + P ]\n>> Delete A Key                 [ ESC + BACKSPACE ]\n>> Clear Screen                 [ ESC + C ]\n>> List Added Keys              [ ESC + L ]\n>> Change An Existed Key        [ ESC + K ]\n>> EXIT at anypoint             [ CTRL + C ]\n'
def key_work(key):
    xyindx = xykey.index(key)
    kpx = xpos.__getitem__(xyindx)
    kpy = ypos.__getitem__(xyindx)
    keyboard.mouse.move(kpx, kpy, True, 0)
    time.sleep(0.05)
    # keyboard.mouse.press('left')
    # keyboard.mouse.release('left')
    ## New Update Here ##
    keyboard.mouse.click()
    pass
def set_key_pos(key):
    xyindx = xykey.index(key)
    print("before xpos: ",xpos)
    print("ypos: ",ypos)
    xpos.pop(xyindx)
    ypos.pop(xyindx)
    print("after xpos: ",xpos)
    print("ypos: ",ypos)
    print("SET_POSITION_FOR_KEY_[ " ,key ," ]")
    print('WATING FOR LEFT CLICK ON POSITION !!')
    while True:
        post = keyboard.mouse.is_pressed('left')
        if post:
            kpx, kpy = keyboard.mouse.get_position()
            xpos.insert(xyindx, int(kpx))
            ypos.insert(xyindx, int(kpy))
            print('[ ',key ,' ] set to >> x= ',kpx ,' y= ' ,kpy)
            break
    pass
def tool_key(key):
    if len(key) == 1:
        key = str.upper(key)
        try:
            if xykey.__getitem__(xykey.index(key)) == key:
                print("KEY_Exist !!")
                # set_key_pos(key)
                ## New Update Here ##
                print("What Do You Want to do??")
                print("1 >> Change Position For >",key,"<")
                print("2 >> Change The Key.")
                print("3 >> Nothing !!")
                time.sleep(0.3)
                inpt = int(input("Enter An Option >> "))
                if inpt == 1:
                    set_key_pos(key)
                    pass
                elif inpt == 2:
                    cng_key(key)
                    pass
                elif inpt == 3:
                    os.system('CLS')
                    print(INTRO)
                    pass
                else:
                    print('Invalid Opion !!!')
                    pass
        except ValueError:
            xykey.append(key)
            xpos.append(0)
            ypos.append(0)
            print('New_key_Added', key)
            set_key_pos(key)
            pass
        pass  
    else:
        print('Please Enter Only One Key !!')
        pass
def pass_key(key):
    try:
        if xpos.__getitem__(xykey.index(key)) != 0 or ypos.__getitem__(xykey.index(key)) != 0:
            return True
        else:
            return False
    except ValueError:
        pass
def get_key():
    key = keyboard.read_key()
    try:
        if xpos.__getitem__(xykey.index(key)) != 0 or ypos.__getitem__(xykey.index(key)) != 0:
            return key
        else:
            pass
    except ValueError:
        pass
def pop_key(key):
    key = str.upper(key)
    idx = xykey.index(key)
    xykey.pop(idx)
    xpos.pop(idx)
    ypos.pop(idx)
    print('KEY Deleted [ ',key,' ] !')
    pass
## New Update Here ##
def cng_key(key):
    nkey = input("Please Enter the new kew >")
    if len(nkey) == 1:
        nkey = str.upper(nkey)
        try:
            if xykey.__getitem__(xykey.index(nkey)) == nkey:
                print("Key_Exist")
                print("please Try Again !!")
                cng_key(key)
                pass
        except ValueError:
            idx = xykey.index(key)
            xykey.pop(idx)
            xykey.insert(idx,nkey)
            print('key > ', key,' < Changed To New Key > ',nkey,' <')
            pass
    else:
        print("Please Enter Only One Key !!")
        cng_key(key)
        pass
    pass
while True:
    os.system('CLS')
    print(INTRO)
    while True:
        ON = keyboard.is_pressed('capslock')
        POSITION = keyboard.is_pressed(' + p')
        NEW = keyboard.is_pressed(' + n')
        POP = keyboard.is_pressed(' + backspace')
        HELP = keyboard.is_pressed(' + h')
        CLEAR = keyboard.is_pressed(' + c')
        KEYLIST = keyboard.is_pressed(' + l')
        CNGKEY = keyboard.is_pressed(' + k')
        while ON:
            OFF = keyboard.is_pressed('capslock')
            print('KEY_MAP_ON')
            time.sleep(0.3)
            while True:
                KEY = keyboard.read_key()
                if KEY != 'caps lock':
                    key = get_key()
                    key_pass = pass_key(key)
                    if key_pass:
                        key_work(key)
                        pass
                else:
                    print('KEY_MAP_OFF')
                    break
            if OFF:
                time.sleep(0.3)
                break
        if POSITION:
            time.sleep(0.5)
            key = input("Enter A key To Modify > ")
            tool_key(key)
        elif NEW:
            time.sleep(0.5)
            key = input("Enter A New Key > ")
            tool_key(key)
        elif POP:
            key = input('Enter Key To Delete > ')
            key = str.upper(key)
            try:
                if xykey.__getitem__(xykey.index(key)) == key:
                    pop_key(key)
            except ValueError:
                print('Key Not Found !')
        elif CLEAR:
            os.system('CLS')
            print(INTRO)
            time.sleep(0.2)
        elif KEYLIST:
            time.sleep(0.3)
            print(xykey)
        ## Ne Update Here ##
        elif CNGKEY:
            time.sleep(0.3)
            key = input("Enter The key To Change >")
            key = str.upper(key)
            try:
                if xykey.__getitem__(xykey.index(key)) == key:
                    cng_key(key)
                    pass
            except ValueError:
                print("No Key  Found !!!")
                print(" What Do you want to do ?")
                print("1 >> Add new key.")
                print("2 >> Nothing !")
                inpt = int(input("Enter An Option >"))
                if inpt == 1:
                    key = input("Enter a new key >")
                    tool_key(key)
                    pass
                else:
                    os.system('CLS')
                    print(INTRO)
                    pass
        elif HELP:
            print(HLP)
            time.sleep(0.2)
# DEVELOPER Tension_IDK [ JIHAD ]