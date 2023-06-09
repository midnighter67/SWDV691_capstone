from django.urls import path
from . import views

urlpatterns = [
    # path('template', views.functionName, name='name')
    path('', views.home, name="home"),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('create_user', views.register_user, name='createAccount'),
    path('user_profile', views.edit_profile, name='userProfile'),  # path('user_profile', views.edit_profile, name='userProfile')
    path('change_password', views.change_password, name='changePassword'),  # path('change_password', views.change_password, name='change_password'), 
    path('results', views.search_results, name='search'),
    path('user_reviews', views.user_reviews, name='userReviews'),
    path('user_profile', views.edit_profile, name='updateUser'),  # path('user_profile', views.update_user_profile, name='updateUser')
]