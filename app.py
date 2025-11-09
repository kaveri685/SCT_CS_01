import tkinter as tk
from tkinter import messagebox, filedialog

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def on_encrypt():
    message = entry_message.get("1.0", tk.END).strip()
    try:
        shift = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Error", "Shift must be an integer")
        return

    result = encrypt(message, shift)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)

def on_decrypt():
    message = entry_message.get("1.0", tk.END).strip()
    try:
        shift = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Error", "Shift must be an integer")
        return

    result = decrypt(message, shift)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)

def save_result():
    text = output_box.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "No result to save")
        return

    filepath = filedialog.asksaveasfilename(
        initialdir="~/OneDrive/Documents",
        title="Save result",
        defaultextension=".txt",
        filetypes=(("Text Files", ".txt"), ("All Files", ".*"))
    )
    if filepath:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(text)
        messagebox.showinfo("Saved", f"Saved to:\n{filepath}")

# ---------------- GUI Setup -----------------
root = tk.Tk()
root.title("Caesar Cipher Tool")
root.geometry("600x450")
root.resizable(False, False)

label_message = tk.Label(root, text="Enter Message:")
label_message.pack()
entry_message = tk.Text(root, height=5, width=60)
entry_message.pack()

label_shift = tk.Label(root, text="Shift Value:")
label_shift.pack()
entry_shift = tk.Entry(root, width=10)
entry_shift.pack()

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_encrypt = tk.Button(frame_buttons, text="Encrypt", width=15, command=on_encrypt)
btn_encrypt.grid(row=0, column=0, padx=10)

btn_decrypt = tk.Button(frame_buttons, text="Decrypt", width=15, command=on_decrypt)
btn_decrypt.grid(row=0, column=1, padx=10)

label_output = tk.Label(root, text="Output:")
label_output.pack()
output_box = tk.Text(root, height=5, width=60)
output_box.pack()

btn_save = tk.Button(root, text="Save Result to OneDrive", command=save_result)
btn_save.pack(pady=10)

root.mainloop()