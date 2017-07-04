import xbmc, xbmcgui, shutil, urllib2, urllib, os, xbmcaddon, zipfile, time, re
import shutil
import xbmcvfs

ADDONID = 'script.ivueguide'
ADDON = xbmcaddon.Addon(ADDONID)
HOME = ADDON.getAddonInfo('path')
ICON = os.path.join(HOME, 'icon.png')
PACKAGES       = xbmc.translatePath(os.path.join('special://home', 'addons', 'packages'))
TEMP =	  ADDON.getSetting('tempskin')
USER_AGENT     = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
d = xbmcgui.Dialog()
dp = xbmcgui.DialogProgress()
path = xbmc.translatePath(os.path.join('special://profile', 'addon_data', 'script.ivueguide', 'resources', 'skins'))
prnum=""
try:
    prnum= sys.argv[ 1 ]
except:
    pass


def openURL(url):
	  req = urllib2.Request(url)
	  req.add_header('User-Agent', USER_AGENT)
	  response = urllib2.urlopen(req)
	  link=response.read()
	  response.close()
	  return link

def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
	try:
		percent = min((numblocks*blocksize*100)/filesize, 100)
		print 'done' +str(percent)+'%'
		dp.update(percent)
	except:
		percent = 100
		dp.update(percent)
	if dp.iscanceled():
		raise Exception("Cancelled")
		dp.close()

def extract(_in, _out):
	dp = xbmcgui.DialogProgress()
	zin    = zipfile.ZipFile(_in,  'r')
	nFiles = float(len(zin.infolist()))
	count  = 0
	for item in zin.infolist():
		count += 1
		update = count / nFiles * 100
		zin.extract(item, _out)


def Custom():
	  folder = xbmc.translatePath(os.path.join('special://home', 'addons', 'packages', 'customskin'))
	  if not os.path.exists(folder):
	      os.makedirs(folder)
	  choice = xbmc.Keyboard('','[COLOR fffea800][B]ENTER ZIP URL[/B][/COLOR]')
	  choice.setDefault(ADDON.getSetting('customSkin.url'))
	  choice.setHiddenInput(False)
	  choice .doModal()
	  input= choice.getText()
	  zipSkin = os.path.join(PACKAGES,'Custom.zip') 
	  dp.create("iVue","downloading skin from %s" % input,'')
	  urllib.urlretrieve(input,zipSkin,lambda nb, bs, fs, url=input: _pbhook(nb,bs,fs,input,dp))
	  extract(zipSkin, folder) 
	  time.sleep(1)
	  skinName = os.walk(folder).next()[1]
	  join = os.path.join(folder, *(skinName))
	  set = '%s' % join
	  ADDON.setSetting('customSkin.url', input)
	  splitName = os.path.basename(join)
	  SkinFolder = xbmc.translatePath(os.path.join('special://profile', 'addon_data', 'script.ivueguide', 'resources', 'skins', '%s' % splitName))
	  if os.path.exists(SkinFolder):
	      shutil.rmtree(SkinFolder)
	  shutil.move(join, SkinFolder)
	  ADDON.setSetting('skin', splitName)
	  ADDON.setSetting('customSkin.enabled', 'false') 
	  shutil.rmtree(folder)
	  d.ok('Ivue', 'Download complete', '',"%s is now set as current skin" % splitName) 

def listskins():
    files = [] 
    if os.path.exists(path):
        for name in os.listdir(path): 
            files.append(name)
        skin = d.select("ivue", files)
        if skin == -1:
            return
        else:
            selected = files[skin]
            ADDON.setSetting('skin', selected)
    else:
        d.ok('Ivue', 'Skin Folder Missing', '',"Please run iVue to complete setup")

def getskins():
    folder = 'http://ivuetvguide.com/ivueguide/skins/'
    view = openURL(folder)
    match=re.compile('<a href="(.*?)">').findall(view)
    files = [] 
    for name in match:
        name = re.sub(r'/ivueguide/', '', name)
        name = re.sub(r'%20', ' ', name)
        name = re.sub(r'.zip', '', name)
        if not name in os.listdir(path):
            files.append(name)
    skin = d.select("ivue", files)
    if skin == -1:
        return
    else:
        selected = files[skin]
        zipurl = 'http://ivuetvguide.com/ivueguide/skins/%s.zip' % (selected).replace(' ', '%20') 
        zipfile = os.path.join(PACKAGES,"%s.zip" % selected) 
        dp.create("iVue","Downloading %s" % selected,'')
        urllib.urlretrieve(zipurl,zipfile,lambda nb, bs, fs, url=zipurl: _pbhook(nb,bs,fs,zipurl,dp))
        extract(zipfile, path) 
        time.sleep(1)
        dp.close() 
        if os.path.exists(path + "/%s" % selected): 
            ADDON.setSetting('skin', '%s' % selected)
            ADDON.setSetting('download.skin', '')

            d.ok('Ivue', 'Download complete', '', '%s is now set as current skin' % selected)
        else:
            d.ok('Ivue', 'Download failed', 'Please try downloading again')
 
def delskins():
    files = [] 
    if os.path.exists(path):
        for name in os.listdir(path): 
            files.append(name)
        skin = d.select("ivue", files)
        if skin == -1:
            return
        else:
            selected = files[skin]
            installed = xbmc.translatePath(os.path.join('special://profile', 'addon_data', 'script.ivueguide', 'resources', 'skins', '%s' % selected))
            shutil.rmtree(installed)
            if not os.path.exists(installed):
                d.ok("iVue", '','%s has been successfully removed' % selected, " [COLOR gold]Brought To You By iVue[/COLOR]")
            else:
                d.ok("iVue", '','%s was not removed' % selected, " [COLOR gold]Please try again[/COLOR]")
    else:
        d.ok('Ivue', 'No skins installed', '',"Please run iVue to complete setup")

def updater():
	message = 'Checking Addon Updates'
	xbmc.executebuiltin('XBMC.Notification(%s, %s, 2000, %s)' % (ADDONID, message, ICON))
	xbmc.executebuiltin("XBMC.UpdateAddonRepos()")
	d.ok("iVue", '',' CHECKING FOR REPO UPDATES SUCCESSFUL :)', " [COLOR gold]Brought To You By iVue[/COLOR]")
	return

if prnum == 'Custom':
    Custom()
 
elif prnum == 'List':
    listskins()

elif prnum == 'Get':
    getskins()

elif prnum == 'Delete':
    delskins()

elif prnum == 'Update':
    updater()
