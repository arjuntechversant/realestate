from django.urls import path
from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from django.views.generic import UpdateView

app_name = 'realapp'
urlpatterns = [
    path('reg', views.RegisterUserView.as_view(), name="reg"),
    path('', views.HomeUserView.as_view(), name='home'),
    path('login', views.LoginUserView.as_view(), name="login"),
    path('adposting', views.AdPostingView.as_view(), name="adposting"),
    path('details/<int:pk>/', views.DetailUserView.as_view(), name="details"),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('edit/<int:pk>/', views.EditAdd.as_view(), name="edit"),
    path('delete/<int:pk>/', views.DeleteAdd.as_view(), name="delete"),
    path('myads/',views.MyAds.as_view(), name="myads"),
    path('registration/<str:key>', views.RegistrationSuccess.as_view(), name='product_success'),

    # path('details/',views.DetailUserView.as_view(),name='details'),

    # path('details/(?P<pk>\d+)/$/',views.DetailUserView.as_view(),name="details"),


]
