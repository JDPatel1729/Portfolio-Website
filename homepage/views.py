from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from .models import Experience, Project, Skill, Admin, About


def homepage(request):
    about = About.objects.get(pk=1)
    admin = Admin.objects.get(pk=1)
    skills = Skill.objects.order_by('skill_val')[::-1]
    experiences = Experience.objects.all()[:]
    project = Project.objects.all()[:]
    content = {'admin': admin,
               'about': about,
               'skills': skills,
               'experience': experiences,
               'project': project,
               }
    return render(request, 'homepage/homepage.html', content)
