from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.conf import settings
import csv

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    bus_stations = []
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bus_stations.append({
                'Name': row['Name'],
                'Street': row['Street'],
                'District': row['District']
            })

    page_number = request.GET.get('page', 1)
    paginator = Paginator(bus_stations, 10)  # 10 остановок на страницу
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page
    }
    return render(request, 'stations/index.html', context)
