import re
import csv
import random
from tkinter import Tk, StringVar, BooleanVar, messagebox
from tkinter.ttk import (
    Label,
    Entry,
    Button,
    Radiobutton,
    OptionMenu,
    Checkbutton,
)


class User:
    __re_name = re.compile(r"^[A-Za-z\s.]+$")
    __re__phone = re.compile(r"[1-9]{1}\d{9}")

    def __init__(self, name: str = "", phone: str = "") -> None:
        self.name = name
        self.phone = phone
        self.__invalid = {self.name: False, self.phone: False}

    # def name(self, name: str | None = None):
    #     if name is None:
    #         return self.name
    #     else:
    #         self.name = name

    # def phone(self, phone: str | None = None):
    #     if phone is None:
    #         return self.phone
    #     else:
    #         self.phone = phone

    def validate(self):
        name_match = User.__re_name.match(self.name)
        phone_match = User.__re__phone.match(self.phone)

        if name_match is None:
            self.__invalid.update({self.name: True})
            return False
        elif phone_match is None:
            self.__invalid.update({self.phone: True})
            return False
        else:
            return True


def load_boos(n: int):
    books = []
    with open(
        r"/home/bivas/devel/projects/python/dataset/goodreads_books.csv"
    ) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for rows in csv_reader:
            res = rows.get("Title")
            if res is not None:
                books.append(res)
    return random.sample(population=books, k=n)


def validation_error():
    messagebox.showerror(message="Please check your Name and Phone")


def book_not_selected():
    messagebox.showwarning(message="Please select a book you want to borrow")


def TandC_not_agreed():
    messagebox.showerror(message="You have to agree to the Library's T&C")


def onSubmit(name: Entry, phone: Entry, book: StringVar, TandC: BooleanVar):
    user = User(name=name.get(), phone=phone.get())

    if not user.validate():
        validation_error()
    else:
        # if TandC
        if book.get() == "Choose a book...":
            book_not_selected()
        elif TandC.get() == False:
            TandC_not_agreed()


def main():
    # construct a Tk window
    app = Tk()
    app.title("Library Management System")
    app.minsize(1280, 720)

    # configure grid geometry manager
    app.rowconfigure(
        index=0,
        weight=1,
    )
    app.rowconfigure(
        index=1,
        weight=1,
    )
    app.rowconfigure(
        index=2,
        weight=1,
    )
    app.rowconfigure(
        index=3,
        weight=1,
    )
    app.rowconfigure(
        index=4,
        weight=1,
    )
    app.columnconfigure(
        index=0,
        weight=1,
    )
    app.columnconfigure(
        index=1,
        weight=1,
    )

    # widgets go here
    name_label = Label(
        master=app,
        text="Full Name",
    )
    name_label.grid(
        row=0,
        column=0,
        sticky="new",
    )

    name_entry = Entry(
        master=app,
    )
    name_entry.grid(
        row=0,
        column=1,
        sticky="new",
    )

    phone_label = Label(
        master=app,
        text="Phone No.",
    )
    phone_label.grid(
        row=1,
        column=0,
        sticky="new",
    )

    phone_entry = Entry(
        master=app,
    )
    phone_entry.grid(
        row=1,
        column=1,
        sticky="new",
    )

    book_label = Label(
        master=app,
        text="Which book are you borrowing?",
    )
    book_label.grid(
        row=2,
        column=0,
        sticky="new",
    )

    # book_entry = Entry(
    #     master=app,
    # )
    # book_entry.grid(
    #     row=2,
    #     column=1,
    #     sticky="new",
    # )

    # book_label
    books = load_boos(16)
    book_option_var = StringVar()
    book_option = OptionMenu(
        app,
        book_option_var,
        "Choose a book...",
        *books,
    )
    book_option.grid(row=2, column=1, sticky="new")

    TandC_var = BooleanVar()
    TandC_checkbox = Checkbutton(
        master=app,
        text="I agree to the Terms & Conditions of this Library.",
        offvalue=False,
        onvalue=True,
        variable=TandC_var,
    )
    TandC_checkbox.grid(
        row=3,
        column=0,
        columnspan=2,
        sticky="sew",
    )

    submit_button = Button(
        master=app,
        text="Borrow",
        command=lambda: onSubmit(
            name_entry,
            phone_entry,
            books,
            TandC_var,
        ),
    )
    submit_button.grid(
        row=4,
        column=1,
        sticky="se",
    )

    # run the app
    app.mainloop()


if __name__ == "__main__":
    main()
