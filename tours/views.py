from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views import View

from .data.data import * # Добавляем данные

class MainPageView(View):
    def get(self, request, *args, **kwargs):
        
        return render(request, 'tours/index.html', context =
            { 'title': title, 'subtitle': subtitle, 'description' : description, 'departures' : departures, 
            'tours' : tours } )
  
class DepartureView(View):
    def get(self, request, departure_id, *args, **kwargs):
        if departure_id not in departures:
            raise Http404
        
        departure_name = departures[departure_id]
        
        departure_tours = {}
        total_tours = 0
        min_price = 0
        max_price = 0
        min_nights = 0
        max_nights = 0
        for tour_key, tour_val in tours.items() :
#            print(tour_val['departure'])
            if tour_val['departure'] == departure_id :
                total_tours += 1
                if total_tours == 1 :
                    min_price = tour_val['price']
                    max_price = tour_val['price']
                    min_nights = tour_val['nights']
                    max_nights = tour_val['nights']
                else:
                    if min_price > tour_val['price']:
                        min_price = tour_val['price']
                    if max_price < tour_val['price']:
                        max_price = tour_val['price']
                    if min_nights > tour_val['nights']:
                        min_nights = tour_val['nights']
                    if max_nights < tour_val['nights']:
                        max_nights = tour_val['nights']
                departure_tours[tour_key] = tours[tour_key]
       
        return render(request, 'tours/departure.html', context = 
            { 'title': title, 'name': departure_name, 'departures' : departures, 'tours' : departure_tours, 
             'departure_active_key' : departure_id, 
             'departure_add_info': {'total_tours': total_tours, 
                                   'min_price': min_price, 'max_price': max_price,
                                   'min_nights': min_nights, 'max_nights': max_nights, } 
            } )
        
class TourView(View):
    def get(self, request, tour_id, *args, **kwargs):
        if tour_id not in tours:
            raise Http404

        cur_tour = tours[tour_id]
        departure_name = departures[cur_tour["departure"]]
        departure_active_key = cur_tour["departure"]
        
        return render(request, 'tours/tour.html', context = {'title': title, 'cur_tour': cur_tour, 'departure_name' : departure_name, 
                                                            'departures' : departures, 'departure_active_key' : departure_active_key, })