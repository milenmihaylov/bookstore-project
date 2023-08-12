from django import forms
from django.contrib.auth import get_user_model, authenticate, password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

USER_MODEL = get_user_model()


class LogInForm(AuthenticationForm):
	user = None

	username = forms.EmailField(
		widget=forms.EmailInput(
			attrs={
				'type': "email",
				'class': "form-control rounded-0",
				'name': "email",
				'id': "signinEmail1",
				'placeholder': "ilovebooks@bookworm.com",
				'aria-label': "ilovebooks@bookworm.com",
				'aria-describedby': "signinEmailLabel1",
			}
		)
	)

	password = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				'type': "password",
				'class': "form-control rounded-0",
				'name': "password",
				'id': "signinPassword1",
				'placeholder': "",
				'aria-label': "",
				'aria-describedby': "signinPasswordLabel1",
			}
		)
	)

	def clean_password(self):
		super().clean()
		self.user = authenticate(
			email=self.cleaned_data['username'],
			password=self.cleaned_data['password'],
		)
		if not self.user:
			raise ValidationError('Email and/or password incorrect')

	def save(self):
		return self.user


class RegisterForm(UserCreationForm):
	password1 = forms.CharField(
		label="Password",
		strip=False,
		widget=forms.PasswordInput(
			attrs={
				"autocomplete": "new-password",
				'type': "password",
				'class': "form-control rounded-0",
				'name': "password",
				'id': "signinPassword1",
				'placeholder': "",
				'aria-label': "",
				'aria-describedby': "signinPasswordLabel1",
			}
		),
		help_text=password_validation.password_validators_help_text_html(),
	)
	password2 = forms.CharField(
		label="Password confirmation",
		widget=forms.PasswordInput(
			attrs={
				"autocomplete": "new-password",
				'type': "password",
				'class': "form-control rounded-0",
				'name': "password",
				'id': "signinPassword1",
				'placeholder': "",
				'aria-label': "",
				'aria-describedby': "signinPasswordLabel1",
			}
		),
		strip=False,
		help_text="Enter the same password as before, for verification.",
	)

	class Meta:
		model = USER_MODEL
		fields = ('email',)
		field_classes = {"email": forms.EmailField}
		widgets = {
			'email': forms.EmailInput(
				attrs={
					'type': "email",
					'class': "form-control rounded-0",
					'name': "email",
					'id': "signinEmail1",
					'placeholder': "ilovebooks@bookworm.com",
					'aria-label': "ilovebooks@bookworm.com",
					'aria-describedby': "signinEmailLabel1",
				}
			),
		}
