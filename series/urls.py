"""series URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers
from profiles import views as profile_views
from tvseries import views as tvseries_views
from rest_framework.urlpatterns import format_suffix_patterns


router = routers.DefaultRouter()
router.register(r'users', profile_views.UserViewSet)
router.register(r'series', tvseries_views.SerieViewSet)
router.register(r'follow', tvseries_views.FollowSeries)
#router.register(r'add', tvseries_views.Addseries)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^serie/$',tvseries_views.SerieViewSet),
    url(r'^series/relations/(?P<pk>[0-9]+)/$',tvseries_views.SerieViewSet)
]

urlpatterns = router.urls