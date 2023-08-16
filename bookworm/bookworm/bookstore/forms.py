from django import forms

from bookworm.bookstore.models import Category, Review, NewsletterList, Book, Author


class BookSearchForm(forms.Form):
	search_query = forms.CharField(
		max_length=100,
		widget=forms.TextInput(
			attrs={
				'class': "form-control bg-white-100 min-width-380 py-2d75 height-4 border-white-100",
				'type': "search",
				'placeholder': "Search for Books by Keyword ...",
				'aria-label': "Search",
				'required': "",
			}
		)
	)


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


class AuthorForm(forms.ModelForm):
	class Meta:
		model = Author
		fields = '__all__'
		widgets = {
			'name': forms.TextInput(
				attrs={
					'class': 'form-control rounded-0 p-4',
					'name': 'companyName',
					'id': "inputCompanyName",
					'placeholder': "Author Name",
				},
			),
			'image': forms.FileInput(
				attrs={
					'class': "img-fluid d-block mx-auto attachment-shop_catalog size-shop_catalog wp-post-image img-fluid",
				},
			),
			'about': forms.Textarea(
				attrs={
					'input type': "text",
					'class': "form-control px-5 height-60 border-dark",
					'name': "name",
					'id': "signupSrName",
					'placeholder': "About",
					'aria-label': "Your name",
					'data-success-class': "u-has-success",
				}
			)
		}


class BookCreateForm(forms.ModelForm):
	class Meta:
		model = Book
		exclude = ('ave_rating', 'sold_copies')
		widgets = {
			'publication_date': forms.DateInput(
				attrs={

				}
			),
			'title': forms.TextInput(
				attrs={
					'class': 'form-control rounded-0 p-4',
					'name': 'companyName',
					'id': "inputCompanyName",
					'placeholder': "title",
				},
			),
			'short_description': forms.Textarea(
				attrs={
					'input type': "text",
					'class': "form-control px-5 height-60 border-dark",
					'name': "name",
					'id': "signupSrName",
					'placeholder': "short description",
					'aria-label': "Your name",
					'required': "",
					'data-success-class': "u-has-success",
				}
			),
			'long_description': forms.Textarea(
				attrs={
					'input type': "text",
					'class': "form-control px-5 height-60 border-dark",
					'name': "name",
					'id': "signupSrName",
					'placeholder': "long description",
					'aria-label': "Your name",
					'required': "",
					'data-success-class': "u-has-success",
				}
			),
			'cover_image': forms.FileInput(),
			'price': forms.NumberInput(),
			'pages': forms.NumberInput(),

		}
