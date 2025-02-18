from django.shortcuts import render

# Create your views here.
#from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
#from django.views.generic import TemplateView
#from django.contrib.auth.models import User
from django.shortcuts import redirect
from .forms import ProfileForm
from .models import Profile


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = '/login/'

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect('login')

class ProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile.html'

    def get_object(self):
        return self.request.user.profile
