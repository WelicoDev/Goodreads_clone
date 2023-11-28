from django import forms

from users.models import CustomUser


"""class UserCreateForm(forms.Form):
    username = forms.CharField(max_length=250)
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    password = forms.CharField(max_length=128)


    def save(self):
        username = self.changed_data['username']
        first_name = self.changed_data['first_name']
        last_name = self.changed_data['last_name']
        email = self.changed_data['email']
        password = self.changed_data['password']

        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

        user.set_password(password)
        user.save()

        return user"""

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("username" , "first_name" , "last_name" , "email" , "password")

    def save(self , commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])

        user.save()

        return user

# class UserLoginForm(forms.Form):
#
#     username = forms.CharField(max_length=200)
#     password = forms.CharField(max_length=128)
#
#     # def clean(self):
#     #     username = self.cleaned_data['username']
#     #     password = self.cleaned_data['password']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('profile_picture','username' , 'first_name' , 'last_name' , 'email')






