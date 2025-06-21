from PIL import Image
import stepic
import os

def decode_text_from_image(image_path):
    print(f"[INFO] Trying to decode from: {image_path}")

    if not os.path.isfile(image_path):
        print(f"[ERROR] File not found: {image_path}")
        return

    try:
        image = Image.open(image_path)
        hidden_text = stepic.decode(image)
        print(f"[+] Hidden text: {hidden_text}")
    except Exception as e:
        print(f"[ERROR] Failed to decode: {e}")

if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    encoded_image_path = os.path.join(base_dir, "encoded_image2.png")  # Use fixed path
    decode_text_from_image(encoded_image_path)
from PIL import Image
import stepic
import os

def decode_text_from_image(image_path):
    print(f"[INFO] Trying to decode from: {image_path}")

    if not os.path.isfile(image_path):
        print(f"[ERROR] File not found: {image_path}")
        return

    try:
        image = Image.open(image_path)
        hidden_text = stepic.decode(image)
        print(f"[+] Hidden text: {hidden_text}")
    except Exception as e:
        print(f"[ERROR] Failed to decode: {e}")

if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    encoded_image_path = os.path.join(base_dir, "encoded_image2.png")  # Use fixed path
    decode_text_from_image(encoded_image_path)
