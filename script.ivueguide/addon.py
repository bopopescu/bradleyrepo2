#
#      Copyright (C) 2012 Tommy Winther
#      http://tommy.winther.nu

#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this Program; see the file LICENSE.txt.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#
import gui, settings
import utils, base64
import sys

import xbmc,xbmcgui,xbmcaddon,os,time
import urllib
import urllib2
import datetime
import skins
import shutil
import gui, settings
import utils, base64
import sys
import threading
import re
from shutil import copytree

ADDONID = 'script.ivueguide'
ADDON = xbmcaddon.Addon(ADDONID) 
PACKAGES       = xbmc.translatePath(os.path.join('special://home', 'addons', 'packages'))
FORCE       = xbmc.translatePath(os.path.join('special://home', 'addons', 'script.ivueguide', 'force.py'))

skin = ADDON.getSetting('skin')
default = xbmc.translatePath(os.path.join('special://profile', 'addon_data', 'script.ivueguide', 'resources', 'skins', 'Default'))
setSkin = xbmc.translatePath(os.path.join('special://profile', 'addon_data', 'script.ivueguide', 'resources', 'skins', skin))
SkinFolder = xbmc.translatePath(os.path.join('special://profile', 'addon_data', 'script.ivueguide', 'resources', 'skins'))
iniPath = xbmc.translatePath(os.path.join('special://profile', 'addon_data', 'script.ivueguide', 'addons2.ini')) 
skinType = int(ADDON.getSetting('customSkin.type'))
iniFile = xbmc.translatePath(os.path.join('special://profile', 'addon_data', 'script.ivueguide', 'addons.ini'))
catsFile = xbmc.translatePath(os.path.join('special://profile', 'addon_data', 'script.ivueguide', 'categories.ini'))
ivueFile = 'http://ivuetvguide.com/ivueguide/categories.ini'
ivueINI = 'http://ivuetvguide.com/ivueguide/addons.ini'
skinsurl = 'http://ivuetvguide.com/ivueguide/skins/'
viewskins = skins.openURL(skinsurl)
matchskin =re.compile('<a href="(.*?)">').findall(viewskins)
skinfiles = [] 
d = xbmcgui.Dialog()
dp = xbmcgui.DialogProgress()

interval = int(ADDON.getSetting('creator.interval'))

INTERVAL_ALWAYS = 0
INTERVAL_12 = 1
INTERVAL_24 = 2
INTERVAL_48 = 3
INTERVAL_72 = 4
INTERVAL_96 = 5
INTERVAL_120 = 6
INTERVAL_OFF = 7

#Karls changes
def creator():
    if os.path.exists(iniPath) and not interval == INTERVAL_OFF:
        if interval <> INTERVAL_ALWAYS:
            modTime = datetime.datetime.fromtimestamp(os.path.getmtime(iniPath))
            td = datetime.datetime.now() - modTime
            diff = (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10 ** 6) / 10 ** 6
            if ((interval == INTERVAL_12 and diff >= 43200) or
                    (interval == INTERVAL_24 and diff >= 86400) or
                    (interval == INTERVAL_48 and diff >= 172800) or
                    (interval == INTERVAL_72 and diff >= 259200) or
                    (interval == INTERVAL_96 and diff >= 345600) or
                    (interval == INTERVAL_120 and diff >= 432000)):
                xbmc.executebuiltin('RunPlugin(plugin://plugin.video.IVUEcreator/update)')
            else:
                w = gui.TVGuide()
                w.doModal()
                del w
        else:
            xbmc.executebuiltin('RunPlugin(plugin://plugin.video.IVUEcreator/update)')

if os.path.exists(FORCE) and os.path.exists(SkinFolder):
    for name in matchskin:
        name = re.sub(r'%20', ' ', name)
        name = re.sub(r'.zip', '', name)
        if name in os.listdir(SkinFolder):
            shutil.rmtree(os.path.join(SkinFolder, name))
    url = 'http://ivuetvguide.com/ivueguide/skins/skins.zip'
    zipfile = os.path.join(PACKAGES,"skins.zip") 
    dp.create("iVue","Downloading latest Skin Pack",'')
    urllib.urlretrieve(url,zipfile,lambda nb, bs, fs, url=url: skins._pbhook(nb,bs,fs,url,dp))
    skins.extract(zipfile, SkinFolder)
    time.sleep(1)
    os.remove(FORCE)
    dp.close() 
elif os.path.exists(FORCE) and not os.path.exists(SkinFolder):
    os.remove(FORCE)

if not os.path.exists(default):
    url = 'http://ivuetvguide.com/ivueguide/skins/Default.zip'
    zipfile = os.path.join(PACKAGES,"default.zip") 
    dp.create("iVue","Downloading Default Skin",'')
    urllib.urlretrieve(url,zipfile,lambda nb, bs, fs, url=url: skins._pbhook(nb,bs,fs,url,dp))
    skins.extract(zipfile, SkinFolder)
    time.sleep(1)
    dp.close() 
 
if not os.path.exists(setSkin):
    url = 'http://ivuetvguide.com/ivueguide/skins/%s.zip' %(skin).replace (" ","%20") 
    try: 
        urllib2.urlopen(url)
        zipfile = os.path.join(PACKAGES,"%s.zip" % skin) 
        dp.create("iVue","Downloading %s" % skin,'')
        urllib.urlretrieve(url,zipfile,lambda nb, bs, fs, url=url: skins._pbhook(nb,bs,fs,url,dp))
        skins.extract(zipfile, SkinFolder)
        time.sleep(1)
        dp.close() 
    except urllib2.HTTPError, e:
            ADDON.setSetting('skin', 'Default')

if  ADDON.getSetting('focus.color') == 'text':
    ADDON.setSetting('focus.color', '[COLOR ffffffff]white[/COLOR]')
if  ADDON.getSetting('nofocus.color') == 'text':
    ADDON.setSetting('nofocus.color', '[COLOR ffffffff]white[/COLOR]') 

SKIN_FOLDER = 0
if ADDON.getSetting('customSkin.enabled') == 'true':
    if skinType == SKIN_FOLDER:
        if not ADDON.getSetting('customSkin.file') == '':
            customFile = str(ADDON.getSetting('customSkin.file'))
            skinName = os.path.split(os.path.dirname(customFile))[1]
            SkinFolder = xbmc.translatePath(os.path.join('special://profile', 'addon_data', 'script.ivueguide', 'resources', 'skins', '%s' % skinName))
            copytree(customFile, SkinFolder)
            ADDON.setSetting('customSkin.enabled', 'false')
            ADDON.setSetting('skin', skinName)

if ADDON.getSetting('ivue.addons.ini') == 'true':
    dp.create("iVue","Downloading addons.ini",'')
    urllib.urlretrieve(ivueINI,iniFile,lambda nb, bs, fs, url=ivueINI: skins._pbhook(nb,bs,fs,url,dp))
    dp.close()
    ADDON.setSetting('ivue.addons.ini', 'false')

elif ADDON.getSetting('ivue.addons.ini') == 'false' and not os.path.exists(iniFile):
    dp.create("iVue","Downloading addons.ini",'')
    urllib.urlretrieve(ivueINI,iniFile,lambda nb, bs, fs, url=ivueINI: skins._pbhook(nb,bs,fs,url,dp))
    dp.close()

if ADDON.getSetting('ivue-categories.ini.enabled') == 'true':
    dp.create("iVue","Downloading categories file",'')
    urllib.urlretrieve(ivueFile,catsFile,lambda nb, bs, fs, url=ivueFile: skins._pbhook(nb,bs,fs,url,dp))
    dp.close()
    ADDON.setSetting('ivue-categories.ini.enabled', 'false')

elif ADDON.getSetting('categories.ini.enabled') == 'true':
    if ADDON.getSetting('categories.ini.type') == '0':
        if not ADDON.getSetting('categories.ini.file') == '':
            if os.path.exists(catsFile):
                os.remove(catsFile)
            customFile = str(ADDON.getSetting('categories.ini.file'))
            shutil.copy(customFile, catsFile)
            ADDON.setSetting('categories.ini.enabled', 'false')
    else:
        customURL = str(ADDON.getSetting('categories.ini.url')) 
        urllib.urlretrieve(customURL, catsFile)
        ADDON.setSetting('categories.ini.enabled', 'false')

elif ADDON.getSetting('ivue-categories.ini.enabled') == 'false' and ADDON.getSetting('categories.ini.enabled') == 'false' and not os.path.exists(catsFile):
    dp.create("iVue","Downloading categories file",'')
    urllib.urlretrieve(ivueFile,catsFile,lambda nb, bs, fs, url=ivueFile: skins._pbhook(nb,bs,fs,url,dp))
    dp.close()

#End of Karls changes


#addons ini fix start

# set filepath
addons_data_ini_path = xbmc.translatePath('special://profile/addon_data/plugin.video.IVUEcreator/addons_index.ini')
old_ini_path = xbmc.translatePath('special://home/addons/plugin.video.IVUEcreator/addons_index.ini')

if os.path.exists(old_ini_path):
    shutil.move(old_ini_path, addons_data_ini_path)
#addons ini end


settings.setUrl()

try:
	runType = len(sys.argv)    
	if interval == INTERVAL_OFF:	        
	    w = gui.TVGuide()
	    w.doModal()
	    del w
	elif not interval == INTERVAL_OFF and runType == 1:
	    creator()
	elif not interval == INTERVAL_OFF and runType > 1:
	    w = gui.TVGuide()
	    w.doModal()
	    del w


except urllib2.HTTPError, e:
		if e.code == 401:
			utils.notify(addon_id, ae)
		else:
		    utils.notify(addon_id, e)