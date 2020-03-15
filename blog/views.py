from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView
# Create your views here.
#def index(request):
    #return render(request, 'base.html')

class HomePageView(ListView):
    model = Article
    template_name = 'home.html'
   
    

class PostDetailView(DetailView):
    model = Article
    template_name = 'post_detail.html'
    slug_field = 'slug'

def AboutPageView(request):
    return render(request,'about.html')

def ContactPageView(request):
    return render(request,'contact.html')

