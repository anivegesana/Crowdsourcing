"""csgame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from users.views import player, home, gamep, images
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('admin/users/experiment', player.downloadExperiment),
    path('', home.home, name='home'),

    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/signup/', home.SignUpView.as_view(), name='signup'),
    path('accounts/signup/player/', player.PlayerSignUpView.as_view(), name='player_signup'),
    # path('accounts/signup/requester/', requester.RequesterSignUpView.as_view(), name='requester_signup'),
    # path('uploads/', upload.ZipfileCreateView.as_view(), name='test_upload')

    url(r'^profile/$', views.profile, name='profile'),
    url(r'^over/$', views.over, name='over'),
    url(r'^about/$', views.about, name='about'),
    url(r'^stop/$', views.stop, name='stop'),
    url(r'^feedback/$', views.feedback, name='feedback'),

    # url(r'^phase01/$', gamep.phase01, name='phase01'),
    url(r'^phase01a/$', gamep.phase01a, name='phase01a'),
    url(r'^phase01b/$', gamep.phase01b, name='phase01b'),
    url(r'^phase02/$', gamep.phase02, name='phase02'),
    url(r'^phase03/$', gamep.phase03, name='phase03'),

    url(r'^images/(.+)/$', images.main, name='images'),
    url(r'^images/(.+)/pane$', images.pane, name='images2'),

    url(r'^mturk/externalSubmit/$', views.adminSubmit, name='adminSubmit'),
]

handler404 = 'csgame.views.handler404'
handler500 = 'csgame.views.handler500'
