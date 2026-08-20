from about.models import about
from django.http import HttpResponse
from django.shortcuts import render
from home.models import home, socialmedia
from about.models import about, informati
from service.models import service
from skill.models import count,skil
from resume.models import Education,Experience,summary
from contact.models import contact
from form.models import form
data={}
def homes(request):
    homedata=home.objects.all()
    sociallink=socialmedia.objects.all()
    aboutdata=about.objects.all()
    servicedata=service.objects.all()
    infomative=informati.objects.all()
    counts=count.objects.all()
    skill=skil.objects.all()
    education=Education.objects.all()
    experience=Experience.objects.all()
    contactdata=contact.objects.all()
    summar=summary.objects.all()


    data={'homedata':homedata,
        'social':sociallink,
        'about':aboutdata,
        'informative':infomative,
        'service':servicedata,
        'counts':counts,
        'skill':skill,
        'education':education,
        'experience':experience,
        'contactdata':contactdata,
        'summary':summar
        }
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        fo=form(name=name,email=email,subject=subject,message=message)
        fo.save()

    return render(request,"index.html",data)

