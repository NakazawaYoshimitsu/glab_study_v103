from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    #return HttpResponse("GLab Top.")
    return render(request, 'top/top.html')

