from django.urls import path, include

from . import views

app_name = 'ncas'
urlpatterns = [
    path('Students/', views.StdView.as_view(), name='std'),
    path('Course/', views.CoursView.as_view(), name='course'),
    path('<int:pk>/', views.CoursDView.as_view(), name='coursed'),
    path('Students/<int:pk>/', views.StdDView.as_view(), name='stdd'),
    path('signup/', views.SignUp.as_view(), name='signup')
]
