from PIL import Image as PILImage
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile


def generate_thumbnail(file, thumbnail_height):
    """
    Generates a thumbnail image from the given image file.

    This function takes an image file and resizes it to create a thumbnail image with 
    the specified height while maintaining
    the original aspect ratio. The generated thumbnail is saved in JPEG format.

    Args:
        file (File): The original image file to generate a thumbnail from.
        thumbnail_height (int): The desired height of the thumbnail image.

    Returns:
        SimpleUploadedFile: A Django SimpleUploadedFile object containing the generated 
        thumbnail image in JPEG format.

    Dependencies:
        - Python Imaging Library (PIL) or Pillow library is required for image processing.

    Example usage:
        thumbnail = generate_thumbnail(image_file, 200)
        # 'thumbnail' will contain the generated thumbnail image.

    """
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
