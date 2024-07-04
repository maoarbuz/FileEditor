import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def new_file():
    text_area.delete(1.0, tk.END)
    root.title("Новый файл - Текстовый редактор")

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Все файлы", "*.*"), ("Текстовые файлы", "*.txt")])
    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(1.0, content)
            root.title(f"{file_path} - Текстовый редактор")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось открыть файл: {e}")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Все файлы", "*.*"), ("Текстовые файлы", "*.txt")])
    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                content = text_area.get(1.0, tk.END)
                file.write(content)
            root.title(f"{file_path} - Текстовый редактор")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")

root = tk.Tk()
root.title("Текстовый редактор")
root.geometry("600x400")

# Создание меню
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Новый", command=new_file)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.quit)
menu_bar.add_cascade(label="Файл", menu=file_menu)

root.config(menu=menu_bar)

# Создание текстового поля
text_area = tk.Text(root, wrap='word', font='Arial 12')
text_area.pack(expand=1, fill=tk.BOTH)

# Запуск главного цикла Tkinter
root.mainloop()
