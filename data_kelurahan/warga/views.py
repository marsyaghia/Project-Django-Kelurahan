from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Warga, Pengaduan   

# Create your views here.
class WargaListView(ListView):
    model = Warga

class WargaDetailView(DetailView):
    model = Warga

class PengaduanListView(ListView):
    model = Pengaduan
    temolate_name = 'pengaduan_list.html'