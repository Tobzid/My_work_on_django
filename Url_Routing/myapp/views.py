from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def post(request, pk):
    return render(request, 'post.html', {'pk': pk})

def counter(request):
    posts = [1, 2, 3, 4, 5, 'Tobzid', 'God']
    return render(request, 'counter.html', {'posts': posts})
    