from django.contrib import admin
from django.urls import path
import portfolio.views

urlpatterns = [
    path('home', portfolio.views.home, name='home'),
    path('post/<int:post_id>/', portfolio.views.detail, name='detail'),
    path('post/new/', portfolio.views.post_new, name='new'),
    path('post/<int:post_id>/edit',portfolio.views.post_edit, name='edit'),
    path('post/<int:post_id>/delete',portfolio.views.post_delete, name='delete'),



]
