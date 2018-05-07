from django.urls import path
from django.conf.urls import url
from . import views
app_name = 'realapp'
urlpatterns = [
    path('reg', views.RegisterUserView.as_view(), name="reg"),
    path('home', views.HomeUserView.as_view(), name="home"),
    path('login', views.LoginUserView.as_view(), name="login"),
    path('adposting', views.AdPostingView.as_view(), name="adposting")

]
