from django.urls import path, re_path

from . import views

urlpatterns=[
    path('audio/',views.Audio_store),
    path('',views.Audio_store),
    # re_path('^$',views.Take_num),
]