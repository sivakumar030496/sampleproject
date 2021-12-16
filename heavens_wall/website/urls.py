from django.urls import path, re_path
from . import views
app_name='website'
urlpatterns= [
    path('',views.index,name='index'),
    path('about_us',views.about_us,name='about_us'),
    path('home',views.home,name='home'),
    path("profile_views/<slug:slug>",views.profile_views,name="profile_views"),
    path('profiles',views.profiles,name='profiles'),
    path('privacy_policy',views.privacy_policy,name='privacy_policy'),
    path('terms_conditions',views.announcement,name='announcement'),
    path('contactus',views.contactus,name='contacts'),
    path('login',views.login,name='login'),
    path('get_profile_view',views.get_profile_view,name='get_profile_view')

]
