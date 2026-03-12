
from django.contrib.auth.forms import UserCreationForm
from users.models import NewUser


class CreateUserForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ['name', 'email', 'mobile_no', 'password1', 'password2']
