from django.shortcuts import redirect, render
from importlib_resources import contents
from .models import Contact, Feedback
from django.contrib import messages
import smtplib
from datetime import datetime
from decouple import config

# Validators
def validate_proid(value):
    key = [char for char in value]
    if key[0] != 'P' or key[1] != 'R':
        return 1



# Processing Functions
def sendnote(nameemail,**kwargs):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        mymail = config('EMAIL_ADDR')
        password = config('EMAIL_PASS')

        connection.starttls()

        connection.login(user=mymail, password=password)

        if nameemail=="contact":
            connection.sendmail(from_addr=mymail, to_addrs="agraradev2218@gmail.com",
                                msg=f"Subject: New Project Request\n\n Client Name: {kwargs['name']}\n\n Client Contact: {kwargs['contact']}\n\n Project Name: {kwargs['proname']}\n\n Project Description: {kwargs['prodetails']}\n\n Project Quotation: {kwargs['proquote']}\n\n")
        if nameemail=="feedback":
            connection.sendmail(from_addr=mymail, to_addrs="agraradev2218@gmail.com",
                                msg=f"Subject: New Project Feedback\n\n Project ID: {kwargs['proid']}\n\n Project Name: {kwargs['proname']}\n\n Project Date: {kwargs['prodate']}\n\n Project Rating: {kwargs['prorate']}\n\n Project Exp Description: {kwargs['prodesp']}\n\n Project Suggestions: {kwargs['prosug']}")

# Create your views here.
def Homepage(request):
    return render(request, 'devansh/main.html')

def Contactpage(request):
    if request.method == 'POST':
        name = request.POST['contact-name']
        contact = request.POST['contact-email']
        proname = request.POST['contact-project-name']
        prodetails = request.POST['contact-project-desp']
        proquote = request.POST['contact-project-quote']

        if len(name) == 0 or len(contact) == 0:
            messages.error(request, "Fill out the Required Fields")

        if len(name) != 0 and len(contact) != 0:
            new_contact = Contact(firstname=name, phoneno=contact, proname=proname, prodesp=prodetails, proquote=proquote)
            new_contact.save()
            messages.success(request, "Project Request Submitted Successfully")
            sendnote(nameemail="contact", name=name, contact=contact, proname=proname, prodetails=prodetails, proquote=proquote)
            return redirect('/contact/')

    else:
        return render(request, 'devansh/contact.html')

    return render(request, 'devansh/contact.html')

def Feedbackpage(request):
    date_str = str(datetime.now().date())
    date = str(datetime.strptime(date_str, "%Y-%m-%d"))
    date_today = {'date': date.split(" ")[0]}
    if request.method == 'POST':
        proid = request.POST['project-id']
        proname = request.POST['project-name']
        prodate = request.POST['project-date']
        prorate = request.POST['project-rate']
        prodesp = request.POST['project-desp']
        prosug = request.POST['project-suggest']

        if len(proname) == 0 or len(proid) ==0:
            messages.error(request, "Fill out the Required Fields!")

        if validate_proid(proid) == 1:
            messages.error(request, "Invalid Project ID!")

        if len(proname) != 0 and validate_proid(proid) != 1:
            new_feedback = Feedback(proid=proid, proname=proname, prodate=prodate, prorate = prorate, proexp=prodesp, prosuggest=prosug)
            new_feedback.save()
            messages.success(request, "Feedback Submitted Successfully!")
            sendnote(nameemail="feedback", proid=proid, proname=proname, prodate=prodate, prorate=prorate, prodesp=prodesp, prosug=prosug)
            return redirect('/feedback/', context=date_today)

    return render(request, 'devansh/feedback.html', context=date_today)

def Aboutpage(request):
    return render(request, 'devansh/aboutme.html') 

def error_400(request, exception):
    return render(request, 'devansh/404.html')

def error_404(request, exception):
    return render(request, 'devansh/404.html')

def error_500(request):
    return render(request, 'devansh/404.html')