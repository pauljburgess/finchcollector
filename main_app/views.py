from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Place
from .forms import SightingForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches' : finches
    })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    id_list = finch.places.all().values_list('id')
    places_finches_havent_been_seen = Place.objects.exclude(id__in=id_list)
    sighting_form = SightingForm()
    return render(request, 'finches/detail.html', {
        'finch' : finch , 'sighting_form' : sighting_form, 'places' : places_finches_havent_been_seen
    })

def add_sighting(request, finch_id):
    form = SightingForm(request.POST)
    if form.is_valid():
        new_sighting = form.save(commit=False)
        new_sighting.finch_id = finch_id
        new_sighting.save()
    return redirect('detail', finch_id=finch_id)

def assoc_place(request, finch_id, place_id):
    Finch.objects.get(id=finch_id).places.add(place_id)
    return redirect('detail', finch_id=finch_id)


def remove_place(request, finch_id, place_id):
    print(finch_id)
    Finch.objects.get(id=finch_id).places.remove(place_id)
    return redirect('detail', finch_id=finch_id)




class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    success_url = '/finches'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['subtype' , 'description', 'size', 'range']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'

class PlaceList(ListView):
    model = Place

class PlaceCreate(CreateView):
    model = Place
    fields = '__all__'
    success_url = '/places'
