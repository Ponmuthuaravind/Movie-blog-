from django.shortcuts import render
from django.http import HttpResponse
from .forms import MovieForm,CommentForm
from .models import MovieModel,CommentsModel
from django.shortcuts import render, get_object_or_404
# Create your views here.

def AddMovieView(request):
    if request.method == 'POST' and request.FILES:
        form = MovieForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('movie added')
        else:
            return render(request,'add_movie.html',{'form':form})
    form = MovieForm()
    return render(request,'add_movie.html',{'form':form})




def homeview(request):
    data = MovieModel.objects.all()
    return render(request,'home.html',{'data':data})






def movie_detail(request, id):
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
        else:
            data = get_object_or_404(MovieModel, id=id)
            return render(request,'movie_detail.html', context)
    
    data = get_object_or_404(MovieModel, id=id)
    comment_form=CommentForm()
    Comment = CommentsModel.objects.filter(movie_id=id)
    context = {'data': data,'form':comment_form,'Comment':Comment}    
    return render(request,'movie_detail.html',context)
