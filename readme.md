# RecruitR

## Goal
The goal of this app is to help the recruitment process for a company and to manage applicants.

## Quickstart

- pip install django, django-bower
- npm install bower
- pip install --upgrade google-api-python-client
- ./manage.py bower install

- python manage.py runserver

- open a new tab at localhost:8000/recruitr/home

- In a new terminal tab launch a server for checking the sent emails: 
python -m smtpd -n -c DebuggingServer localhost:1025

## Dependencies

- Django, Django-bower,bower,npm, jquery-datetimepicker,jquery, bootstrap, Google calendar api

## Requirements

HR representatives should be able to:
- Create some positions to be filled
- Assign skills to positions (marketing, javascript, ruby…)
- Upon receiving a candidate, the recruiter is going to create a candidate profile and match her/him with a the position she/he is applying for
- When the candidate is matched to a position, the recruiters matching the skills are suggested
- The recruiter can then select a datetime, which will create an event through the google calendar API and invite the suggested employee and the applicant

- The recruiter can select an available time slot for a given employee
- The list of potential matching recruiters could be smart, with a score based on:
  - Random, so that everybody participates
  - her/his skills (perfect match, better match, partial match)
  - her/his seniority (number of previously matched applicants)
- Notification system: send a mail to both recruiter and applicant, AngelList-style
- Applicant scorecard, to be filled by company members (HR rep filling the application and recruiters) with specific traits such as experience, dynamism, interest in the company. We could have some sort of radar-graph, with an average from every members

## Overview

The project mainly requires admin tasks therefore most of the work of this project is to customize the admin generated automatically by Django. Django is therefore a very good fit for such requirements.

If you are not familiar with the architecture of a Django project or the model view template please read one of the following : https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django (english) or https://openclassrooms.com/courses/developpez-votre-site-web-avec-le-framework-django (french)



## Database

The database schema is defined in models.py.

The main tables are Applicant, Position, Recruiter, Schedule, Skill, Match.

We have one to one links between :
- Applicant and Position, 
- Match and Recruiter, 
-Match and Schedule,
-Match and Applicant. 

We have one to many links between :
- Position and Skill 
- Recruiter and Skill

## Routing

There are  different urls :
-/recruitr/home
-/recruitr/applicants : links for adding applicants, and to the list of applicants
-/recruitr/match/id_position/id_applicant : page to match an applicant and a recruiter
-/recruitr/schedule/id_match/id_recruiter : page to add a schedule for an interview associated with a match
-/recrutir/position : List of all available positions
-/admin : Django admin, to administrate all the database

## Forms 

-RecruiterForm : Form with a selection of the recruiter (sorted in descending order of matching skills)
-ScheduleForm : Form for interview schedule selection with jquery-datetimepicker

## Admin.py

Custom methods to redirect to add matches after adding applicant.

## To do list

-Check if recruiter is available before adding the event (easy : custom validation of the form)
-Write tests
- - - -

_Quick links:_
- Google Calendar API quickstart: [Ruby Quickstart  |  Google Calendar API](https://developers.google.com/google-apps/calendar/quickstart/ruby)
- Create an event: [Create Events  |  Google Calendar API](https://developers.google.com/google-apps/calendar/create-events)
- Datetime picker example: [GitHub - xdan/datetimepicker: jQuery Plugin Date and Time Picker](https://github.com/xdan/datetimepicker)


