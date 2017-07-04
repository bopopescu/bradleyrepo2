import sys
import os
import urllib
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import logging
from operator import itemgetter

def show_tags():
  tag_handle = int(sys.argv[1])
  xbmcplugin.setContent(tag_handle, 'tags')

  for tag in tags:
    iconPath = os.path.join(home, 'logos', tag['icon'])
    li = xbmcgui.ListItem(tag['name'], iconImage=iconPath)
    url = sys.argv[0] + '?tag=' + str(tag['id'])
    xbmcplugin.addDirectoryItem(handle=tag_handle, url=url, listitem=li, isFolder=True)

  xbmcplugin.endOfDirectory(tag_handle)


def show_streams(tag):
  stream_handle = int(sys.argv[1])
  xbmcplugin.setContent(stream_handle, 'streams')
  logging.warning('TAG show_streams!!!! %s', tag)
  for stream in streams[str(tag)]:
    logging.debug('STREAM HERE!!! %s', stream['name'])
    iconPath = os.path.join(home, 'logos', stream['icon'])
    li = xbmcgui.ListItem(stream['name'], iconImage=iconPath)
    xbmcplugin.addDirectoryItem(handle=stream_handle, url=stream['url'], listitem=li)

  xbmcplugin.endOfDirectory(stream_handle)


def get_params():
  """
  Retrieves the current existing parameters from XBMC.
  """
  param = []
  paramstring = sys.argv[2]
  if len(paramstring) >= 2:
    params = sys.argv[2]
    cleanedparams = params.replace('?', '')
    if params[len(params) - 1] == '/':
      params = params[0:len(params) - 2]
    pairsofparams = cleanedparams.split('&')
    param = {}
    for i in range(len(pairsofparams)):
      splitparams = {}
      splitparams = pairsofparams[i].split('=')
      if (len(splitparams)) == 2:
        param[splitparams[0]] = splitparams[1]
  return param


def lower_getter(field):
  def _getter(obj):
    return obj[field].lower()

  return _getter


addon = xbmcaddon.Addon()
home = xbmc.translatePath(addon.getAddonInfo('path'))

tags = [
  {
    'name': 'Live TV',
    'id': 'LiveTV',
    'icon': 'livetv.png'
  }, {
    'name': 'Movies',
    'id': 'Movies',
    'icon': 'movies.png'
  }
]


LiveTV = [{
  'name': 'Vevo Tv',
  'url': 'http://51.255.74.170:7000/live/robyn/robyn/3479.ts',
  'icon': 'Vevo Tv.png',
  'disabled': False
}, {
  'name': 'National Geographic',
  'url': '',
  'icon': 'National Geographic.png',
  'disabled': False
}, {
  'name': 'Food Network',
  'url': '',
  'icon': 'Food Network.png',
  'disabled': False
}, {
  'name': 'FX',
  'url': '',
  'icon': 'FX.png',
  'disabled': False
}]


Movies = [{
  'name': 'Despicable Me 2',
  'url': '',
  'icon': 'Despicable Me 2.png',
  'disabled': False
}]


streams = {
  'LiveTV': sorted((i for i in LiveTV if not i.get('disabled', False)), key=lower_getter('name')),
  'Movies': sorted((i for i in Movies if not i.get('disabled', False)), key=lower_getter('name')),
  # 'LiveTV': sorted(LiveTV, key=lower_getter('name')),
  # 'Movies': sorted(Movies, key=lower_getter('name')),
}

PARAMS = get_params()
TAG = None
logging.warning('PARAMS!!!! %s', PARAMS)

try:
  TAG = PARAMS['tag']
except:
  pass

logging.warning('ARGS!!!! sys.argv %s', sys.argv)

if TAG == None:
  show_tags()
else:
  show_streams(TAG)
