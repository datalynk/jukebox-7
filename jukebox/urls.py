# Brandon Edens
# AS220
# 2009-12-24
# Copyright (C) 2009 Brandon Edens <brandon@as220.org>
#
# This file is part of Jukebox.
#
# Jukebox is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Jukebox is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Jukebox.  If not, see <http://www.gnu.org/licenses/>.
"""
"""

###############################################################################
## Imports
###############################################################################

from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import direct_to_template

from jukebox.views import index


###############################################################################
## Statements
###############################################################################

handler500 = 'jukebox.views.server_error'

admin.autodiscover()

urlpatterns = patterns('',

    # Administrative services.
    (r'^admin/', include(admin.site.urls)),

    # Third party URLs.
    (r'^accounts/', include('registration.urls')),

    # Top level URLS.
    url(r'^$', index,
        name='index'),

    url(r'^about/$', direct_to_template,
        {'template': 'about.html',},
        name='about'),
    url(r'^faq/$', direct_to_template,
        {'template': 'faq.html',},
        name='faq'),


    # Application URLs.
    (r'^music/', include('music.urls')),
    (r'^profile/', include('profile.urls')),
    (r'^review/', include('review.urls')),
    (r'^search/', include('search.urls')),


)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
    (r'^'+settings.MEDIA_URL[1:]+'(?P<path>.*)$', 'serve',
     {'document_root': settings.MEDIA_ROOT,
      'show_indexes': True }),)

