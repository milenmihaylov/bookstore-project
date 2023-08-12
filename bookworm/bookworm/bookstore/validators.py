from django.core.exceptions import ValidationError


def validate_isbn_length(value):
	length = len(str(value))
	msg = 'The ISBN should be 10 or 13 characters long'
	if length != 10 and length != 13:
		raise ValidationError(msg)
