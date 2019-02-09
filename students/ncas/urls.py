from django.urls import path


from . import views

app_name = 'ncas'
urlpatterns = [
    path('Students/', views.StdView.as_view(), name='std'),
    path('Course/', views.CoursView.as_view(), name='course'),
    path('<int:pk>/', views.CoursDView.as_view(), name='coursed'),
    path('Students/<int:pk>/', views.StdDView.as_view(), name='stdd'),
    path('signup/', views.signUp, name='signup'),
    path('admno/', views.admnoverification, name='admno'),
    path('semview/', views.SemView.as_view(), name='semv'),
    path('semd/', views.SemDLView.as_view(), name='semd'),
]
