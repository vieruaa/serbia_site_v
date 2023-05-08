from django.conf.urls.static import static
from django.urls import path

from app import settings
from .views import main_page, page_numb, each_house

urlpatterns = [
    path('', main_page),
    path('ns_houses/<int:page_n_s>/<int:page_n_e>', page_numb),
    path('ns_houses/house_with_num_<int:qwerty>', each_house),
]
