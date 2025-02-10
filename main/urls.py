from django.urls import path
from .views import index, blog_list, blog_detail, portfolio_list, portfolio_detail

urlpatterns = [
    path('', index, name='home'),
    path('blogs/', blog_list, name='blog_list'),
    path('blogs/<slug:slug>/', blog_detail, name='blog_detail'),
    path('portfolio/', portfolio_list, name='portfolio_list'),
    path('portfolio/<int:id>/', portfolio_detail, name='portfolio_detail'),

]
