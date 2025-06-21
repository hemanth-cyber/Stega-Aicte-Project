# 🕵️‍♂️ Stega-Aicte-Project

This project is a simple steganography tool that allows users to **hide secret messages within images using Python**. The tool provides a graphical user interface (GUI) for both **encrypting** and **decrypting** messages.

---

## ✨ Features

- 🔐 **Encrypt a Message**: Embed a secret message into an image file by modifying the least significant bits (LSB) of the image's pixel data.
- 🔓 **Decrypt a Message**: Retrieve the hidden message from an encrypted image.
- 🖼️ **User-Friendly GUI**: Built using [Tkinter](https://docs.python.org/3/library/tkinter.html) for easy interaction.

---

## 📦 Requirements

- Python 3.x  
- [Pillow](https://pypi.org/project/Pillow/) (PIL Fork)  
- [Stepic](https://pypi.org/project/stepic/)  
- Tkinter (usually comes pre-installed with Python)

---

## ⚙️ Installation

```bash
# 1. Clone this repository:
git clone https://github.com/hemanth-cyber/Stega-Aicte-Project.git
cd Stega-Aicte-Project

# 2. Install the required libraries:
pip install pillow stepic
```

---

## 🚀 Usage

### 🔐 Encrypting a Message

```bash
python encrypt.py
```

In the GUI that opens:
- Enter your secret message in the text box.
- Click **"Select Image"** to choose an image file (PNG or JPG) where you want to hide your message.
- Click **"Encrypt Message"** to save the encrypted image as `encoded_image.png`.

---

### 🔓 Decrypting a Message

```bash
python decrypt.py
```

In the GUI that opens:
- Click **"Select Encrypted Image"** to choose the previously encrypted image.
- The hidden message will be displayed in a pop-up window.

---

## ⚠️ Important Notes

- The tool currently supports **PNG and JPG** images.
- Ensure that your input images are **large enough** to accommodate your secret messages; otherwise, you may encounter issues with longer messages.
- The delimiter used to indicate the end of the hidden message is `1111111111111110`.

---

## 🙏 Acknowledgments

- This project utilizes the [Pillow](https://pillow.readthedocs.io/en/stable/) library for image processing.
- Special thanks to [Tkinter](https://docs.python.org/3/library/tkinter.html) for providing a simple way to create GUIs in Python.

