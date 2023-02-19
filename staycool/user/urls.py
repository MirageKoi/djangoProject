from django.urls import path
from . import views


urlpatterns = [
    path('signin/', views.signin_view, name='signin_view'),
    path('signup/', views.signup_view, name='signup_view'),

]