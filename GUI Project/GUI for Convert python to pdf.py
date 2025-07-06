import tkinter as tk
from tkinter import filedialog, messagebox
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

class PyToPdfConverterGUI:
    def __init__(self, master):
        self.master = master
        master.title(".py to PDF Converter")

        self.folder_path = tk.StringVar()

        # --- GUI Elements ---
        self.label = tk.Label(master, text="Select a folder containing .py files:")
        self.label.pack(pady=10)

        self.folder_entry = tk.Entry(master, textvariable=self.folder_path, width=50, state='disabled')
        self.folder_entry.pack(pady=5)

        self.browse_button = tk.Button(master, text="Browse", command=self.browse_folder)
        self.browse_button.pack(pady=5)

        self.convert_button = tk.Button(master, text="Convert to PDF", command=self.convert_files)
        self.convert_button.pack(pady=10)

        self.status_label = tk.Label(master, text="")
        self.status_label.pack(pady=5)

    def browse_folder(self):
        """Opens a dialog to select a folder."""
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_path.set(folder_selected)
            self.status_label.config(text=f"Selected folder: {folder_selected}")

    def convert_files(self):
        """Initiates the conversion process."""
        root_folder = self.folder_path.get()
        if not root_folder:
            messagebox.showwarning("Warning", "Please select a folder first.")
            return

        if not os.path.isdir(root_folder):
            messagebox.showerror("Error", "Invalid folder path.")
            return

        self.status_label.config(text="Starting conversion...")
        self.master.update_idletasks() # Update GUI immediately

        py_files_found = 0
        converted_count = 0

        try:
            # Walk through the directory and its subdirectories
            for dirpath, dirnames, filenames in os.walk(root_folder):
                for filename in filenames:
                    if filename.endswith(".py"):
                        py_files_found += 1
                        filepath = os.path.join(dirpath, filename)
                        output_pdf_path = os.path.splitext(filepath)[0] + ".pdf"

                        self.status_label.config(text=f"Converting: {filename}...")
                        self.master.update_idletasks()

                        try:
                            self.convert_py_to_pdf(filepath, output_pdf_path)
                            converted_count += 1
                        except Exception as e:
                            self.status_label.config(text=f"Error converting {filename}: {e}")
                            self.master.update_idletasks()
                            # Continue to the next file even if one fails

            self.status_label.config(text=f"Conversion complete. Converted {converted_count} of {py_files_found} .py files.")
            messagebox.showinfo("Success", f"Conversion complete. Converted {converted_count} of {py_files_found} .py files.")

        except Exception as e:
            self.status_label.config(text=f"An unexpected error occurred: {e}")
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def convert_py_to_pdf(self, py_filepath, output_pdf_path):
        """Converts a single .py file to PDF."""
        try:
            with open(py_filepath, 'r', encoding='utf-8') as f:
                code_content = f.read()

            doc = SimpleDocTemplate(output_pdf_path, pagesize=letter)
            story = []
            styles = getSampleStyleSheet()

            # Add the filename as a title
            title_style = styles['h2']
            story.append(Paragraph(os.path.basename(py_filepath), title_style))
            story.append(Spacer(1, 12))

            # Add the code content using Preformatted to preserve formatting
            code_style = styles['Code']
            # You might want to adjust font size or add line numbers here
            story.append(Preformatted(code_content, code_style))

            doc.build(story)

        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {py_filepath}")
        except Exception as e:
            raise Exception(f"Error during PDF generation for {py_filepath}: {e}")


if __name__ == "__main__":
    # Ensure reportlab is installed
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.lib import colors
    except ImportError:
        messagebox.showerror("Error", "reportlab library not found. Please install it using 'pip install reportlab'")
        exit()

    root = tk.Tk()
    app = PyToPdfConverterGUI(root)
    root.mainloop()
