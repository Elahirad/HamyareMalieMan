# Financial Assistant written by Python and Tkinter
# Hamyare Malie Man
# Ali Elahiraad

from tkinter import *
from tkinter import messagebox
from Functions import *
import csv

logged_in = False
logged_username = ''
catched_data = []


def search_by_date_action():
    from_date_info = fromDateVar.get()
    to_date_info = toDateVar.get()
    i = 0
    END = len(catched_data)
    indexes_to_be_removed = []
    while i < END:
        if not (JalaliToGrg(catched_data[i]['date']) > JalaliToGrg(from_date_info) and JalaliToGrg(
                catched_data[i]['date']) < JalaliToGrg(to_date_info)):
            indexes_to_be_removed.append(i)
        i += 1
    M = 0
    for index in indexes_to_be_removed:
        catched_data.pop(index - M)
        M += 1
    root.destroy()
    main_screen()


def search_by_date():
    sd_sc = Toplevel(root)
    sd_sc.title('جستجو')
    sd_sc.geometry('400x400')
    sd_sc.config(bg='white')
    sd_sc.resizable(width=False, height=False)
    global fromDateVar
    global toDateVar
    fromDateVar = StringVar()
    toDateVar = StringVar()
    Label(sd_sc, text='فیلتر بر اساس تاریخ', font=('B Homa', '20', 'bold'), bg='white').pack()
    Label(sd_sc, text='فرمت صحیح تاریخ بصورت زیر می باشد', font=('B Nazanin', '10'), bg='white').pack()
    Label(sd_sc, text='روز/ماه/سال', font=('B Nazanin', '10'), bg='white').pack()
    Label(sd_sc, text='1400/01/01', bg='white').pack()
    Label(sd_sc, text='از تاریخ', font=('B Roya', '13'), bg='white').pack()
    Entry(sd_sc, textvariable=fromDateVar, bd='2', bg='#f7f7f7').pack()
    Label(sd_sc, text='تا تاریخ', font=('B Roya', '13'), bg='white').pack()
    Entry(sd_sc, textvariable=toDateVar, bd='2', bg='#f7f7f7').pack()
    Label(sd_sc, text='', bg='white').pack()
    Button(sd_sc, text='اعمال', width=10, height=1, command=search_by_date_action,
           font=('B Koodak', '10', 'bold'), bg='#0078D4', fg='white', bd='0',
           activeforeground='black',
           activebackground='#EBEBEB').pack()


def search_by_name_action():
    nameKeyWord_info = nameKeyWord.get()
    i = 0
    END = len(catched_data)
    indexes_to_be_removed = []
    while i < END:
        if nameKeyWord_info not in catched_data[i]['subject']:
            indexes_to_be_removed.append(i)
        i += 1
    M = 0
    for index in indexes_to_be_removed:
        catched_data.pop(index - M)
        M += 1
    root.destroy()
    main_screen()


def search_by_name():
    sn_sc = Toplevel(root)
    sn_sc.title('جستجو')
    sn_sc.geometry('400x300')
    sn_sc.config(bg='white')
    sn_sc.resizable(width=False, height=False)
    global nameKeyWord
    nameKeyWord = StringVar()
    Label(sn_sc, text='جستجو بر اساس عنوان', font=('B Homa', '20', 'bold'), bg='white').pack()
    Label(sn_sc, text='', bg='white').pack()
    Label(sn_sc, text='کلیدواژه', font=('B Roya', '13'), bg='white').pack()
    Entry(sn_sc, textvariable=nameKeyWord, bd='2', bg='#f7f7f7').pack()
    Label(sn_sc, text='', bg='white').pack()
    Button(sn_sc, text='جستجو', width=10, height=1, command=search_by_name_action,
           font=('B Koodak', '10', 'bold'), bg='#0078D4', fg='white', bd='0',
           activeforeground='black',
           activebackground='#EBEBEB').pack()


def search_by_type_action():
    typeKeyWord_info = typeKeyWord.get()
    i = 0
    END = len(catched_data)
    indexes_to_be_removed = []
    while i < END:
        if typeKeyWord_info not in catched_data[i]['type']:
            indexes_to_be_removed.append(i)
        i += 1
    M = 0
    for index in indexes_to_be_removed:
        catched_data.pop(index - M)
        M += 1
    root.destroy()
    main_screen()


def search_by_type():
    st_sc = Toplevel(root)
    st_sc.title('جستجو')
    st_sc.config(bg='white')
    st_sc.geometry('400x300')
    st_sc.resizable(width=False, height=False)
    global typeKeyWord
    typeKeyWord = StringVar()
    Label(st_sc, text='جستجو بر اساس نوع', font=('B Homa', '20', 'bold'), bg='white').pack()
    Label(st_sc, text='', bg='white').pack()
    Label(st_sc, text='کلیدواژه', font=('B Roya', '13'), bg='white').pack()
    Entry(st_sc, textvariable=typeKeyWord, bd='2', bg='#f7f7f7').pack()
    Label(st_sc, text='', bg='white').pack()
    Button(st_sc, text='جستجو', width=10, height=1, command=search_by_type_action,
           font=('B Koodak', '10', 'bold'), bg='#0078D4', fg='white', bd='0',
           activeforeground='black',
           activebackground='#EBEBEB').pack()


def search_by_amount_action():
    from_amount_info = fromAmountVar.get()
    to_amount_info = toAmountVar.get()
    i = 0
    END = len(catched_data)
    indexes_to_be_removed = []
    while i < END:
        if not (int(catched_data[i]['amount']) > int(from_amount_info) and int(
                catched_data[i]['amount']) < int(to_amount_info)):
            indexes_to_be_removed.append(i)
        i += 1
    M = 0
    for index in indexes_to_be_removed:
        catched_data.pop(index - M)
        M += 1
    root.destroy()
    main_screen()


def search_by_amount():
    sa_sc = Toplevel(root)
    sa_sc.title('جستجو')
    sa_sc.geometry('400x350')
    sa_sc.config(bg='white')
    sa_sc.resizable(width=False, height=False)
    global fromAmountVar
    global toAmountVar
    fromAmountVar = StringVar()
    toAmountVar = StringVar()
    Label(sa_sc, text='فیلتر بر اساس مبلغ', font=('B Homa', '20', 'bold'), bg='white').pack()
    Label(sa_sc, text='', bg='white').pack()
    Label(sa_sc, text='از مبلغ', font=('B Roya', '13'), bg='white').pack()
    Entry(sa_sc, textvariable=fromAmountVar, bd='2', bg='#f7f7f7').pack()
    Label(sa_sc, text='تا مبلغ', font=('B Roya', '13'), bg='white').pack()
    Entry(sa_sc, textvariable=toAmountVar, bd='2', bg='#f7f7f7').pack()
    Label(sa_sc, text='', bg='white').pack()
    Button(sa_sc, text='اعمال', width=10, height=1, command=search_by_amount_action,
           font=('B Koodak', '10', 'bold'), bg='#0078D4', fg='white', bd='0',
           activeforeground='black',
           activebackground='#EBEBEB').pack()


def search_reset():
    global catched_data
    catched_data = dataCatching(logged_username)
    root.destroy()
    main_screen()


def date_sort():  # Descending sort by date
    sortDataByDate(logged_username, True)
    global catched_data
    messagebox.showinfo("موفق", "مرتب سازی نزولی بر اساس تاریخ انجام گرفت")
    catched_data = dataCatching(logged_username)
    root.destroy()
    main_screen()


def date_sort2():  # Ascending sort by date
    sortDataByDate(logged_username, False)
    global catched_data
    messagebox.showinfo("موفق", "مرتب سازی صعودی بر اساس تاریخ انجام گرفت")
    catched_data = dataCatching(logged_username)
    root.destroy()
    main_screen()


def date_sort_screen():  # Sorting by date screen
    date_sc = Toplevel(root)
    date_sc.title('مرتب سازی')
    date_sc.config(bg='white')
    date_sc.geometry('400x200')
    date_sc.resizable(width=False, height=False)
    Label(date_sc, text='مرتب سازی بر اساس تاریخ', font=('B Homa', '20', 'bold'), bg='white').pack()
    Button(date_sc, text='مرتب سازی نزولی', width=10, height=1,
           font=('B Koodak', '10', 'bold'), command=date_sort, bg='#0078D4', fg='white', bd='0',
           activeforeground='black',
           activebackground='#EBEBEB').pack()
    Button(date_sc, text='مرتب سازی صعودی', width=10, height=1,
           font=('B Koodak', '10', 'bold'), command=date_sort2, bg='#0078D4', fg='white', bd='0',
           activeforeground='black',
           activebackground='#EBEBEB').pack()


def amount_sort():  # Descending sort by amount
    global catched_data
    sortDataByAmount(logged_username, True)
    messagebox.showinfo("موفق", "مرتب سازی نزولی بر اساس مبلغ انجام گرفت")
    catched_data = dataCatching(logged_username)
    root.destroy()
    main_screen()


def amount_sort2():  # Ascending sort by amount
    global catched_data
    sortDataByAmount(logged_username, False)
    messagebox.showinfo("موفق", "مرتب سازی صعودی بر اساس مبلغ انجام گرفت")
    catched_data = dataCatching(logged_username)
    root.destroy()
    main_screen()


def amount_sort_screen():  # Sorting by amount screen
    amount_sc = Toplevel(root)
    amount_sc.title('مرتب سازی')
    amount_sc.geometry('400x200')
    amount_sc.config(bg='white')
    amount_sc.resizable(width=False, height=False)
    Label(amount_sc, text='مرتب سازی بر اساس مبلغ', font=('B Koodak', '20', 'bold'), bg='white').pack()
    Button(amount_sc, text='مرتب سازی نزولی', width=10, height=1,
           font=('B Koodak', '10', 'bold'), command=amount_sort, bg='#0078D4', fg='white', bd='0',
           activeforeground='black',
           activebackground='#EBEBEB').pack()
    Button(amount_sc, text='مرتب سازی صعودی', width=10, height=1,
           font=('B Koodak', '10', 'bold'), command=amount_sort2, bg='#0078D4', fg='white', bd='0',
           activeforeground='black',
           activebackground='#EBEBEB').pack()


def delete_screen():  # Deleting item screen
    global catched_data
    deleteItem(logged_username, id_fetched)
    messagebox.showinfo("موفق", "داده مورد نظر با موفقیت حذف شد")
    catched_data = dataCatching(logged_username)
    root.destroy()
    main_screen()


def add_item():  # Adding new data to CSV files
    global catched_data
    amount_info = amountVar.get()
    subject_info = subjectVar.get()
    type_info = typeVar.get()
    date_info = dateVar.get()
    dataAdding(logged_username, amount_info, subject_info, type_info, date_info)
    catched_data = dataCatching(logged_username)
    messagebox.showinfo("موفق", "داده های شما با موفقیت اضافه شدند !")
    root.destroy()
    main_screen()


def add_item_screen():  # Adding item screen
    global amount_add_entry
    global subject_add_entry
    global type_add_entry
    global date_add_entry
    global amountVar
    global subjectVar
    global typeVar
    global dateVar
    add_sc = Toplevel(root)
    add_sc.title('ثبت مورد جدید')
    add_sc.geometry('400x550')
    add_sc.config(bg='white')
    add_sc.resizable(width=False, height=False)
    amountVar = StringVar()
    subjectVar = StringVar()
    typeVar = StringVar()
    dateVar = StringVar()
    Label(add_sc, text='ثبت مورد جدید', font=('B Homa', '20', 'bold'), bg='white').pack()
    Label(add_sc, text='', bg='white').pack()
    Label(add_sc, text='مبلغ', font=('B Roya', '13'), bg='white').pack()
    amount_add_entry = Entry(add_sc, textvariable=amountVar, bd='2', bg='#f7f7f7').pack()
    Label(add_sc, text='عنوان', font=('B Roya', '13'), bg='white').pack()
    subject_add_entry = Entry(add_sc, textvariable=subjectVar, bd='2', bg='#f7f7f7').pack()
    Label(add_sc, text='نوع', font=('B Roya', '13'), bg='white').pack()
    type_add_entry = Entry(add_sc, textvariable=typeVar, bd='2', bg='#f7f7f7').pack()
    Label(add_sc, text='تاریخ', font=('B Roya', '13'), bg='white').pack()
    date_add_entry = Entry(add_sc, textvariable=dateVar, bd='2', bg='#f7f7f7').pack()
    Label(add_sc, text='فرمت صحیح تاریخ بصورت زیر می باشد', font=('B Nazanin', '10'), bg='white').pack()
    Label(add_sc, text='روز/ماه/سال', font=('B Nazanin', '10'), bg='white').pack()
    Label(add_sc, text='1400/01/01', bg='white').pack()
    Button(add_sc, text='ثبت', width=10, height=1, command=add_item, font=('B Koodak', '10', 'bold'), bg='#0078D4',
           fg='white', bd='0',
           activeforeground='black',
           activebackground='#EBEBEB').pack()


def submit():  # Editing values
    global catched_data
    amount_value = entry1_value.get()
    subject_value = entry2_value.get()
    type_value = entry3_value.get()
    date_value = entry4_value.get()
    dataReplacing(logged_username, id_fetched, amount_value, subject_value, type_value, date_value)
    messagebox.showinfo("موفق", "داده های مورد نظر با موفقیت ویرایش شدند")
    catched_data = dataCatching(logged_username)
    root.destroy()
    main_screen()


def listbox_selected(event):  # Fetching selected item's data
    selection = event.widget.curselection()
    index = selection[0]
    targetSubject = str(event.widget.get(index))
    global id_fetched
    id_fetched = ''
    for char in targetSubject:
        if char.isnumeric():
            id_fetched += char
    for data in dataCatching(logged_username):
        if data['id'] == id_fetched:
            entry1_value.set(data['amount'])
            entry2_value.set(data['subject'])
            entry3_value.set(data['type'])
            entry4_value.set(data['date'])
            IDValue.set(data['id'])


def logout():  # Logging out
    global logged_in
    global logged_username
    logged_in = False
    logged_username = ''
    root.destroy()
    main_screen()


def login():  # Logging in and checking if username and password is correct
    global logged_in
    global logged_username
    global catched_data
    username_info2 = username2.get()
    password_info2 = password2.get()
    flag = False
    try:
        with open('Users.csv', 'r') as dataopening:
            csv_reading = list(csv.DictReader(dataopening))
            for user in csv_reading:
                if user['username'] == username_info2 and user['password'] == password_info2:
                    logged_in = True
                    logged_username = username_info2
                    messagebox.showinfo("موفق", "ورود با موفقیت صورت گرفت")
                    flag = True
                    catched_data = dataCatching(logged_username)
                    root.destroy()
                    main_screen()
                    break
    except AttributeError:
        messagebox.showerror("خطا", "خطایی صورت گرفت")
    if not flag:
        messagebox.showerror("خطا", "نام کاربری یا رمز عبور اشتباه می باشد")


def login_screen():  # Login screen
    global username2
    global password2
    global username_entry2
    global password_entry2
    log_sc = Toplevel(root)
    log_sc.config(bg='white')
    log_sc.title('ورود')
    log_sc.geometry('300x350')
    log_sc.resizable(width=False, height=False)
    username2 = StringVar()
    password2 = StringVar()
    Label(log_sc, text='ورود به حساب کاربری', font=('B Homa', '20', 'bold'), bg='white').pack()
    Label(log_sc, text='', bg='white').pack()
    Label(log_sc, text='نام کاربری', font=('B Roya', '13'), bg='white', ).pack()
    username_entry2 = Entry(log_sc, textvariable=username2, bd='2', bg='#f7f7f7').pack()
    Label(log_sc, text='رمز عبور', font=('B Roya', '13'), bg='white').pack()
    password_entry2 = Entry(log_sc, textvariable=password2, show='*', bd='2', bg='#f7f7f7').pack()
    Label(log_sc, text='', bg='white').pack()
    Button(log_sc, text='ورود', width=10, height=1, command=login, font=('B Koodak', '10', 'bold'), bg='#0078D4',
           fg='white', bd='0', activeforeground='black',
           activebackground='#EBEBEB').pack()


def register():  # Adding new user's data to CSV files
    username_info = username.get()
    password_info = password.get()
    flag = False
    with open('Users.csv', 'r') as dataopening:
        csv_reading = csv.DictReader(dataopening)
        for user in csv_reading:
            if user['username'] == username_info:
                flag = True
    if not flag:
        with open('Users.csv', 'a') as dataopening:
            field_names = ['username', 'password']
            csv_writing = csv.DictWriter(dataopening, fieldnames=field_names)
            csv_writing.writerow({'username': username_info, 'password': password_info})
            messagebox.showinfo("موفق", "کاربر با موفقیت ساخته شد")
            global logged_in
            global logged_username
            logged_in = True
            logged_username = username_info
            with open(f"{username_info}.csv", mode='w+') as dbcreate:
                field_names = ['id', 'amount', 'subject', 'type', 'date']
                csv_writing = csv.DictWriter(dbcreate, fieldnames=field_names)
                csv_writing.writeheader()
            root.destroy()
            main_screen()
    else:
        messagebox.showerror("خطا", "نام کاربری از قبل موجود می باشد")


def register_screen():  # register screen
    global username
    global password
    global username_entry
    global password_entry
    reg_sc = Toplevel(root)
    reg_sc.title('ثبت نام')
    reg_sc.geometry('300x350')
    reg_sc.config(bg='white')
    reg_sc.resizable(width=False, height=False)
    username = StringVar()
    password = StringVar()
    Label(reg_sc, text='ثبت کاربر جدید', font=('B Homa', '20', 'bold'), bg='white').pack()
    Label(reg_sc, text='', bg='white').pack()
    Label(reg_sc, text='نام کاربری', font=('B Roya', '13'), bg='white').pack()
    username_entry = Entry(reg_sc, textvariable=username, bd='2', bg='#f7f7f7').pack()
    Label(reg_sc, text='رمز عبور', font=('B Roya', '13'), bg='white').pack()
    password_entry = Entry(reg_sc, textvariable=password, bd='2', bg='#f7f7f7').pack()
    Label(reg_sc, text='', bg='white').pack()
    Button(reg_sc, text='ثبت نام', width=10, height=1, command=register, font=('B Koodak', '10', 'bold'), bg='#0078D4',
           fg='white', bd='0', activeforeground='black',
           activebackground='#EBEBEB').pack()


def main_screen():  # Main Loop
    global root
    global UserFrame
    global catched_data
    root = Tk()
    root.geometry("1200x700")
    root.resizable(width=False, height=False)
    root.config(bg='white')
    root.title('همیار مالی من')
    # ================================Login and Register Section================================
    UserFrame = Frame(root, bg='#2D78D6')
    UserFrame.pack(side=TOP)
    welcomeFrame = Frame(UserFrame)
    Label(welcomeFrame, text='همیار مالی من', width=root.winfo_screenwidth(), height=3,
          anchor=CENTER, bg='#2D78D6', fg='white', font=('B Titr', '20', 'bold')).pack(side=RIGHT)
    if not logged_in:
        user_frame = Frame(UserFrame, bg='white')
        Button(user_frame, text="ورود", height="1", width="15", command=login_screen,
               font=('B Koodak', '10', 'bold'), bg='#91C5F0', fg='white', bd='0', activeforeground='black',
               activebackground='#EBEBEB').pack(side=TOP)
        Button(user_frame, text="ثبت نام", height="1", width="15", command=register_screen,
               font=('B Koodak', '10', 'bold'), bg='#91C5F0', fg='white', bd='0', activeforeground='black',
               activebackground='#EBEBEB').pack(
            side=BOTTOM)
        user_frame.pack(side=LEFT)
    else:
        user_frame = Frame(UserFrame, bg='#2D78D6')
        Label(user_frame, text=f" وارد شده اید {logged_username} به عنوان ", height="1", width="45", bg='#2D78D6',
              fg='white', font=('B Koodak', '10', 'bold')).pack(side=TOP)
        Button(user_frame, text="خروج", height="1", width="15", command=logout, font=('B Koodak', '10', 'bold'),
               bg='#91C5F0', fg='white', bd='0', activeforeground='black',
               activebackground='#EBEBEB').pack(
            side=BOTTOM)
        user_frame.pack(side=LEFT)
    welcomeFrame.pack(side=RIGHT)

    if logged_in:
        midFrame = Frame(root, bg='white')
        selectFrame = Frame(midFrame, bg='white')
        dataFrame = Frame(midFrame, bg='white')
        # ================================Selecting Data Section================================
        addFrame = Frame(dataFrame, bg='white')
        Label(addFrame, text='            برای افزودن مورد از دکمه روبرو استفاده کنید', font=('B Titr', '10', 'bold'),
              anchor=CENTER, bg='white').pack(side=RIGHT)
        add_item_button = Button(addFrame, text='افزودن مورد جدید',
                                 command=add_item_screen, font=('B Koodak', '10', 'bold'),
                                 bg='#0078D4', fg='white', bd='0', activeforeground='black',
                                 activebackground='#EBEBEB')
        add_item_button.pack(side=LEFT)
        addFrame.pack()
        scrolled_listbox = Frame(selectFrame, bg='white')
        Label(selectFrame, text='انتخاب مورد', font=('B Titr', '20', 'bold'),
              anchor=CENTER, bg='white').pack(side=TOP)
        global listbox
        listbox = Listbox(scrolled_listbox)
        listbox.config(width='60')
        listbox.pack(side=LEFT, fill=BOTH)
        scrollbar = Scrollbar(scrolled_listbox)
        scrollbar.pack(side=RIGHT, fill=BOTH)
        for data in catched_data:
            listbox.insert(END, f"{data['subject']}|{data['id']}")
        listbox.bind("<<ListboxSelect>>", listbox_selected)
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)
        scrolled_listbox.pack(side=BOTTOM)
        selectFrame.pack(side=LEFT)
        # ================================Showing Data Section================================
        Label(dataFrame, text='داده های مورد انتخاب شده', font=('B Titr', '15', 'bold'), anchor=CENTER,
              bg='white').pack()
        Label(dataFrame,
              text='جهت تغییر دادن موارد میتوانید تغییرات خود را ایجاد کرده و بر روی دکمه اعمال تغییرات کلیک کنید',
              font=('B Nazanin', '8', 'bold'), anchor=CENTER, bg='white').pack()
        # ============================Globalizing variables============================
        dataFrame.config(width='80', height='100', bg='white')
        global entry1_value
        global entry2_value
        global entry3_value
        global entry4_value
        global IDValue
        global entry_1
        global entry_2
        global entry_3
        global entry_4
        entry1_value = StringVar()
        entry2_value = StringVar()
        entry3_value = StringVar()
        entry4_value = StringVar()
        IDValue = StringVar()
        id_frame1 = Frame(dataFrame, bg='white')
        entry_frame1 = Frame(dataFrame, bg='white')
        entry_frame2 = Frame(dataFrame, bg='white')
        entry_frame3 = Frame(dataFrame, bg='white')
        entry_frame4 = Frame(dataFrame, bg='white')
        id = Entry(id_frame1, textvariable=IDValue)
        entry_1 = Entry(entry_frame1, textvariable=entry1_value, width='60', bd='2', bg='#f7f7f7')
        entry_2 = Entry(entry_frame2, textvariable=entry2_value, width='60', bd='2', bg='#f7f7f7')
        entry_3 = Entry(entry_frame3, textvariable=entry3_value, width='60', bd='2', bg='#f7f7f7')
        entry_4 = Entry(entry_frame4, textvariable=entry4_value, width='60', bd='2', bg='#f7f7f7')
        Label(id_frame1, text=f"ID", font=('B Koodak', '10', 'bold'), bg='white').pack(side=RIGHT)
        id.config(state='readonly')
        id.pack(side=LEFT)
        Label(entry_frame1, text='مبلغ', font=('B Koodak', '10', 'bold'), anchor=E, bg='white').pack(side=RIGHT)
        entry_1.pack(side=LEFT)
        Label(entry_frame2, text='عنوان', font=('B Koodak', '10', 'bold'), anchor=E, bg='white').pack(side=RIGHT)
        entry_2.pack(side=LEFT)
        Label(entry_frame3, text='نوع  ', font=('B Koodak', '10', 'bold'), anchor=E, bg='white').pack(side=RIGHT)
        entry_3.pack(side=LEFT)
        Label(entry_frame4, text='تاریخ', font=('B Koodak', '10', 'bold'), anchor=E, bg='white').pack(side=RIGHT)
        entry_4.pack(side=LEFT)
        id_frame1.pack()
        entry_frame1.pack()
        entry_frame2.pack()
        entry_frame3.pack()
        entry_frame4.pack()
        submit_btn = Button(dataFrame, text='        ثبت تغییرات         ', command=submit,
                            font=('B Koodak', '10', 'bold'), bg='#0078D4', fg='white', bd='0', activeforeground='black',
                            activebackground='#EBEBEB')
        delete_btn = Button(dataFrame, text='         حذف مورد        ', command=delete_screen,
                            font=('B Koodak', '10', 'bold'), bg='#0078D4', fg='white', bd='0', activeforeground='black',
                            activebackground='#EBEBEB')
        date_sort_btn = Button(dataFrame, text='    مرتب سازی بر اساس تاریخ    ', command=date_sort_screen,
                               font=('B Koodak', '10', 'bold'), bg='#0078D4', fg='white', bd='0',
                               activeforeground='black',
                               activebackground='#EBEBEB')
        amount_sort_btn = Button(dataFrame, text='    مرتب سازی بر اساس مبلغ    ', command=amount_sort_screen,
                                 font=('B Koodak', '10', 'bold'), bg='#0078D4', fg='white', bd='0',
                                 activeforeground='black',
                                 activebackground='#EBEBEB')
        submit_btn.pack(side=LEFT)
        delete_btn.pack(side=LEFT)
        date_sort_btn.pack(side=LEFT)
        amount_sort_btn.pack(side=LEFT)
        dataFrame.pack(side=RIGHT)
        midFrame.pack(side=TOP)
        # ================================Searching Section================================
        bottom_frame = Frame(root)
        bottom_frame.config(bg='white')
        Label(bottom_frame, text='جستجو', font=('B Titr', '20'), bg='white').pack()
        Label(bottom_frame,
              text='می توانید برای ریست کردن جستجوهای خود از دکمه ریست که در پایین تعبیه شده استفاده نمایید',
              font=('B Nazanin', '10'), bg='white').pack()
        search_by_date_btn = Button(bottom_frame, text='فیلتر بر اساس تاریخ', command=search_by_date,
                                    font=('B Koodak', '10', 'bold'), bg='#0078D4', fg='white', bd='0',
                                    activeforeground='black',
                                    activebackground='#EBEBEB')
        search_by_name_btn = Button(bottom_frame, text='جستجو بر اساس عنوان', command=search_by_name,
                                    font=('B Koodak', '10', 'bold'), bg='#0078D4', fg='white', bd='0',
                                    activeforeground='black',
                                    activebackground='#EBEBEB')
        search_by_type_btn = Button(bottom_frame, text='جستجو بر اساس نوع', command=search_by_type,
                                    font=('B Koodak', '10', 'bold'), bg='#0078D4', fg='white', bd='0',
                                    activeforeground='black',
                                    activebackground='#EBEBEB')
        search_by_amount_btn = Button(bottom_frame, text='فیلتر بر اساس مبلغ', command=search_by_amount,
                                      font=('B Koodak', '10', 'bold'), bg='#0078D4', fg='white', bd='0',
                                      activeforeground='black',
                                      activebackground='#EBEBEB')
        search_reset_btn = Button(bottom_frame, text='ریست', command=search_reset, font=('B Titr', '15'), bg='#0078D4',
                                  fg='white', bd='0', activeforeground='black',
                                  activebackground='#EBEBEB')
        search_by_date_btn.pack(side=RIGHT)
        search_by_name_btn.pack(side=RIGHT)
        search_by_type_btn.pack(side=RIGHT)
        search_by_amount_btn.pack(side=RIGHT)
        Label(bottom_frame, text='       ', bg='white').pack(side=RIGHT)
        search_reset_btn.pack(side=RIGHT)
        bottom_frame.pack()
    root.mainloop()


main_screen()
