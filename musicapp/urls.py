from django.contrib import admin
from django.urls import path, include
from musicapp import views


class ArtistListApiView:
    pass


urlpatterns = {
    path('admin/', admin.site.urls),
    path('musicapp/', views.ArtistListApiView.as_view()),
    path('musicapp/', views.SongListApiView.as_view()),
    path('musicapp/', include()),
}

