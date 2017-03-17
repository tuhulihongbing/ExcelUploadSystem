"""evalidator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from loadfile import views as loadfile_view
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',loadfile_view.treat),
    url(r'^Reports/Pages/Folder$',loadfile_view.folder, name='folder'),
    url(r'^Reports/Pages/File$',loadfile_view.file, name='file'),
    url(r'^Reports/Pages/Upload$',loadfile_view.upload, name='upload'),
    # url(r'^Reports/Pages/Folder$',loadfile_view.disk, name='folder'),
]
