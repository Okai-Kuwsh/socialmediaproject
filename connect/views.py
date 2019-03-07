from django.shortcuts import render
from django.http import HttpResponse, QueryDict, HttpResponseBadRequest, JsonResponse, HttpResponseServerError, FileResponse
from .models import Interest, Profile, Member
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from datetime import date


def getContext(request):
    return {
        sitename: "Connect"
    }

def signup(request):
    if request.method == "GET":
        render(request, "./templates/signup.html", getContext(request))
    elif request.method == "POST":
        prof = Profile.objects.create(dob=datetime.datetime.strptime(request["POST"]['profile[dob]'][0], "%Y-%m-%d").date(),gender=request["POST"]["profile[gender"])
        prof.save()
        mem = Member...
        mem.profile = prof
        mem.save()
        return HttpResponse()