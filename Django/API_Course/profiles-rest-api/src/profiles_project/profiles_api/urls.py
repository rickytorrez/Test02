from django.conf.urls import url
from . import views                                                             # import views module

urlpatterns = [
    url(r'^hello-view/', views.HelloAPIView.as_view()),                         # It maps to our api view and it must be returned as a view object
]
