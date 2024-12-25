import tkinter as tk
from tkinter import ttk, messagebox

def enkripsi(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isupper():
            cipher_text += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            cipher_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            cipher_text += char
    return cipher_text

def dekripsi(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        if char.isupper():
            plain_text += chr((ord(char) - 65 - shift) % 26 + 65)
        elif char.islower():
            plain_text += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            plain_text += char
    return plain_text

def process_text():
    text = text_input.get("1.0", tk.END).strip() 
    try:
        shift = int(shift_input.get())
    except ValueError:
        messagebox.showerror("Error", "Kunci pergeseran harus berupa angka!")
        return

    action = action_var.get()
    if action == "Encrypt":
        result = enkripsi(text, shift)
    elif action == "Decrypt":
        result = dekripsi(text, shift)
    else:
        result = "Pilih aksi yang valid!"

    result_output.delete("1.0", tk.END)  
    result_output.insert(tk.END, result)


app = tk.Tk()
app.title("Caesar Cipher - Modern UI")
app.geometry("500x400")
app.configure(bg="#f5f5f5")

style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 10), background="#f5f5f5")
style.configure("TButton", font=("Helvetica", 10), padding=5)
style.configure("TRadiobutton", font=("Helvetica", 10), background="#f5f5f5")

frame = ttk.Frame(app, padding=10)
frame.pack(fill="both", expand=True)

ttk.Label(frame, text="Masukkan Teks:").grid(row=0, column=0, sticky="w", pady=5)
text_input = tk.Text(frame, height=5, width=50, wrap="word")
text_input.grid(row=1, column=0, columnspan=2, pady=5)

ttk.Label(frame, text="Masukkan Kunci Pergeseran (Shift):").grid(row=2, column=0, sticky="w", pady=5)
shift_input = ttk.Entry(frame, width=10)
shift_input.grid(row=2, column=1, sticky="w", pady=5)

ttk.Label(frame, text="Pilih Aksi:").grid(row=3, column=0, sticky="w", pady=5)
action_var = tk.StringVar(value="Encrypt")
ttk.Radiobutton(frame, text="Encrypt", variable=action_var, value="Encrypt").grid(row=3, column=1, sticky="w")
ttk.Radiobutton(frame, text="Decrypt", variable=action_var, value="Decrypt").grid(row=4, column=1, sticky="w")

process_button = ttk.Button(frame, text="Proses", command=process_text)
process_button.grid(row=5, column=0, columnspan=2, pady=10)

ttk.Label(frame, text="Hasil:").grid(row=6, column=0, sticky="w", pady=5)
result_output = tk.Text(frame, height=5, width=50, wrap="word", state="normal")
result_output.grid(row=7, column=0, columnspan=2, pady=5)

app.mainloop()
