from django.shortcuts import render
def profileview(req):
    return render(req,'spproapp/profile(sp).html')
def profileaboutview(req):
    return render(req,'spproapp/profile(sp)_about.html')
def profilecontactview(req):
    return render(req,'spproapp/profile(sp)_contact.html')
def profileprojectsview(req):
    return render(req,'spproapp/profile(sp)_projects.html')
def profileresumeview(req):
    return render(req,'spproapp/profile(sp)_resume.html')
