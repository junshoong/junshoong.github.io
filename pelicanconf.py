#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Junshoong'
SITENAME = 'Junshoong의 기술블로그'
SITEURL = 'http://blog.junshoong.net'

OUTPUT_PATH = 'output'
PATH = 'content'

TIMEZONE = 'Asia/Seoul'

DEFAULT_LANG = 'ko'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('email', 'junshoong@gmail.com'),
          ('facebook', 'https://www.facebook.com/vaporize93'),
          ('linkedin', 'https://www.linkedin.com/in/junshoong'),
          ('slideshare', 'https://www.slideshare.net/junshoong'),
          ('github','https://github.com/junshoong'),
          ('stack-overflow','https://www.stackoverflow.com/users/4466697/junsu-kim'),)

DEFAULT_PAGINATION = 7
SUMMARY_MAX_LENGTH = 20

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Theme
THEME = "theme/cared"
DEFAULT_DATE_FORMAT = '%Y-%m-%d, %a'

# Url settings, remove '.html'
#ARCHIVE_URL = '{archive}'
#ARCHIVE_SAVE_AS = ARCHIVE_URL+'.html'

ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL+'index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL+'index.html'

CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = CATEGORY_URL+'index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = TAG_URL+'index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'

AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = AUTHOR_URL+'index.html'

# Profile Settings
PROFILE_IMAGE = 'profile.png'

# Pagination
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/{number}/', '{base_name}/{number}/index.html'),
)
