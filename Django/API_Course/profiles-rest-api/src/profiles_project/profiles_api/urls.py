from django.conf.urls import url
from django.conf.urls import include                                            # Include import

from rest_framework.routers import DefaultRouter                                # Default Router class

from . import views                                                             # import views module

router = DefaultRouter()                                                        # Create a router variable and assign it to a Default Router object
router.register('hello-viewset', views.HelloViewSet, base_name="hello-viewset") # Register a new URL with our router that points to 'hello-viewset'
                                                                                # 1st param: name of our APIV - 'hello-viewset'
                                                                                # 2nd param: name of the viewset that we want to register (function on views.py) - views.HelloViewSet
                                                                                # 3rd param: base name - "hello-viewset"

router.register('profile', views.UserProfileViewSet)                            # Base_name doesnt need to be specified when a model is given on the view set

router.register('login', views.LoginViewSet, base_name="login")

urlpatterns = [
    url(r'^hello-view/', views.HelloAPIView.as_view()),                         # It maps to our api view and it must be returned as a view object
    url(r'', include(router.urls))                                              # Assign a blank string and include a router.urls; this way the router will create a url for us
]
