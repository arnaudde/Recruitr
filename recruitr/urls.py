from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^home$',views.home, name="home"),
    url(r'^match/(\d+)/(\d+)$',views.new_match,name="match"),
    url(r'^schedule/(\d+)/(\d+)$',views.new_schedule,name="schedule"),   
    url(r'^positions$',views.positions.as_view(),name="positions"),
    url(r'^applicants$',views.applicants,name="applicants")
]