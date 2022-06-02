from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm
from .models import User
from django.forms import HiddenInput


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "password"
        )

    def __init__(self, *arg, **kwarg):
        super(LoginForm, self).__init__(*arg, **kwarg)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control bg-dark border border-secondary border-1 rounded-2 text-white"
            field.widget.attrs["style"] = "font-size: 1.6vmax"
            # if field_name == "username":
            #     field.widget.attrs["id"] = "validationCustomUsername"
            #     field.widget.attrs["type"] = "text"
            #     field.widget.attrs.update({"required": True})


class EditAccountForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "vk",
            "email",
        )

    def __init__(self, *arg, **kwarg):
        super(EditAccountForm, self).__init__(*arg, **kwarg)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control bg-dark border border-secondary border-1 rounded-2 text-white"
            field.widget.attrs["style"] = "font-size: 1.6vmax"
            if field_name == "password":
                field.widget = HiddenInput()


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "age",
            "grade",
            "game_modes",
            "vk",
            "email",
        )

    def __init__(self, *arg, **kwarg):
        super(RegistrationForm, self).__init__(*arg, **kwarg)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control bg-dark border border-secondary border-1 rounded-2 text-white"
            field.widget.attrs["style"] = "font-size: 1.6vmax"
            if field_name == "password":
                field.widget = HiddenInput()
