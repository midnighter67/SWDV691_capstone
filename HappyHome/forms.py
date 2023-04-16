from django import forms
from django.forms import ModelForm
from .models import Provider, SiteUser, Review, Reply
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User



class RegisterUserForm(UserCreationForm):
    # adding other User fields 
    # email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].label = ''
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].help_text = ''

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].label = ''
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['last_name'].help_text = ''

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].label = ''
        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
        self.fields['email'].help_text = ''
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label = ''
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].help_text = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].label = ''
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].help_text = '<small>Your password must contain at least 8 characters</small>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].label = ''
        self.fields['password2'].widget.attrs['placeholder'] = 'Re-enter Password'
        self.fields['password2'].help_text = ''

class EditProfileForm(UserChangeForm):
    password = forms.CharField(label="", widget=forms.TextInput(attrs={'type': 'hidden'})) # hides link django puts on page

    class Meta:
        model = User
        # exclude = (list exclusions) instead of fields = ()
        fields = ('username', 'first_name', 'last_name', 'email', 'password',) # must have password

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label = ''
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].help_text = ''

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].label = ''
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        #self.fields['first_name'].help_text = '<small>Your password must contain at least 8 characters</small>'

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].label = ''
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        #self.fields['last_name'].help_text = '<small>Your password must contain at least 8 characters</small>'
"""
class UpdatePasswordForm(PasswordChangeForm):
        class Meta:
            model = User
            fields = ('password1', 'password1', 'password2')

        def __init__(self, *args, **kwargs):
            super(UpdatePasswordForm, self).__init__(*args, **kwargs)
         
            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].label = ''
            self.fields['password1'].widget.attrs['placeholder'] = 'Username'
            self.fields['password1'].help_text = ''
                
            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].label = ''
            self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['password1'].help_text = ''

            self.fields['password2'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].label = ''
            self.fields['password2'].widget.attrs['placeholder'] = 'Re-enter Password'
            self.fields['password2'].help_text = ''
"""

class UserProfileForm(ModelForm):
    class Meta:
        model = SiteUser
        fields = ('first', 'last', 'address', 'city', 'state', 'zip', 'email')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

        self.fields['first'].widget.attrs['class'] = 'form-control'
        self.fields['first'].label = 'First Name'
        self.fields['first'].widget.attrs['placeholder'] = ''
        self.fields['first'].help_text = ''

        self.fields['last'].widget.attrs['class'] = 'form-control'
        self.fields['last'].label = 'Last Name'
        self.fields['last'].widget.attrs['placeholder'] = ''
        self.fields['last'].help_text = ''

        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['address'].label = 'Address'
        self.fields['address'].widget.attrs['placeholder'] = ''
        self.fields['address'].help_text = ''

        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['city'].label = 'City'
        self.fields['city'].widget.attrs['placeholder'] = ''
        self.fields['city'].help_text = ''

        self.fields['state'].widget.attrs['class'] = 'form-control'
        self.fields['state'].label = 'State'
        self.fields['state'].widget.attrs['placeholder'] = ''
        self.fields['state'].help_text = ''

        self.fields['zip'].widget.attrs['class'] = 'form-control'
        self.fields['zip'].label = 'Zip Code'
        self.fields['zip'].widget.attrs['placeholder'] = ''
        self.fields['zip'].help_text = ''

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].label = 'Email Address'
        self.fields['email'].widget.attrs['placeholder'] = ''
        self.fields['email'].help_text = ''