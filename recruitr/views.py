from django.shortcuts import render, get_object_or_404,redirect
from .models import Position,Recruiter,Match,Applicant,Schedule
from .forms import RecruiterForm,ScheduleForm
from django.views.generic import ListView
import sys


from google_calendar.event_adder import create_event,get_credentials
# Create your views here.

class positions(ListView):
	# List of all positions
    model = Position
    context_object_name = "positions"
    template_name = "recruitr/position.html"

def applicants(request):
	# List of all applicants

	#location to update the navbar
	loc="applicants"

	return render(request, 'recruitr/applicants.html', locals())

def home(request):
	loc="home"
	#Get credentials for adding events to the google calendar
	get_credentials()
	return render(request, 'recruitr/home.html', locals())

def new_match(request,id_position,id_applicant):
	# Match a recruiter with an applicant
	position = get_object_or_404(Position,id=id_position)
	skills = position.skill.all()

	#Get recruiter matching the skills of the position
	rcs = Recruiter.objects.filter(skill__in=  skills).distinct()

	#If non is available just take the 10 first ones
	if not rcs:
		rcs = Recruiter.objects.filter()[:10]

	#Sort them by descending number of matching skills
	rcs =sorted(rcs, key= lambda i: -(i.skill.all() &skills).count())

	#Format the available choices of recruiters (id_recruiter,"Name of the recruiter matching skills")
	rcs = [(rc.id,str(rc)+" \ Matching skills: "+" / ".join([r.name for r in rc.skill.all()&skills])) for rc in rcs]
	
	skills =[s.name for s in skills]
	

	form = RecruiterForm(request.POST or None,choices=rcs)
	if form.is_valid():

		#If the form is valid create the match and redirect to create the asssociated Schedule

		id_recruiter = form.cleaned_data['id_recruiter']
		recruiter = get_object_or_404(Recruiter,id=id_recruiter)
		applicant = get_object_or_404(Applicant,id=id_applicant)
		m =Match(recruiter=recruiter,applicant=applicant)
		m.save()
		url = '/recruitr/schedule/'+str(m.id)+'/'+str(m.recruiter.id)
		return redirect(url)
	else :
		print(form.errors)
	return render(request, 'recruitr/new_match.html', locals())

def new_schedule(request,id_match,id_recruiter):
	#Create a Schedule associated with a match

	m = Match.objects.get(id=id_match)
	success =False
	form = ScheduleForm(request.POST or None)
	if form.is_valid():
		# Create the Schedule
		datetime_begin = form.cleaned_data['datetime_begin']
		datetime_end = form.cleaned_data['datetime_end']
		m = get_object_or_404(Match,id=id_match)
		s =Schedule(name ="Interview : " +str(m.applicant)+" / "+str(m.recruiter),start=datetime_begin,end=datetime_end)
		s.save()

		# Associate it with the match
		m.schedule=s
		m.save() 

		#create the google calendar event
		start =  datetime_begin.isoformat("T")
		end =   datetime_end.isoformat("T")
		link = create_event(start,end,m.recruiter.email,m.applicant.email,"Interview : " +str(m.applicant)+" / "+str(m.recruiter),"A chance to discover Awesome&Cie")
		success =True
	else :
		print(form.errors)
	return render(request, 'recruitr/new_schedule.html', locals())