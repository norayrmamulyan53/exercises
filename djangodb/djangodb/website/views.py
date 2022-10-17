from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberForm
from django.contrib import messages


def index(request):
    params = {
        'all': Member.objects.all
    }
    return render(request, 'index.html', params)


def join(request):
    if request.method == 'POST':
        form = MemberForm(request.POST or None)
        if not form.is_valid():
            raise Exception(f'form is not valid {form.errors}')
        form.save()
        messages.success(request, 'Registration passed successfully')
        return redirect('index')
    else:
        return render(request, 'join.html', {})
