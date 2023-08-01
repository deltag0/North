from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import tic_tac_toe
# Create your views here.

def index(response):
	return render(response, "main/me.html", {})

def home(response):
	return render(response, "main/home.html", {})
	
def program(response):
	result = tic_tac_toe.main()
	return HttpResponse(f"Result: {result}")