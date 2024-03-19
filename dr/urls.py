
from django.urls import path
from . import views
urlpatterns = [
    path("drinks/",views.drink_list),
    path("drinks/<int:id>/",views.drink_details),
    path("drinks/search/",views.drink_search),
]