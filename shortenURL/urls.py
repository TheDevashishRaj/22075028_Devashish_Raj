from django.urls import path
from . import views

urlpatterns = [
    path("", views.shorten_url, name='shorten_url'),
    path('shorten/', views.shorten_url, name='shorten_url'),
    path('list/', views.display_short_urls, name='shorten_url_list'),
    path('<str:code>/', views.redirect_to_original, name='redirect_to_original'),
]