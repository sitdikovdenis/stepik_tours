# from django.conf import settings
from django.shortcuts import render
from django.views import View
# from django.http import HttpResponse, Http404
# from django.views.generic import ListView


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'tours/index.html', context={}
        )


class DepartureView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'tours/departure.html', context={}
        )


class TourView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'tours/tour.html', context={}
        )
