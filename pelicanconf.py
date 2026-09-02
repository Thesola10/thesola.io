import nerdfont

JINJA_FILTERS = {
        'nf': lambda name: nerdfont.icons[name],
}

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

TAGLINES = (
        #     neutral                        hover
        # <-----------28ch----------->   <------------28ch---------->
        ("nix-shell -p peace_quiet",    "TODO: port to flake"         ),
        ("#[do_not_crash]",             None                          ),
        ("meaningOfLife :: IO ()",      None                          ),
        ("ザ・ソーラ・テン",            None                          ),
        ("Unregistered HyperCam 2",     None                          ),
        ("xkcd/838 compliant",          None                          ),
        ("raised by cd-roms",           None                          ),
        ("f3 e5 g4 Qh4#",               None                          ),
        ("kernel panic - not syncing",  "attempted to kill init!"     ),
        (":() { :|:& }; (:&)",          None                          ),
        ("btw i use Silverblue",        None                          ),
        ("just one more project!",      None                          ),
        ("お前の保証はもう、死んでいる","your warranty's already dead"),
        ("What is a sops file?",        "A miserable little pile of secrets!"),
        ("continuously integrated",     None                          ),
        ("rin-chaaaaaaan!",             "watch yurucamp"              ),
        ("managed to exit vim",         None                          ),
)


SOCIAL = (('nf-md-mail', 'mailto:me@thesola.io'),
          ('nf-fa-github', 'https://github.com/thesola10'),
          ('nf-md-mastodon', 'https://thesola.io/@me'),
          ('nf-fa-twitter', 'https://twitter.com/itsthesola10'),
          ('nf-fa-linkedin_square', 'https://linkedin.com/in/thesola10'),
          ('nf-fa-lastfm', 'https://www.last.fm/user/thesola10'),
          ('nf-fa-reddit_alien', 'https://reddit.com/u/thesola10')
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

