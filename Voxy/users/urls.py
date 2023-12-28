from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.log_in, name='login-view'),
    #path('hello/<firstname>', views.hello, name='hello-view'),
    #path('test',views.test_template, name='test'),
    #path('<int:question_id>/',views.detail, name='detail'),
    #path('<int:question_id>/results/',views.results, name='results'),
    #path('<int:question_id>/vote/',views.vote, name='vote'),
]
