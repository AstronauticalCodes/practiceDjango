from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='article_list'),
    path('list_of_articles/', views.list_of_articles, name='list_of_articles'),
    path('contributors/', views.contributors, kwargs={'name': 'Anonymous', 'age': 45, 'experience': 'Experienced'}, name='contributors'),
]
