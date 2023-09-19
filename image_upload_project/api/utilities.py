from PIL import Image as PILImage
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile

def generate_thumbnail(image, thumbnail_height):
    thumbnail = PILImage.open(image.file)
    ratio = (thumbnail_height/float(thumbnail.size[1]))
    thumbnail_width = int((float(thumbnail.size[0])*float(ratio)))
    thumbnail = thumbnail.resize((thumbnail_width,thumbnail_height), PILImage.Resampling.LANCZOS)
    thumbnail_io = BytesIO()
    thumbnail.save(thumbnail_io, format='JPEG')
    thumbnail_file = SimpleUploadedFile(
        name=image.file.name,
        content=thumbnail_io.getvalue(),
        content_type='image/jpeg'
    )
    return thumbnail_file
