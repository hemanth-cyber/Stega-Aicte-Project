from PIL import Image
import stepic
import os

def encode_text_into_image(image_path, text, output_image_path):
    print(f"[INFO] Trying to open: {image_path}")
    
    if not os.path.isfile(image_path):
        print(f"[ERROR] File not found: {image_path}")
        return

    try:
        image = Image.open(image_path)
        encoded_image = stepic.encode(image, text.encode())
        encoded_image.save(output_image_path)
        print(f"[+] Text has been hidden inside '{output_image_path}'.")
    except Exception as e:
        print(f"[ERROR] Failed to encode: {e}")

if __name__ == "__main__":
    confirm = input("Do you want to encrypt a message into an image? (y/n): ").strip().lower()
    
    if confirm == 'y':
        text = input("Enter the text to hide: ").strip()
        
        base_dir = os.path.dirname(__file__)
        image_path = os.path.join(base_dir, "input_image.png")             
        output_image_path = os.path.join(base_dir, "encoded_image2.png")   
        
        encode_text_into_image(image_path, text, output_image_path)
    else:
        print("[INFO] Encryption cancelled.")
