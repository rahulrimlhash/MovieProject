from django.http import HttpResponse
from django.shortcuts import render, redirect
#from .models import movie
from movieapp.models import movie
from .forms import MovieForm
# Create your views here.

def index(request):
    result = movie.objects.all()
    context = {
        'movie_list': result
    }
    return render(request,'index.html',context)

def detail(request,movie_id):

    result = movie.objects.get(id=movie_id)

    return render(request,'detail.html',{'result': result})



def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name',)
        description = request.POST.get('description', )
        year = request.POST.get('year', )
        image = request.FILES['image']
        result = movie(name=name,description=description,year=year,image=image)
        result.save()


    return render(request,'add.html')

def update(request, id):
    Movie = movie.objects.get(id=id)

    form = MovieForm(request.POST or None,request.FILES,instance=Movie)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'Movie':Movie})

def delete(request,id):

    if request.method == 'POST':
        Movie = movie.objects.get(id=id)
        Movie.delete()
        return redirect('/')
    return render(request,'delete.html')
