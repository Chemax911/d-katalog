from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.utils.translation import gettext_lazy as _


class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username')


class UserAdminChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username')


class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('email', 'username')


class UserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'username')


# class UserCreationForm(UserCreationForm):
#     email = forms.EmailField(
#         max_length=254,
#         widget=forms.EmailInput(
#             attrs={
#                 'class': 'form-control',
#                 'autocomplete': 'email'}))

#     class Meta(UserCreationForm.Meta):
#         model = get_user_model()
#         fields = ('email', 'username')

#     def __init__(self, *args, **kwargs):
#         super(UserCreationForm, self).__init__(*args, **kwargs)
#         for fieldname, field in self.fields.items():
#             field.label = False
#         self.fields['username'].widget.attrs.update({
#             'class': 'form-control'})
