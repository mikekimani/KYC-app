import io
import os
from google.cloud import vision

def extract_text(image_path: str) -> dict:
    client = vision.ImageAnnotatorClient()
    with io.open(image_path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if not texts:
        return {}

    full_text = texts[0].description
    return {"text": full_text}
