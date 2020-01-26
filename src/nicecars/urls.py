"""nicecars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from cars.views import (
    index,
    category_shop, 
    viewcar_detail, 
    filter_page, 
    carlist_page,
    sidebar,
    search,
    viewcar_detail2,
    sidebar_detail,
    createview,
    updateview,
    deleteview
)

urlpatterns = [
    path('', index),
    path('category/', category_shop, name='category'),
    path('category/<int:id>/', viewcar_detail2, name='viewcar_detail2'),
    path('category/<str:make>/', carlist_page, name='view-list'),
    path('category/<str:make>/<int:id>/', viewcar_detail, name='view-list2'),
    path('search/', search, name='search'),
    path('sidebar/', sidebar, name='sidebar'),
    path('create/', createview, name='create'),
    path('category/<int:id>/update/', updateview, name='update'),
    path('category/<int:id>/delete/', deleteview, name='delete'),
    path('sidebar/<int:id>/', sidebar_detail, name='sidebar_detail'),
    path('filter/', filter_page, name='filter-list'),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)