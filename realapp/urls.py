from django.urls import path
from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

app_name = 'realapp'
urlpatterns = [
    path('reg', views.RegisterUserView.as_view(), name="reg"),
    path('home', views.HomeUserView.as_view(), name="home"),
    path('', views.LoginUserView.as_view(), name="login"),
    path('adposting', views.AdPostingView.as_view(), name="adposting"),
    path('details/<int:pk>/',views.DetailUserView.as_view(),name="details"),
    # path('details/',views.DetailUserView.as_view(),name='details'),

    # path('details/(?P<pk>\d+)/$/',views.DetailUserView.as_view(),name="details"),


]
