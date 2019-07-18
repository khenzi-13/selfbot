from linepy import *
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup as bSoup
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
#from gtts import gTTS
from threading import Thread
from io import StringIO
from multiprocessing import Pool
from googletrans import Translator
from urllib.parse import urlencode
from tmp.MySplit import *
from random import randint
from shutil import copyfile
from youtube_dl import YoutubeDL
import subprocess, youtube_dl, humanize, traceback
import subprocess as cmd
import platform
import requests, json
import time, random, sys, json, null, pafy, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
_session = requests.session()
#======================================================================================
botStart = time.time()
#======================================================================================
ghi = LINE("gmail","pass")
ghi.log("Auth Token : " + str(ghi.authToken))
ghi.log("Timeline Token : " + str(ghi.tl.channelAccessToken))

print(*SUCCES LOGIN TO NAUGHTY FINGER*)

waitOpen = codecs.open("Max2.json","r","utf-8")
settingsOpen = codecs.open("max.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
wait = json.load(waitOpen)
images = json.load(imagesOpen)
settings = json.load(settingsOpen)
stickers = json.load(stickersOpen)
#==============================================================================#
ghiMID = ghi.profile.mid
ghiProfile = ghi.getProfile()
ghiSettings = ghi.getSettings()
#==============================================================================#
ghiPoll = OEPoll(ghi)
ghiMID = ghi.getProfile().mid
unsendchat = {}
msgdikirim = {}
msg_image={}
msg_video={}
msg_sticker={}
wbanlist = []
msg_dict = {}
temp_flood = {}

#==============================================================================#
did = {"join": True,}
kcn = {"autojoin": False,"Members":5,}
sets = {
    "l":True, 
      "c":True, 
      "cm":"Auto Like By.✡Khenzi✡\nline.me/ti/p/0KGxZx8VYs",  
    "winvite": False,
    "wblacklist": False,
    "tagsticker": False,
    "Sticker": False,
    "autoJoin": False,
    "autoCancel": False,
    "autoJoinTicket": False,
   "changePictureProfile": False, 
    "addSticker": {
        "name": "",
        "status": False,
    },
    "messageSticker": {
        "addName": "",
        "addStatus": False,
        "listSticker": {
            "tag": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "lv": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "wc": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "add": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "join2": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
        }
    },
}
chatbot = {
    "admin": [],
    "botMute": [],
    "botOff": [],
}

anyun = {
    "addTikel": {
        "name": "",
        "status": False
        },
}
nissa = {
    "addTikel2": {
        "name": "",
        "status": False
        },
}
admin = [ghiMID]
loop = asyncio.get_event_loop()
listToken = ['desktopmac','desktopwin','iosipad','chromeos','win10']
mc = {"wr":{}}
tagadd = {
    "tagss": False,
    "tags": False,
    "tag": "Ciee ngetag.. \n Mau minta jajan yaa....🤣🤣🤣",
    "add": "Senang berkenalan denganmu 😃\nTerima kasi akak..😊😊",
    "wctext": "Selamat datang akak..☺☺",
    "lv": "Bye bye akak..Semoga tenang diluar sana..😢😢😢",
    "b": "Akun ini juga dilindungi Self Bot By. 🐧Khenzi🐧 Sistem secara otomatis memblokir akun Anda😝😝😝",
    "c":"Auto Like By. 🐧Khenzi🐧",
    "m": " >_<",
}
apalo = {
    "winvite": False,
    "wblacklist": False,
    "blacklist":{},
    "Talkblacklist": {},
    "talkban": True,
    "Talkwblacklist": False,
    "Talkdblacklist": False,
}
temp = {"te": "#FF9900","t": "#333300"}
read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "setTime":{},
    "ROM": {}
}
rfuSet = {
    'setTime':{},
    'ricoinvite':{},
    'winvite':{},
    }

ProfileMe = {
    "coverId": "",
    "statusMessage": "",
    "PictureMe": "",
    "NameMe": "",
}
peler = { 
    "receivercount": 0,
    "sendcount": 0
}
hoho = {
    "savefile": False,
    "namefile": "",
}

user1 = ghiMID
user2 = ""

setTime = {}
setTime = rfuSet['setTime']

contact = ghi.getProfile() 
backup = ghi.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mulai = time.time()
Start = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

settings["myProfile"]["displayName"] = ghiProfile.displayName
settings["myProfile"]["statusMessage"] = ghiProfile.statusMessage
settings["myProfile"]["pictureStatus"] = ghiProfile.pictureStatus
cont = ghi.getContact(ghiMID)
settings["myProfile"]["videoProfile"] = cont.videoProfile
coverId = ghi.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId

ProfileMe["statusMessage"] = ghiProfile.statusMessage
ProfileMe["pictureStatus"] = ghiProfile.pictureStatus
coverId = ghi.getProfileDetail()["result"]["objectId"]
ProfileMe["coverId"] = coverId
#=====================================================================
with open("max.json", "r", encoding="utf_8_sig") as f:
    anu = json.loads(f.read())
    anu.update(settings)
    settings = anu
with open("Max2.json", "r", encoding="utf_8_sig") as f:
    itu = json.loads(f.read())
    itu.update(wait)
    wait = itu
#==============================================================================#
def RhyN_(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Ma '
        ghi.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def sendMessageCustom(to, text, icon , name):
    annda = {'MSG_SENDER_ICON': icon,
        'MSG_SENDER_NAME':  name,
    }
    ghi.sendMessage(to, text, contentMetadata=annda)
def sendMessageCustomContact(to, icon, name, mid):
    annda = { 'mid': mid,
    'MSG_SENDER_ICON': icon,
    'MSG_SENDER_NAME':  name,
    }
    ghi.sendMessage(to, '', annda, 13)
def cloneProfile(mid):
    contact = ghi.getContact(mid)
    if contact.videoProfile == None:
        ghi.cloneContactProfile(mid)
    else:
        profile = ghi.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        ghi.updateProfile(profile)
        pict = ghi.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = ghi.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = ghi.getProfileDetail(mid)['result']['objectId']
    ghi.updateProfileCoverById(coverId)
def backupProfile():
    profile = ghi.getContact(ghiMID)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    settings['myProfile']['videoProfile'] = profile.videoProfile
    coverId = ghi.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)
def restoreProfile():
    profile = ghi.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        ghi.updateProfileAttribute(8, profile.pictureStatus)
        ghi.updateProfile(profile)
    else:
        ghi.updateProfile(profile)
        pict = ghi.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = ghi.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    ghi.updateProfileCoverById(coverId)
def autoresponuy(to,msg,wait):
    to = msg.to
    if msg.to not in wait["GROUP"]['AR']['AP']:
        return
    if msg.to in wait["GROUP"]['AR']['S']:
        ghi.sendMessage(msg.to,text=None,contentMetadata=wait["GROUP"]['AR']['S'][msg.to]['Sticker'], contentType=7)
    if(wait["GROUP"]['AR']['P'][msg.to] in [""," ","\n",None]):
        return
    if '@!' not in wait["GROUP"]['AR']['P'][msg.to]:
        wait["GROUP"]['AR']['P'][msg.to] = '@!'+wait["GROUP"]['AR']['P'][msg.to]
    nama = ghi.getGroup(msg.to).name
    sd = ghi.waktunjir()
    ghi.sendMention(msg.to,wait["GROUP"]['AR']['P'][msg.to].replace('greeting',sd).replace(';',nama),'',[msg._from]*wait["GROUP"]['AR']['P'][msg.to].count('@!'))
def ClonerV2(to):
    try:
        contact = ghi.getContact(to)
        profile = ghi.profile
        profileName = ghi.profile
        profileStatus = ghi.profile
        profileName.displayName = contact.displayName
        profileStatus.statusMessage = contact.statusMessage
        ghi.updateProfile(profileName)
        ghi.updateProfile(profileStatus)
        profile.pictureStatus = ghi.downloadFileURL('http://dl.profile.line-cdn.net/{}'.format(contact.pictureStatus, 'path'))
        if ghi.getProfileCoverId(to) is not None:
            ghi.updateProfileCoverById(ghi.getProfileCoverId(to))
        ghi.updateProfilePicture(profile.pictureStatus)
        print("Success Clone Profile {}".format(contact.displayName))
        return ghi.updateProfile(profile)
        if contact.videoProfile == None:
            return "Get Video Profile"
        path2 = "http://dl.profile.line-cdn.net/" + profile.pictureStatus
        ghi.updateProfilePicture(path2, 'vp')
    except Exception as error:
        print(error)
        
def sendMentionFooter(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@LopeAgri"
        slen = str(len(text))
        elen = str(len(text) + len(mention))
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        nama = "{}".format(ghi.getContact(ghiMID).displayName)
        img = "http://dl.profile.line-cdn.net/{}".format(ghi.getContact(ghiMID).pictureStatus)
        ticket = "https://line.me/ti/p/~topzalove123"
        ghi.sendMessage(to, text, {'AGENT_LINK': ticket, 'AGENT_ICON': img, 'AGENT_NAME': nama, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        ghi.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def ggggg(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    return '%02d Hari\n───────────\n%02d Jam\n───────────\n%02d Menit\n───────────\n' %(days ,hours, mins)
    
def mentions(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@"
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    ghi.sendMessage(to, textx, {'AGENT_NAME':'LINE OFFICIAL', 'AGENT_LINK': 'line://ti/p/~{}'.format(ghi.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + ghi.getContact("u6a31b61828cb0744374e35c55243062a").picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = ghi.genOBSParams({'oid': ghiMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = ghi.server.postContent('{}/talk/vp/upload.nhn'.format(str(ghi.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        ghi.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
        os.remove("FadhilvanHalen.mp4")
def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = ghi.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def sendTemplate(group, data):
    xyz = LiffChatContext(group)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = ghi.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
    
def NOTIFIED_READ_MESSAGE(op):
    try:
        if read['readPoint'][op.param1]:
            if op.param2 in read['readMember'][op.param1]:
                pass
            else:
                read['readMember'][op.param1][op.param2] = True
                read['ROM'][op.param1] = op.param2
        else:
            pass
    except:
        pass
def logError(text):
    ghi.log("[ alert ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType,mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        ghi.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        ghi.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def mentionMembers(to, mid):
    try:
        group = ghi.getGroup(to)
        mids = [mem.mid for mem in group.members]
        jml = len(mids)
        arrData = ""
        if mid[0] == mids[0]:
            textx = ""
        else:
            textx = ""
        arr = []
        for i in mid:
            no = mids.index(i) + 1
            textx += "{}.".format(str(no))
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
        if no == jml:
            textx += ""
            textx += ""
        ghi.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        ghi.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def timeChange(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weeks, days = divmod(days,7)
    months, weeks = divmod(weeks,4)
    text = ""
    if months != 0: text += "%02d bulan" % (months)
    if weeks != 0: text += " %02d minggu" % (weeks)
    if days != 0: text += " %02d hari" % (days)
    if hours !=  0: text +=  " %02d jam" % (hours)
    if mins != 0: text += " %02d menit" % (mins)
    if secs != 0: text += " %02d detik" % (secs)
    if text[0] == " ":
            text = text[1:]
    return text
def restartBot():
    print ("RESETBOT..")
    python = sys.executable
    os.execl(python, python, *sys.argv)
def load():
    global images
    global stickers
    with open("image.json","r") as fp:
        images = json.load(fp)
    with open("sticker.json","r") as fp:
        stickers = json.load(fp)
def sendStickers(to, sver, spkg, sid):
    contentMetadata = {
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    ghi.sendMessage(to, '', contentMetadata, 7)
def sendSticker(to, mid, sver, spkg, sid):
    contentMetadata = {
        'MSG_SENDER_NAME': ghi.getContact(mid).displayName,
        'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + ghi.getContact(mid).pictureStatus,
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    ghi.sendMessage(to, '', contentMetadata, 7)
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            ghi.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
def removeCmd(cmd, text):
    key = settings["keyCommand"]
    if settings["setKey"] == False: key = ''  
    rmv = len(key + cmd) + 1
    return text[rmv:]
def duc1(to, duc1):
    data={
"type": "flex",
"altText": duc1,
"contents": {
"type": "bubble",
"styles": {
"footer": {"backgroundColor": "#000000"},
},
"footer": {
"type": "box",
"layout": "vertical",
"spacing": "sm",
"contents": [
{
"type": "box",
"layout": "baseline",
"contents": [
{
"type": "icon",
"url": "https://obs.line-scdn.net/{}".format(ghi.getContact(ghiMID).pictureStatus),
"size": "md"
},
{
"type": "text",
"text": duc1,
"color":"#00FF00",
"gravity": "center",
"align":"center",
"wrap": True,
"size": "md"
},
{
"type": "icon",
"url": "https://obs.line-scdn.net/{}".format(ghi.getContact(ghiMID).pictureStatus),
"size": "md"
},
]
}
]
}
}
}
    sendTemplate(to, data)
#=====================================================================
#=====================================================================
def backupData():
    try:
        backup = settings
        f = codecs.open('max.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = images
        f = codecs.open('image.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = stickers
        f = codecs.open('sticker.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = wait
        f = codecs.open('Max2.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
#==============================================================================#
async def ghiBot(op):
    try:
        if settings["restartPoint"] != None:
            ghi.sendMessage(settings["restartPoint"], 'Successfully logged in')
            settings["restartPoint"] = None
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
              ghi.findAndAddContactsByMid(op.param1)
              ghi.sendMessage(op.param1,"{}".format(tagadd["add"]))
              msgSticker = sets["messageSticker"]["listSticker"]["add"]
              if msgSticker != None:
                  sid = msgSticker["STKID"]
                  spkg = msgSticker["STKPKGID"]
                  sver = msgSticker["STKVER"]
                  sendSticker(op.param1, sver, spkg, sid)
              print ("[ 5 ] AUTO ADD")
        if op.type == 5:
            if settings["autoblock"] == True:
              ghi.sendMessage(op.param1,tagadd["b"])
              ghi.blockContact(op.param1)
              print ("[ 5 ] AUTO BLOCK")
        if op.type == 13:
         if kcn["autojoin"] == True:
             G = ghi.getCompactGroup(op.param1)
             if len(G.members) <= kcn["Members"]:
                 ghi.acceptGroupInvitation(op.param1)
                 ghi.leaveGroup(op.param1)               	
             else:
                 ghi.acceptGroupInvitation(op.param1)
                 
        if op.type == 13:
            if ghiMID in op.param3:
                if did["join"] == True:
                    friend = ghi.getAllContactIds()
                    kontak = ghi.getContacts(friend)
                    for ids in kontak:
                      The = ids.mid
                      if op.param2 not in The:
                          try:
                             ghi.acceptGroupInvitation(op.param1)
                             ginfo = ghi.getGroup(op.param1)
                          except:
                             ghi.acceptGroupInvitation(op.param1)
                             ginfo = ghi.getGroup(op.param1)
                             ghi.sendMessage(op.param1,"BYE BYE~~")
                             ghi.leaveGroup(op.param1)
        if op.type == 13:
            if ghiMID in op.param3:
                G = ghi.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            ghi.acceptGroupInvitation(op.param1)
                        else:
                            ghi.leaveGroup(op.param1)
                    else:
                        ghi.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        ghi.acceptGroupInvitation(op.param1)
                        ghi.leaveGroup(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in apalo["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    ghi.acceptGroupInvitation(op.param1, matched_list)
                    ghi.leaveGroup(op.param1, matched_list)
                    print ("[ 17 ] LEAVE GROUP")
        if op.type == 15:
          if settings["Leave"] == True:
            if op.param2 in admin:
                return
            ginfo = ghi.getGroup(op.param1)
            contact = ghi.getContact(op.param2)
            name = contact.displayName
            pp = contact.pictureStatus
            s = name + " " + tagadd["lv"]
            data = {
                "type": "flex",
                "altText": "BAPER",
                "contents": {
                    "type": "bubble",
                    "styles": {
                        "body": {
                            "backgroundColor": '#EE1289'
                        },
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "{}".format(s),
                                "wrap": True,
                                "color": "#00F5FF",
                                "gravity": "center",
                                "size": "md"
                            },
                        ]
                    }
                }
            }
            sendTemplate(op.param1, data)
            data = {
                "type": "flex",
                "altText": "BAPER",
                "contents": {
                    "type": "bubble",
                    "hero": {
                         "type":"image",
                         "url": "https://profile.line-scdn.net/" + str(pp),
                         "size":"full",
                         "action": {
                             "type": "uri",
                             "uri": "line://ti/p/~nonbysignal"
                     #      
                     #   "
                         }
                    },
                }
            }
            sendTemplate(op.param1, data)
        if op.type == 15:
          if settings["lv"] == True:
              ginfo = ghi.getGroup(op.param1)
              msg = sets["messageSticker"]["listSticker"]["lv"]
              if msg != None:
                  contact = ghi.getContact(ghiMID)
                  a = contact.displayName
                  stk = msg['STKID']
                  spk = msg['STKPKGID']
                  data={'type':'template','altText': str(a)+' Send stickers','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                  sendTemplate(op.param1, data)
        if op.type == 17:
          if settings["Welcome"] == True:
            if op.param2 in admin:
                return
            g = ghi.getGroup(op.param1)
            contact = ghi.getContact(op.param2)
            gname = g.name
            name = contact.displayName
            pp = contact.pictureStatus
            s = "〖 Group Welcome 〗\n"
            s += "\n• Group name : {}".format(gname)
            s += "\n• Welcome togroup : {}\n\n".format(name)
            s += tagadd["wctext"]
            data = {
                "type": "flex",
                "altText": "WELCOME",
                "contents": {
                    "type": "bubble",
                    "styles": {
                        "body": {
                            "backgroundColor": '#EE1289'
                        },
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "{}".format(s),
                                "wrap": True,
                                "color": "#00F5FF",
                                "align": "center",
                                "gravity": "center",
                                "size": "md"
                            },
                        ]
                    }
                }
            }
            sendTemplate(op.param1, data)
            data = {
                "type": "flex",
                "altText": "WELCOME",
                "contents": {
                    "type": "bubble",
                    "hero": {
                         "type":"image",
                         "url": "https://profile.line-scdn.net/" + str(pp),
                         "size":"full",
                         "action": {
                             "type": "uri",
                             "uri": "line://ti/p/~nonbysignal"
                           #"
                         }
                    },
                }
            }
            sendTemplate(op.param1, data)
        if op.type == 17:
          if settings["Wc"] == True:
            if op.param2 in admin:
                return
            ginfo = ghi.getGroup(op.param1)
            contact = ghi.getContact(op.param2)
            cover = ghi.getProfileCoverURL(op.param2)
            names = contact.displayName
            status = contact.statusMessage
            pp = contact.pictureStatus
            data = {
                "type": "flex",
                "altText": "ELCOME TO MY GROUP",
                "contents": {
                    "type": "bubble",
                    'styles': {
                        "body": {
                            "backgroundColor": '#EE1289'
                        },
                     },
                     "hero": {
                         "type":"image",
                         "url": cover,
                         "size":"full",
                         "aspectRatio":"20:13",
                         "aspectMode":"cover"
                     },
                     "body": {
                         "type": "box",
                         "layout": "vertical",
                         "contents": [
                             {
                                 "type": "image",
                                 "url": "https://profile.line-scdn.net/" + str(pp),
                                 "size": "lg"
                             },
                             {
                                 "type":"text",
                                 "text":" "
                             },
                             {
                                 "type":"text",
                                 "text":"{}".format(names),
                                 "size":"xl",
                                 "weight":"bold",
                                 "color":"#00F5FF",
                                 "align":"center"
                             },
                             {
                                 "type": "text",
                                 "text": status,
                                 "wrap": True,
                                 "align": "center",
                                 "gravity": "center",
                                 "color": "#00F5FF",
                                 "size": "md"
                            },
                        ]
                    }
                }
            }
            sendTemplate(op.param1, data)
        if op.type == 17:
          if settings["wcsti2"] == True:
              ginfo = ghi.getGroup(op.param1)
              msg = sets["messageSticker"]["listSticker"]["wc"]
              if msg != None:
                  contact = ghi.getContact(ghiMID)
                  a = contact.displayName
                  stk = msg['STKID']
                  spk = msg['STKPKGID']
                  data={'type':'template','altText': str(a)+' kirim stiker','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                  sendTemplate(op.param1, data)
                     
        if op.type == 24:
            if settings["autoLeave"] == True:
                ghi.leaveRoom(op.param1)                      
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if apalo["winvite"] == True:
                     if msg._from in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = ghi.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 ghi.sendMessage(msg.to,"-> " + _name + " Berhasil diundang")
                                 break
                             elif invite in apalo["blacklist"]:
                                 ghi.sendMessage(msg.to,"Maaf " + _name + " Orang ini ada dalam daftar hitam")
                                 ghi.sendMessage(msg.to,"ใช้คำสั่ง!,ล้างดำ,ดึง" )
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     ghi.findAndAddContactsByMid(target)
                                     ghi.inviteIntoGroup(msg.to,[target])
                                     ghi.sendMessage(msg.to,"undang :" + _name + "selesai")
                                     apalo["winvite"] = False
                                     break
                                 except:
                                     try:
                                         ghi.findAndAddContactsByMid(invite)
                                         ghi.inviteIntoGroup(op.param1,[invite])
                                         apalo["winvite"] = False
                                     except:
                                         ghi.sendMessage(msg.to,"😧Mendeteksi kesalahan yang tidak diketahui😩Mungkin akun Anda telah diblokir😨")
                                         apalo["winvite"] = False
                                         break
        if op.type == 25:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.to not in unsendchat:
                unsendchat[msg.to] = {}
            if msg_id not in unsendchat[msg.to]:
                unsendchat[msg.to][msg_id] = msg_id
            msgdikirim[msg_id] = {"text":text}
            to = msg.to
            isValid = True
            cmd = command(text)
            setkey = settings['keyCommand'].title()
            if settings['setKey'] == False: setkey = ''
            if isValid != False:
                if msg.contentType in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]:
                    try:
                        if msg.to not in wait['Unsend']:
                            wait['Unsend'][msg.to] = {'B':[]}
                        if msg._from not in [ghiMID]:
                            return
                        wait['Unsend'][msg.to]['B'].append(msg.id)
                    except:pass
        if op.type in [25, 26]:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != ghiMID: to = sender
                else: to = receiver
                if msg._from not in ghiMID:
                  if apalo["talkban"] == True:
                    if msg._from in apalo["Talkblacklist"]:
                        ghi.sendMention(to, "akun anda dalam tahanan @! :)","",[msg._from])
                        ghi.kickoutFromGroup(msg.to, [msg._from])
                if msg.contentType == 13:
                  if apalo["Talkwblacklist"] == True:
                    if msg._from in admin:
                      if msg.contentMetadata["mid"] in apalo["Talkblacklist"]:
                          ghi.sendMessage(msg.to,"Sudah Ada")
                          apalo["Talkwblacklist"] = False
                      else:
                          apalo["Talkblacklist"][msg.contentMetadata["mid"]] = True
                          apalo["Talkwblacklist"] = False
                          duc1(to, "Tambahkan akun ini ke daftar hitam")
                  if apalo["Talkdblacklist"] == True:
                    if msg._from in admin:
                      if msg.contentMetadata["mid"] in apalo["Talkblacklist"]:
                          del apalo["Talkblacklist"][msg.contentMetadata["mid"]]
                          duc1(to, "Tambahkan akun ini ke daftar putih")
                          apalo["Talkdblacklist"] = False
                      else:
                          apalo["Talkdblacklist"] = False
                          ghi.sendMessage(msg.to,"Tidak Ada Dalam Da ftar Blacklist")
        if op.type in [25,26]:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            isValid = True
            if isValid != False:
                if msg.toType == 0 and sender != ghiMID: to = sender
                else: to = receiver
                if msg.contentType == 16:
                    if msg.toType in [2,1,0]:
                        try:
                            if sets["l"] == True:
                                purl = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                                duc1(to,"like for you")
                                if purl[1] not in wait['postId']:
                                    ghi.likePost(purl[0], purl[1], random.choice([1001]))
                                if sets["c"] == True:
                                    ghi.createComment(purl[0], purl[1], sets["cm"])
                                    wait['postId'].append(purl[1])
                                else:
                                    pass
                        except Exception as e:
                                if sets["l"] == True:
                                    purl = msg.contentMetadata['postEndUrl'].split('homeId=')[1].split('&postId=')
                                    duc1(to,"like for you")
                                    if purl[1] not in wait['postId']:
                                        ghi.likePost(msg._from, purl[1], random.choice([1001]))
                                    if sets["c"] == True:
                                        ghi.createComment(msg._from, purl[1], sets["cm"])
                                        wait['postId'].append(purl[1])
                                    else:pass
              
#=====================================================================
#=====================================================================
        if op.type == 25:
            print("[ 25 ] SEND MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != ghi.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if text.lower() == "umumkan":
                    sa="Cara menggunakan pengumuman"
                    sa+="\n- Pesan pengumuman / ID line"
                    sa+="\nContoh"
                    sa+="\n- Pengumuman/Id line"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": " 🐧Khenzi🐧", "iconUrl": "https://obs.line-scdn.net/{}".format(ghi.getContact(ghiMID).pictureStatus),"linkUrl": "line.me/ti/p/0KGxZx8VYs"}}
                    sendTemplate(to,data)
                if text.lower() == "set api":
                    sa = "Cara menggunakan set api"
                    sa += "\n- Tetapkan kata kunci api ;; balas"
                    sa += "\nContoh"
                    sa += "\n- Set api tes ;; mengapa?"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "🐧Khenzi🐧 ", "iconUrl": "https://obs.line-scdn.net/{}".format(ghi.getContact(ghiMID).pictureStatus),"linkUrl": "line.me/ti/p/0KGxZx8VYs"}}
                    sendTemplate(to,data)
                if text.lower() == "stag":
                    sa = "Cara menggunakan stag"
                    sa += "\n- stag Jumlah @user"
                    sa += "\nContoh"
                    sa += "\n- stag 1 @user"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "🐧Khenzi🐧", "iconUrl": "https://obs.line-scdn.net/{}".format(ghi.getContact(ghiMID).pictureStatus),"linkUrl": "line.me/ti/p/0KGxZx8VYs"}}
                    sendTemplate(to,data)
                if text.lower() == "Mantra":
                    sa = "Cara menggunakan mantra"
                    sa += "\n- Mantra [pesan] @user"
                    sa += "\nContoh"
                    sa += "\n- Mantra pesan @user"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "🐧Khenzi🐧 ", "iconUrl": "https://obs.line-scdn.net/{}".format(ghi.getContact(ghiMID).pictureStatus),"linkUrl": "line.me/ti/p/0KGxZx8VYs"}}
                    sendTemplate(to,data)
                if text.lower() == "settings" or text.lower() == "set":
                    sas = "☆ Settings ☆"
                    if settings["autoAdd"] == True: sa = "\n• Autoadd ( On )"
                    else:sa = "\n• Autoadd ( Off )"
                    if settings["autoblock"] == True: sa += "\n• Autoblock ( On )"
                    else:sa += "\n• Autoblock ( Off )"
                    if settings["autoCancel"]["on"] == True: sa +="\n• Autocancel (On) " + str(settings["autoCancel"]["members"])
                    else:sa += "\n• Autocancel ( Off )"
                    if tagadd["tags"] == True: sa += "\n• Tags ( On )"
                    else:sa += "\n• Tags ( Off )"
                    if tagadd["tagss"] == True: sa += "\n• Tagss2 ( On )"
                    else:sa += "\n• Tagss2 ( Off )"
                    if sets["tagsticker"] == True: sa += "\n• Tagsticker ( On )"
                    else:sa += "\n• Tagsticker ( Off )"
                    if settings["autolike"] == True: sa += "\n• Autolike ( On )"
                    else:sa += "\n• Autolike ( Off )"
                    if settings["com"] == True: sa += "\n• Comment ( On )"
                    else:sa += "\n• Comment ( Off )"
                    if settings["Welcome"] == True: sa += "\n• Welcome ( On )"
                    else:sa += "\n• Welcome ( Off )"
                    if settings["Wc"] == True: sa += "\n• Welcome2 ( On )"
                    else:sa += "\n• Welcome2 ( Off )"
                    if settings["wcsti2"] == True: sa += "\n• Wcsti2 ( On )"
                    else:sa += "\n• Wcsti2 ( Off )"
                    if settings["Leave"] == True: sa += "\n• Respon leave ( On )"
                    else:sa += "\n• Respon leave ( Off )"
                    if settings["lv"] == True: sa += "\n• Autolv ( On )"
                    else:sa += "\n• Autolv ( Off )"
                    if settings["unsendMessage"] == True: sa += "\n• UnsendMessage ( On )"
                    else:sa += "\n• UnsendMessage ( Off )"
                    if settings["Sticker"] == True: sa += "\n• Sticker ( On )"
                    else:sa += "\n• Sticker ( Off )"
                    if sets["Sticker"] == True: sa += "\n• Kode sticker ( On )"
                    else:sa += "\n• Kode stiker ( Off )"
                    
                    data = {
                        "type": "flex",
                        "altText": "{}".format(sas),
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#0033FF'
                                },
                            },
                            "hero": {
                                            "type": "image",
                                            "url": "https://obs.line-scdn.net/{}".format(ghi.getContact(sender).pictureStatus),
                                            "size": "full",
                                            "aspectRatio": "1:1",
                                            "aspectMode": "fit",
                                        },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": sas,
                                        "color": "#00F5FF",
                                        "align": "center",
                                        "weight": "bold",
                                        "size": "xxl"
                                    },
                                    {
                                        "type": "text",
                                        "text": "{}".format(sa),
                                        "wrap": True,
                                        "color": "#003300",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            },
                        }
                    }
                    sendTemplate(to, data)
                elif text.lower() == 'clearban' or text.lower() == "clear":
                      apalo["Talkblacklist"] = []
                      duc1(to, "Succes Clearban")
                
                elif text.lower() == "blaklist":
                    if msg._from in ghiMID:
                        if apalo["Talkblacklist"] == []:
                            duc1(to, "Tidak ada orang blacklist")
                        else:
                            for bl in apalo["Talkblacklist"]:
                                ghi.sendMessage(to, text=None, contentMetadata={'mid': bl}, contentType=13)
                elif text.lower() == "kickblack":
                    if msg.toType == 2:
                        groupMemberMids = [contact.mid for contact in ghi.getGroup(to).members]
                        matched_list = []
                        for mid in apalo["Talkblacklist"]:
                            matched_list += [x for x in groupMemberMids if x == mid]
                        if matched_list == []:
                            duc1(to, "Tidak ada blacklist")
                        else:
                            for mids in matched_list:
                                try:
                                    ghi.kickoutFromGroup(to, [mids])
                                except:pass
                
                elif "Kick " in msg.text:
                    Ri0 = text.replace("kick ","")
                    Ri1 = Ri0.rstrip()
                    Ri2 = Ri1.replace("@","")
                    Ri3 = Ri2.rstrip()
                    _name = Ri3
                    gs = ghi.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    ghi.kickoutFromGroup(to,[target])
                                except:
                                    pass
                              
                elif "kidding " in msg.text:
                    Ri0 = text.replace("kidding ","")
                    Ri1 = Ri0.rstrip()
                    Ri2 = Ri1.replace("@","")
                    Ri3 = Ri2.rstrip()
                    _name = Ri3
                    gs = ghi.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    ghi.kickoutFromGroup(to,[target])
                                    ghi.findAndAddContactsByMid(target)
                                    ghi.inviteIntoGroup(to,[target])
                                except:
                                    pass
                
                elif "kick2 " in msg.text:
                        vkick0 = msg.text.replace("kick2 ","")
                        vkick1 = vkick0.rstrip()
                        vkick2 = vkick1.replace("@","")
                        vkick3 = vkick2.rstrip()
                        _name = vkick3
                        gs = ghi.getGroup(msg.to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    ghi.kickoutFromGroup(msg.to,[target])
                                    ghi.findAndAddContactsByMid(target)
                                    ghi.inviteIntoGroup(msg.to,[target])
                                    ghi.cancelGroupInvitation(msg.to,[target])
                                except:
                                    pass
                elif msg.text.lower().startswith("warna "):
                            text_ = removeCmd("warna", text)
                            try:
                                temp["t"] = text_
                                ghi.sendMessage(to,"「 Kode warna 」\nPilih : " + text_)
                            except:
                                ghi.sendMessage(to,"Already")
                elif msg.text.lower().startswith("font color "):
                            text_ = removeCmd("Font color", text)
                            try:
                                temp["te"] = text_
                                ghi.sendMessage(to,"「 Kode warna 」\nPilih : " + text_)
                            except:
                                ghi.sendMessage(to,"Already")
                elif msg.text.lower() == "kode warna":
                            c="https://i.pinimg.com/originals/d0/9c/8a/d09c8ad110eb44532825df454085a376.jpg"
                            p="https://i.pinimg.com/originals/7c/d3/aa/7cd3aa57150f8f6f18711ff22c9f6d4a.jpg"
                            m="Contoh1\n\nPesan ubah warna \nWarna #333333'\nContoh2 \n\nPerintah perubahan warnatag\nSet Warna #333333'"
                            ghi.sendImageWithURL(to,c)
                            ghi.sendImageWithURL(to,p)
                            ghi.sendMessage(to,m)
                elif msg.text.lower().startswith("Setblok "):
                            text_ = removeCmd("Setblok", text)
                            try:
                                tagadd["b"] = text_
                                ghi.sendMessage(to,"「 Blok otomatis 」\nApakah : " + text_)
                            except:
                                duc1(to, "Successfully completed")
                elif text.lower().startswith("autocancel "):
                            text_ = removeCmd("Autocancel", text)
                            try:
                                settings["autoCancel"]["members"] = text_
                                ghi.sendMessage(to,"「 Set autocancel 」\nNomor : " + text_)
                            except:
                                duc1(to, "Successfully completed")
                if text.lower() == "black":
                  if msg._from in admin:
                      apalo["Talkwblacklist"] = True
                      duc1(to, "Kirim targetnya")
                if text.lower() == "Putih":
                  if msg._from in admin:
                      apalo["Talkdblacklist"] = True
                      duc1(to, "Kirim targetnya")
                elif msg.text.lower().startswith("settag "):
                      text_ = removeCmd("settag", text)
                      try:
                          tagadd["tag"] = text_
                          sa = "「 Settag 」\nApakah : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "🐧Khenzi🐧 ", "iconUrl": "https://obs.line-scdn.net/{}".format(ghi.getContact(ghiMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ubd86e8c77559b1493f0ad64b1dba2d6c"}}
                          sendTemplate(to,data)
                      except:
                          ghi.sendMessage(to,"Done. >_<")
                elif msg.text.lower().startswith("setchat "):
                      text_ = removeCmd("Setchat", text)
                      try:
                          settings["reply"] = text_
                          sa = "「 Setcat 」\nApakah : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "🐧Khenzi🐧", "iconUrl": "https://obs.line-scdn.net/{}".format(ghi.getContact(ghiMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ubd86e8c77559b1493f0ad64b1dba2d6c"}}
                          sendTemplate(to,data)
                      except:
                          ghi.sendMessage(to,"Done. >_<")
                elif msg.text.lower().startswith("setwecome "):
                      text_ = removeCmd("Setwelcome", text)
                      try:
                          tagadd["wctext"] = text_
                          sa = "「 Setwelcome 」\nApakah : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": " 🐧Khenzi🐧", "iconUrl": "https://obs.line-scdn.net/{}".format(ghi.getContact(ghiMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ubd86e8c77559b1493f0ad64b1dba2d6c"}}
                          sendTemplate(to,data)
                      except:
                          ghi.sendMessags(to,"Done. >_<")
                elif msg.text.lower().startswith("setlv "):
                            text_ = removeCmd("Setlv", text)
                            try:
                                tagadd["lv"] = text_
                                ghi.sendMessage(to,"「 Setlv 」\nApakah : " + text_)
                            except:
                                ghi.sendMessage(to,"Done..")
                elif msg.text.lower().startswith("setadd "):
                      text_ = removeCmd("Setadd", text)
                      try:
                          tagadd["add"] = text_
                          sa = "「 Setadd 」\nApakah : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "🐧Khenzi🐧", "iconUrl": "https://obs.line-scdn.net/{}".format(ghi.getContact(ghiMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ubd86e8c77559b1493f0ad64b1dba2d6c"}}
                          sendTemplate(to,data)
                      except:
                          ghi.sendMessags(to,"Done. >_<")
                elif msg.text.lower().startswith("setcomment "):
                      text_ = removeCmd("Setcomment", text)
                      try:
                          settings["commet"] = text_
                          sa = "「 Setcomment 」\nApakah : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "🐧Khenzi🐧", "iconUrl": "https://obs.line-scdn.net/{}".format(ghi.getContact(ghiMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ubd86e8c77559b1493f0ad64b1dba2d6c"}}
                          sendTemplate(to,data)
                      except:
                          ghi.sendMessags(to,"Done. >_<")
                elif msg.text.lower() == "sayhallo":
                  if msg.toType == 0:
                     sendMention(to, to, "──┅••••••••●✦͜͡✾͜͡✦●••••••••┅──\n", "\n──┅••••••••●✦͜͡✾͜͡✦●••••••••┅──")
                  elif msg.toType == 2:
                     group = ghi.getGroup(to)
                     contact = [mem.mid for mem in group.members]
                     mentionMembers(to, contact)
                if text.lower() == "putar":
                    add = tagadd["add"]
                    tag = tagadd["tag"]
                    like = settings["commet"]
                    wc = tagadd["wctext"]
                    lv = tagadd["lv"]
                    c = settings["autoCancel"]["members"]
                    b = tagadd["b"]
                    Re = settings["reply"]
                    ghi.sendMessags(id, to, "Add text :\n"+str(add)+"\n\Tag text :\n"+str(tag)+"\n\nMessage :\n"+str(like)+"\n\nWelcome message :\n"+str(wc)+"\n\nlv message :\n"+str(lv)+"\n\nInvited amount :\n"+str(c)+" number\n\nBlock message :\n"+str(b)+"\n\nTag Chat Message :\n"+str(Re))
                if text.lower() == "help" or text.lower() == "!help":
                            s = "#00F5FF"
                            sa = "•✨ Help\n"
                            sa += "•✨ Me/Me2\n"
                            sa += "•✨ Mid\n"
                            sa += "•✨ Tag/!Tag\n"
                            sa += "•✨ settings\n"
                            sa += "•✨ Mynane\n"
                            sa += "•✨ Mybio\n"
                            sa += "•✨ Mypicture\n"
                            sa += "•✨ Myvideo\n"
                            sa += "•✨ Mycover\n"
                            sa += "•✨ Update [kirim]\n"
                            sa += "•✨ Myname: [Text]\n"
                            sa += "•✨ Mybio: [Text]\n"
                            sa += "•✨ Ginfo\n"
                            sa += "•✨ Gid\n"
                            sa += "•✨ Gname\n"
                            sa += "•✨ Gpict\n"
                            sa += "•✨ Glink\n"
                            ss = "•✨ Ourl\n"
                            ss += "•✨ Curl\n"
                            ss += "•✨ Add\n"
                            ss += "•✨ Cancel\n"
                            ss += "•✨ Clone: @user\n"
                            ss += "•✨ Unclone\n"
                            ss += "•✨ About\n"
                            ss += "•✨ Reset\n"
                            ss += "•✨ Runtime\n"
                            ss += "•✨ stag: [Jlh @target]\n"
                            ss += "•✨ Sikat: [mid]\n"
                            ss += "•✨ Youtube: [Text]\n"
                            ss += "•✨ image: [Tex]\n"
                            ss += "•✨ Wilayah: [Text]\n"
                            ss += "•✨ Kode warna\n"
                            ss += "•✨ Warna: [Kode warna]\n"
                            ss += "•✨ Font warna: [Kode warna]\n"
                            sd = "•✨ Idline [idline]\n"
                            sd += "•✨ Black [Kirim]\n"
                            sd += "•✨ White [kirim]\n"
                            sd += "•✨ White: @user\n"
                            sd += "•✨ Black: @user\n"
                            sd += "•✨ Clear: @user\n"
                            sd += "•✨ Blacklist\n"
                            sd += "•✨ Clearban\n"
                            sd += "•✨ Setwelcome: [Text]\n"
                            sd += "•✨ Setlv: [Text]\n"
                            sd += "•✨ Setadd: [Text]\n"
                            sd += "•✨ Settag: [Text]\n"
                            sd += "•✨ Setcomment: [Text]\n"
                            sd += "•✨ Setchat: [Text]\n"
                            sd += "•✨ Setblock: [Text]\n"
                            sd += "•✨ Tulis1: [Text]\n"
                            sd += "•✨ Kickall\n"
                            se = "•✨ Tags:On/ Off\n"
                            se += "•✨ Tagss:On/Pff\n"
                            se += "•✨ Sticker1:On/Off\n"
                            se += "•✨ Stkbig:On/Off\n"
                            se += "•✨ Tagsticker:On/Off\n"
                            se += "•✨ Comment:On/Off\n"
                            se += "•✨ Jointicket On/Off\n"
                            se += "•✨ Autolike:On/Off\n"
                            se += "•✨ Autojoin:On/Off\n"
                            se += "•✨ Autoblock:On/Off\n"
                            se += "•✨ Autoadd:On/Off\n"
                            se += "•✨ Autocancel:On/Off\n"
                            se += "•✨ Welcome:On/Off\n"
                            se += "•✨ Welcome2:On/Off\n"
                            se += "•✨ Autoleave:On/Off\n"
                            se += "•✨ Unsend:On/Off\n"
                            se += "•✨ Wcsti2:On/Off\n"
                            se += "•✨ Lv:On/Off\n"
                            sti = "•✨ Chat:on\n"
                            sti += "•✨ Chat:off\n"
                            sti += "•✨ Stkadd\n"
                            sti += "•✨ Dellstkadd\n"
                            sti += "•✨ Addstktag\n"
                            sti += "•✨ Dellstktag\n"
                            sti += "•✨ Addstkwc\n"
                            sti += "•✨ Dellstkwc\n"
                            sti += "•✨ Addstklv\n"
                            sti += "•✨ Dellstklv\n"
                            sti += "•✨ Addstkjoin\n"
                            sti += "•✨ Dellstkjoin\n"
                            sti += "•✨ Winvite [contak]\n"
                            sti += "•✨ Winvite: @user\n"
                            sti += "•✨ Blokir: @user\n"
                            sti += "•✨ Addfriend: @user\n"
                            sti += "•✨ Dellfriend: @user\n"
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#0033FF"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                               "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(ghi.getContact(ghiMID).pictureStatus),
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": "•MENU•",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sa,
                                                "color": s, 
                                                "wrap": True,
                                                "gravity": "center",
                                        #        "size": "md"
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#333300",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"✡Naughty Finger✡",
                                                     "uri":"line://ti/p/~nonbysignal"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#0033FF"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(ghi.getContact(ghiMID).pictureStatus),
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": "• MENU•",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": ss, 
                                                "color": s,
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#333300",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"✡Naughty Finger✡",
                                                     "uri":"line://ti/p/~nonbysignal"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#0033FF"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(ghi.getContact(ghiMID).pictureStatus),
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": "• MENU •",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sd, 
                                                "color": s,
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#333300",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"✡Naughty Finger✡",
                                                     "uri":"line://ti/p/~nonbysignal"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#0033FF"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(ghi.getContact(ghiMID).pictureStatus),
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": "• MENU •",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                          #  {
                                          #      "type": "text",
                                           #     "text": " "
                                         #   },
                                         #   {
                                            #    "type": "text",
                                           #     "text": " "
                                          #  },
                                            {
                                                "type": "text",
                                                "text": se, 
                                                "color": s,
                                           #     "size": "lg",
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            #{
                                            #    "type": "text",
                                            #    "text": " "
                                           # },
                                          #  {
                                           #     "type": "text",
                                            #    "text": " "
                                           # },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                          #  {
                                          #      "type": "text",
                                          #      "text": "สนใจบอท ติดต่อได้ที่ปุ่มเลยค้ะ >_<",
                                          #      "color": "#B5B5B5",
                                          #      "size": "xs"
                                          #  },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#333300",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"✡Naughty Finger✡",
                                                     "uri":"line://ti/p/~nonbysignal"
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#0033FF"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(ghi.getContact(ghiMID).pictureStatus),
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": "• MENU •",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sti, 
                                                "color": s,
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#333300",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"✡Naughty Finger✡",
                                                     "uri":"line://ti/p/~nonbysignal"
                                                 },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "TOLOOOONG",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
#=====================================================================
                elif msg.text.lower().startswith("clone "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                clone = ast.literal_eval(msg.contentMetadata['MENTION'])
                                clones = clone['MENTIONEES']
                                target = []
                                for clone in clones:
                                    if clone["M"] not in target:
                                        target.append(clone["M"])
                                for she in target:
                                    BackupProfile = ghi.getContact(sender)
                                    Save1 = "http://dl.profile.line-cdn.net/{}".format(BackupProfile.pictureStatus);Save2 = "{}".format(BackupProfile.displayName);ProfileMe["PictureMe"] = Save1;ProfileMe["NameMe"] = Save2
                                    contact = ghi.getContact(she);ClonerV2(she)
                                    sendMention(to, contact.mid, "=͟͟͞͞➳ You are copying", "succeeded >_<");ghi.sendContact(to, str(BackupProfile.mid));ghi.sendContact(to, str(contact.mid))
                elif text.lower() == "unclone":
                            try:
                                ghistatus = ghi.getProfile()
                                ghiName = ghi.getProfile()
                                ghiName.statusMessage = ProfileMe["statusMessage"]
                                ghiName.pictureStatus = str(ProfileMe["pictureStatus"])
                                ghi.updateProfile(ghistatus)
                                ghiName.displayName = ProfileMe["NameMe"]
                                ghi.updateProfile(ghiName)
                                path = ghi.downloadFileURL(ProfileMe["PictureMe"])
                                ghi.updateProfilePicture(path)
                                coverId = ProfileMe["coverId"]
                                ghi.updateProfileCoverById(coverId)
                                BackupProfile = ghi.getContact(sender)
                                sendMention(to, BackupProfile.mid, "=͟͟͞͞➳ Succes kembali ke konsep awal", ">_<");ghi.sendContact(to, str(BackupProfile.mid))
                            except Exception as error:
                                duc1(to, "You have not copied")
                elif msg.text.lower().startswith("."):
                    text = msg.text.lower().replace("."," ")
                    duc1(msg.to,text)
                if text.lower() == "Khot":
                    ghi.generateReplyMessage(msg.id) 
                    ghi.sendReplyMessage(msg.id, to, None, contentMetadata={'mid': ghiMID}, contentType=13)
                if text.lower() == "mid" or text.lower() == "mymid":
                    ghi.generateReplyMessage(msg.id)
                    ghi.sendReplyMessage(msg.id, to,ghiMID)
                elif text.lower() == "myname" or text.lower() == "myname":
                            h = ghi.getContact(ghiMID)
                            ghi.generateReplyMessage(msg.id)
                            ghi.sendReplyMessage(msg.id, to, "「 Your Name 」\n"+str(h.displayName))
                elif text.lower() == "mybio" or text.lower() == "mybio":
                            h = ghi.getContact(ghiMID)
                            ghi.generateReplyMessage(msg.id)
                            ghi.sendReplyMessage(msg.id, to, "「 Your bio 」\n"+str(h.statusMessage))
                elif text.lower() == "mypicture" or text.lower() == "mypicture":
                            h = ghi.getContact(ghiMID)
                            image = "http://dl.profile.line-cdn.net/" + h.pictureStatus
                            ghi.generateReplyMessage(msg.id)
                            ghi.sendReplyImageWithURL(msg.id, to, image)
                elif text.lower() == "myvideo" or text.lower() == "myvideo":
                            h = ghi.getContact(ghiMID)
                            if h.videoProfile == None:
                            	return ghi.sendMessage(to, "You don't have a video 😝😝😝")
                            ghi.generateReplyMessage(msg.id)
                            ghi.sendReplyVideoWithURL(msg.id, to,"http://dl.profile.line-cdn.net/" + h.pictureStatus + "/vp")
                elif text.lower() == "mycover" or text.lower() == "mycover":
                            h = ghi.getContact(ghiMID)
                            cu = ghi.getProfileCoverURL(ghiMID)
                            image = str(cu)
                            ghi.generateReplyMessage(msg.id)
                            ghi.sendReplyImageWithURL(msg.id, to, image)
                elif msg.text in ["tarik"]:
                        apalo["winvite"] = True
                        duc1(to, "Send the cots to pull down")
                            
                elif "myname " in text.lower():
                    if msg._from in admin:
                        proses = text.split(" ")
                        string = text.replace(proses[0] + " ","")
                        profile_A = ghi.getProfile()
                        profile_A.displayName = string
                        ghi.updateProfile(profile_A)
                        ghi.sendMessage(msg.to,"Update to :\n" + string)
                        print ("Update Name")

                elif "mybio " in msg.text.lower():
                    if msg._from in admin:
                        proses = text.split(" ")
                        string = text.replace(proses[0] + " ","")
                        profile_A = ghi.getProfile()
                        profile_A.statusMessage = string
                        ghi.updateProfile(profile_A)
                        ghi.sendMessage(msg.to,"Succes Update :\n" + string)
                        print ("Update Bio Succes")
                        
                elif text.lower() == "update":
                    sets["changePictureProfile"] = True
                    #maxgie.unsendMessage(msg_id)
                    duc1(to, "Send pictures that will be updated")
                elif text.lower() == 'On':
                    did["join"] = True
                    #maxgie.unsendMessage(msg_id)
                    duc1(to, "Automatically include chat (open)")
                elif text.lower() == 'Off':
                    did["join"] = False
                    #maxgie.unsendMessage(msg_id)
                    duc1(to, "Automatically chat out (closed)") 
                if text.lower() == "On1":
                    cover = ghi.getProfileCoverURL(ghi.profile.mid)
                    pp = ghi.getProfile().pictureStatus
                    profile = "https://profile.line-scdn.net/" + str(pp)
                    name = ghi.getProfile().displayName
                    status = ghi.getProfile().statusMessage     
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    eltime = time.time() - mulai
                    van = ggggg(eltime)
                    van2 = "\n\nTanggal :"+ datetime.strftime(timeNow,'%d-%m-%Y')+"\n───────────\n◐Jam:"+ datetime.strftime(timeNow,'%H:%M:%S')+"\n\n"      
                    data={
"type":"flex",
"altText":"WELCOME",
"contents":{
"type": "carousel",
"contents": [
{
"type": "bubble",
"styles": {
"header": {"backgroundColor": "#EE1289", "separator": True, "separatorColor": "#0033FF"},
"body": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"},
"footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"}
},
"header": {
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": "Aktif",
"align": "center",
"size": "lg",
"weight": "bold",
"color": "#00F5FF",
"wrap": True
}
]
},
"type": "bubble",
"body": {
"contents": [
{
"contents": [
{
"url": profile,
"type": "image"
},
{
"type": "separator",
"color": "#00F5FF"
},
{
"url": profile,
"type": "image"
}
],
"type": "box",
"spacing": "md",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#00F5FF"
},
{
"contents": [
{
"text": "The duration of the bot",
"size": "md",
"align": "center",
"color": "#00F5FF",
"wrap": True,
"weight": "bold",
"type": "text"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
{
"type": "separator",
"color": "#00F5FF"
},
{
"contents": [
{
"contents": [
{
"type": "text",
"text": van,
"align": "center",
"size": "xs",
"weight": "bold",
"color": "#00F5FF",
"wrap": True
}
],
"type": "box",
"layout": "baseline"
},
{
"contents": [
{
"url": profile,
"type": "icon",
"size": "md"
},
{
"text": " ➡ Creator By : \n 🐧Khenzi🐧",
"size": "xs",
"margin": "none",
"color": "#00F5FF",
"wrap": True,
"weight": "regular",
"type": "text"
}
],
"type": "box",
"layout": "baseline"
}
],
"type": "box",
"layout": "vertical"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
"footer": {
"type": "box",
"layout": "horizontal",
"spacing": "sm",
"contents": [
{
"type": "button",
"flex": 2,
"style": "primary",
"color": "#00F5FF",
"height": "sm",
"action": {
"type": "uri",
"label": "Contact us",
"uri": "https://line.me/ti/p/0KGxZx8VYs",
}
},
{
"flex": 3,
"type": "button",
"style": "primary",
"color": "#00F5FF",
"margin": "sm",
"height": "sm",
"action": {
"type": "uri",
"label": "Contact Us",
"uri": "https://line.me/ti/p/0KGxZx8VYs",
}
}
]
}
},
{
"type": "bubble",
"styles": {
"header": {"backgroundColor": "#0033FF", "separator": True, "separatorColor": "#0033FF"},
"body": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"},
"footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"}
},
"header": {
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": "Calendar",
"align": "center",
"size": "lg",
"weight": "bold",
"color": "#00F5FF",
"wrap": True
}
]
},
"type": "bubble",
"body": {
"contents": [
{
"contents": [
{
"url": profile,
"type": "image"
},
{
"type": "separator",
"color": "#00F5FF"
},
{
"url": profile,
"type": "image"
}
],
"type": "box",
"spacing": "md",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#00F5FF"
},
{
"contents": [
{
"text": "Date, month and time",
"size": "md",
"align": "center",
"color": "#00F5FF",
"wrap": True,
"weight": "bold",
"type": "text"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
{
"type": "separator",
"color": "#00F5FF"
},
{
"contents": [
{
"contents": [
{
"type": "text",
"text": van2,
"align": "center",
"size": "xs",
"weight": "bold",
"color": "#00F5FF",
"wrap": True
}
],
"type": "box",
"layout": "baseline"
},
{
"contents": [
{
"url": profile,
"type": "icon",
"size": "md"
},
{
"text": " ➡ Creator By : \n 🐧Khenzi🐧",
"size": "xs",
"margin": "none",
"color": "#00F5FF",
"wrap": True,
"weight": "regular",
"type": "text"
}
],
"type": "box",
"layout": "baseline"
}
],
"type": "box",
"layout": "vertical"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
"footer": {
"type": "box",
"layout": "horizontal",
"spacing": "sm",
"contents": [
{
"type": "button",
"flex": 2,
"style": "primary",
"color": "#00F5FF",
"height": "sm",
"action": {
"type": "uri",
"label": "Contact the creator",
"uri": "https://line.me/ti/p/0KGxZx8VYs",
}
},
{
"flex": 3,
"type": "button",
"style": "primary",
"color": "#00F5FF",
"margin": "sm",
"height": "sm",
"action": {
"type": "uri",
"label": "Contact the creator",
"uri": "https://line.me/ti/p/0KGxZx8VYs",
}
}
]
}
}
]
}
}                    
                    sendTemplate(to, data)
                if text.lower() == "runtime" or text.lower() == "runtime":
                    contact = ghi.getContact(sender)
                    timeNow = time.time() - Start
                    runtime = timeChange(timeNow)
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)   
                    a = "Tanggal"+ datetime.strftime(timeNow,'%d-%m-%Y')+"Waktu"+ datetime.strftime(timeNow,'%H:%M:%S')+"\n"
                    run = "「Time On 」\n"
                    run += runtime
                    data = {
                            "type": "flex",
                            "altText": "{}".format(run),
                            "contents": {
                            "styles": {
                              "body": {
                                "backgroundColor": "#0033FF"
                              },
                              "footer": {
                                "backgroundColor": "#0033FF"
                              }
                            },
                            "type": "bubble",
                            "body": {
                              "contents": [
                                {
                                  "contents": [
                                    {
                                      "url": "https://obs.line-scdn.net/{}".format(ghi.getContact(ghiMID).pictureStatus),
                                      "type": "image"
                                    },
                                    {
                                      "type": "separator",
                                      "color": "#00F5FF"
                                    },
                                    {
                                      "url": "https://obs.line-scdn.net/{}".format(ghi.getContact(ghiMID).pictureStatus),
                                      "type": "image"
                                    }
                                  ],
                                  "type": "box",
                                  "spacing": "md",
                                  "layout": "horizontal"
                                },
                                {
                                  "type": "separator",
                                  "color": "#00F5FF"
                                },
                                {
                                  "contents": [
                                    {
                                      "text": "working period",
                                      "size": "lg",
                                      "align": "center",
                                      "color": "#00F5FF",
                                      "wrap": True,
                                      "weight": "bold",
                                      "type": "text"
                                    }
                                  ],
                                  "type": "box",
                                  "spacing": "md",
                                  "layout": "vertical"
                                },
                                {
                                  "type": "separator",
                                  "color": "#00F5FF"
                                },
                                {
                                  "contents": [
                                    {
                                      "contents": [
                                        {
                                          "text": "{}".format(run),
                                          "size": "lg",
                                          "align": "center",
                                          "margin": "none",
                                          "color": "#00F5FF",
                                          "wrap": True,
                                          "weight": "regular",
                                          "type": "text"
                                        }
                                      ],
                                      "type": "box",
                                      "layout": "baseline"
                                    },
                                  ],
                                  "type": "box",
                                  "layout": "vertical"
                                }
                              ],
                              "type": "box",
                              "spacing": "md",
                              "layout": "vertical"
                            },
                            "footer": {
                              "contents": [
                                {
                                  "contents": [
                                    {
                                      "contents": [
                                        {
                                          "text": "🐧Khenzi🐧",
                                          "size": "xl",
                                          "action": {
                                            "uri": "line.me/ti/p/0KGxZx8VYs",
                                            "type": "uri",
                                            "label": "Add Maker"
                                          },
                                          "margin": "xl",
                                          "align": "center",
                                          "color": "#00F5FF",
                                          "weight": "bold",
                                          "type": "text"
                                        }
                                      ],
                                      "type": "box",
                                      "layout": "baseline"
                                    }
                                  ],
                                  "type": "box",
                                  "layout": "horizontal"
                                }
                              ],
                              "type": "box",
                              "layout": "vertical"
                            }
                        }
                    }
                    sendTemplate(to, data)
                if text.lower() == "me":
                    cover = ghi.getProfileCoverURL(ghi.profile.mid)
                    pp = ghi.getProfile().pictureStatus
                    profile = "https://profile.line-scdn.net/" + str(pp)
                    name = ghi.getProfile().displayName
                    status = ghi.getProfile().statusMessage
                    s = temp["te"]
                    a = temp["t"]
                    data={"type":"flex","altText":"{} sendFlex".format(name),"contents":{"type":"bubble",'styles': {"body":{"backgroundColor":a}},"hero":{"type":"image","url":cover,"size":"full","aspectRatio":"20:13","aspectMode":"cover"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":" "},{"type":"image","url":profile,"size":"lg"},{"type":"text","text":" "},{"type":"text","text":name,"size":"xl","weight":"bold","color":s,"align":"center"},{"type":"text","text":" "},{"type":"text","text":status,"align":"center","size":"xs","color":s,"wrap":True},{"type":"text","text":" "},{"type":"button","style":"primary","color":"#003300","action":{"type":"uri","label":"🐧Khenzi🐧","uri":"line://app/1602687308-GXq4Vvk9?type=video&ocu=https://is.gd/pv49jP&piu=https://i.pinimg.com/originals/63/c4/12/63c412c55c99b6e0742bebaf53dd40d6.jpg"}}]}}}
                    sendTemplate(to, data)
                elif text.lower() == "me2":
                            s = temp["te"]
                            a = temp["t"]
                            contact = ghi.getContact(ghiMID)
                            cover = ghi.getProfileCoverURL(ghiMID)
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": a},
                                        "body": {"backgroundColor": a},# "separator": True, "separatorColor": "#0033FF"},
                                        "footer": {"backgroundColor": a, "separator": True, "separatorColor": s}
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                        "size": "full",
                                        "aspectRatio": "1:1",
                                        "aspectMode": "fit",
                                    },
                                    "body": {
                                       "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.displayName),
                                                "align": "center",
                                                "weight": "bold",
                                                "color": s,
                                                "size": "lg",
                                                'flex': 1
                                            },
                                            {
                                                "type": "text",
                                                "text": " profile picture ",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s,
                                                "size": "lg",
                                                'flex': 1,
                                           },
                                       ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://os.line.naver.jp/os/p/"+ghiMID,
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "🐧Khenzi🐧",
                                                        "align": "center",
                                                        "color": s,
                                                        "size": "md",
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/0KGxZx8VYs"
                                                        }
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm",
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": a},
                                        "body": {"backgroundColor": a},
                                        "footer": {"backgroundColor": a, "separator": True, "separatorColor": s}
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(cover),
                                        "size": "full",
                                        "aspectRatio":"20:13",
                                        "aspectMode":"cover"
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.mid),
                                                "align": "center",
                                                "color": s,
                                                "size": "sm",
                                                "flex": 1,
                                            },
                                            {
                                                "type": "text",
                                                "text": "Background cover ",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s,
                                                "size": "lg",
                                                'flex': 1,
                                           },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://os.line.naver.jp/os/p/"+ghiMID,
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "🐧Khenzi🐧",
                                                        "align": "center",
                                                        "color": s,
                                                        "size": "md",
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line://ti/p/~nonbysignal"
                                                        }
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm",
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": a},
                                        "body": {"backgroundColor": a},# "separator": True, "separatorColor": "#0033FF"},
                                        "footer": {"backgroundColor": a, "separator": True, "separatorColor": s}
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Your Name",
                                                "size": "lg",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.displayName),
                                                "align": "center",
                                                "color": s,
                                                "size": "md"
                                            },
                                            {
                                                "type": "text",
                                                "text": "-",
                                                "align": "center",
                                                "color": a,
                                                "size": "sm",
                                            },
                                            {
                                                "type": "text",
                                                "text": "Your status ",
                                                "size": "lg",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.statusMessage),
                                                "align": "center",
                                                "color": s,
                                                "wrap": True,
                                                "size": "md"
                                           },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://os.line.naver.jp/os/p/"+ghiMID,
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "🐧Khenzi🐧",
                                                        "align": "center",
                                                        "color": s,
                                                        "size": "md",
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line://ti/p/~nonbysignal"
                                                        }
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                }
                            ]
                            data = {
                                "type": "flex",
                                "altText": "{}".format(contact.displayName),
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
                if text.lower() == "me3":
                    contact = ghi.getContact(sender)
                    sendTemplate(to,{"type":"flex","altText": " 🐧Khenzi🐧","contents":{"type":"bubble","footer":{"type":"box","layout":"horizontal","contents":[{"color":"#333333","size":"xs","wrap":True,"action":{"type":"uri","uri":"line://app/1602687308-GXq4Vvk9?type=video&ocu=https://img.live/images/2019/02/10/1549778907829.jpg"},"type":"text","text":"🐧Khenzi🐧","align":"center","weight":"bold"},{"type":"separator","color":"#003300"},{"color":"#003300","size":"xs","wrap":True,"action":{"type":"uri","uri":"line.me/ti/p/0KGxZx8VYs"},"type":"text","text":"Creator","align":"center","weight":"bold"}]},"styles":{"footer":{"backgroundColor":"#000000"},"body":{"backgroundColor":"#0033FF"}},"body":{"type":"box","contents":[{"type":"box","contents":[{"type":"separator","color":"#003300"},{"aspectMode":"cover","gravity":"bottom","aspectRatio":"1:1","size":"sm","type":"image","url":"https://img.live/images/2019/02/21/c5f4e567380d0f1e31acb822d0b5cfd2819c8e3b_00.jpg"},{"type":"separator","color":"#003300"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/02/21/d1566d9832bd42f14ec4d2538f74ab76.jpg"},{"type":"separator","color":"#003300"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/02/10/1549778907829.jpg"},{"type":"separator","color":"#003300"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/02/10/1549778907829.jpg"},{"type":"separator","color":"#003300"}],"layout":"vertical","spacing":"none","flex":1},{"type":"separator","color":"#003300"},{"type":"box","contents":[{"type":"separator","color":"#003300"},{"color":"#003300","size":"md","wrap":True,"type":"text","text":" 🐧Khenzi🐧","weight":"bold"},{"type":"separator","color":"#003300"},{"color":"#003300","size":"md","wrap":True,"type":"text","text":"{}".format(contact.displayName),"weight":"bold"},{"type":"separator","color":"#003300"},{"color":"#003300","size":"xs","wrap":True,"type":"text","text":"Status Profile:","weight":"bold"},{"type":"text","text":"{}".format(contact.statusMessage),"size":"xxs","wrap":True,"color":"#003300"}],"layout":"vertical","flex":2}],"layout":"horizontal","spacing":"md"},"hero":{"aspectMode":"cover","margin":"xxl","aspectRatio":"1:1","size":"full","type":"image","url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus)}}})            
                elif text.lower() == "/runtime" or text.lower() == "/runtime":
                    timeNow = time.time() - Start
                    runtime = timeChange(timeNow)
                    run = "Time on \n"
                    run += runtime
                    helps = "{}".format(str(run))
                    data = {
                        "type": "text",
                        "text": "{}".format(str(run)),
                        "sentBy": {
                             "label": "{}".format(displayName),
                             "iconUrl": "https://obs.line-scdn.net/{}".format(pictureStatus),
                             "linkUrl": "line://nv/profilePopup/mid=uca43cd15fb994f5e04c0984b7c1693ef"
                        } 
                    }
                    sendTemplate(to, data)
                elif text.lower() == "!runtime" or text.lower() == "!runtime":
                    timeNow = time.time() - Start
                    runtime = timeChange(timeNow)
                    run = "⇨ Time on ⇦\n"
                    run += runtime
                    helps = "{}".format(str(run))
                    data = {
                        "type": "text",
                        "text": "{}".format(str(run)),
                        "sentBy": {
                             "label": "{}".format(displayName),
                             "iconUrl": "https://obs.line-scdn.net/{}".format(pictureStatus),
                             "linkUrl": "line://nv/profilePopup/mid=ubd86e8c77559b1493f0ad64b1dba2d6c"
                        }
                    }
                    sendTemplate(to, data)
                if text.lower() == "runtime2" or text.lower() == "runtime2":
                    timeNow = time.time() - Start
                    runtime = timeChange(timeNow)
                    run = "⇨ Time on ⇦\n"
                    run += runtime
                    data = {
                        "type": "flex",
                        "altText": "{}".format(run),
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#0033FF'
                                 },
                            },
                            "hero": {
                                            "type": "image",
                                            "url": "https://obs.line-scdn.net/{}".format(ghi.getContact(sender).pictureStatus),
                                            "size": "full",
                                            "aspectRatio": "1:1",
                                            "aspectMode": "fit",
                                        },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                              #  {
                                              #  "type": "image",
                                                #"url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                               # "size": "full"
                                             #  },
                                    {
                                        "type": "text",
                                        "text": "{}".format(run),
                                        "wrap": True,
                                        "color": "#003300",
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)
                elif text.lower() == "reset" or text.lower() == "reset":
                    gifnya = ["https://i.pinimg.com/originals/2e/d7/37/2ed737ba301b048afdb355fd9d1c2e86.gif"]
                    data = {
                        "type": "template",
                        "altText": "kecepatan",
                        "template": {
                            "type": "image_carousel",
                            "columns": [
                                {
                                     "imageUrl": "{}".format(random.choice(gifnya)),
                                     "size": "full",
                                     "action": {
                                         "type": "uri",
                                          "uri": "line.me/ti/p/0KGxZx8VYs"
                                     }
                                }
                            ]
                        }
                    }
                    sendTemplate(to, data)
                    restartBot()
                    time.sleep(1)
                    ga = "succeeded"
                    data = {
                        "type": "text",
                        "text": "{}".format(str(ga)),
                        "sentBy": {
                             "label": "🐧Khenzi🐧",
                             "iconUrl": "https://obs.line-scdn.net/{}".format(ghi.getContact(ghiMID).pictureStatus),
                             "linkUrl": "line.me/ti/p/0KGxZx8VYs"
                        }
                    }
                    sendTemplate(to, data)
                elif text.lower() == "sp" or text.lower() == "speed":                       
                    contact = ghi.getContact(sender)
                    start = time.time()
                    ghi.sendMessage(to, "Speed ​​test")
                    elapsed_time = time.time() - start
                    took = time.time() - start
                    a = " Speed ​​bots \nSpeed ​​ping ✔\n speed : %.3fms ✔️\nspeeds: %.10f ✔️" % (took,elapsed_time)
                    LINKFOTO = "https://os.line.naver.jp/os/p/" + sender
                    LINKVIDEO = "https://os.line.naver.jp/os/p/" + sender + "/vp"                            
                    data = {
                        "type": "flex",
                                "altText": "{}".format(a),
                                "contents": {
                                    "type": "bubble",
                                        'styles': {
                                            "header": {
                                                "backgroundColor": '#0033FF'
                                            },
                                            "footer": {
                                                "backgroundColor": '#0033FF'
                                                 },
                                              },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                                "size": "full",
                                                "aspectRatio": "1:1",
                                                "aspectMode": "fit",
                                            },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "margin": "lg",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "box",
                                                        "layout": "baseline",
                                                        "spacing": "sm",
                                                        "contents": [
                                                            {
                                                                "type": "text",
                                                                "text":  "{}".format(a),
                                                                "color": "#000000",
                                                                "wrap": True,
                                                                "size": "sm",
                                                                "flex": 1    
                                                            } 
                                                        ]
                                                    }
                                                ] 
                                            }
                                        ]
                                    },                                                                                                    
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "style": "link",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "🐧Khenzi🐧",
                                                    "uri": "line.me/ti/p/0KGxZx8VYs"
                                                }                                                   
                                            },
                                            {
                                                "type": "spacer",
                                                "size": "sm",
                                            }
                                        ],
                                        "flex": 0        
                                    }
                                }
                            }
                    sendTemplate(to, data)
                elif "call" in msg.text.lower():
                   if msg.toType == 2:
                      sep = msg.text.split(" ")
                      resp = msg.text.replace(sep[0] + " ","")
                      num = int(resp)
                      try:
                            duc1(to, "Sedang berlangsung") 
                      except:
                         pass
                      for var in range(num):
                            group = ghi.getGroup(msg.to)
                            members = [mem.mid for mem in group.members]
                            ghi.acquireGroupCallRoute(msg.to)
                            ghi.inviteIntoGroupCall(msg.to, contactIds=members)
                      duc1(to, "Invited to call")

                elif msg.text.startswith("call"):
                    dan = text.split(" ")
                    num = int(dan[1])
                    ret_ = "╭──[ Berhasil mengundang panggilan ]"
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            for var in range(0,num):
                                group = maxgie.getGroup(to)
                                members = [ls]
                                ghi.acquireGroupCallRoute(to)
                                ghi.inviteIntoGroupCall(to, contactIds=members)
                            ret_ += "\n├> @!"
                        ret_ += "\n╰──────────"
                        maxgie.sendPhu(to, ret_, lists)
                                        
                elif "Spam " in msg.text:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                               ghi.sendMessage(msg.to, teks)
                        else:
                           ghi.sendMessage(msg.to, "Out of Range!")
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            ghi.sendMessage(msg.to, tulisan)
                elif text.lower() == 'about' or text.lower() == "about":
                    try:
                        arr = []
                        owner = "u6a31b61828cb0744374e35c55243062a"
                        creator = ghi.getContact(owner)
                        contact = ghi.getContact(ghiMID)
                        grouplist = ghi.getGroupIdsJoined()
                        contactlist = ghi.getAllContactIds()
                        blockedlist = ghi.getBlockedContactIds()
                        IdsInvit = ghi.getGroupIdsInvited()
                        times = time.time() - Start
                        runtime = timeChange(times)
                        ret_ = "╭───「 About Your 」"
                        ret_ += "\n├ Name : {}".format(contact.displayName)
                        ret_ += "\n├ Group : {}".format(str(len(grouplist)))
                        ret_ += "\n├ Friend : {}".format(str(len(contactlist)))
                        ret_ += "\n├ Block : {}".format(str(len(blockedlist)))
                        ret_ += "\n├ Pending : {}".format(str(len(IdsInvit)))
                        ret_ += "\n├────────────"
                        ret_ += "\n├ Time on the bot :"
                        ret_ += "\n├ {}".format(str(runtime))
                        ret_ += "\n├────────────"
                        ret_ += "\n├ Creator : {}".format(str(creator.displayName))
                        ret_ += "\n╰───「 🐧Khenzi🐧 」"
                        feds = "{}".format(str(ret_))
                        data = {
                            "type": "text",
                            "text": "{}".format(str(ret_)),
                            "sentBy": {
                                 "label": "{}".format(ghi.getContact(ghiMID).displayName),
                                 "iconUrl": "https://obs.line-scdn.net/{}".format(ghi.getContact(ghiMID).pictureStatus),
                                 "linkUrl": "line://ti/p/~nonbysignal"
                            }
                        }
                        sendTemplate(to, data)
                        ghi.sendContact(msg.to, creator.mid)
                    except Exception as e:
                        ghi.sendMessage(msg.to, str(e))
                elif text.lower() == "fail":
                            gifnya = ['https://i.pinimg.com/originals/87/a8/9b/87a89b5aeaf35ba0c8879db5a136ccbd.gif']
                            data = {
                                "type": "template",
                                "altText": "Image carouserl",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(gifnya)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line.me/ti/p/0KGxZx8VYs"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == "love" or text.lower() == "Love":
                            gifnya = ['https://thumbs.gfycat.com/KlutzyUglyGelding-small.gif']
                            data = {
                                "type": "template",
                                "altText": "Image carouserl",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(gifnya)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line.me/ti/p/0KGxZx8VYs"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif cmd == "random":
                            gifnya = ['https://thumbs.gfycat.com/AngelicCloudyJaeger-size_restricted.gif','https://thumbs.gfycat.com/AgedZealousBlackfootedferret-size_restricted.gif','https://thumbs.gfycat.com/FondHastyChinesecrocodilelizard-size_restricted.gif','https://thumbs.gfycat.com/LividCrazyDipper-size_restricted.gif','https://thumbs.gfycat.com/LoathsomeDevotedGossamerwingedbutterfly-size_restricted.gif','https://thumbs.gfycat.com/SamePhysicalHarrierhawk-size_restricted.gif','https://thumbs.gfycat.com/ColorlessPinkLangur-size_restricted.gif','https://thumbs.gfycat.com/ThoseBitesizedBrahmanbull-size_restricted.gif','https://thumbs.gfycat.com/FakeSlowBengaltiger-size_restricted.gif','https://thumbs.gfycat.com/TanSpitefulChupacabra-size_restricted.gif']
                            data = {
                                "type": "template",
                                "altText": "Image carouserl",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(gifnya)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line.me/ti/p/0KGxZx8VYs"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                            
                elif msg.text.lower().startswith("Setpictpro"):
                            link = removeCmd("Set profile picture", text)
                            contact = ghi.getContact(sender)
                            ghi.sendMessage(to, "Type: Profile\n • Detail: Change video url\n • Status: Download...")
                            print("Sedang Mendownload Data ~")
                            pic = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            subprocess.getoutput('youtube-dl --format mp4 --output TeamAnuBot.mp4 {}'.format(link))
                            pict = ghi.downloadFileURL(pic)
                            vids = "TeamAnuBot.mp4"
                            changeVideoAndPictureProfile(pict, vids)
                            ghi.sendMessage(to, "Type: Profile\n • Detail: Change video url\n • Status: Succes")
                            os.remove("TeamAnuBot.mp4")
#=====================================================================

#=====================================================================
                elif msg.text.lower().startswith("mid "):
                   if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = ghi.getContact(ls)
                            mi_d = contact.mid
                            ghi.sendContact(msg.to, mi_d)
                            
                elif text.lower() == "Tes":
                    duc1(to, "█▒... 10.0%")
                    duc1(to, "███▒... 25.0%")
                    duc1(to, "█████▒... 50.0%")
                    duc1(to, "███████▒... 75.0%")
                    duc1(to, "███████████..100.0%")

                elif msg.text in ["count"]:
                    duc1(to,"「 🐧Khenzi🐧 」")
                    duc1(to,"??:::⭐ 1 ⭐:::💖")
                    duc1(to,"💚:::⭐ 5 ⭐:::💚")
                    duc1(to,"💖:::⭐ 10 ⭐:::💖")
                    duc1(to,"Do you count on each other" +datetime.today().strftime('%H:%M:%S')+ "™")
#=====================================================================
                elif msg.text.lower().startswith("broadcast: "):
                    sep = text.split(" ")
                    txt = text.replace(sep[0] + " ","")
                    friends = ghi.friends
                    for friend in friends:
                        ghi.sendMessage(friend, "「Pesan otomatis mengumumkan obrolan」\n{}".format(str(txt)))
                    duc1(to, "Kirim pesan ke teman {} Orang".format(str(len(friends))))
#=============================================================================           
                elif msg.text.lower().startswith("black "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        apalo["Talkblacklist"][ls] = True
                                        ghi.sendMessage(to, 'Add to TalkBan')
                                    except:
                                        pass
                elif msg.text.lower().startswith("clear "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        del apalo["Talkblacklist"][ls]
                                        ghi.sendMessage(to, 'Deleted from TalkBan')
                                    except:
                                        pass
                elif text.lower() == "Talkban":
                            if apalo["Talkblacklist"] == {}:
                              duc1(to, "Not found people who stuffed black")
                            else:
                              ma = ""
                              a = 0
                              for m_id in apalo["Talkblacklist"]:
                                  a = a + 1
                                  end = '\n'
                                  ma += str(a) + ". " +ghi.getContact(m_id).displayName + "\n"
                              duc1(to,"Talkbanlist :\n\n"+ma+"\nNumber %s Tahanan" %(str(len(apalo["Talkblacklist"]))))
#=====================================================================                
                if text.lower() == "autoblock:on":
                  if msg._from in admin:
                      settings["autoblock"] = True
                      sa = "Open"
                  else:
                      sa = "Allready On"
                  duc1(to, sa)
                if text.lower() == "autoblock:off":
                  if msg._from in admin:
                      settings["autoblock"] = False
                      duc1(to,"Close")
                  else:
                      duc1(to,"Allready Off")
                if text.lower() == "tags:on":
                    tagadd["tags"] = True
                    sa = "Allready On"
                    duc1(to,str(sa))
                if text.lower() == "tags:off":
                    tagadd["tags"] = False
                    sa = "Allready Off"
                    duc1(to,str(sa))
                if text.lower() == "autocancel:on":
                    settings["autoCancel"]["on"] = True
                    duc1(to, "Allready On")
                if text.lower() == "autocancel:off":
                    settings["autoCancel"]["on"] = False
                    duc1(to, "Allready Off")
                if text.lower() == "autojoin:on":
                  if msg._from in ghiMID:
                      kcn["autojoin"] = True
                      duc1(to, "Allready On")
                  else:
                      ghi.sendMessage(msg.to,"「 Status Autoleave 」\nActivate to eat the roomAlready approved")
                if text.lower() == "autojoin:off":
                  if msg._from in maxgieMID:
                      kcn["autojoin"] = False
                      duc1(to, "🌟Allready Off🌟")
                  else:
                      ghi.sendMessage(msg.to,"「 Status Autoleave 」\nEnable automatic eating room") 
                if text.lower() == "autoadd:on":
                    settings["autoAdd"] = True
                    duc1(to, "Allready On")
                if text.lower() == "autoadd:off":
                    settings["autoAdd"] = False
                    duc1(to, "Allready Off")
                if text.lower() == "autolike:on":
                   sets["l"] = False
                   duc1(to, "Allready On")
                if text.lower() == "autolike:off":
                   sets["l"] = True
                   duc1(to, "Allready Off")
                if text.lower() == "tagss:on":
                    tagadd["tagss"] = True
                    duc1(to, "Allready On")
                if text.lower() == "tagss:off":
                    tagadd["tagss"] = False
                    duc1(to, "Allready Off")
                if text.lower() == "comment:on":
                    settings["com"] = True
                    duc1(to, "Allready On")
                if text.lower() == "comment:off":
                    settings["com"] = False
                    duc1(to, "Allready Off")
                if text.lower() == "welcome:on":
                    settings["Welcome"] = True
                    duc1(to, "Allready On")
                if text.lower() == "welcome:off":
                    settings["Welcome"] = False
                    duc1(to, "Allready Off")
                if text.lower() == "welcome2:on":
                    settings["Wc"] = True
                    duc1(to, "Allready On")
                if text.lower() == "welcome2:off":
                    settings["Wc"] = False
                    duc1(to, "Allready Off")
                if text.lower() == "autoleave:0n":
                    settings["Leave"] = True
                    duc1(to, "Allready On")
                if text.lower() == "autoleave:off":
                    settings["Leave"] = False
                    duc1(to, "Allready Off")
                if text.lower() == "unsend:on":
                    settings["unsendMessage"] = True
                    duc1(to, "Allready On")
                if text.lower() == "unsend:off":
                    settings["unsendMessage"] = False
                    duc1(to, "Allready Off🌟")
                if text.lower() == "stkbig:on":
                    settings["Sticker"] = True
                    duc1(to, "Allready On")
                if text.lower() == "stkbig:off":
                    settings["Sticker"] = False
                    duc1(to, "Allready Off")
                if text.lower() == "sticker1:on":
                    sets["Sticker"] = True
                    duc1(to, "Allready On")
                if text.lower() == "sticker1:off":
                    sets["Sticker"] = False
                    duc1(to, "Allready Off")
                if text.lower() == "tagsticker:on":
                    sets["tagsticker"] = True
                    duc1(to, "Allready On")
                if text.lower() == "tagsticker:off":
                    sets["tagsticker"] = False
                    duc1(to, "Allready Off")
                if text.lower() == "lv:on":
                    settings["lv"] = True
                    duc1(to, "Allready Off")
                if text.lower() == "lv:ooff":
                    settings["lv"] = False
                    duc1(to, "Allready Off")
                if text.lower() == "wcsti2:on":
                    settings["wcsti2"] = True
                    duc1(to, "Allready On")
                if text.lower() == "wcsti2:off":
                    settings["wcsti2"] = False
                    duc1(to, "Allredy Off")
                if text.lower() == "jointicket:on":
                    sets["autoJoinTicket"] = True
                    duc1(to, "Open the link")
                if text.lower() == "jointicket:off":
                    sets["autoJoinTicket"] = False
                    duc1(to, "Close the link")

                elif text.lower() == 'speed':start = time.time();ghi.sendMessage("ubd86e8c77559b1493f0ad64b1dba2d6c", "🐧Khenzi🐧");elapsed_time = time.time() - start;duc1(to, "Speed : %s second"%str(round(elapsed_time,4)))
                
                elif msg.text.lower().startswith("announce "):
                            txt = removeCmd("Announce", text)
                            groups = ghi.getGroupIdsJoined()
                            url = 'https://nekos.life/api/v2/img/ngif'
                            text1 = requests.get(url).text
                            image = json.loads(text1)['url']
                            for group in groups:
                                sa = " Announce \n\n{}".format(str(txt))
                                data = {
"type":"flex",
"altText":"Give free chel",
"contents":{
"type": "carousel",
"contents": [
{
"type": "bubble",
"styles": {
"header": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#0033FF"},
"body": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#0033FF"},
"footer": {"backgroundColor": "#0033FF", "separator": True, "separatorColor": "#0033FF"}
},
"header": {
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": "Pengumuman grup",
"align": "center",
"size": "lg",
"weight": "bold",
"color": "#00F5FF",
"wrap": True
}
]
},
"type": "bubble",
"body": {
"contents": [
{
"contents": [
{
"url": "https://obs.line-scdn.net/{}".format(ghi.getContact(ghiMID).pictureStatus),
"type": "image"
},
{
"type": "separator",
"color": "#000000"
},
{
"url": "https://obs.line-scdn.net/{}".format(ghi.getContact(ghiMID).pictureStatus),
"type": "image"
}
],
"type": "box",
"spacing": "md",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#000000"
},
{
"contents": [
{
"text": sa,
"size": "md",
"align": "center",
"color": "#00F5FF",
"wrap": True,
"weight": "bold",
"type": "text"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
{
"type": "separator",
"color": "#000000"
},
{
"contents": [
{
"contents": [
{
"type": "text",
"text": sa,
"align": "center",
"size": "xs",
"weight": "bold",
"color": "#000000",
"wrap": True
}
],
"type": "box",
"layout": "baseline"
},
{
"contents": [
{
"url": "https://obs.line-scdn.net/{}".format(ghi.getContact(ghiMID).pictureStatus),
"type": "icon",
"size": "md"
},
{
"text": " ➡ Creator By : \n ➡ 🐧Khenzi🐧",
"size": "xs",
"margin": "none",
"color": "#00F5FF",
"wrap": True,
"weight": "regular",
"type": "text"
}
],
"type": "box",
"layout": "baseline"
}
],
"type": "box",
"layout": "vertical"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
"footer": {
"type": "box",
"layout": "horizontal",
"spacing": "sm",
"contents": [
{
"type": "button",
"flex": 2,
"style": "primary",
"color": "#00F5FF",
"height": "sm",
"action": {
"type": "uri",
"label": "🐧Khenzi🐧",
"uri": "https://line.me/ti/p/0KGxZx8VYs",
}
},
{
"flex": 3,
"type": "button",
"style": "primary",
"color": "#00F5FF",
"margin": "sm",
"height": "sm",
"action": {
"type": "uri",
"label": "🐧Khenzi🐧",
"uri": "https://line.me/ti/p/0KGxZx8VYs",
}
}
]
}
}
]
}
}
                                sendTemplate(group, data)
                                time.sleep(1)
                            ghi.sendMessage(to, "Kirim pengumuman nomor  {} Group".format(str(len(groups))))
                elif msg.text.lower().startswith("promo"):
                            contact = ghi.getContact(sender) 
                            groups = ghi.getGroupIdsJoined()
                            for group in groups:
                                dataProfile = [ 
                                      {
                                      "type": "bubble",
                                      "styles": {
                                          "header": {
                                              "backgroundColor": '#000000'
                                              },
                                          "body": {
                                              "backgroundColor": '#000000'
                                              },
                                          "footer": {
                                              "backgroundColor": '#0033FF'
                                               },
                                           },
                                            "header": {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "🐧Khenzi🐧",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "color": "#FF0033"
                                                    }
                                                ]
                                            },
                                            "hero": {
                                              "type": "image",
                                              "url": "https://img.live/images/2019/03/28/1553773108509.jpg",
                                              "size": "full",
                                              "aspectRatio": "20:13",
                                              "aspectMode": "cover",
                                              "action": {
                                                "type": "uri",
                                                "uri": "line.me/ti/p/0KGxZx8VYs"
                                              }
                                            },
                                        "body": {
                                          "type": "box",
                                          "layout": "horizontal",
                                          "spacing": "md",
                                          "contents": [
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 1,
                                              "contents": [
                                                {
                                                  "type": "image",
                                                  "url": "https://img.live/images/2019/03/25/F6FBB34A-3B96-41A7-944D-E17454BC6F25.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "size": "sm",
                                                  "gravity": "bottom"
                                                },
                                                {
                                                  "type": "image",
                                                  "url": "https://img.live/images/2019/03/25/1553451636487.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "margin": "md",
                                                  "size": "sm"
                                                }
                                              ]
                                            },
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 2,
                                              "contents": [
                                                {
                                                  "type": "text",
                                                  "text": "self bot python3",
                                                  "color": "#FF0033",
                                                  "gravity": "top",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "Price 100 baht / month",
                                                  "color": "#FF0033",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "Bot room",
                                                  "color": "#FF0033",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ราคา 200 บาท",
                                                  "color": "#FF0033",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "Care throughout the use",
                                                  "color": "#FF0033",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                              ]
                                            }
                                          ]
                                        },
                                        "footer": {
                                          "contents": [
                                            {
                                              "contents": [
                                                {
                                                  "contents": [
                                                    {
                                                      "text": "For more information",
                                                      "size": "xl",
                                                      "action": {
                                                        "uri": "line.me/ti/p/0KGxZx8VYs",
                                                        "type": "uri",
                                                        "label": "Add Maker"
                                                      },
                                                      "margin": "xl",
                                                      "align": "center",
                                                      "color": "#000000",
                                                      "weight": "bold",
                                                      "type": "text"
                                                    }
                                                  ],
                                                  "type": "box",
                                                  "layout": "baseline"
                                                }
                                              ],
                                              "type": "box",
                                              "layout": "horizontal"
                                            }
                                          ],
                                          "type": "box",
                                          "layout": "vertical"
                                       }
                                   },
                                      {
                                      "type": "bubble",
                                      "styles": {
                                          "header": {
                                              "backgroundColor": '#000000'
                                              },
                                          "body": {
                                              "backgroundColor": '#000000'
                                              },
                                          "footer": {
                                              "backgroundColor": '#FF0033'
                                               },
                                           },
                                            "header": {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "🐧Khenzi🐧",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "color": "#FF0033"
                                                    }
                                                ]
                                            },
                                            "hero": {
                                              "type": "image",
                                              "url": "https://img.live/images/2019/03/28/1553773108509.jpg",
                                              "size": "full",
                                              "aspectRatio": "20:13",
                                              "aspectMode": "cover",
                                              "action": {
                                                "type": "uri",
                                                "uri": "line.me/ti/p/0KGxZx8VYs"
                                              }
                                            },
                                        "body": {
                                          "type": "box",
                                          "layout": "horizontal",
                                          "spacing": "md",
                                          "contents": [
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 1,
                                              "contents": [
                                                {
                                                  "type": "image",
                                                  "url": "https://img.live/images/2019/03/25/D88BDCD7-3CFC-4BD9-BE86-210B7A22CD3C.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "size": "sm",
                                                  "gravity": "bottom"
                                                },
                                                {
                                                  "type": "image",
                                                  "url": "https://img.live/images/2019/03/25/1553451634501.jpg",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "margin": "md",
                                                  "size": "sm"
                                                }
                                              ]
                                            },
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 2,
                                              "contents": [
                                                {
                                                  "type": "text",
                                                  "text": "Cheap ticker",
                                                  "color": "#FF0033",
                                                  "gravity": "top",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "Real Mao Coin",
                                                  "color": "#FF0033",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "Tick ​​every day",
                                                  "color": "#FF0033",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "Cheap price can be inquired",
                                                  "color": "#FF0033",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "Kind seller",
                                                  "color": "#FF0033",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                              ]
                                            }
                                          ]
                                        },
                                        "footer": {
                                          "contents": [
                                            {
                                              "contents": [
                                                {
                                                  "contents": [
                                                    {
                                                      "text": "For more information",
                                                      "size": "xl",
                                                      "action": {
                                                        "uri": "line.me/ti/p/0KGxZx8VYs",
                                                        "type": "uri",
                                                        "label": "Add Maker"
                                                      },
                                                      "margin": "xl",
                                                      "align": "center",
                                                      "color": "#000000",
                                                      "weight": "bold",
                                                      "type": "text"
                                                    }
                                                  ],
                                                  "type": "box",
                                                  "layout": "baseline"
                                                }
                                              ],
                                              "type": "box",
                                              "layout": "horizontal"
                                            }
                                          ],
                                          "type": "box",
                                          "layout": "vertical"
                                        }
                                   },
                                      {
                                      "type": "bubble",
                                      "styles": {
                                          "header": {
                                              "backgroundColor": '#000000'
                                              },
                                          "body": {
                                              "backgroundColor": '#000000'
                                              },
                                          "footer": {
                                              "backgroundColor": '#FF0033'
                                               },
                                           },
                                            "header": {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "🐧Khenzi🐧",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "color": "#FF0033"
                                                    }
                                                ]
                                            },
                                            "hero": {
                                              "type": "image",
                                              "url": "https://img.live/images/2019/03/28/1553773108509.jpg",
                                              "size": "full",
                                              "aspectRatio": "20:13",
                                              "aspectMode": "cover",
                                              "action": {
                                                "type": "uri",
                                                "uri": "line.me/ti/p/0KGxZx8VYs"
                                              }
                                            },
                                        "body": {
                                          "type": "box",
                                          "layout": "horizontal",
                                          "spacing": "md",
                                          "contents": [
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 1,
                                              "contents": [
                                                {
                                                  "type": "image",
                                                  "url": "https://img.live/images/2019/03/25/2832_20180721151831.png",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "size": "sm",
                                                  "gravity": "bottom"
                                                },
                                                {
                                                  "type": "image",
                                                  "url": "https://i.dlpng.com/static/png/75778_thumb.png",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "margin": "md",
                                                  "size": "sm"
                                                }
                                              ]
                                            },
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 2,
                                              "contents": [
                                                {
                                                  "type": "text",
                                                  "text": "Sell ​​skip / fec / kick / plain",
                                                  "color": "#FF0033",
                                                  "gravity": "top",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "Dotlock-in light",
                                                  "color": "#FF0033",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "Rent rental server",
                                                  "color": "#FF0033",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "Casual price",
                                                  "color": "#FF0033",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "Care throughout the use",
                                                  "color": "#FF0033",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                              ]
                                            }
                                          ]
                                        },
                                        "footer": {
                                          "contents": [
                                            {
                                              "contents": [
                                                {
                                                  "contents": [
                                                    {
                                                      "text": "For more information",
                                                      "size": "xl",
                                                      "action": {
                                                        "uri": "line.me/ti/p/0KGxZx8VYs",
                                                        "type": "uri",
                                                        "label": "Add Maker"
                                                      },
                                                      "margin": "xl",
                                                      "align": "center",
                                                      "color": "#000000",
                                                      "weight": "bold",
                                                      "type": "text"
                                                    }
                                                  ],
                                                  "type": "box",
                                                  "layout": "baseline"
                                                }
                                              ],
                                              "type": "box",
                                              "layout": "horizontal"
                                            }
                                          ],
                                          "type": "box",
                                          "layout": "vertical"
                                        }
                                   },
                                ]
                                data = {
                                    "type": "flex",
                                    "altText": "Have products for sale",
                                    "contents": {
                                        "type": "carousel",
                                        "contents": dataProfile
                                    }
                                }
                                sendTemplate(group, data)
                                time.sleep(1)
                            ghi.sendMessage(to, "Kirim pengumuman nomor  {} Grup".format(str(len(groups))))
#==============================================================================#
                elif text.lower() == "tag":
                        group = ghi.getGroup(to);nama = [contact.mid for contact in group.members];nama.remove(ghi.getProfile().mid)
                        ghi.datamention(to,'all',nama)
                elif text.lower() == "/tag" or text.lower() == "tagall":
                    if msg._from in ghiMID:
                        group = ghi.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members]
                        nm1, nm2, nm3, nm4, nm5, nm6, nm7, nm8, nm9, jml = [], [], [], [], [], [], [], [], [], len(nama)
                        if jml <= 20:
                          mentionMembers(msg.to, nama)
                        if jml > 20 and jml < 40:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, len(nama)):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                        if jml > 40 and jml < 60:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, len(nama)):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                        if jml > 60 and jml < 80:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, len(nama)):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                        if jml > 80 and jml < 100:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for m in range (80, len(nama)):
                              nm5 += [nama[m]]
                          mentionMembers(msg.to, nm5)
                        if jml > 100 and jml < 120:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [nama[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, len(nama)):
                              nm6 += [nama[o]]
                          mentionMembers(msg.to, nm6)
                        if jml > 120 and jml < 140:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [nama[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, 119):
                              nm6 += [nama[o]]
                          mentionMembers(msg.to, nm6)
                          for v in range (120, len(nama)):
                              nm7 += [nama[v]]
                          mentionMembers(msg.to, nm7)
                        if jml > 140 and jml < 160:
                          for i in range (0, 19):
                               nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [nama[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, 119):
                              nm6 += [nama[o]]
                          mentionMembers(msg.to, nm6)
                          for q in range (120, 139):
                              nm7 += [nama[q]]
                          mentionMembers(msg.to, nm7)
                          for r in range (140, len(nama)):
                              nm8 += [nama[r]]
                          mentionMembers(msg.to, nm8)
                        if jml > 160 and jml < 180:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [nama[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, 119):
                              nm6 += [nama[o]]
                          mentionMembers(msg.to, nm6)
                          for q in range (120, 139):
                              nm7 += [nama[q]]
                          mentionMembers(msg.to, nm7)
                          for z in range (140, 159):
                              nm8 += [nama[z]]
                          mentionMembers(msg.to, nm8)
                          for f in range (160, len(nama)):
                              nm9 += [nama[f]]
                          mentionMembers(msg.to, nm9)
#==============================================================================#
                elif msg.text.lower().startswith("Write "):
                    sep = msg.text.split(" ")
                    textnya = msg.text.replace(sep[0] + " ","")
                    urlnya ="http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya +"&chts=ff3333,70&chf=bg,s,ff3333"
                    ghi.sendImageWithURL(msg.to, urlnya)
                elif msg.text.lower().startswith("Write 1 "):
                    sep = text.split(" ")
                    textnya = text.replace(sep[0] + " ", "")
                    text = "{}".format(textnya)
                    contact = ghi.getContact(ghiMID)
                    data = {
                        "type": "flex",
                        "altText": "Come to read",
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#0033FF'
                                    },
                                 },
                            "hero": {
                                "type": "image",
                                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                "size": "full",
                                "aspectRatio":"1:1",
                                "aspectMode":"cover"
                            },
                            "body": {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "{}".format(text),
                                        "color":"#000000",
                                        "wrap": True,
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "xl"
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)
                elif msg.text.lower().startswith("pull "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                       ghi.findAndAddContactsByMid(ls)
                                       ghi.inviteIntoGroup(to, [ls])
                                    except:
                                       duc1(to, "Limited !")
                elif msg.text.lower().startswith("Mantra"):
                  if msg.toType == 2:
                    data = text.replace("Mantra ","")
                    yud = data.split(' ')
                    yud = yud[0].replace(' ','_')
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            ghi.sendMessage(to, yud,contentMetadata={"MSG_SENDER_NAME": str(ghi.getContact(ls).displayName),"MSG_SENDER_ICON":"http://dl.profile.line-cdn.net/%s" % ghi.getContact(ls).pictureStatus})
                elif text.startswith("ยูทูป "):
                   a = ghi.adityarequestweb("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q="+ghi.adityasplittext(text,'s')+"&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8")
                   if a["items"] != []:
                       no = 0
                       ret_ = []
                       for music in a["items"]:
                           no += 1
                           ret_.append({"type": "bubble","styles": {"header": {"backgroundColor": "#0033FF", "separator": True, "separatorColor": "#FFFFFF"},"body": {"backgroundColor": "#0033FF", "separator": True, "separatorColor": "#FFFFFF"},"footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FFFFFF"},},"header": {"type": "box","layout": "horizontal","contents": [{"type": "text","text": "Youtube","weight": "bold","color": "#FFFFFF","size": "sm"}]},"hero": {"type": "image","url": 'https://i.ytimg.com/vi/{}/maxresdefault.jpg'.format(music['id']['videoId']),"size": "full","aspectRatio": "20:13","aspectMode": "fit","action": {"type": "uri","uri": 'https://www.youtube.com/watch?v=' +music['id']['videoId']}},"body": {"type": "box","layout": "vertical","contents": [{"type": "box","layout": "vertical","margin": "lg","spacing": "sm","contents": [{"type": "box","layout": "baseline","spacing": "sm","contents": [{"type": "text","text": "information","color": "#FFFFFF","size": "sm","flex": 1},{"type": "text","text": "{}".format(music['snippet']['title']),"color": "#FFFFFF","wrap": True,"size": "sm","flex": 5}]}]}]},"footer": {"type": "box","layout": "horizontal","spacing": "sm","contents": [{"type": "button","flex": 2,"style": "primary","color": "#EE1289","height": "sm","action": {"type": "uri","label": "🌟MP4🌟","uri": "{}video%20https://www.youtube.com/watch?v={}".format(wait['ttt'],music['id']['videoId'])}},{"type": "button","flex": 2,"style": "primary","color": "#EE1289","height": "sm","action": {"type": "uri","label": "🌟MP3🌟","uri": "{}the sound%20https://www.youtube.com/watch?v={}".format(wait['ttt'],music['id']['videoId'])}},],}})
                       k = len(ret_)//10
                       for aa in range(k+1):
                           data = {"messages": [{"type": "flex","altText": "Youtube","contents": {"type": "carousel","contents": ret_[aa*10 : (aa+1)*10]}}]}
                           ghi.sendMessage(to,data)
                   else:
                      ghi.sendMessage(to,"Type: Search Youtube Video\nStatus: "+str(self.adityasplittext(msg.text,'s'))+" not found")
                
                elif msg.text.lower().startswith("image "):
                                query = removeCmd("image", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/{}".format(str(search)))
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    ret_ = []
                                    for food in data:
                                        if 'http://' in food["url"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(food["url"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Send Image",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(str(food["url"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "sendImage",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
                elif msg.text.lower().startswith("pesto "):
                                query = removeCmd("Pesto", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("http://api.farzain.com/playstore.php?id={}&apikey=KJaOT94NCD1bP1veQoJ7uXc9M".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if data != []:
                                    ret_ = []
                                    for music in data:
                                        if 'http://' in music["url"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(music["icon"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Download",
                                                        "uri": "{}".format(str(music["url"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "Searching App",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
                elif msg.text.lower().startswith("Gambar "):
                                query = removeCmd("Gambar", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("https://api.boteater.co/googleimg?search={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if data["result"] != []:
                                    ret_ = []
                                    for fn in data["result"]:
                                        if 'http://' in fn["img"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(fn["img"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Send Image",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(str(fn["img"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "Google_Image",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
                                        
                 #=====================================================================

                elif msg.text.lower().startswith("Invite"):
                                if msg._from in ghiMID:
                                    if msg.toType == 2:
                                        group = ghi.getGroup(receiver)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        k = len(gMembMids)//20
                                        ghi.sendMessage(msg.to,"[ Hold down the invitation number {} person] \nPlease wait...".format(str(len(gMembMids))))
                                        num=1
                                        for i in range(k+1):
                                            for j in gMembMids[i*20 : (i+1)*20]:
                                                time.sleep(random.uniform(0.5,0.4))
                                                ghi.cancelGroupInvitation(msg.to,[j])
                                                print ("[Command] "+str(num)+" => "+str(len(gMembMids))+" cancel members")
                                                num = num+1
                                            ghi.sendMessage(receiver,"wait a minute🕛Single lift 20 person\n 『.🐧Khenzi🐧』 ")
                                            time.sleep(random.uniform(15,10))
                                        ghi.sendMessage(receiver,"[ Hold down the invitation number {} person completed👏]".format(str(len(gMembMids))))
                                        time.sleep(random.uniform(0.95,1))
                                        ghi.sendMessage(receiver, None, contentMetadata={"STKID": "52002735","STKPKGID": "11537","STKVER": "1" }, contentType=7)
                                        gname = line.getGroup(receiver).name
                                        ghi.sendMessage(Notify,"[ Hold the invitation >> "+gname+"  <<] \n number {} person completed👏\n『🐧Khenzi🐧』".format(str(len(gMembMids))))
                                        time.sleep(random.uniform(0.95,1))
                                        ghi.leaveGroup(receiver)
                                								
                                    ghi.sendMessage(receiver,"[There is no outstanding invitation😁]")
                                    ghi.sendMessage(receiver, None, contentMetadata={"STKID": "52114123","STKPKGID": "11539","STKVER": "1" }, contentType=7)
                                    ghi.leaveGroup(receiver)
                #=====================================================================              
                elif msg.text.lower().startswith("cancaled "):
                   args = msg.text.lower().replace("canceled ","")
                   mes = 0
                   try:
                       mes = int(args[1])
                   except:
                       mes = 100
                       M = ghi.getRecentMessagesV2(to, 100)
                       MId = []
                       for ind,i in enumerate(M):
                           if ind == 0:
                               pass
                           else:
                               if i._from == ghi.profile.mid:
                                   MId.append(i.id)
                                   if len(MId) == mes:
                                       break
                       def unsMes(id):
                           ghi.unsendMessage(id)
                       for i in MId:
                           thread1 = threading.Thread(target=unsMes, args=(i,))
                           thread1.start()
                           thread1.join()
                       duc1(to, ' 「 Canceling」\nCancel all {} message'.format(len(MId)))
#=====================================================================                                       
                
                
                elif msg.text.lower().startswith("addfriend "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = ghi.getContact(ls)
                                    ghi.findAndAddContactsByMid(ls)
                                ghi.generateReplyMessage(msg.id)
                                duc1(id, to, "Success add " + str(contact.displayName) + " to Friendlist")
                elif msg.text.lower().startswith("dellfriend "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = ghi.getContact(ls)
                                    n = len(ghi.getAllContactIds())
                                    try:
                                        ghi.deleteContact(ls)
                                    except:pass
                                    t = len(ghi.getAllContactIds())
                                    ghi.generateReplyMessage(msg.id)
                                    duc1(id, to, "Type: Friendlist\n • Detail: Delete friend\n • Status: Succes..\n • Before: %s Friendlist\n • After: %s Friendlist"%(n,t))
                elif msg.text.lower().startswith("Block "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = ghi.getContact(ls)
                                    ghi.blockContact(ls)
                                ghi.generateReplyMessage(msg.id)
                                duc1(id, to, "Success add " + str(contact.displayName) + " to Blocklist")
                elif msg.text.lower().startswith("idline "):
                            a = removeCmd("idline", text)
                            b = ghi.findContactsByUserid(a)
                            line = b.mid
                            duc1(to, "line://ti/p/~" + a)
                            ghi.sendContact(to, line)                                                                                           
                            ghi.sendMessage(to,str(hasil))
                elif msg.text.lower().startswith("stag "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = ghi.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                contact = ghi.getContact(receiver)
                                RhyN_(to, contact.mid)
                elif "!reinvite" in msg.text.lower():
                    spl = re.split("!reinvite",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        spl[1] = spl[1].strip()
                        ag = ghi.getGroupIdsInvited()
                        txt = "Canceling, holding, inviting, number "+str(len(ag))+" Group"
                        if spl[1] != "":
                            txt = txt + " With text \""+spl[1]+"\""
                        txt = txt + "\nplease wait.."
                        data = {"type": "text","text": "{}".format(str(txt)),"sentBy": {"label": "{}".format(ghi.getContact(ghiMID).displayName),"iconUrl": "https://obs.line-scdn.net/{}".format(ghi.getContact(ghiMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ubd86e8c77559b1493f0ad64b1dba2d6c"}}
                        sendTemplate(to, data)
                        procLock = len(ag)
                        for gr in ag:
                            try:
                                ghi.acceptGroupInvitation(gr)
                                if spl[1] != "":
                                    ghi.sendMessage(gr,spl[1])
                                ghi.leaveGroup(gr)
                            except:
                                pass
                        sis = "succeeded"
                        data = {"type": "text","text": "{}".format(str(sis)),"sentBy": {"label": "{}".format(ghi.getContact(ghiMID).displayName),"iconUrl": "https://obs.line-scdn.net/{}".format(ghi.getContact(ghiMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ubd86e8c77559b1493f0ad64b1dba2d6c"}}
                        sendTemplate(to, data)
            
#=====================================================================
#==============================================================================#
                elif text.lower() == 'buatgroup' or text.lower() == "Buatgroup":
                    group = ghi.getGroup(to)
                    cg = group.creator
                    c = cg.mid
                    name = cg.displayName
                    pp = cg.pictureStatus
                 #   profile = "https://profile.line-scdn.net/" + str(pp)
                    data = {
                        "type": "flex",
                        "altText": "Grup iklan",
                        "contents": {
                            "type": "bubble",
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type":"text",
                                        "text": "🐧Khenzi🐧",
                                        "size":"md",
                                       # "weight":"bold",
                                        "color":"#FF3333",
                                        "align":"center"
                                    },
                                    {
                                        "type": "text",
                                        "text": " "
                                    },
                                    {
                                        "type": "image",
                                        "url": "https://profile.line-scdn.net/" + str(pp),
                                        "size": "xl"
                                    },
                                    {
                                        "type":"text",
                                        "text":" "
                                    },
                                    {
                                       "type":"text",
                                       "text": name,
                                       "color":"#FF3333",
                                       "align":"center",
                                       "size":"xl",
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)
                    ghi.sendContact(to, c)
                elif text.lower() == 'gid':
                    gid = ghi.getGroup(to)
                    duc1(to, "{ Group ID }\n" + gid.id)
                    ghi.sendMessage(to, ghi.getGroup(to).name, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+ghi.getGroup(to).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~', 'type': 'mt', 'subText': "🐧Khenzi🐧", 'a-installUrl': 'https://line.me/ti/p/~', 'a-installUrl': ' https://line.me/ti/p/~', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~', 'i-linkUri': 'https://line.me/ti/p/~', 'id': 'mt000000000a6b79f9', 'text': '🐧Khenzi🐧', 'linkUri': 'https://line.me/ti/p/~'}, contentType=19)
                elif text.lower() == 'gpict':
                    group = ghi.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ghi.sendImageWithURL(to, path)
                elif text.lower() == 'gname':
                    gid = ghi.getGroup(to)
                    duc1(to, "Group name -> \n" + gid.name) 
                elif text.lower() == 'glink':
                    if msg.toType == 2:
                        group = ghi.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = ghi.reissueGroupTicket(to)
                            ghi.sendMessage(to, "Group link : "+group.name+"\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                elif text.lower() == '0url':
                    if msg.toType == 2:
                        group = ghi.getGroup(to)
                        if group.preventedJoinByTicket == False:
                           duc1(to, "Open link successfully")
                        else:
                            group.preventedJoinByTicket = False
                            ghi.updateGroup(group)
                            ghi.sendMessage(to, "Open the link")
                elif text.lower() == 'curl':
                    if msg.toType == 2:
                        group = ghi.getGroup(to)
                        if group.preventedJoinByTicket == True:
                           duc1(to, "Close link")
                        else:
                            group.preventedJoinByTicket = True
                            ghi.updateGroup(group)
                            ghi.sendMessage(to, "Close link")
                elif text.lower() == 'ginfo':
                    group = ghi.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "The creator of this group deleted the"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "close"
                        gTicket = "ไม่สมารถแสดงลิ้งได้"
                    else:
                        gQr = "0pen"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(ghi.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ Information of this group ]"
                    ret_ += "\n╠ Group name : {}".format(str(group.name))
                    ret_ += "\n╠ Group id : {}".format(group.id)
                    ret_ += "\n╠ Creator group : {}".format(str(gCreator))
                    ret_ += "\n╠ Total members : {}".format(str(len(group.members)))
                    ret_ += "\n╠ Pending : {}".format(gPending)
                    ret_ += "\n╠ Group link : {}".format(gQr)
                    ret_ += "\n╠ Group ticket👉 : {}".format(gTicket)
                    ret_ += "\n╚══『🐧Khenzi🐧』"
                    data = {
                        "type": "flex",
                        "altText": "Group",
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#0033FF'
                                 },
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                            #        {
                            #            "type": "image",
                            #            "url": path, 
                            #            "size": "xl"
                            #        },
                                    {
                                        "type": "text",
                                        "text": ret_,
                                        "color": "#000000",
                                        "wrap": True,
                                        "size": "md",
                                    },
                                ]
                            },
                        }
                    }
                    sendTemplate(to, data)
                    ghi.sendImageWithURL(to, path)
                elif text.lower() == '!tag':
                    if msg.toType == 2:
                        group = ghi.getGroup(to)
                        ret_ = "List janda&duda\n"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n{}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n\nTotal {} person".format(str(len(group.members)))
                        data = {
                            "type": "flex",
                            "altText": "Daftar Janda&Duda",
                            "contents": {
                                "type": "bubble",
                                "styles": {
                                    "body": {
                                        "backgroundColor": '#0033FF'
                                    },
                                },
                                   "hero": {
                                            "type": "image",
                                            "url": "https://obs.line-scdn.net/{}".format(ghi.getContact(sender).pictureStatus),
                                            "size": "full",
                                            "aspectRatio": "1:1",
                                            "aspectMode": "fit",
                                        },
                                "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": ret_,
                                            "color": "#003300",
                                            "wrap": True,
                                            "size": "md"
                                        },
                                    ]
                                }
                            }
                        }
                        sendTemplate(to, data)
                elif text.lower() == 'glist':
                        groups = ghi.groups
                        ret_ = "List of all groups :\n"
                        no = 0 + 1
                        for gid in groups:
                            group = ghi.getGroup(gid)
                            ret_ += "\n{}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n\nTotal {} group".format(str(len(groups)))
                        data = {
                            "type": "flex",
                            "altText": "Group list",
                            "contents": {
                                "type": "bubble",
                                "styles": {
                                    "body": {
                                         "backgroundColor": '#0033FF'
                                    },
                                },
                                "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type":"text",
                                            "text": ret_,
                                            "color": "#003300",
                                            "wrap": True,
                                            "size": "md"
                                        },
                                    ]
                                }
                            }
                        }
                        sendTemplate(to, data)                        
                elif text.lower() == "Proimg":
                    sets["changePictureProfile"] = True
                    duc1(to, "Send pictures that will be updated")
                elif text.lower() == "gphoto":
                    if msg.toType == 2:
                        if to not in sets["changeGroupPicture"]:
                            sets["changeGroupPicture"].append(to)
                        duc1(to, "Send pictures that will be updated")
            
                elif text.lower() == 'friendlist':
                    contactlist = ghi.getAllContactIds()
                    kontak = ghi.getContacts(contactlist)
                    num=1
                    msgs="List of all friends"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\nList of all friends\n\nAre as follows : %i" % len(kontak)
                    ghi.sendMessage(msg.to, msgs)
                                
#====================================================================
                elif msg.text.lower()== "addstktag":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "tag"
                    duc1(to, "Send the tick to use")
                elif msg.text.lower() == "dellstktag":
                    sets["messageSticker"]["listSticker"]["tag"] = None
                    #maxgie.unsendMessage(msg_id)
                    duc1(to, "Remove the tick tag")
                elif msg.text.lower()== "addstkwc":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "wc"
                    #maxgie.unsendMessage(msg_id)
                    duc1(to, "Send the tick to use")
                elif msg.text.lower() == "dellstkwc":
                    sets["messageSticker"]["listSticker"]["wc"] = None
                   # maxgie.unsendMessage(msg_id)
                    duc1(to, "Remove the tick welcome")
                elif msg.text.lower()== "addstklv":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "lv"
                    #maxgie.unsendMessage(msg_id)
                    duc1(to, "Send the tick to use")
                elif msg.text.lower() == "dellstklv":
                    sets["messageSticker"]["listSticker"]["lv"] = None
                    #maxgie.unsendMessage(msg_id)
                    duc1(to, "Remove the tick lv")
                elif msg.text.lower()== "stkadd":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "add"
                    #maxgie.unsendMessage(msg_id)
                    duc1(to, "Send the tick to use")
                elif msg.text.lower() == "dellstkadd":
                    sets["messageSticker"]["listSticker"]["add"] = None
                    #maxgie.unsendMessage(msg_id)
                    duc1(to, "Remove the tick add")
                elif msg.text.lower() == "addstkjoin":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "join2"
                    #maxgie.unsendMessage(msg_id)
                    duc1(to, "Send the tick to use")
                elif msg.text.lower() == "dellstkjoin":
                    sets["messageSticker"]["listSticker"]["join2"] = None
                    #maxgie.unsendMessage(msg_id)
                    duc1(to, "Remove the tick join")
                    
#=====================================================================
            elif msg.contentType == 1:
                if sets["changePictureProfile"] == True:
                    path = ghi.downloadObjectMsg(msg_id)
                    sets["changePictureProfile"] = False
                    ghi.updateProfilePicture(path)
                    #maxgie.unsendMessage(msg_id)
                    duc1(to, "Make changes")
                    
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != ghi.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                elif msg.contentType == 7:
                    if sets["Sticker"] == True:
                        try:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "「 Check Sticker 」\n"
                            ret_ += "\nSTKID : {}".format(stk_id)
                            ret_ += "\nSTKPKGID : {}".format(pkg_id)
                            ret_ += "\nSTKVER : {}".format(stk_ver)
                            ret_ += "\nLINK : line://shop/detail/{}".format(pkg_id)
                            print(msg)
                            ghi.sendImageWithURL(to, "http://dl.stickershop.line.naver.jp/products/0/0/"+msg.contentMetadata["STKVER"]+"/"+msg.contentMetadata["STKPKGID"]+"/WindowsPhone/stickers/"+msg.contentMetadata["STKID"]+".png")
                            ghi.sendMessage(to, str(ret_))
                        except Exception as error:
                            ghi.sendMessage(to, str(error))
                if msg.text:
                    if msg.text.lower().lstrip().rstrip() in wbanlist:
                        if msg.text not in ghiMID:
                            try:
                                ghi.kickoutFromGroup(msg.to,[sender])
                                #maxgie.unsendMessage(msg_id)
                                duc1(to, "Tell me, don't pimp it")
                            except Exception as e:
                                print(e)
                    if "/ti/g/" in msg.text.lower():
                        if sets["autoJoinTicket"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = ghi.findGroupByTicket(ticket_id)
                                ghi.acceptGroupInvitationByTicket(group.id,ticket_id)
                                ghi.sendMessage(group.id,str(tagadd["m"]))
                                duc1(to, "Move into the link group% s successfully" % str(group.name))
                if msg.contentType == 7:
                    if sets["messageSticker"]["addStatus"] == True:
                        name = sets["messageSticker"]["addName"]
                        if name != None and name in sets["messageSticker"]["listSticker"]:
                            sets["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            ghi.sendMessage(to, "Success Sticker " + name + " Done...")
                        sets["messageSticker"]["addStatus"] = False
                        sets["messageSticker"]["addName"] = None
                    if sets["addSticker"]["status"] == True:
                        stickers[sets["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[sets["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[sets["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        ghi.sendMessage(to, "Success Added sticker {}".format(str(sets["addSticker"]["name"])))
                        sets["addSticker"]["status"] = False
                        sets["addSticker"]["name"] = ""
            elif msg.contentType == 7:
                if sets["Sticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ Finish ]"
                    ghi.sendMessage(to, str(ret_))
#=====================================================================
        if op.type == 22:
            if did["join"] == True:
                ghi.leaveRoom(op.param1)              
        if op.type == 24:
            if did["join"] == True:
                ghi.leaveRoom(op.param1)
#========================================================================
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != ghi.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if text.lower() == ".":
                    duc1(to, "🐧Khenzi🐧")
#========================================================================
            elif msg.contentType == 7: # Content type is sticker
                if settings['Sticker']:
                    if 'STKOPT' in msg.contentMetadata:
                        contact = ghi.getContact(sender)
                        A = contact.displayName
                        stk = msg.contentMetadata['STKID']
                        spk = msg.contentMetadata['STKPKGID']
                        data={'type':'template','altText': str(A)+' Send stickers','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                        sendTemplate(to, data)
                    else:
                        contact = ghi.getContact(sender)
                        A = contact.displayName
                        stk = msg.contentMetadata['STKID']
                        spk = msg.contentMetadata['STKPKGID']
                        data={'type':'template','altText': str(A)+' Send stickers','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                        sendTemplate(to, data)
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
            #    elif msg.contentType == 7:
                if msg.toType == 0 and sender != ghiMID: to = sender
                else: to = receiver
                if msg.contentType == 0 and sender not in ghiMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if tagadd["tags"] == True:
                             me = ghi.getContact(sender)
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                   if mention['M'] in ghiMID:
                                          cover = ghi.getProfileCoverURL(sender)
                                          pp = me.pictureStatus
                                          profile = "https://profile.line-scdn.net/" + str(pp)
                                          name = me.displayName
                                          status = "\nstatus\n" + me.statusMessage
                                          pk = str(tagadd["tag"])
                                          tz = pytz.timezone("Asia/Jakarta")
                                          timeNow = datetime.now(tz=tz)
                                          van2 = "Time:"+ datetime.strftime(timeNow,'%H:%M:%S')                                 	
                                          data = {
"type":"flex",
"altText": pk, 
"contents":{
"type": "carousel",
"contents": [
{
"type": "bubble",
"styles": {
"header": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#EE1289"},
"body": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"},
"footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#EE1289"}
},
"type": "bubble",
"body": {
"contents": [
{
"contents": [
{
"url": profile,
"type": "image"
},
{
"type": "separator",
"color": "#33FF33"
},
{
"url": profile,
"type": "image"
}
],
"type": "box",
"spacing": "md",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#33FF33"
},
{
"contents": [
{
"text": name,
"size": "sm",
"align": "center",
"color": "#33FF33",
"wrap": True,
"weight": "bold",
"type": "text"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
{
"contents": [
{
"contents": [
{
"type": "text",
"text": pk, 
"align": "center",
"size": "sm",
"weight": "bold",
"color": "#33FF33",
"wrap": True
}
],
"type": "box",
"layout": "baseline"
}
],
"type": "box",
"layout": "vertical"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
"footer": {
"type": "box",
"layout": "horizontal",
"spacing": "sm",
"contents": [
{
"text": " Tack Time :"+van2 +" \n 🐧Khenzi🐧",
"size": "xs",
"margin": "none",
"color": "#33FF33",
"wrap": True,
"weight": "regular",
"type": "text"
}
]
}
}
]
}
}                                          
                                          sendTemplate(to, data)
        if op.type == 26:
            print ("[Self Bot Finger Killer ] ")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.contentType == 0 and sender not in ghiMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        if sets["tagsticker"] == True:
                            name = re.findall(r'@(\w+)', msg.text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                 if ghiMID in mention["M"]:
                                      msg = sets["messageSticker"]["listSticker"]["tag"]
                                      if msg != None:
                                          contact = ghi.getContact(ghiMID)
                                          a = contact.displayName
                                          stk = msg['STKID']
                                          spk = msg['STKPKGID']
                                          data={'type':'template','altText': str(a)+' Send stickers','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                                          sendTemplate(to, data)
                                      else:
                                          contact = ghi.getContact(ghiMID)
                                          a = contact.displayName
                                          stk = msg['STKID']
                                          spk = msg['STKPKGID']
                                          data={'type':'template','altText': str(a)+'Send stickers','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                                          sendTemplate(to, data)
#==============================================================================#
        if op.type == 19:
            if ghiMID in op.param3:
                apalo["Talkblacklist"][op.param2] = True
        if op.type == 26 or op.type == 25:
            msg = op.message
            sender = msg._from
            try:
               if mc["wr"][str(msg.text)]:
                   ghi.sendMessage(msg.to,mc["wr"][str(msg.text)])
            except:
              pass
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != ghi.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if msg.text.lower().startswith("hapus "):
                    delcmd = msg.text.split(" ")
                    getx = msg.text.replace(delcmd[0] + " ","")
                    ghi.sendContact(msg.to,str(getx))
                if msg.text.startswith("Setapi "):
                    try:
                        delcmd = msg.text.split(" ")
                        get = msg.text.replace(delcmd[0]+" ","").split(";;")
                        kw = get[0]
                        ans = get[1]
                        mc["wr"][kw] = ans
                        f=codecs.open('sb.json','w','utf-8')
                        json.dump(mc, f, sort_keys=True, indent=4, ensure_ascii=False)
                        ghi.sendMessage(msg.to,"Keywords: " + str(kw) + "\nreply: "+ str(ans))
                    except Exception as Error:
                        print(Error)
                if msg.text.startswith("clear api "):
                    try:
                        delcmd = msg.text.split(" ")
                        getx = msg.text.replace(delcmd[0] + " ","")
                        del mc["wr"][getx]
                        ghi.sendMessage(msg.to, "Kata " + str(getx) + " Dihapus")
                        f=codecs.open('sb.json','w','utf-8')
                        json.dump(mc, f, sort_keys=True, indent=4, ensure_ascii=False)
                    except Exception as Error:
                        print(Error)
                if msg.text.lower() == "jalankan api":
                    lisk = "[ All responses ]\n"
                    for i in mc["wr"]:
                        lisk+="\nKeywords: "+str(i)+"\nTanggapi: "+str(mc["wr"][i])+"\n"
                    lisk+="\nCara membersihkan api >\\<\nBersihkan api Diikuti oleh kata-kata yang mau di hapus"
                    data = {"type": "text","text": "{}".format(lisk),"sentBy": {"label": "list API", "iconUrl": "https://obs.line-scdn.net/{}".format(ghi.getContact(ghiMID).pictureStatus),"linkUrl": "line://ti/p/~topzalove123"}}
                    sendTemplate(to,data)
#==============================================================================#
#==============================================================================#
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != ghi.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
#========================================================================
                if msg.contentType == 7:
                    if sets["messageSticker"]["addStatus"] == True:
                        name = sets["messageSticker"]["addName"]
                        if name != None and name in sets["messageSticker"]["listSticker"]:
                            sets["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            ghi.sendMessage(to, "Success Added " + name)
                        sets["messageSticker"]["addStatus"] = False
                        sets["messageSticker"]["addName"] = None
                    if sets["addSticker"]["status"] == True:
                        stickers[sets["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[sets["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[sets["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        line.sendMessage(to, "Success Added sticker {}".format(str(sets["addSticker"]["name"])))
                        sets["addSticker"]["status"] = False
                        sets["addSticker"]["name"] = ""
                        
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != ghiMID: to = sender
                else: to = receiver
                if msg.contentType == 0 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            if msg.location != None:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"location":msg.location,"from":msg._from,"waktu":unsendmsg}
                            else:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"waktu":unsendmsg}
                        except Exception as e:
                            print (e)
                if msg.contentType == 1 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg1 = time.time()
                            path = ghi.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"image":path,"waktu":unsendmsg1}
                        except Exception as e:
                            print (e)
                if msg.contentType == 2 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg2 = time.time()
                            path = ghi.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"video":path,"waktu":unsendmsg2}
                        except Exception as e:
                            print (e)
                if msg.contentType == 3 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg3 = time.time()
                            path = ghi.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"audio":path,"waktu":unsendmsg3}
                        except Exception as e:
                            print (e)
                if msg.contentType == 7 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg7 = time.time()
                            sticker = msg.contentMetadata["STKID"]
                            link = "http://dl.stickershop.line.naver.jp/stickershop/v1/sticker/{}/android/sticker.png".format(sticker)
                            msg_dict[msg.id] = {"from":msg._from,"sticker":link,"waktu":unsendmsg7}
                        except Exception as e:
                            print (e)
                if msg.contentType == 13 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg13 = time.time()
                            mid = msg.contentMetadata["mid"]
                            msg_dict[msg.id] = {"from":msg._from,"mid":mid,"waktu":unsendmsg13}
                        except Exception as e:
                            print (e)
                if msg.contentType == 14 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg14 = time.time()
                            path = ghi.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"file":path,"waktu":unsendmsg14}
                        except Exception as e:
                            print (e)
        if op.type == 65:
            if op.param1 not in chatbot["botMute"]:
                if settings["unsendMessage"] == True:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        ah = time.time()
                        ikkeh = ghi.getContact(msg_dict[msg_id]["from"])
                        if "text" in msg_dict[msg_id]:
                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                            waktumsg = format_timespan(waktumsg)
                            rat_ = "\nSend At :\n{} ago".format(waktumsg)
                            rat_ += "\nText :\n{}".format(msg_dict[msg_id]["text"])
                            sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                            del msg_dict[msg_id]
                        else:
                            if "image" in msg_dict[msg_id]:
                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                waktumsg = format_timespan(waktumsg)
                                rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                rat_ += "\nImage :\nBelow"
                                sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                ghi.sendImage(at, msg_dict[msg_id]["image"])
                                del msg_dict[msg_id]
                            else:
                                if "video" in msg_dict[msg_id]:
                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                    waktumsg = format_timespan(waktumsg)
                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                    rat_ += "\nVideo :\nBelow"
                                    sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                    ghi.sendVideo(at, msg_dict[msg_id]["video"])
                                    del msg_dict[msg_id]
                                else:
                                    if "audio" in msg_dict[msg_id]:
                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                        waktumsg = format_timespan(waktumsg)
                                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                        rat_ += "\nAudio :\nBelow"
                                        sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                        ghi.sendAudio(at, msg_dict[msg_id]["audio"])
                                        del msg_dict[msg_id]
                                    else:
                                        if "sticker" in msg_dict[msg_id]:
                                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                                            waktumsg = format_timespan(waktumsg)
                                            rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                            rat_ += "\nSticker :\nBelow"
                                            sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                            ghi.sendImageWithURL(at, msg_dict[msg_id]["sticker"])
                                            del msg_dict[msg_id]
                                        else:
                                            if "mid" in msg_dict[msg_id]:
                                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                waktumsg = format_timespan(waktumsg)
                                                rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                rat_ += "\nContact :\nBelow"
                                                sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                ghi.sendContact(at, msg_dict[msg_id]["mid"])
                                                del msg_dict[msg_id]
                                            else:
                                                if "location" in msg_dict[msg_id]:
                                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                    waktumsg = format_timespan(waktumsg)
                                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                    rat_ += "\nLocation :\nBelow"
                                                    sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                    ghi.sendLocation(at, msg_dict[msg_id]["location"])
                                                    del msg_dict[msg_id]
                                                else:
                                                    if "file" in msg_dict[msg_id]:
                                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                        waktumsg = format_timespan(waktumsg)
                                                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                        rat_ += "\nFile :\nBelow"
                                                        sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                        ghi.sendFile(at, msg_dict[msg_id]["file"])
                                                        del msg_dict[msg_id]
                else:
                    print ("[ ERROR ] Terjadi Error Karena Tidak Ada Data Chat Tersebut~")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------                    
        if op.type in [26]:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                  to = receiver
               elif msg.toType == 2:
                  to = receiver
               if msg.contentType == 0:
                  if text is None:
                     return
                  else:
                    if receiver in temp_flood:
                      if temp_flood[receiver]["expire"] == True:
                        if msg.text == "/open":
                           temp_flood[receiver]["expire"] = False
                           temp_flood[receiver]["time"] = time.time()
                           ghi.sendMessage(to,"Bot Actived")
                        return
                      elif time.time() - temp_flood[receiver]["time"] <= 5:
                         temp_flood[receiver]["flood"] += 1
                         if temp_flood[receiver]["flood"] >= 200:
                            temp_flood[receiver]["flood"] = 0
                            temp_flood[receiver]["expire"] = True
                            duc1(to, "Orang yang mengirim lebih dari 200 pesan, meminta keluar otomatis")
                            ghi.leaveGroup(to)
                      else:
                       temp_flood[receiver]["flood"] = 0
                      temp_flood[receiver]["time"] = time.time()
                    else:
                      temp_flood[receiver] = {
                       "time": time.time(),
                       "flood": 0,
                       "expire": False
}
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------                                        
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            NOTIFIED_READ_MESSAGE(op)
    except Exception as error:
        logError(error)

#==============================================================================#
        backupData()
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)

def run():
    while True:
        try:
            ops = ghiPoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                   loop.run_until_complete(ghiBot(op))
                   ghiPoll.setRevision(op.revision)
        except Exception as e:
            logError(e)
if __name__ == "__main__":
    run()
