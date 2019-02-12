from django.urls import path


from . import views

app_name = 'ncas'
urlpatterns = [

    path('course/<int:pk>/', views.CourseDetail.as_view(), name='course'),
    path('courselist/',views.CourseList.as_view(), name='clist'),
    path('students/<int:pk>/', views.StudentDetail.as_view(), name='studentd'),
    path('signup/', views.signUp, name='signup'),
    path('admno/', views.admnoverification, name='admno'),

]
