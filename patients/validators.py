# custom validator - used in models.py
def validate_image_extension(value):
    import os
    from django.core.exceptions import ValidationError
    extn = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.png', '.jpeg']
    if not extn.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
