import tkinter as tk
from tkinter import filedialog, messagebox

def expose_bits_to_file(input_path, output_path):
    try:
        with open(input_path, 'rb') as infile, open(output_path, 'w') as outfile:
            byte = infile.read(1)
            count = 0
            while byte:
                bits = format(ord(byte), '08b')
                outfile.write(bits + ' ')
                count += 1
                if count % 16 == 0:
                    outfile.write('\n')
                byte = infile.read(1)
        messagebox.showinfo("Success", f"Binary data written to:\n{output_path}")
    except FileNotFoundError:
        messagebox.showerror("Error", f"File not found: {input_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def select_input_file():
    path = filedialog.askopenfilename(title="Select Input File")
    if path:
        input_path_var.set(path)

def select_output_file():
    path = filedialog.asksaveasfilename(title="Select Output File", defaultextension=".txt",
                                        filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if path:
        output_path_var.set(path)

def run_conversion():
    input_path = input_path_var.get()
    output_path = output_path_var.get()
    if not input_path or not output_path:
        messagebox.showwarning("Missing Info", "Please select both input and output files.")
        return
    expose_bits_to_file(input_path, output_path)

# GUI setup
root = tk.Tk()
root.title("Binary Dumper")
root.geometry("400x300")
root.resizable(False, False)

input_path_var = tk.StringVar()
output_path_var = tk.StringVar()

# Input
tk.Label(root, text="Input File:").pack(pady=(10, 0))
tk.Entry(root, textvariable=input_path_var, width=50).pack()
tk.Button(root, text="Browse...", command=select_input_file).pack()

# Output
tk.Label(root, text="Output File:").pack(pady=(10, 0))
tk.Entry(root, textvariable=output_path_var, width=50).pack()
tk.Button(root, text="Browse...", command=select_output_file).pack()

# Convert button
tk.Button(root, text="Convert to Bits", command=run_conversion, bg="black", fg="white").pack(pady=15)

root.mainloop()
