from django.shortcuts import render

# Create your views here.
def hot(request):
   return render(request,"hot.html")

def spunk(request):
	return render(request, 'pink.html')

def one(request):
	return render(request, 'lays/next.html')

def hh(request):
	return render(request, 'lays/help.html')

def suc(request):
	return render(request, 'suc.html')

