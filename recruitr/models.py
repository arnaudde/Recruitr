from django.db import models
from django.core.mail import send_mail
# Create your models here.
#Skills, positions,candidate,recruitr recruiter, schedules

CHOICES = [(i,i) for i in range(11)]

class Applicant(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=250)
	experience =models.IntegerField(choices=CHOICES,blank=True,null=True)
	dynamism = models.IntegerField(choices=CHOICES,blank=True,null=True)
	interest = models.IntegerField(choices=CHOICES,blank=True,null=True)
	position = models.ForeignKey('Position')
	def __str__(self):
		return """{} {}""".format(self.first_name,self.last_name)
class Position(models.Model):
	name = models.CharField(max_length=100)
	skill = models.ManyToManyField('Skill')
	def __str__(self):
		return self.name
class Recruiter(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=250)
	skill = models.ManyToManyField('Skill')
	def __str__(self):
		return """{} {}""".format(self.first_name,self.last_name)
class Schedule(models.Model):
	name = models.CharField(max_length=100)
	start = models.DateTimeField()
	end = models.DateTimeField()
	def __str__(self):
		return self.name
class Skill(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name
class Match(models.Model):
	recruiter = models.ForeignKey('Recruiter')
	applicant = models.ForeignKey('Applicant')
	schedule = models.ForeignKey('Schedule',null=True,blank=True)
	def __str__(self):
		return """ Match between {} {} and {} {}""".format(self.recruiter.first_name,self.recruiter.last_name,self.applicant.first_name,self.applicant.last_name)
	def save(self, *args, **kwargs):
		super(Match, self).save()
		if self.schedule :
			send_mail(
			    'New match for the position : '+self.applicant.position.name+' at Awesome&Cie',
			    'Dear Applicant, you are invited for an interview with '+str(self.recruiter)+' from '+str(self.schedule.start)+' to '+str(self.schedule.end),
			    self.recruiter.email,
			    [self.applicant.email],
			    fail_silently=False,
			)
			send_mail(
			    'Reminder match for the position : '+self.applicant.position.name+' at Awesome&Cie',
			    'Dear Recruiter, you have just been matched  for an interview with '+str(self.recruiter)+' from '+str(self.schedule.start)+' to '+str(self.schedule.end),
			    self.recruiter.email,
			    [self.recruiter.email],
			    fail_silently=False,
			)