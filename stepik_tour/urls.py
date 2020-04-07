from django.contrib import admin
from django.urls import path
from tours.views import MainPageView, DepartureView, TourView

urlpatterns = [
    path("", MainPageView.as_view(), name='main'),
    path("departure/<str:departure_id>/", DepartureView.as_view(), name='departure'),
    path("tour/<int:tour_id>/", TourView.as_view(), name='tour'),
    
    path('admin/', admin.site.urls),
]
