from django.urls import path, include
from ebuilder.core.views import home, index


urlpatterns = [
    path('', index, name='index'),
    path('home', home, name='home'),

]
