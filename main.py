import steam
import requests
from bs4 import BeautifulSoup
import vk
import webbrowser
import pyautogui
import time
import json
config = json.load(open("config.json", "r"))
vk_token = config["vk_api_token"]
session = vk.Session(access_token=str(vk_token))
vk_api = vk.API(session)
group_id = str(config["group_id"])
r = vk_api.wall.get(domain=group_id, v=5.126)['items']
r = r[1]
r = r['text']
r = r.split('\n')
r1 = [str(r[4])[2:len(r[4])], str(r[5])[2:len(r[5])], str(r[6])[2:len(r[6])], str(r[7])[2:len(r[7])]]
codes = []
for code in range(4):
    for c in range(10):
        codes.append(str(r1[code]).replace('*', str(c)))
print(codes)
screentype = input('\n-=-=-=-=-=-=-=-=-=-=-=\n\nInput dev type(pc( undefined ); laptop( 1920x1080 ); config( values from config file )) or custom screen resolution\nex: 510(x coordinates of "Terms of use" button) 558(y) 1304(x coordinates of "Confirmation" button) 516(y)\n> ')
if screentype == 'pc':
    xver = 510
    yver = 558
    xsend = 1028
    ysend = 516
    print('pc | ver:x{}, y{}; send:x{}, y{}'.format(str(xver), str(yver), str(xsend), str(xsend)))
elif screentype == 'laptop':
    xver = 225
    yver = 558
    xsend = 742
    ysend = 516
    print('laptop | ver:x{}, y{}; send:x{}, y{}'.format(str(xver), str(yver), str(xsend), str(xsend)))
elif screentype == 'config':
    cr = config["default_screen_resolution"]
    xver = int(cr["xver"])
    yver = int(cr["yver"])
    xsend = int(cr["xsend"])
    ysend = int(cr["ysend"])
    print('laptop | ver:x{}, y{}; send:x{}, y{}'.format(str(xver), str(yver), str(xsend), str(xsend)))
else:
    cords = screentype.split(' ')
    xver = cords[0]
    yver = cords[1]
    xsend = cords[2]
    ysend = cords[3]
for tick in range(40):
    link = 'https://store.steampowered.com/account/registerkey?key=' + str(codes[tick])
    tab = webbrowser.open(link)
    time.sleep(1.75)
    pyautogui.click(x=xver, y=yver, clicks=1, interval=1, button='left')
    time.sleep(0.1)
    pyautogui.click(x=xsend, y=ysend, clicks=1, interval=1, button='left')
    time.sleep(1.5)
    print(str(codes[tick]) + " is done sending\n")
    pyautogui.hotkey('ctrl', 'f4')