from django.core.exceptions import ValidationError
from django.contrib import messages
from django.shortcuts import render
import os
#Makes sure users only upload files smaller than 6mb
def validate_file_size_type(value):
    filesize = value.size
    ext = os.path.splitext(value.name)[1]
    valid_extentions = ['.txt', '.png', '.jpg', '.jpeg']

    if filesize > 5242880:
         
        raise ValidationError("Maximum file size is 5MB")
          
    elif not ext.lower() in valid_extentions:
        
        raise ValidationError("Not a supported file type")
    else:
        return value
