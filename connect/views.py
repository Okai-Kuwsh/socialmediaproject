from django.shortcuts import render
from django.http import HttpResponse, QueryDict, HttpResponseBadRequest, JsonResponse, HttpResponseServerError, FileResponse
from .models import Interest, Profile, Member
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.db.models.functions import datetime


def getContext(request):
    return {
        "sitename": "Connect"
    }

@csrf_exempt
def signup(request):
    if request.method == "GET":
        context = getContext(request)
        interests = []
        for interest in Interest.objects.all():
            interests.append({
                "type": interest.type,
                "name": interest.name
            })
        return render(request, "connect/signup.html", context)
    elif request.method == "POST":
        print(request.POST)
        prof = Profile.objects.create(name=request.POST['profile[name]'],dob=datetime.datetime.strptime(request.POST['profile[dob]'], "%Y-%m-%d").date(),gender=request.POST["profile[gender]"])
        interests = []
        for interest in request.POST['profile[interests]']:
            interests.append(Interest.objects.get(name=interest))
        prof.interests = interests
        prof.save()
        mem = Member.objects.create(username=request.POST["username"])
        mem.set_password(request.POST["password"])
        mem.profile = prof
        mem.save()
        return HttpResponse()

@csrf_exempt
def login(request):
    if request.method == "GET":
        return render(request, "connect/login.html", getContext(request))
    elif request.method == "POST":
        try:
            user = Member.objects.get(username=request.POST["username"])
            if user.password == request.POST["password"]:
                request.session["username"] = request.POST["username"]
                prof = user.profile
                request.session["profile"] = prof
                return HttpResponse()
            else:
                return HttpResponseBadRequest("Authentication Failed")
        except Member.DoesNotExist:
            return HttpResponseBadRequest("Authentication Failed")


@csrf_exempt
def profile(request, id):
    if request.method == "GET":
        context = getContext(request)
        profile = Member.objects.get(id=id).profile
        context.profile = profile
        return render(request, "connect/profile.html", context)


@csrf_exempt
def userProfile(request):
    if request.method == "GET":
        context = getContext(request)
        context.profile = request.session["profile"]
        return render(request, "connect/profile.html", context)


@csrf_exempt
def home(request):
    if request.method == "GET":
        context = getContext(request)
        members = Member.objects.all()
        profiles = []
        for member in members:
            if member.profile != request.session["profile"]:
                profiles.append(member.profile)
        context.profiles = profiles
        return render(request, "connect/index.html", context)


