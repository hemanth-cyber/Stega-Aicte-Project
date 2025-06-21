from tkinter import Tk, Label, Button, filedialog, messagebox
from PIL import Image
import stepic
import os

class SteganographyDecoderApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Text Decoder")

        self.label = Label(master, text="Click the button below to select an image to decode:")
        self.label.pack(pady=10)

        self.select_image_button = Button(master, text="Select Encoded Image", command=self.decode_text)
        self.select_image_button.pack(pady=10)

    def decode_text(self):
        image_path = filedialog.askopenfilename(filetypes=[("PNG images", "*.png")])

        if not image_path:
            return

        if not os.path.isfile(image_path):
            messagebox.showerror("File Error", "Selected file does not exist.")
            return

        try:
            image = Image.open(image_path)
            hidden_text = stepic.decode(image)
            messagebox.showinfo("Hidden Message", f"Decoded text:\n{hidden_text}")
        except Exception as e:
            messagebox.showerror("Decoding Error", f"An error occurred:\n{e}")


if __name__ == "__main__":
    root = Tk()
    app = SteganographyDecoderApp(root)
    root.geometry("400x150")
    root.mainloop()
