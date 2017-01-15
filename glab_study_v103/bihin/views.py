#-----------------------------------------------------------------------
#	bihin アプリケーションのviews
#
#	2016.09.xx	V0.01	Yoshimitsu.Nakazawa
#				Djangoの勉強のために作成。
#	YYYY.MM.DD	Vx.xx	XXXX
#				XXXXXXXXXXXXXXXXXXXXXXX
#
#-----------------------------------------------------------------------
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from bihin.models import Bihin, Userinfo, Display, Mouse, Keybord, Lease
#from bihin.forms import BihinForm

# Create your views here.

#-----------------------------------------------------------------------
#	bihin_top：
#   urls.py の index からここが起動される.
#   ここでは備品DBを取得し、bihin.htmlを動かす.
#-----------------------------------------------------------------------
#@login_required
def bihin_top(request):
#    return HttpResponse("Bihin Top.")
    bihins = Bihin.objects.all().order_by('id')
    userinfos = Userinfo.objects.all().order_by('id')
#    return render(request, 'bihin/bihin.html', {'bihins':bihins, 'user':request.user})
    return render(request, 'bihin/bihin.html', {'bihins':bihins, 'userinfos':userinfos})

#-----------------------------------------------------------------------
#	bihin_edit：
#   urls.py の index からここが起動される.
#   ここでは備品DBを取得し、bihin.htmlを動かす.
#-----------------------------------------------------------------------
#@login_required
def bihin_edit(request):
    return HttpResponse("Bihin Edit.")
#    bihins = Bihin2.objects.all().order_by('id')
#    return render(request, 'bihin/bihin2.html', {'bihins':bihins, 'user':request.user})

