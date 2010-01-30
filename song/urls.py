# Brandon Edens
# 2010-01-27
# Copyright (C) 2010 Brandon Edens <brandon@as220.org>
#
# This file is part of jukebox.
#
# jukebox is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# jukebox is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with jukebox. If not, see <http://www.gnu.org/licenses/>.
"""
"""

###############################################################################
## Imports
###############################################################################

from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_detail
from django.views.generic.list_detail import object_list

from jukebox import settings
from jukebox.song.models import Song


###############################################################################
## Constants
###############################################################################

urlpatterns = patterns('jukebox.song.views',
    url(r'^$', object_list,
        {'queryset': Song.objects.all(),
         'template_object_name': 'song',
         'paginate_by': settings.SONGS_PER_PAGE,},
        name='song_list',),
)
