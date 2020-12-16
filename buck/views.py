from django.db.models import Q
from django.shortcuts import render
from .models import Upload, Sign, Login
from .sign import Signin
from .loginP import LoginPage
from .upload import FileUpload


# Create your views here.
def enter(request):
    return render(request, 'Enter.html')


def logger(request):
    form = LoginPage(request.POST, request.FILES)
    if request.method == 'POST':
        form = LoginPage(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            form.save()

    form = LoginPage
    info = Sign.objects.all()
    context = {'form': form, 'info': info}
    return render(request, 'Login.html', context)


def signer(request):
    form = Signin(request.POST, request.FILES)
    if request.method == 'POST':
        form = Signin(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            pass

    forms = Signin
    info = Sign.objects.all()
    context = {'form': forms, "info": info}
    return render(request,  'Sign.html', context)


def uploader(request):
    form = FileUpload(request.POST, request.FILES)
    if request.method == 'POST':
        form = FileUpload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            pass

    form = FileUpload
    info = Sign.objects.all()
    context = {'form': form, "info": info}
    return render(request, 'upload.html', context)


def main(request):
    qs = Upload.objects.all()
    #  title_contains = request.GET.get('rogers')
    #  print(title_contains)

    #  if title_contains != '' and title_contains is not None:
    #      qs = qs.filter(item__icontains=title_contains)
        #  else:
        #  qs = qs.filter(Q(item__icontains=title_contains) | Q(Country__icontains=title_contains) | Q(State__icontains=title_contains)).distinct()
    #  info = Sign.objects.all()
    #  context = {
    #      'form': qs,
    #      'info': info
    #  }
    #  qs = Upload.objects.all()

    srch = request.GET.get('rogers')
    print(srch)

    if srch != '' and srch is not None:
        qs = qs.filter(Q(item__icontains=srch) | Q(Country__icontains=srch) | Q(State__icontains=srch)).distinct()
        #qs = qs.filter(item__icontains=srch)

    info = Sign.objects.all()
    context = {
        'form': qs,
        "info": info
    }
    return render(request, 'main.html', context)


def home(request):
    info = Sign.objects.all()
    context = {'info': info}
    return render(request, 'home.html', context)


def contacts(request):
    info = Sign.objects.all()
    context = {'info': info}
    return render(request, 'about.html', context)


def intro(request):
    info = Sign.objects.all()
    context = {'info': info}
    return render(request, 'intro.html', context)
