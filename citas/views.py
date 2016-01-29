from django.shortcuts import render
import datetime
from citas.models import Centro
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required 
# Create your views here.

def hola(request):
	ahora = datetime.datetime.now()
	logotipo = Centro.objects.all()[0]
	return render(request,'citas/hola.html',{'logo_web':logotipo})

def login(request):
	return render(request,'citas/login.html')

def index(request):
	logotipo = Centro.objects.all()[0]
	return render(request,'citas/index.html',{'logo_web':logotipo})

def login_view(request):
    if request.user.is_authenticated():
        return redirect(reverse('index'))
	mensaje =''

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect(reverse('index'))
			else:
				pass
		mensaje='Datos invalidos'
	return render(request,'login.html')


