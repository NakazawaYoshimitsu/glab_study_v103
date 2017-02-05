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
from bihin.forms import BihinForm, UserinfoForm, DisplayForm, MouseForm, KeybordForm, LeaseForm

# Create your views here.

#-----------------------------------------------------------------------
#	bihin_top：
#   urls.py の index からここが起動される.
#   ここでは備品DBを取得し、bihin.htmlを動かす.
#-----------------------------------------------------------------------
@login_required
def bihin_top(request):
    #return HttpResponse("Bihin Top.")
    bihins = Bihin.objects.all().order_by('id')
    return render(request, 'bihin/bihin.html', {'bihins':bihins})

#-----------------------------------------------------------------------
#	bihin_edit：
#   urls.py の bihin_add/bihin_mod からここが起動される.
#   ここでは備品DBを取得し、bihin_edit.htmlを動かす.
#-----------------------------------------------------------------------
@login_required
def bihin_edit(request, bihin_id=None):
    #return HttpResponse("Bihin Edit.")

    """備品の登録・編集"""
    if bihin_id:
        print ( "bihin_edit id" )
        bihin = get_object_or_404(Bihin, pk=bihin_id)

        try:
            #userinfo = get_object_or_404(Userinfo, pk=bihin_id)
            userinfo = Userinfo.objects.get(pk=bihin_id)
        except Userinfo.DoesNotExist:
            userinfo = Userinfo()

        try:
            display = Display.objects.get(pk=bihin_id)
        except Display.DoesNotExist:
            display = Display()

        try:
            mouse = Mouse.objects.get(pk=bihin_id)
        except Mouse.DoesNotExist:
            mouse = Mouse()

        try:
            keybord = Keybord.objects.get(pk=bihin_id)
        except Keybord.DoesNotExist:
            keybord = Keybord()

        try:
            lease = Lease.objects.get(pk=bihin_id)
        except Lease.DoesNotExist:
            lease = Lease()

    else:
        print ( "bihin_edit new" )
        bihin = Bihin()
        userinfo = Userinfo()
        display = Display()
        mouse = Mouse()
        keybord = Keybord()
        lease = Lease()

    if request.method == 'POST':
        print ( "bihin_edit POST" )
        bihin_form = BihinForm(request.POST, instance=bihin)           # POST された request データからフォームを作成
        if bihin_form.is_valid():    # フォームのバリデーション
            display_form = DisplayForm(request.POST, instance=display)     # POST された request データからフォームを作成
            if display_form.is_valid():
                mouse_form = MouseForm(request.POST, instance=mouse)           # POST された request データからフォームを作成
                if mouse_form.is_valid():
                    keybord_form = KeybordForm(request.POST, instance=keybord)     # POST された request データからフォームを作成
                    if keybord_form.is_valid():
                        userinfo_form = UserinfoForm(request.POST, instance=userinfo)  # POST された request データからフォームを作成
                        if userinfo_form.is_valid():
                            lease_form = LeaseForm(request.POST, instance=lease)           # POST された request データからフォームを作成
                            if lease_form.is_valid():
                                bihin = bihin_form.save(commit=False)
                                bihin.save()

                                userinfo = userinfo_form.save(commit=False)
                                userinfo.save()

                                if display.dispno:
                                    display = display_form.save(commit=False)
                                    display.bihin = bihin
                                    display.save()

                                if mouse.mouseno:
                                    mouse = mouse_form.save(commit=False)
                                    mouse.bihin = bihin
                                    mouse.save()

                                if keybord.keybordno:
                                    keybord = keybord_form.save(commit=False)
                                    keybord.bihin = bihin
                                    keybord.save()

                                if lease.lease_date:
                                    lease = lease_form.save(commit=False)
                                    lease.bihin = bihin
                                    lease.save()

                                return redirect('bihin:bihin_top')

                        else:
                            lease_form = LeaseForm(instance=lease)

                    else:
                        userinfo_form = UserinfoForm(instance=userinfo)
                        lease_form = LeaseForm(instance=lease)

                else:
                    keybord_form = KeybordForm(instance=keybord)
                    userinfo_form = UserinfoForm(instance=userinfo)
                    lease_form = LeaseForm(instance=lease)

            else:
                userinfo_form = UserinfoForm(instance=userinfo)
                mouse_form = MouseForm(instance=mouse)
                keybord_form = KeybordForm(instance=keybord)
                lease_form = LeaseForm(instance=lease)
        else:
            userinfo_form = UserinfoForm(instance=userinfo)
            display_form = DisplayForm(instance=display)
            mouse_form = MouseForm(instance=mouse)
            keybord_form = KeybordForm(instance=keybord)
            lease_form = LeaseForm(instance=lease)

    else:    # GET の時
        print ( "bihin_edit get" )
        bihin_form = BihinForm(instance=bihin)
        userinfo_form = UserinfoForm(instance=userinfo)
        display_form = DisplayForm(instance=display)
        mouse_form = MouseForm(instance=mouse)
        keybord_form = KeybordForm(instance=keybord)
        lease_form = LeaseForm(instance=lease)

    d = {
        'bihin_form':bihin_form,
        'userinfo_form':userinfo_form,
        'display_form':display_form,
        'mouse_form':mouse_form,
        'keybord_form':keybord_form,
        'lease_form':lease_form,
        'bihin_id':bihin_id,
    }

    return render(request, 'bihin/bihin_edit.html', d)

#-----------------------------------------------------------------------
#	bihin_del：
#   urls.py の bihin_del からここが起動される.
#   ここでは備品DBを削除し、bihin.htmlに遷移する.
#-----------------------------------------------------------------------
@login_required
def bihin_del(request, bihin_id=None):

    print ( u"Debug:bihin_del(bihin_id)", bihin_id )

    if bihin_id:

        bihin = get_object_or_404(Bihin, pk=bihin_id)

        try:
            userinfo = Userinfo.objects.get(pk=bihin_id)
        except Userinfo.DoesNotExist:
            print ( "userinfo obj none" )
        else:
            userinfo.delete()
            print ( "userinfo obj del" )

        try:
            display = Display.objects.get(pk=bihin_id)
        except Display.DoesNotExist:
            print ( "display obj none" )
        else:
            display.delete()
            print ( "display obj del" )

        try:
            mouse = Mouse.objects.get(pk=bihin_id)
        except Mouse.DoesNotExist:
            print ( "mouse obj none" )
        else:
            mouse.delete()
            print ( "mouse obj del" )

        try:
            keybord = Keybord.objects.get(pk=bihin_id)
        except Keybord.DoesNotExist:
            print ( "keybord obj none" )
        else:
            keybord.delete()
            print ( "keybord obj del" )

        try:
            lease = Lease.objects.get(pk=bihin_id)
        except Lease.DoesNotExist:
            print ( "lease obj none" )
        else:
            lease.delete()
            print ( "lease obj del" )

        bihin.delete()

    bihins = Bihin.objects.all().order_by('id')
    return render(request, 'bihin/bihin.html', {'bihins':bihins})



