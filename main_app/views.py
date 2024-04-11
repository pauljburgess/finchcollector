from django.shortcuts import render

finches = [
  {'name': 'American Goldfinch', 'subtype': 'goldfinch', 'description': 'yellow with black wings', 'size': 'small'},
  {'name': 'Rose-Breasted Grosbeak', 'subtype': 'grosbeak', 'description': 'black back with a dark pink breast', 'size': 'large'},
]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches' : finches
    })