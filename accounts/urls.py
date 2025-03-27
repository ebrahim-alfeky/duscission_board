from django.urls import path,reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    
    path('signup/',views.signup,name='signup'),
    
    path('login/',views.login,name='login'),
    
    # path('',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    
    path(
            'password_change/', 
            auth_views.PasswordChangeView.as_view
            (
            template_name='accounts/password_change.html',
            success_url=reverse_lazy('password_change_done') 
            )
            , name='password_change'
        ),
    
    path('password_change_done/',auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),name='password_change_done'),
    
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    
    path('update_account/', views.update_account, name='update_account'),
    
]