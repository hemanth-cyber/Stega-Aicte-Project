from tkinter import Tk, Label, Button, Entry, filedialog, messagebox
from PIL import Image
import stepic
import os

class SteganographyApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Text Encoder")

        self.label = Label(master, text="Enter the text to hide:")
        self.label.pack(pady=5)

        self.entry = Entry(master, width=50)
        self.entry.pack(pady=5)

        self.select_image_button = Button(master, text="Select Image", command=self.select_image)
        self.select_image_button.pack(pady=5)

        self.encode_button = Button(master, text="Encode and Save", command=self.encode_text)
        self.encode_button.pack(pady=5)

        self.image_path = None

    def select_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("PNG images", "*.png")])
        if self.image_path:
            messagebox.showinfo("Image Selected", f"Image loaded: {os.path.basename(self.image_path)}")

    def encode_text(self):
        if not self.image_path:
            messagebox.showwarning("No Image", "Please select an image first.")
            return

        text = self.entry.get()
        if not text:
            messagebox.showwarning("No Text", "Please enter the text to hide.")
            return

        try:
            image = Image.open(self.image_path)
            encoded_image = stepic.encode(image, text.encode())

            save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG images", "*.png")],
                                                     title="Save encoded image")
            if save_path:
                encoded_image.save(save_path)
                messagebox.showinfo("Success", f"Text has been hidden in: {save_path}")
        except Exception as e:
            messagebox.showerror("Encoding Failed", f"An error occurred:\n{e}")


if __name__ == "__main__":
    root = Tk()
    app = SteganographyApp(root)
    root.geometry("400x200")
    root.mainloop()
