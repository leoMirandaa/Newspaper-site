from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy #wait db its completed


class SignUpView(CreateView):
  form_class = CustomUserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"