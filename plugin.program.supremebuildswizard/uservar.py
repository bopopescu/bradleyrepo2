import os, xbmc, xbmcaddon

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'Supreme Builds Wizard'
EXCLUDES       = [ADDON_ID, 'repository.supremebuilds', 'repository.infadroid']
# Text File with build info in it.
BUILDFILE      = 'http://supreme1.srve.io/sbwiz/texts/builds.txt'
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.
APKFILE        = 'http://supreme1.srve.io/sbwiz/texts/apks.txt'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = 'YouTube Videos'
YOUTUBEFILE    = 'http://supreme1.srve.io/sbwiz/texts/youtube.txt'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'http://supreme1.srve.io/sbwiz/texts/addons.txt'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'http://supreme1.srve.io/sbwiz/texts/advanced.txt'

# Dont need to edit just here for icons stored locally
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'http://supreme1.srve.io/sbwiz/images/supremebuilds.png'
ICONMAINT      = 'http://supreme1.srve.io/sbwiz/images/maintenance.png'
ICONAPK        = 'http://supreme1.srve.io/sbwiz/images/apkinstaller.png'
ICONADDONS     = 'http://supreme1.srve.io/sbwiz/images/addoninstaller.png'
ICONYOUTUBE    = 'http://supreme1.srve.io/sbwiz/images/youtube.png'
ICONSAVE       = 'http://supreme1.srve.io/sbwiz/images/savedata.png'
ICONTRAKT      = 'http://supreme1.srve.io/sbwiz/images/trakt.png'
ICONREAL       = 'http://supreme1.srve.io/sbwiz/images/realdebrid.png'
ICONLOGIN      = 'http://supreme1.srve.io/sbwiz/images/login.png'
ICONCONTACT    = 'http://supreme1.srve.io/sbwiz/images/contactus.png'
ICONSETTINGS   = 'http://supreme1.srve.io/sbwiz/images/settings.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '='

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'firebrick'
COLOR2         = 'ghostwhite'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+'][B][I]([COLOR '+COLOR2+']Supreme Builds[/COLOR])[/B][/COLOR] [COLOR '+COLOR2+']%s[/COLOR][/I]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'Thank you for choosing Supreme Builds.\r\n\r\nContact us and get support on facebook at http://facebook.com/groups/supremebuilds'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = 'http://supreme1.srve.io/sbwiz/images/contactus.png'
CONTACTFANART  = 'http://supreme1.srve.io/sbwiz/images/sbforumfanart.jpg'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'No'
# Url to wizard version
WIZARDFILE     = ''
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'No'
# Addon ID for the repository
REPOID         = 'repository.supremebuilds'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'https://raw.githubusercontent.com/kodiskills/supremebuildsrepo/master/repository.supremebuilds/addon.xml'
# Url to folder zip is located in
REPOZIPURL     = 'https://github.com/kodiskills/supremebuildsrepo/raw/master/zips'
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'Yes'
# Url to notification file
NOTIFICATION   = 'http://supreme1.srve.io/sbwiz/texts/notify.txt'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Image'
HEADERMESSAGE  = ''
# url to image if using Image 424x180
HEADERIMAGE    = 'http://supreme1.srve.io/sbwiz/images/sbnews.png'
# Background for Notification Window
BACKGROUND     = 'http://supreme1.srve.io/sbwiz/images/sbsplash.jpg'
#########################################################