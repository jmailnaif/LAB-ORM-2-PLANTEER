
from . import views
from django.urls import path

app_name = "App"

urlpatterns=[ 
    path('', views.home_page, name="home_page"),
    path('add/',views.add_post_view,name="add_post_view"),
    path("post/detail/<post_id>/", views.post_detail_view, name="post_detail_view"),
    path("post/update/<post_id>/", views.update_post_view, name="update_post_view"),
    path("post/delete/<post_id>/", views.delete_post_view, name="delete_post_view"),
    path("post/search/", views.posts_search_view, name="posts_search_view"),
    path("post/all/", views.all_posts_view, name="all_posts_view"),
    path("comments/add/<post_id>/", views.add_comment_view, name="add_comment_view"),
    path('contact/', views.contact_us_view, name='contact_us_view'),
    path('contact/messages/', views.contact_messages_view, name='contact_messages_view'),






  
]


    
