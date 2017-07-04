import time
import os, shutil
import xbmc
import xbmcgui
import xbmcaddon

databasePath = xbmc.translatePath('special://profile/addon_data/script.ivueguide')
dialog = xbmcgui.Dialog()

for root, dirs, files in os.walk(databasePath,topdown=True):
    dirs[:] = [d for d in dirs if d not in ['skins']]
    for name in files:
        os.remove(os.path.join(root,name))

    for root, dirs, files in os.walk(databasePath,topdown=True):
        dirs[:] = [d for d in dirs if d not in ['skins']]							
        for name in dirs:
            if name not in ["resources"]:
                shutil.rmtree(os.path.join(root,name),ignore_errors=True, onerror=None)

for root, dirs, files in os.walk(databasePath,topdown=True):
    dirs[:] = [d for d in dirs if d not in ['skins', 'resources']]
    if not files:
        dialog.ok('Ivue guide Hard reset', 'Please restart for ','the changes to take effect','[COLOR yellow]Thank you for using Hard Reset[/COLOR]')
    else:
        dialog.ok('Ivue guide Hard reset', 'Failed to remove some files','[COLOR yellow]Please try again[/COLOR]')
    
