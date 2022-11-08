from django.contrib import admin
from django.urls import path, include
from musicapp import views


urlpatterns = {
    path('admin/', admin.site.urls),
    path('musicapp/', views.artist_list(request={})),
    path('musicapp/', views.song_list(request={})),
}

