from cachetools import cached, TTLCache

import os
import time
import pylast

API_KEY = os.environ['LASTFM_API_KEY']
USER = "thesola10"

@cached(TTLCache(maxsize=256, ttl=3600*24))
def _lastfm_user():
    return pylast.LastFMNetwork(API_KEY).get_user(USER)

@cached(TTLCache(maxsize=256, ttl=30))
def get_nowplaying():
    play = _lastfm_user().get_now_playing()
    if play:
        return { "playing": True
               , "artist": play.get_artist().get_name()
               , "title": play.get_title()
               , "lastfm_url": play.get_url()
               }
    else:
        return { "playing": False }
