from django.urls import path
from . import views

app_name='users'
urlpatterns = [
    path('../', views.index_view, name='index'),
    path('connection/',views.connnexion_view, name='login'),
    path('signup/', views.sign_up, name='sign_up'),  # Use another path for registering
    path('login/', views.log_in, name='log_in')
]
