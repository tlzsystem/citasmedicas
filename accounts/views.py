from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from .forms import RegistroUserForm
from .models import UserProfile

def registro_usuario_view(request):

    if request.method == 'POST':
        form = RegistroUserForm(request.POST)
        if form.is_valid():
            variable = request.POST['username'] #prueba para obtener valor desde el request
            cleaned_data = form.cleaned_data
            usernames =form.cleaned_data['username']
            print usernames
            print variable
            passwords = cleaned_data.get('password')
            email = cleaned_data.get('email')
            user_model = User.objects.create_user(username=usernames, password=passwords)
            user_model.email = email
            user_model.save()
            user_profile = UserProfile()
            user_profile.user = user_model
            user_profile.save()
            return redirect(reverse('accounts.gracias', kwargs={'username': username}))
    else:
        form = RegistroUserForm()
    context = {'form': form}
    return render(request, 'accounts/registro.html', context)

def gracias_view(request, username):
    return render(request, 'accounts/gracias.html', {'username': username})
