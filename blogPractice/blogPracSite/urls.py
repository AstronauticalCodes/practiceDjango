from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('post/<int:pk>/', views.PostView.as_view(), name='post'),
    # path('commentator/<int:pk>/', views.CommentatorView.as_view(), name='commentator'),
    # path('commentatorsList/', views.CommentatorsListView.as_view(), name='commentatorsList'),
    # commentig.. declaring end of support for this project of django. Thanks for learning.
]
