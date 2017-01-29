from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    contexts = {
        'user': request.user,
    }
    #return render(request, 'top/top.html', contexts)
    return HttpResponseRedirect( "top/top.html" )

