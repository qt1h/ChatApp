from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _


def sign_up(request):
    if request.method == 'POST':
        # Créer une instance du formulaire
        form = UserCreationForm(request.POST)

        # Modifier les messages d'aide dynamiquement
        form.fields['username'].help_text = ''#Will be displayed
        form.fields['password1'].help_text = ''#Decide a new password

        if form.is_valid():
            user = form.save()
            return redirect('users:index')  # Rediriger vers la page d'accueil après une inscription réussie
    else:
        # Si la méthode n'est pas POST, créer une instance normale du formulaire
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'users/connection.html', context)

def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to your home page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'users/connection.html', {'form': form})

def index_view(request):
    return render(request, 'index.html')

def connnexion_view(request):
    return render(request, 'users/connection.html')