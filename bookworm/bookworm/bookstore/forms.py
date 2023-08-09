from django import forms

from bookworm.bookstore.models import Category, Review


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

