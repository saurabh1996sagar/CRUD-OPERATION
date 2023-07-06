from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('add-new', views.add, name='new'),
    path('posts', views.posts),
    path('post/<str:pk>', views.post),
    path('update/<str:pk>', views.update),
    path('changedata/<str:pk>', views.changedata),
    path('delete/<str:pk>', views.delete)
]
