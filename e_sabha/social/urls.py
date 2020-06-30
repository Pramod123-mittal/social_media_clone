from django.urls import path
from django.views.generic.base import RedirectView
from .import views
urlpatterns = [
    path('',views.AboutView.as_view()),
    path('home/',views.HomeView.as_view()),
    path('contact/',views.contact),
    path('profile/edit/<int:pk>/',views.MyProfileUpdateView.as_view(success_url = '/social')),
    path('mypost/list',views.MyPostListView.as_view()),
    path('mypost/create',views.MyPostCreateView.as_view(success_url = '/social/mypost/list')),
    path('mypost/detail/<int:pk>',views.MyPostDetailView.as_view()),
    path('mypost/delete/<int:pk>',views.MyPostDeleteView.as_view(success_url = '/social/mypost/list')),
    path('myprofile/list',views.MyProfileListView.as_view()),
    path('myprofile/detail/<int:pk>',views.MyProfileDetailView.as_view()),
    path('myprofile/follow/<int:pk>',views.follow),
    path('myprofile/unfollow/<int:pk>',views.unfollow),
    path('mypost/like/<int:pk>',views.like),
    path('mypost/unlike/<int:pk>',views.unlike),
   
    
]
