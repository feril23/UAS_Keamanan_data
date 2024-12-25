import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import base64

def pad(text):
    padding_len = 8 - (len(text) % 8) 
    padding = chr(padding_len) * padding_len 
    return text + padding

def unpad(text):
    padding_len = ord(text[-1]) 
    return text[:-padding_len]

def enkripsi(plain_text, key):
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plain_text)
    enkripsi_text = des.encrypt(padded_text.encode('utf-8'))
    return base64.b64encode(enkripsi_text).decode('utf-8')

def dekripsi(enkripsi_text, key):
    des = DES.new(key, DES.MODE_ECB)
    decode_enkripsi_text = base64.b64decode(enkripsi_text)
    dekripsi_text = des.decrypt(decode_enkripsi_text).decode('utf-8')
    return unpad(dekripsi_text)

def handle_enkripsi():
    plain_text = entry_plain_text.get()
    key = entry_key.get()

    if len(key) != 8:
        messagebox.showerror("Error", "Key harus memiliki panjang 8 karakter")
        return

    try:
        key_bytes = key.encode('utf-8')
        hasil_enkripsi = enkripsi(plain_text, key_bytes)
        entry_encrypted_text.delete(0, tk.END)
        entry_encrypted_text.insert(0, hasil_enkripsi)
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

def handle_dekripsi():
    encrypted_text = entry_encrypted_text.get()
    key = entry_key.get()

    if len(key) != 8:
        messagebox.showerror("Error", "Key harus memiliki panjang 8 karakter")
        return

    try:
        key_bytes = key.encode('utf-8')
        hasil_dekripsi = dekripsi(encrypted_text, key_bytes)
        entry_decrypted_text.delete(0, tk.END)
        entry_decrypted_text.insert(0, hasil_dekripsi)
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

# Membuat GUI
root = tk.Tk()
root.title("DES Encryption and Decryption")

# Input untuk Plain Text
label_plain_text = tk.Label(root, text="Plain Text:")
label_plain_text.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_plain_text = tk.Entry(root, width=40)
entry_plain_text.grid(row=0, column=1, padx=10, pady=5)

# Input untuk Key
label_key = tk.Label(root, text="Key (8 karakter):")
label_key.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_key = tk.Entry(root, width=40)
entry_key.grid(row=1, column=1, padx=10, pady=5)

# Tombol Enkripsi
button_encrypt = tk.Button(root, text="Enkripsi", command=handle_enkripsi)
button_encrypt.grid(row=2, column=0, columnspan=2, pady=10)

# Hasil Enkripsi
label_encrypted_text = tk.Label(root, text="Encrypted Text:")
label_encrypted_text.grid(row=3, column=0, padx=10, pady=5, sticky="e")

entry_encrypted_text = tk.Entry(root, width=40)
entry_encrypted_text.grid(row=3, column=1, padx=10, pady=5)

# Tombol Dekripsi
button_decrypt = tk.Button(root, text="Dekripsi", command=handle_dekripsi)
button_decrypt.grid(row=4, column=0, columnspan=2, pady=10)

# Hasil Dekripsi
label_decrypted_text = tk.Label(root, text="Decrypted Text:")
label_decrypted_text.grid(row=5, column=0, padx=10, pady=5, sticky="e")

entry_decrypted_text = tk.Entry(root, width=40)
entry_decrypted_text.grid(row=5, column=1, padx=10, pady=5)

# Menjalankan GUI
root.mainloop()
