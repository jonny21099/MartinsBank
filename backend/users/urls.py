from django.urls import include, path, re_path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'users', views.UserView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
