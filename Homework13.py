import tkinter as tk
from tkinter import filedialog, messagebox
class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Текстовый редактор")
        self.text_area = tk.Text(root, wrap='word', font=("Arial", 12))
        self.text_area.pack(expand=True, fill='both')
        self.save_button = tk.Button(root, text="Сохранить", command=self.save_file)
        self.save_button.pack(side='left', padx=5, pady=5)
        self.open_button = tk.Button(root, text="Открыть", command=self.open_file)
        self.open_button.pack(side='left', padx=5, pady=5)
        self.exit_button = tk.Button(root, text="Выход", command=root.quit)
        self.exit_button.pack(side='right', padx=5, pady=5)
        self.save_button.bind("<Enter>", lambda e: self.save_button.config(bg='lightblue'))
        self.save_button.bind("<Leave>", lambda e: self.save_button.config(bg='SystemButtonFace'))
        self.open_button.bind("<Enter>", lambda e: self.open_button.config(bg='lightblue'))
        self.open_button.bind("<Leave>", lambda e: self.open_button.config(bg='SystemButtonFace'))
        self.exit_button.bind("<Enter>", lambda e: self.exit_button.config(bg='lightblue'))
        self.exit_button.bind("<Leave>", lambda e: self.exit_button.config(bg='SystemButtonFace'))
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                   filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(self.text_area.get(1.0, tk.END))
            messagebox.showinfo("Сохранение", "Файл успешно сохранен!")
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())
            messagebox.showinfo("Открытие", "Файл успешно открыт!")
if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()
