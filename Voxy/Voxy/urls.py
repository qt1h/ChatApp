
from django.contrib import admin
from django.urls import path,include
from . import views
from .views import custom_404
handler404 = custom_404
urlpatterns = [
    path('', views.index_view, name='index'),
    path('help/', views.help, name='help'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('chatrooms.urls'))
]

