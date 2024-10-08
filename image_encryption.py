import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

class ImageEncryptionTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Pixel Manipulation Image Encryption Tool")
        self.root.geometry("600x400")
        self.root.configure(bg="#2c2c2c")

        self.description_label = tk.Label(self.root, text="Encrypt and Decrypt Images using Pixel Manipulation", 
                                          font=("Helvetica", 14, "bold"), fg="#00FF7F", bg="#2c2c2c")
        self.description_label.pack(pady=10)

        self.image_label = tk.Label(self.root, bg="#2c2c2c")
        self.image_label.pack(pady=10)

        self.upload_button = tk.Button(self.root, text="Upload Image", font=("Arial", 12, "bold"), 
                                       command=self.upload_image, bg="#1E90FF", fg="white")
        self.upload_button.pack(pady=10)

        self.encrypt_button = tk.Button(self.root, text="Encrypt Image", font=("Arial", 12, "bold"), 
                                        command=self.encrypt_image, bg="#32CD32", fg="white", state="disabled")
        self.encrypt_button.pack(pady=10)

        self.decrypt_button = tk.Button(self.root, text="Decrypt Image", font=("Arial", 12, "bold"), 
                                        command=self.decrypt_image, bg="#FF6347", fg="white", state="disabled")
        self.decrypt_button.pack(pady=10)

        self.image_path = None

    def upload_image(self):
        # This ensures only image files (.png, .jpg, .jpeg) are displayed
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
        if self.image_path:
            self.display_image(self.image_path)
            self.encrypt_button.config(state="normal")
            self.decrypt_button.config(state="normal")

    def display_image(self, path):
        image = Image.open(path)
        image = image.resize((250, 250))  # Resize the image to fit in the window
        image_tk = ImageTk.PhotoImage(image)
        self.image_label.config(image=image_tk)
        self.image_label.image = image_tk

    def encrypt_image(self):
        if self.image_path:
            encrypted_image_path = self.apply_pixel_operation(self.image_path, operation="encrypt")
            self.display_image(encrypted_image_path)
            messagebox.showinfo("Success", "Image encrypted successfully!")

    def decrypt_image(self):
        if self.image_path:
            decrypted_image_path = self.apply_pixel_operation(self.image_path, operation="decrypt")
            self.display_image(decrypted_image_path)
            messagebox.showinfo("Success", "Image decrypted successfully!")

    def apply_pixel_operation(self, image_path, operation="encrypt"):
        image = Image.open(image_path)
        pixels = image.load()

        width, height = image.size
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]

                # Simple pixel manipulation: swap and add/subtract a constant
                if operation == "encrypt":
                    pixels[x, y] = (r + 50) % 256, (g + 50) % 256, (b + 50) % 256
                else:  # Decrypt
                    pixels[x, y] = (r - 50) % 256, (g - 50) % 256, (b - 50) % 256

        # Save the image based on the operation performed (encrypt/decrypt)
        output_path = "encrypted_image.png" if operation == "encrypt" else "decrypted_image.png"
        image.save(output_path)
        return output_path

def main():
    root = tk.Tk()
    app = ImageEncryptionTool(root)
    root.mainloop()

if __name__ == "__main__":
    main()
