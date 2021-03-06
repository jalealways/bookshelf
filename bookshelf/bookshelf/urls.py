"""bookshelf URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.mytest.urls')),
    url(r'^back/', include('apps.back_books.urls')),
    url(r'^borrow/', include('apps.borrow_books.urls')),
    url(r'^weixin/', include('apps.weixin.urls')),
    url(r'^MP_verify_Hog03Y6CA7OmhcOk.txt', include('apps.mytest.urls')),
    url(r'^bookList/', include('apps.book_list.urls')),
    url(r'^user/', include('apps.register_login.urls')),
]
