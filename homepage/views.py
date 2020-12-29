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


def experience(request):
    try:
        experience = Experience.objects.get(id=1)
    except Experience.DoesNotExist:
        raise HttpResponse('homepage/404.html')
    return render(request, 'homepage/experience.html', {'experience': experience})


def project(request):
    project = Project.objects.get(id=1)
    return render(request, 'homepage/projects.html', {'project': project})


def notFound(request):
    return render(request, '404.html')


def skill(request):
    skill = Skill.objects.order_by('skill_val')[:]

    return render(request, 'homepage/skill.html', {'skill': skill})
