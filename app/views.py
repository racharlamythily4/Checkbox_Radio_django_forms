from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def stud(request):
    ESFO=Student()
    d={'ESFO':ESFO}
    if request.method=='POST':
        DSFO=Student(request.POST)
        if DSFO.is_valid():
            return HttpResponse('Data is Inserted')
    return render(request,'stud.html',d)