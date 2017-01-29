#-----------------------------------------------------------------------
#	bihin アプリケーションのform
#
#	2016.09.xx	V0.01	Yoshimitsu.Nakazawa
#				Djangoの勉強のために作成。
#	YYYY.MM.DD	Vx.xx	XXXX
#				XXXXXXXXXXXXXXXXXXXXXXX
#
#-----------------------------------------------------------------------
#from django.forms import ModelForm
from django import forms
from bihin.models import Bihin, Userinfo, Display, Mouse, Keybord, Lease

# Create your views here.

#-----------------------------------------------------------------------
#	BihinForm：
#   備品登録/編集にて起動される.
#   Formを作成する.
#-----------------------------------------------------------------------
#class BihinForm(ModelForm):
class BihinForm(forms.ModelForm):
    """備品のフォーム"""
    class Meta:
        model = Bihin
        fields = (
            'bihin_no',
            'bihin_type',
            'bihin_shisan',
            'bihin_manufct',
            'bihin_os',
            'bihin_cpu',
            'bihin_hdd',
            'bihin_mem',
            'bihin_mediadrv',
            'bihin_ipaddr',
            'bihin_text',)


class UserinfoForm(forms.ModelForm):
    """使用者情報のフォーム"""
    class Meta:
        model = Userinfo
        fields = (
            'status',
            'user',
            'prj',
            'location',)


class DisplayForm(forms.ModelForm):
    """機器(Display)"""
    class Meta:
        model = Display
        fields = (
            'dispsize',
            'dispno',)


class MouseForm(forms.ModelForm):
    """機器(Mouse)"""
    class Meta:
        model = Mouse
        fields = (
            'mouseno',)


class KeybordForm(forms.ModelForm):
    """機器(Keybord)"""
    class Meta:
        model = Keybord
        fields = (
            'keybordno',)


class LeaseForm(forms.ModelForm):
    """リースのフォーム"""
    class Meta:
        model = Lease
        fields = (
            'lease_date',)



#    def clean_bihin_no(self):
#        # view.pyのPOST時に行っているis_validから呼び出される
#        # イメージとしては、関連チェックをここに記載する
#        # エラーメッセージは、各項目に紐付かない  全体で一つ持っているエラーメッセージ欄に格納される
#        # 今回の場合は、non_filed.errors
#        # 引数はself固定
#        # 返却値はチェック後のデータ(全項目)
#
#        # FORM項目取り出し
#        cleaned_data = super(BihinForm, self).clean()
#        bihin_no = cleaned_data.get('bihin_no')
#
#        # <<重複チェック>>
#        # 管理No.が既に登録されている場合はエラー
#        # 必須項目であれば、models.pyの該当項目に対し、unique=trueを指定すればよいが
#        # 任意項目である場合は、個別に重複チェックを実装する
#
#        # 件数取得(これだと、自レコードが含まれてしまうので、何らかの手立てが必要)
#        bihin_no_cnt = Bihin.objects.filter(bihin_no=bihin_no).count()
#        if bihin_no_cnt > 0:
#            raise forms.ValidationError(u'管理Noが重複しています')
#
#        return cleaned_data


