from django.urls import reverse_lazy
#  CBV
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
# Auth
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin 
# My app
from .forms import UserRegisterationForm


# Create your views here.

class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = UserRegisterationForm
    success_url = reverse_lazy('login')


class MyLoginView(LoginView):
    '''
        `form_class = AuthenticationForm` by default
        `redirect_authenticated_user=False` By default -> if its true it redirects the logged in users who try to access this page
    '''
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class ProtectedTemplateView(LoginRequiredMixin, TemplateView):
    '''
        Remember to inherit from LoginRequiredMixin, TemplateView respectively
        otherwise the `templateView.dispatch` will be called first and the mixin not gonna work. 
        Because of the MRO (Method resolution order).
    '''
    template_name = 'accounts/index.html'
