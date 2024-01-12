from django.urls import path
from . import views

app_name='users'
urlpatterns = [
    path('../', views.index_view, name='index'),
    path('connection/',views.connnexion_view, name='login'),
    path('signup/', views.sign_up, name='sign_up'),  # Utilisation d'un chemin distinct pour l'inscription
    path('login/', views.log_in, name='log_in'),
    
    #path('hello/<firstname>', views.hello, name='hello-view'),
    #path('test',views.test_template, name='test'),
    #path('<int:question_id>/',views.detail, name='detail'),
    #path('<int:question_id>/results/',views.results, name='results'),
    #path('<int:question_id>/vote/',views.vote, name='vote'),
]
