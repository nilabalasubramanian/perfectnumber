from django.urls import path
from . import views
urlpatterns=[path('perfect/<int:n>',views.create,name='create'),
             path('lists/<int:a>$<int:b>',views.check,name='check')]
