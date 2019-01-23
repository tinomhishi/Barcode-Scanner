from django.shortcuts import render

def home(request):
	return render(request, 'index.html' ,{})

def scan(request):
	return render(request, 'scan.html', {})

