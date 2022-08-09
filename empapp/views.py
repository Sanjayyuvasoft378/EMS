from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def student_info(request):
    return render(request, 'home.html')

def add_emp(request):
    print
    return render(request, 'addemp.html')
