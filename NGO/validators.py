from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size

    if filesize > 2621440:
        raise ValidationError("Image size is not more than 2MB")
    else:
        return value
