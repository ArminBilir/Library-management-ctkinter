import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import re

languages = {
    "English": {
        "login": "Login",
        "register": "Register",
        "username": "Username",
        "password": "Password",
        "main_title": "Library Management System",
        "add_book": "Add Book",
        "view_books": "View All Books",
        "rented_books": "View Rented Books",
        "delete_book": "Delete Book",
        "rent_book": "Rent Book",
        "return_book": "Return Book",
        "book_id": "Book ID:",
        "author": "Author",
        "title": "Title",
        "email": "Email Address",
        "success": "Success",
        "error": "Error",
        "book_added": "Book added successfully!",
        "book_deleted": "Book deleted successfully!",
        "book_rented": "Book rented successfully!",
        "book_returned": "Book returned successfully!",
        "invalid_id": "Please enter a valid ID!",
        "login_successful": "Login successful!",
        "register_successful": "Registration successful!",
        "register_failed": "Username already exists!",
        "book_added": "The book has been added successfully.",
        "invalid_title": "The book title cannot be empty.",
        "invalid_author": "The author name cannot be empty.",
        "book_deleted": "The book has been deleted successfully.",
        "book_not_found": "The book does not exist in the database.",
        "add_book": "Add Book",
        "delete_book": "Delete Book",
        "title": "Book Title",
        "author": "Author Name",
        "no_book_found": "No book found with this ID!",
        "settings": "Settings",
        "select_theme": "Select Theme",
        "light_mode": "Light Mode",
        "dark_mode": "Dark Mode",
        "change_password": "Change Password",
        "current_password": "Current Password",
        "new_password": "New Password",
        "confirm_new_password": "Confirm New Password",
        "empty_current_password": "Current password cannot be empty.",
        "empty_new_password": "New password cannot be empty.",
        "passwords_not_match": "Passwords do not match.",
        "incorrect_current_password": "Current password is incorrect.",
        "password_changed": "Password changed successfully!"
    },
    "Türkçe": {
        "login": "Giriş Yap",
        "register": "Kayıt Ol",
        "username": "Kullanıcı Adı",
        "password": "Şifre",
        "email": "E-posta Adresi",
        "main_title": "Kütüphane Yönetim Sistemi",
        "add_book": "Kitap Ekle",
        "view_books": "Tüm Kitapları Görüntüle",
        "rented_books": "Kiralanan Kitapları Görüntüle",
        "delete_book": "Kitap Sil",
        "rent_book": "Kitap Kirala",
        "return_book": "Kiralanan Kitabı Geri Ver",
        "book_id": "Kitap ID:",
        "author": "Yazar",
        "title": "Kitap Adı",
        "success": "Başarılı",
        "error": "Hata",
        "book_added": "Kitap eklendi!",
        "book_deleted": "Kitap silindi!",
        "book_rented": "Kitap kiralandı!",
        "book_returned": "Kitap geri alındı!",
        "invalid_id": "Geçerli bir ID girin!",
        "login_successful": "Giriş başarılı!",
        "register_successful": "Kayıt başarılı!",
        "register_failed": "Bu kullanıcı adı zaten alınmış!",
        "book_added": "Kitap başarıyla eklendi.",
        "invalid_title": "Kitap adı boş bırakılamaz.",
        "invalid_author": "Yazar adı boş bırakılamaz.",
        "book_deleted": "Kitap başarıyla silindi.",
        "book_not_found": "Kitap veritabanında bulunamadı.",
        "add_book": "Kitap Ekle",
        "delete_book": "Kitap Sil",
        "title": "Kitap Adı",
        "author": "Yazar Adı",
        "no_book_found": "Bu ID'ye ait bir kitap bulunamadı!",
        "settings": "Ayarlar",
        "select_theme": "Tema Seç",
        "light_mode": "Açık Mod",
        "dark_mode": "Koyu Mod",
        "change_password": "Şifre Değiştir",
        "current_password": "Mevcut Şifre",
        "new_password": "Yeni Şifre",
        "confirm_new_password": "Yeni Şifreyi Onayla",
        "empty_current_password": "Mevcut şifre boş bırakılamaz.",
        "empty_new_password": "Yeni şifre boş bırakılamaz.",
        "passwords_not_match": "Şifreler uyuşmuyor.",
        "incorrect_current_password": "Mevcut şifre yanlış.",
        "password_changed": "Şifre başarıyla değiştirildi!"
    },
    "Deutsch": {
        "login": "Anmelden",
        "register": "Registrieren",
        "username": "Benutzername",
        "password": "Passwort",
        "email": "E-Mail-Adresse",
        "main_title": "Bibliothek Verwaltungssystem",
        "add_book": "Buch Hinzufügen",
        "view_books": "Alle Bücher Anzeigen",
        "rented_books": "Gemietete Bücher Anzeigen",
        "delete_book": "Buch Löschen",
        "rent_book": "Buch Mieten",
        "return_book": "Buch Zurückgeben",
        "book_id": "Buch ID:",
        "author": "Autor",
        "title": "Titel",
        "success": "Erfolg",
        "error": "Fehler",
        "book_added": "Buch erfolgreich hinzugefügt!",
        "book_deleted": "Buch erfolgreich gelöscht!",
        "book_rented": "Buch erfolgreich gemietet!",
        "book_returned": "Buch erfolgreich zurückgegeben!",
        "invalid_id": "Bitte geben Sie eine gültige ID ein!",
        "login_successful": "Anmeldung erfolgreich!",
        "register_successful": "Registrierung erfolgreich!",
        "register_failed": "Benutzername existiert bereits!",
        "book_added": "Das Buch wurde erfolgreich hinzugefügt.",
        "invalid_title": "Der Buchtitel darf nicht leer sein.",
        "invalid_author": "Der Autorenname darf nicht leer sein.",
        "book_deleted": "Das Buch wurde erfolgreich gelöscht.",
        "book_not_found": "Das Buch existiert nicht in der Datenbank.",
        "add_book": "Buch Hinzufügen",
        "delete_book": "Buch Löschen",
        "title": "Buchtitel",
        "author": "Autorname",
        "no_book_found": "Kein Buch mit dieser ID gefunden!",
        "settings": "Einstellungen",
        "select_theme": "Thema Auswählen",
        "light_mode": "Heller Modus",
        "dark_mode": "Dunkler Modus",
        "change_password": "Passwort Ändern",
        "current_password": "Aktuelles Passwort",
        "new_password": "Neues Passwort",
        "confirm_new_password": "Neues Passwort Bestätigen",
        "empty_current_password": "Das aktuelle Passwort darf nicht leer sein.",
        "empty_new_password": "Das neue Passwort darf nicht leer sein.",
        "passwords_not_match": "Die Passwörter stimmen nicht überein.",
        "incorrect_current_password": "Das aktuelle Passwort ist falsch.",
        "password_changed": "Das Passwort wurde erfolgreich geändert!"

    }
}

selected_language = "English"




def get_text(key):
    return languages[selected_language][key]


def connect_db():
    # SQLite connection
    conn = sqlite3.connect("library.db")
    return conn


def setup_database():
    conn = connect_db()
    cursor = conn.cursor()

    # Create users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            email TEXT
        )
    """)

    # Create books table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def login_user(username, password):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user


def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


def register_user(username, password, email):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", (username, password, email))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


# Kitap ekleme işlemi
def add_book(title, author):
    try:
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author, status) VALUES (?, ?, ?)", (title, author, "Available"))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        messagebox.showerror(get_text("error"), f"{get_text('db_error')} \n\n{e}")


def delete_book(book_id):
    try:
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()

        # Check if the book exists in the database and is available
        cursor.execute("SELECT * FROM books WHERE book_id = ?", (book_id,))
        book = cursor.fetchone()

        if book and book[3] == "Available":  # Verify status is 'Available'
            cursor.execute("DELETE FROM books WHERE book_id = ?", (book_id,))
            conn.commit()
            conn.close()
            return True
        else:
            conn.close()
            return False
    except sqlite3.Error as e:
        messagebox.showerror(get_text("error"), f"Database error: {e}")
        return False


def check_book_status(book_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE book_id = ?", (book_id,))
        book = cursor.fetchone()
        conn.close()

        if book:
            return book[3].strip().lower()  # Kitap durumu ('available' veya 'rented')
        else:
            return None  # Kitap yok
    except sqlite3.Error as e:
        messagebox.showerror(get_text("error"), f"Database error during check: {e}")
        return None


def rent_book(book_id):
    status = check_book_status(book_id)
    if status is None:
        messagebox.showerror(get_text("error"), get_text("no_book_found"))
        return False  # Kitap yok

    if status == "available":
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("UPDATE books SET status = 'Rented' WHERE book_id = ?", (book_id,))
            conn.commit()
            conn.close()
            messagebox.showinfo(get_text("success"), get_text("book_rented"))
            return True
        except sqlite3.Error as e:
            messagebox.showerror(get_text("error"), f"Database error during rent: {e}")
            return False
    else:
        messagebox.showerror(get_text("error"), "The book is already rented.")
        return False


def return_book(book_id):
    status = check_book_status(book_id)
    if status is None:
        messagebox.showerror(get_text("error"), get_text("no_book_found"))
        return False  # Kitap yok

    if status == "rented":
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("UPDATE books SET status = 'Available' WHERE book_id = ?", (book_id,))
            conn.commit()
            conn.close()
            messagebox.showinfo(get_text("success"), get_text("book_returned"))
            return True
        except sqlite3.Error as e:
            messagebox.showerror(get_text("error"), f"Database error during return: {e}")
            return False
    else:
        messagebox.showerror(get_text("error"), "The book is not currently rented.")
        return False


def list_books(status=None):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    if status:
        cursor.execute("SELECT * FROM books WHERE status = ?", (status,))
    else:
        cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return books


def update_widgets(window, rebuild_function):
    for widget in window.winfo_children():
        widget.destroy()
    rebuild_function(window)


def change_language(event, window, rebuild_function):
    global selected_language
    selected_language = language_var.get()
    update_widgets(window, rebuild_function)




def change_password_window(parent):
    def update_password():
        username = username_entry.get()
        current_password = current_password_entry.get()
        new_password = new_password_entry.get()
        confirm_password = confirm_password_entry.get()

        if not username or not current_password or not new_password:
            messagebox.showerror(get_text("error"), get_text("empty_current_password"))
            return

        if new_password != confirm_password:
            messagebox.showerror(get_text("error"), get_text("passwords_not_match"))
            return

        conn = connect_db()
        cursor = conn.cursor()

        # Check if the username and current password match
        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()

        if not result or result[0] != current_password:
            messagebox.showerror(get_text("error"), get_text("incorrect_current_password"))
            conn.close()
            return

        # Update the password
        cursor.execute("UPDATE users SET password = ? WHERE username = ?", (new_password, username))
        conn.commit()
        conn.close()

        messagebox.showinfo(get_text("success"), get_text("password_changed"))
        change_password_win.destroy()

    change_password_win = ctk.CTkToplevel(parent)
    change_password_win.title(get_text("change_password"))

    username_label = ctk.CTkLabel(change_password_win, text=get_text("username"))
    username_label.pack(pady=5)
    username_entry = ctk.CTkEntry(change_password_win)
    username_entry.pack(pady=5)

    current_password_label = ctk.CTkLabel(change_password_win, text=get_text("current_password"))
    current_password_label.pack(pady=5)
    current_password_entry = ctk.CTkEntry(change_password_win, show="*")
    current_password_entry.pack(pady=5)

    new_password_label = ctk.CTkLabel(change_password_win, text=get_text("new_password"))
    new_password_label.pack(pady=5)
    new_password_entry = ctk.CTkEntry(change_password_win, show="*")
    new_password_entry.pack(pady=5)

    confirm_password_label = ctk.CTkLabel(change_password_win, text=get_text("confirm_new_password"))
    confirm_password_label.pack(pady=5)
    confirm_password_entry = ctk.CTkEntry(change_password_win, show="*")
    confirm_password_entry.pack(pady=5)

    update_button = ctk.CTkButton(change_password_win, text=get_text("change_password"), command=update_password)
    update_button.pack(pady=20)

# Ayarlar penceresi

def open_settings_window(parent):
    settings_window = ctk.CTkToplevel(parent)
    settings_window.title(get_text("settings"))
    settings_window.geometry("300x200")

    # Theme selection
    ctk.CTkLabel(settings_window, text=get_text("select_theme")).pack(pady=10)
    ctk.CTkRadioButton(settings_window, text=get_text("light_mode"), variable=theme_mode, value="Light",
                       command=lambda: toggle_theme(parent)).pack()
    ctk.CTkRadioButton(settings_window, text=get_text("dark_mode"), variable=theme_mode, value="Dark",
                       command=lambda: toggle_theme(parent)).pack()

    # Change Password Button
    ctk.CTkButton(settings_window, text=get_text("change_password"),
                  command=lambda: change_password_window(settings_window)).pack(pady=20)

# Tema değiştirme fonksiyonu
def toggle_theme(parent):
    current_mode = ctk.get_appearance_mode()
    new_mode = "Dark" if current_mode == "Light" else "Light"
    ctk.set_appearance_mode(new_mode)

    mode = theme_mode.get()
    if mode == "Dark":
        parent.configure(bg="black")
        for widget in parent.winfo_children():
            widget
    else:
        parent.configure(bg="white")
        for widget in parent.winfo_children():
            widget





def login_window():
    def rebuild_login_window(window):
        global language_var, theme_mode

        theme_mode = ctk.StringVar(value="Light")

        window.title(get_text("login"))
        window.geometry("400x300")
        window.resizable(False, False)

        ctk.CTkLabel(window, text=get_text("username")).pack(pady=(20, 5))
        username_entry = ctk.CTkEntry(window)
        username_entry.pack(pady=5)
        ctk.CTkLabel(window, text=get_text("password")).pack(pady=(10, 5))
        password_entry = ctk.CTkEntry(window, show="*")
        password_entry.pack(pady=5)
        ctk.CTkButton(window, text=get_text("login"),
                      command=lambda: submit_login(username_entry.get(), password_entry.get())).pack(pady=(15, 5))
        ctk.CTkButton(window, text=get_text("register"), command=open_register_window).pack(pady=5)

        language_var = ctk.StringVar(value=selected_language)
        language_menu = ttk.Combobox(window, textvariable=language_var, values=list(languages.keys()), state="readonly",
                                     width=6)
        language_menu.place(x=310, y=10)
        language_menu.bind("<<ComboboxSelected>>", lambda event: change_language(event, window, rebuild_login_window))

        # Ayarlar butonu
        settings_button = ctk.CTkButton(window, text=languages[selected_language]["settings"],
                                        command=lambda: open_settings_window(window))
        settings_button.place(x=10, y=10)  # Sol üst köşe

    def submit_login(username, password):
        if login_user(username, password):
            messagebox.showinfo(get_text("success"), get_text("login_successful"))
            login.destroy()
            main_menu()
        else:
            messagebox.showerror(get_text("error"), get_text("invalid_id"))

    def open_register_window():
        def submit_register():
            username = username_entry.get().strip()
            password = password_entry.get().strip()
            email = email_entry.get().strip()

            # Alanların dolu olup olmadığını kontrol et
            if not username:
                messagebox.showerror("Error", "Username cannot be empty.")
                return
            if not password:
                messagebox.showerror("Error", "Password cannot be empty.")
                return
            if not email:
                messagebox.showerror("Error", "Email cannot be empty.")
                return
            if not is_valid_email(email):
                messagebox.showerror("Error", "Invalid email address format.")
                return

            # Kullanıcı kaydı
            if register_user(username, password, email):
                messagebox.showinfo("Success", "Registration successful!")
                register.destroy()
            else:
                messagebox.showerror("Error", "Registration failed. Username already exists.")

        register = ctk.CTkToplevel(login)
        register.title("Register")
        ctk.CTkLabel(register, text="Username:").pack(pady=(10, 5))
        username_entry = ctk.CTkEntry(register)
        username_entry.pack(pady=5)
        ctk.CTkLabel(register, text="Password:").pack(pady=(10, 5))
        password_entry = ctk.CTkEntry(register, show="*")
        password_entry.pack(pady=5)
        ctk.CTkLabel(register, text="Email:").pack(pady=(10, 5))
        email_entry = ctk.CTkEntry(register)
        email_entry.pack(pady=5)
        ctk.CTkButton(register, text="Register", command=submit_register).pack(pady=10)

    login = ctk.CTk()
    rebuild_login_window(login)
    login.mainloop()


def main_menu():
    def rebuild_main_menu(window):
        global language_var, theme_mode

        theme_mode = ctk.StringVar(value="Light")

        window.title(get_text("main_title"))
        window.geometry("500x500")
        window.resizable(False, False)

        main_frame = ctk.CTkFrame(window)
        main_frame.pack(expand=True)

        ctk.CTkLabel(main_frame, text=get_text("main_title"), font=("Arial", 16)).pack(pady=20)
        ctk.CTkButton(main_frame, text=get_text("add_book"), command=open_add_book_window).pack(pady=5)
        ctk.CTkButton(main_frame, text=get_text("view_books"), command=lambda: open_view_books_window()).pack(pady=5)
        ctk.CTkButton(main_frame, text=get_text("rented_books"), command=lambda: open_view_books_window("Rented")).pack(
            pady=5)
        ctk.CTkButton(main_frame, text=get_text("delete_book"), command=open_delete_book_window).pack(pady=5)
        ctk.CTkButton(main_frame, text=get_text("rent_book"), command=open_rent_book_window).pack(pady=5)
        ctk.CTkButton(main_frame, text=get_text("return_book"), command=open_return_book_window).pack(pady=5)

        language_var = ctk.StringVar(value=selected_language)
        language_menu = ttk.Combobox(window, textvariable=language_var, values=list(languages.keys()), state="readonly",
                                     width=6)
        language_menu.place(x=400, y=10)
        language_menu.bind("<<ComboboxSelected>>", lambda event: change_language(event, window, rebuild_main_menu))


        settings_button = ctk.CTkButton(window, text=languages[selected_language]["settings"],
                                        command=lambda: open_settings_window(window))
        settings_button.place(x=10, y=10)

    root = ctk.CTk()
    root.deiconify()
    rebuild_main_menu(root)
    root.mainloop()





def open_add_book_window():
    def submit_add_book():
        title = title_entry.get().strip()
        author = author_entry.get().strip()
        if not title:
            messagebox.showerror(get_text("error"), get_text("invalid_title"))
        elif not author:
            messagebox.showerror(get_text("error"), get_text("invalid_author"))
        else:
            add_book(title, author)
            messagebox.showinfo(get_text("success"), get_text("book_added"))

    add_window = ctk.CTkToplevel()
    add_window.title(get_text("add_book"))
    ctk.CTkLabel(add_window, text=get_text("title")).pack(pady=5)
    title_entry = ctk.CTkEntry(add_window)
    title_entry.pack(pady=5)
    ctk.CTkLabel(add_window, text=get_text("author")).pack(pady=5)
    author_entry = ctk.CTkEntry(add_window)
    author_entry.pack(pady=5)
    ctk.CTkButton(add_window, text=get_text("add_book"), command=submit_add_book).pack(pady=10)


def open_view_books_window(status=None):
    books_window = ctk.CTkToplevel()
    books_window.title(get_text("view_books"))

    frame = ctk.CTkFrame(books_window)
    frame.pack(fill=ctk.BOTH, expand=True)

    canvas = ctk.CTkCanvas(frame)
    scrollbar = ttk.Scrollbar(frame, orient=ctk.VERTICAL, command=canvas.yview)
    scrollable_frame = ctk.CTkFrame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)
    scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)

    books = list_books(status)
    for book in books:
        ctk.CTkLabel(scrollable_frame, text=f"ID: {book[0]} - {book[1]} by {book[2]} ({book[3]})").pack()


def open_delete_book_window():
    def submit_delete_book():
        book_id = book_id_entry.get().strip()
        if not book_id.isdigit():
            messagebox.showerror(get_text("error"), get_text("book_id"))
        elif not delete_book(int(book_id)):
            messagebox.showerror(get_text("error"), get_text("book_not_found"))
        else:
            messagebox.showinfo(get_text("success"), get_text("book_deleted"))

    delete_window = ctk.CTkToplevel()
    delete_window.title(get_text("delete_book"))
    ctk.CTkLabel(delete_window, text=get_text("book_id")).pack(pady=5)
    book_id_entry = ctk.CTkEntry(delete_window)
    book_id_entry.pack(pady=5)
    ctk.CTkButton(delete_window, text=get_text("delete_book"), command=submit_delete_book).pack(pady=10)



def open_rent_book_window():
    def submit_rent_book():
        book_id = book_id_entry.get()
        if book_id.isdigit():
            if rent_book(int(book_id)):
                messagebox.showinfo(get_text("success"), get_text("book_rented"))
            else:
                messagebox.showerror(get_text("error"), get_text("no_book_found"))
        else:
            messagebox.showerror(get_text("error"), get_text("invalid_id"))

    rent_window = ctk.CTkToplevel()
    rent_window.title(get_text("rent_book"))
    ctk.CTkLabel(rent_window, text=get_text("book_id")).pack(pady=5)
    book_id_entry = ctk.CTkEntry(rent_window)
    book_id_entry.pack(pady=5)
    ctk.CTkButton(rent_window, text=get_text("rent_book"), command=submit_rent_book).pack(pady=10)


def open_return_book_window():
    def submit_return_book():
        book_id = book_id_entry.get().strip()
        if book_id.isdigit():
            if return_book(int(book_id)):  # Yalnızca return_book işlemi çağrılır
                messagebox.showinfo(get_text("success"), get_text("book_returned"))
        else:
            messagebox.showerror(get_text("error"), get_text("invalid_id"))

    # Return Book Penceresi
    return_window = ctk.CTkToplevel()
    return_window.title(get_text("return_book"))
    ctk.CTkLabel(return_window, text=get_text("book_id")).pack(pady=5)
    book_id_entry = ctk.CTkEntry(return_window)
    book_id_entry.pack(pady=5)
    ctk.CTkButton(return_window, text=get_text("return_book"), command=submit_return_book).pack(pady=10)


if __name__ == "__main__":
    setup_database()
    login_window()