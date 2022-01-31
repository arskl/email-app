from django.shortcuts import render, redirect
from django.template import Context
from datetime import datetime
from .models import *
from .forms import *

# Create your views here.

def main(request):
    form = EmailForm()
    if request.method =='POST':
        form = EmailForm(request.POST)
        new_form = form.save(commit=False)
        if Email.objects.filter(email_field = new_form).exists():
            new_form = Email(email_field=new_form, state_field=True, date_field=last_email.date_field)
            new_form.save()
        else:
            form.save()

        return redirect('/')

    if len(Email.objects.all()) < 1:
        set_temp_value = Email(email_field="Записи відсутні", state_field=True)
        set_temp_value.save()
    else:
        temp = Email.objects.filter(email_field="Записи відсутні")
        temp.delete()

    data = Email.objects.latest("date_field")
    context = {'data': data, 'form': form}
    return render(request, 'dashboard/main.html', context)

def email_list(request):
    emails = Email.objects.all().distinct()
    print(type(emails))

    context = {'emails':emails}
    return render(request, 'dashboard/email_list.html', context)
