from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#------------------------------------------------------------------------------------------------------------------------
#                             Admin User Creation Form
#------------------------------------------------------------------------------------------------------------------------
class AdminRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.email = self.cleaned_data['email']
        user.is_staff = True
        print "from valid, saving to db"

        if commit:
            user.save()

        return user
        