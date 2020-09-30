from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:title>',views.title, name='title'),
    path('search', views.search, name='search'),
    path('create', views.create, name='create'),
    path('save',views.save, name='save'),
    path('editpage/<str:title>',views.editpage, name='edit'),
    path('editted/<str:title>',views.editted_saved,name='editted_saved'),
    path('random',views.random_page,name='random')
]
