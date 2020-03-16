from django.urls import path, re_path
from .views import (shortURL_list, shortURL_detail)

urlpatterns = [
    path('short-urls/', shortURL_list),
    re_path(r'(?P<short_url>[a-zA-Z0-9]+)/$', shortURL_detail),
    # re_path(r'[a-zA-Z0-9]+/$', shortURL_detail),
]
