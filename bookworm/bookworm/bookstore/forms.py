from django import forms

from bookworm.bookstore.models import Category, Review, NewsletterList, Book


class CategoryCreateForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = '__all__'


class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ('rating', 'title', 'text')
		widgets = {
			'text': forms.Textarea(
				attrs={
					'class': 'form-control rounded-0 p-4',
					'rows': '7',
					'id': 'descriptionTextarea',
					'placeholder': "What did you like or dislike? What should other shoppers know before buying?",
					'required data - msg': "Please enter your message.",
					'data-error-class': "u-has-error",
					'data-success-class': "u-has-success",
				}
			),
			'title': forms.TextInput(
				attrs={
					'class': 'form-control rounded-0 p-4',
					'name': 'companyName',
					'id': "inputCompanyName",
					'placeholder': "",
				}
			),
		}


class NewsletterListForm(forms.ModelForm):
	def clean_email(self):
		email = self.cleaned_data['email']
		if NewsletterList.objects.filter(email=email).first():
			msg = 'Email already subscribed!'
			raise forms.ValidationError(msg)
		return email

	class Meta:
		model = NewsletterList
		fields = '__all__'
		field_classes = {'email': forms.EmailField}
		widgets = {
			'email': forms.EmailInput(
				attrs={
					'input type': "text",
					'class': "form-control px-5 height-60 border-dark",
					'name': "name",
					'id': "signupSrName",
					'placeholder': "Enter email for weekly newsletter.",
					'aria-label': "Your name",
					'required': "",
					'data-success-class': "u-has-success",
				}
			)
		}


class BookCreateForm(forms.ModelForm):
	class Meta:
		model = Book
		exclude = ('ave_rating',)
		widgets = {
			'publication_date': forms.DateInput(
				attrs={
					'type': 'text',
				}
			)
		}
