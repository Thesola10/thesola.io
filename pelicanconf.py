AUTHOR = 'Karim Vergnes'
SITENAME = 'Karim Vergnes'
SITEURL = ''

THEME = 'theme'
PATH = 'content'

ARCHETYPE = 'front'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

PAGE_LANG_URL = '{lang}/{slug}'
PAGE_LANG_SAVE_AS = '{lang}/{slug}/index.html'

MENUITEMS = (
        ('developer', 'developer'),
        ('artist', 'artist'),
        ('storyteller', 'storyteller')
)

SOCIAL = (('Mail', 'mailto:me@thesola.io'),
          ('GitHub', 'https://github.com/thesola10'),
          ('Fediverse', 'https://thesola.io/@me'),
          ('Twitter', 'https://twitter.com/itsthesola10'),
          ('LinkedIn', 'https://linkedin.com/in/thesola10'),
          ('Last.fm', 'https://www.last.fm/user/thesola10'),
          ('Reddit', 'https://reddit.com/u/thesola10')
         )

PLUGINS = [ 'sitemap', 'pelican_alias' ]

SITEMAP = {
    "exclude": [
        "^/images/",
        "/tag/",
        "^/listening/"
    ]
}

STATIC_PATHS = ['images', 'static', 'robots.txt']
