import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from stegano import lsb

class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Steganografi")
        self.root.geometry("800x550")
        self.root.configure(bg="#f0f0f0")

        # Header
        header = tk.Label(root, text="Aplikasi Steganografi", font=("Roboto", 18, "bold"), bg="#4CAF50", fg="white")
        header.pack(fill=tk.X, pady=(20, 30))

        # Main Container
        main_container = tk.Frame(root, bg="#f0f0f0")
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Left Panel (Image Display)
        image_panel = tk.Frame(main_container, bg="#f0f0f0")
        image_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(image_panel, bg="white", width=500, height=400, highlightthickness=1, highlightbackground="#4CAF50")
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.image_path = None
        self.image = None

        # Right Panel (Buttons and Input)
        button_panel = tk.Frame(main_container, bg="#f0f0f0")
        button_panel.pack(side=tk.RIGHT, fill=tk.Y, padx=(20, 0))

        # Input Frame
        input_frame = tk.Frame(button_panel, bg="#f0f0f0")
        input_frame.pack(pady=(0, 20))

        self.input_label = tk.Label(input_frame, text="Enter data to hide:", font=("Roboto", 12), bg="#f0f0f0")
        self.input_label.pack(side=tk.TOP, pady=5)

        self.input_text = tk.Text(input_frame, height=5, width=30, font=("Roboto", 12))
        self.input_text.pack(side=tk.TOP)

        # Buttons
        open_button = tk.Button(button_panel, text="Open Image", command=self.open_image, width=15, bg="#4CAF50", fg="white", font=("Roboto", 12))
        open_button.pack(pady=10)

        save_button = tk.Button(button_panel, text="Save Image", command=self.save_image, width=15, bg="#4CAF50", fg="white", font=("Roboto", 12))
        save_button.pack(pady=10)

        hide_button = tk.Button(button_panel, text="Hide Data", command=self.hide_data, width=15, bg="#4CAF50", fg="white", font=("Roboto", 12))
        hide_button.pack(pady=10)

        show_button = tk.Button(button_panel, text="Show Data", command=self.show_data, width=15, bg="#4CAF50", fg="white", font=("Roboto", 12))
        show_button.pack(pady=10)

        exit_button = tk.Button(button_panel, text="Exit", command=root.quit, width=15, bg="#FF5722", fg="white", font=("Roboto", 12))
        exit_button.pack(pady=10)

    def open_image(self):
        filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if not filepath:
            return

        self.image_path = filepath
        self.image = Image.open(filepath)
        self.display_image()

    def save_image(self):
        if self.image_path is None:
            messagebox.showwarning("Warning", "No image to save.")
            return

        filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        if filepath:
            try:
                self.image.save(filepath)
                messagebox.showinfo("Success", "Image saved successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Error saving image: {e}")

    def hide_data(self):
        if self.image_path is None:
            messagebox.showwarning("Warning", "No image loaded.")
            return

        data = self.input_text.get("1.0", tk.END).strip()
        if not data:
            messagebox.showwarning("Warning", "No data to hide.")
            return

        try:
            # Use stegano to hide data
            output_path = "hidden_image.png"
            lsb.hide(self.image_path, message=data).save(output_path)
            self.image = Image.open(output_path)
            self.display_image()
            messagebox.showinfo("Success", "Data hidden in image and saved as hidden_image.png.")
            self.input_text.delete("1.0", tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Error hiding data: {e}")

    def show_data(self):
        if self.image_path is None:
            messagebox.showwarning("Warning", "No image loaded.")
            return

        try:
            # Use stegano to reveal data
            data = lsb.reveal(self.image_path)
            if data:
                messagebox.showinfo("Hidden Data", f"Data found: {data}")
            else:
                messagebox.showinfo("Hidden Data", "No hidden data found.")
        except Exception as e:
            messagebox.showerror("Error", f"Error revealing data: {e}")

    def display_image(self):
        resized_image = self.image.resize((500, 400))
        tk_image = ImageTk.PhotoImage(resized_image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
        self.canvas.image = tk_image

if __name__ == "__main__":
    root = tk.Tk()
    app = SteganographyApp(root)
    root.mainloop()
