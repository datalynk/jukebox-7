# Brandon Edens
# 2010-01-09
# Copyright (C) 2010 Brandon Edens <brandon@as220.org>
"""
"""

###############################################################################
## Imports
###############################################################################

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.views.generic.simple import direct_to_template

from jukebox.music.models import Song, Photo


###############################################################################
## Functions
###############################################################################

@login_required
@permission_required('music.song.can_review')
def index(request):
    song_list = Song.objects.filter(reviewed=False)
    photo_list = Photo.objects.filter(reviewed=False)
    return direct_to_template(request, template='review/index.html',
                              extra_context={
                                  'song_list': song_list,
                                  'photo_list': photo_list,
                                  },)

@login_required
@permission_required('music.song.can_review')
def song_accept(request, song_id):
    pass

@login_required
@permission_required('music.song.can_review')
def song_reject(request, song_id):
    pass

