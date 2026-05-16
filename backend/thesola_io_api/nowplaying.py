from cachetools import cached, TTLCache
from dotenv import load_dotenv

from . import app

import os
import time
import pylast
import random

HOUR = 3600

try:
    API_KEY = os.environ['LASTFM_API_KEY']
except:
    API_KEY = app.config['LASTFM_API_KEY']
USER = "thesola10"

@cached(TTLCache(maxsize=256, ttl=24*HOUR))
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

@cached(TTLCache(maxsize=256, ttl=1*HOUR))
def get_one_song():
    hist = _lastfm_user().get_recent_tracks(10)
    sel = random.sample(hist, 1)[0]
    return { "artist": sel.track.get_artist().get_name()
            , "title": sel.track.get_title()
            , "when": sel.timestamp
            }
