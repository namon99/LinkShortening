from django.urls import path, re_path

from .views import MainPageView, RedirectFromShortToLongURLView

urlpatterns = [
    path('', MainPageView.as_view(), name='main-page'),
    re_path(r'^[a-zA-Z0-9]{6}/$', RedirectFromShortToLongURLView.as_view()),
]
