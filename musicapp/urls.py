from django.contrib import admin
from django.urls import path, include
from musicapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('musicapp/', views.artistlistapiview()),
    path('musicapp/', views.songlistapiview()),
    path('musicapp/', include()),
]

