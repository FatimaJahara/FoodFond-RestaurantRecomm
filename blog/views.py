from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{
		'author' : '',
		'title' : 'Welcome to our Restaurant Recommendation System'
	}
]

def home(request):
	context = {
	'posts' : posts
	}
	return render(request, 'blog/home.html',context)

def about(request):
	return render(request, 'blog/about.html',{'title':'About'})
