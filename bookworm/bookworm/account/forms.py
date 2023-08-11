from django import forms

from bookworm.account.models import Account


class AccountForm(forms.ModelForm):

	class Meta:
		model = Account
		exclude = ('user',)
		widgets = {
			'first_name': forms.TextInput(
				attrs={
					'type': "text",
					'class': "form-control rounded-0 pl-3 placeholder-color-3",
					'id': "exampleFormControlInput1",
					'name': "name",
					'aria-label': "Jack Wayley",
					'placeholder': "",
					'required': "",
					'data-error-class': "u-has-error",
					'data-msg': "Please enter your name.",
					'data-success-class': "u-has-success",
				},

			),
			'last_name': forms.TextInput(
				attrs={
					'type': "text",
					'class': "form-control rounded-0 pl-3 placeholder-color-3",
					'id': "exampleFormControlInput1",
					'name': "name",
					'aria-label': "Jack Wayley",
					'placeholder': "",
					'required': "",
					'data-error-class': "u-has-error",
					'data-msg': "Please enter your name.",
					'data-success-class': "u-has-success",
				}
			)
		}
