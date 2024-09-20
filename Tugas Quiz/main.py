import tkinter as tk
from tkinter import filedialog, messagebox
from vigenere import Vigenere

class VigenereCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vigenere Cipher")

        self.text_input = tk.Text(root, height=10, width=50)
        self.text_input.pack(pady=10)

        self.key_label = tk.Label(root, text="Enter Key (min 12 characters):")
        self.key_label.pack()

        self.key_input = tk.Entry(root, width=50)
        self.key_input.pack(pady=5)

        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt_text)
        self.encrypt_button.pack(pady=5)

        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.decrypt_text)
        self.decrypt_button.pack(pady=5)

        self.upload_button = tk.Button(root, text="Upload File", command=self.upload_file)
        self.upload_button.pack(pady=5)

        self.result_label = tk.Label(root, text="Result:")
        self.result_label.pack()

        self.result_output = tk.Text(root, height=10, width=50)
        self.result_output.pack(pady=10)

    def encrypt_text(self):
        key = self.key_input.get()
        text = self.text_input.get("1.0", tk.END).strip()

        if len(key) < 12:
            messagebox.showerror("Error", "Key must be at least 12 characters long.")
            return

        encrypted = Vigenere.encrypt(text, key)
        self.result_output.delete("1.0", tk.END)
        self.result_output.insert(tk.END, encrypted)

    def decrypt_text(self):
        key = self.key_input.get()
        text = self.text_input.get("1.0", tk.END).strip()

        if len(key) < 12:
            messagebox.showerror("Error", "Key must be at least 12 characters long.")
            return

        decrypted = Vigenere.decrypt(text, key)
        self.result_output.delete("1.0", tk.END)
        self.result_output.insert(tk.END, decrypted)

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_input.delete("1.0", tk.END)
                self.text_input.insert(tk.END, content)

if __name__ == "__main__":
    root = tk.Tk()
    app = VigenereCipherApp(root)
    root.mainloop()
