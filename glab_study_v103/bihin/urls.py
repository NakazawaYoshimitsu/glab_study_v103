#-----------------------------------------------------------------------
#	bihin アプリケーションのurls
#
#	2016.09.xx	V0.01	Yoshimitsu.Nakazawa
#				Djangoの勉強のために作成。
#	YYYY.MM.DD	Vx.xx	XXXX
#				XXXXXXXXXXXXXXXXXXXXXXX
#
#-----------------------------------------------------------------------
from django.conf.urls import url
from bihin import views


#-----------------------------------------------------------------------
#	bihinアプリケーションのurlと処理を指定
#-----------------------------------------------------------------------
urlpatterns = [
    url(r'^$', views.bihin_top, name='bihin_top'),								# /bihin		:備品一覧(Top)
    url(r'^add/$', views.bihin_edit, name='bihin_add'),							# /bihin/add	:登録
    url(r'^mod/(?P<bihin_id>\d+)/$', views.bihin_edit, name='bihin_mod'),		# /bihin/mod	:編集
]

