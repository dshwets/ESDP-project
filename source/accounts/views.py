from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from accounts.forms import MyUserCreationForm


class RegisterView(CreateView):
    model = get_user_model()
    template_name = 'user_create.html'
    form_class = MyUserCreationForm
