from django.urls import path
from .views import PengaduanListView, WargaListView, WargaDetailView
from .views import WargaCreateView, PengaduanCreateView 
urlpatterns = [
    path('', WargaListView.as_view(), name='warga-list'),
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'),
    path('<int:pk>/', WargaDetailView.as_view(),name='warga-detail'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan_list'),
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan_tambah'),
]
