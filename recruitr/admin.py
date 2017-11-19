from django.contrib import admin
from .models import Applicant,Position,Schedule,Recruiter,Skill,Match
# Register your models here.
from django.shortcuts import redirect

admin.site.register(Position)
admin.site.register(Schedule)
admin.site.register(Recruiter)
admin.site.register(Skill)
admin.site.register(Match)

class ApplicantAdmin(admin.ModelAdmin):
	def response_add(self, request, obj, post_url_continue=None):

		url = '/recruitr/match/'+str(obj.position.id)+'/'+str(obj.id)
		return redirect(url)
	def response_change(self, request, obj, post_url_continue=None):

		url = '/recruitr/match/'+str(obj.position.id)+'/'+str(obj.id)
		return redirect(url)

admin.site.register(Applicant,ApplicantAdmin)