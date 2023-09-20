from PIL import Image as PILImage
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile


def generate_thumbnail(file, thumbnail_height):
    image = PILImage.open(file)
    ratio = (thumbnail_height/float(image.size[1]))
    thumbnail_width = int((float(image.size[0])*float(ratio)))
    thumbnail = image.resize((thumbnail_width,thumbnail_height), PILImage.Resampling.LANCZOS)
    thumbnail_io = BytesIO()
    thumbnail.save(thumbnail_io, format='JPEG')
    thumbnail_file = SimpleUploadedFile(
        name=file.name,
        content=thumbnail_io.getvalue(),
        content_type='image/jpeg'
    )
    return thumbnail_file
