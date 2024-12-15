import base64
from PIL import Image
from io import BytesIO


def encode_image_to_base64(image: Image.Image) -> str:
    """
    Encode a PIL Image to a Base64 string.

    Args:
        image (PIL.Image.Image): The image to encode.

    Returns:
        str: Base64 encoded string.
    """
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


def decode_base64_to_image(base64_string: str) -> Image.Image:
    """
    Decode a Base64 string back to a PIL Image.

    Args:
        base64_string (str): The Base64 string to decode.

    Returns:
        PIL.Image.Image: The decoded image.
    """
    image_data = base64.b64decode(base64_string)
    return Image.open(BytesIO(image_data))
