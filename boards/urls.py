from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('boards/', views.show_boards,name='boards'),
    path('topic/', views.show_topic,name='topics'),
    path('post/', views.show_post,name='posts'),
    
    path('add_board/',views.add_board,name='add_board'),
    path('update_board/<int:id>',views.update_board,name='update_board'),
    
    path('add_topic/',views.add_topic,name='add_topic'),  
    path('update_topic/<int:id>',views.update_topic,name='update_topic'),
    
    path('add_post/',views.add_post,name='add_post'),    
    path('update_post/<int:id>',views.update_post,name='update_post'),
    
    path('all/',views.all,name='all'),

    
]