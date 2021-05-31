#LIBRERIE
from tkinter import *
import string, random, smtplib
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql

#FUNZIONE CHE INVIA MAIL
def inviamail(messaggio, destinatario):
    mail = 'email@gmail.com'
    to_mail = destinatario
    password = 'password'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(mail, password)
    server.sendmail(mail, to_mail, messaggio.encode('utf-8'))

#FUNZIONE CHE CANCELLA I DATI
def clear():
    userentry.delete(0, END)
    passentry.delete(0, END)

#FUNZIONE CHE CHIUDE LA FINESTRA
def close():
    win.destroy()

#FUNZIONE DI LOGIN
def login():
    if conto.get() == "" or password.get() == "":
        messagebox.showerror("Errore", "Inserisci il conto e la password", parent=win)
    else:
        try:
            con = pymysql.connect(host="localhost", user="admin", password="admin", database="banca")
            cur = con.cursor()
            cur.execute("select * from clientev where conto=%s and password = %s", (conto.get(), password.get()))
            row = cur.fetchone()
            cur.execute("select mail from clientev where conto=%s ", (conto.get()))
            dest= cur.fetchone()
            if row == None:
                messagebox.showerror("Errore", "Conto o password errati", parent=win)
                if dest != None:
                    mess = ("Tentativo di accesso non autorizzato al tuo conto bancario")
                    inviamail(mess, dest)
            else:
                messagebox.showinfo("Successo", "Login effettuato con successo", parent=win)
                deshboard()
            con.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=win)

#FUNZIONE QUERY PER TUTTE LE RATE
def tutte(self):
    con = pymysql.connect(host="localhost", user="admin", password="admin", database="banca")
    cur = con.cursor()
    contox = conto.get()
    for record in self.get_children():
        self.delete(*self.get_children())
    print(cmutuo.get())
    if cmutuo.get() == '':
        cur.execute("select * from rata;")
        total = cur.rowcount
        for record in self.get_children():
            self.delete(*self.get_children())
        print("Total Data Entries:" + str(total))
        rows = cur.fetchall()
        nrata = ""
        interessi = ""
        importo = ""
        scadenza = ""
        stato = ""
        for row in rows:
            nrata = row[0]
            interessi = row[1]
            importo = row[2]
            scadenza = row[3]
            stato = row[4]
            self.insert("", 'end', text=nrata, values=(nrata, interessi, importo, scadenza, stato))
    else:
        cur.execute("select ccliente from mutuo where cmutuo='%s';" % (cmutuo.get()))
        ccliente = cur.fetchone()
        contogetto = "('%s',)" % (conto.get())
        if str(ccliente) == str(contogetto):
            cur.execute("select * from rata where cmutuo='%s';" % (cmutuo.get()))
            total = cur.rowcount
            for record in self.get_children():
                self.delete(*self.get_children())
            print("Total Data Entries:" + str(total))
            rows = cur.fetchall()
            nrata = ""
            interessi = ""
            importo = ""
            scadenza = ""
            stato = ""
            for row in rows:
                nrata = row[0]
                interessi = row[1]
                importo = row[2]
                scadenza = row[3]
                stato = row[4]
                self.insert("", 'end', text=nrata, values=(nrata, interessi, importo, scadenza, stato))

#FUNZIONE QUERY PER RATE NON PAGATE
def rnonpagate(self):
    con = pymysql.connect(host="localhost", user="admin", password="admin", database="banca")
    cur = con.cursor()
    contox = conto.get()
    for record in self.get_children():
        self.delete(*self.get_children())
    print(cmutuo.get())
    if cmutuo.get() == '':
        cur.execute("select * from rata where stato='non pagato';")
        total = cur.rowcount
        for record in self.get_children():
            self.delete(*self.get_children())
        print("Total Data Entries:" + str(total))
        rows = cur.fetchall()
        nrata = ""
        interessi = ""
        importo = ""
        scadenza = ""
        stato = ""
        for row in rows:
            nrata = row[0]
            interessi = row[1]
            importo = row[2]
            scadenza = row[3]
            stato = row[4]
            self.insert("", 'end', text=nrata, values=(nrata, interessi, importo, scadenza, stato))
    else:
        cur.execute("select ccliente from mutuo where cmutuo='%s';" % (cmutuo.get()))
        ccliente = cur.fetchone()
        contogetto = "('%s',)" % (conto.get())
        if str(ccliente) == str(contogetto):
            cur.execute("select * from rata where cmutuo='%s' and stato='non pagato';" % (cmutuo.get()))
            total = cur.rowcount
            for record in self.get_children():
                self.delete(*self.get_children())
            print("Total Data Entries:" + str(total))
            rows = cur.fetchall()
            nrata = ""
            interessi = ""
            importo = ""
            scadenza = ""
            stato = ""
            for row in rows:
                nrata = row[0]
                interessi = row[1]
                importo = row[2]
                scadenza = row[3]
                stato = row[4]
                self.insert("", 'end', text=nrata, values=(nrata, interessi, importo, scadenza, stato))

#FUNZIONE QUERY PER RATE PAGATE
def rpagate(self):
    con = pymysql.connect(host="localhost", user="admin", password="admin", database="banca")
    cur = con.cursor()
    contox = conto.get()
    for record in self.get_children():
        self.delete(*self.get_children())
    print(cmutuo.get())
    if cmutuo.get() == '':
        cur.execute("select * from rata where stato='pagato';")
        total = cur.rowcount
        for record in self.get_children():
            self.delete(*self.get_children())
        print("Total Data Entries:" + str(total))
        rows = cur.fetchall()
        nrata = ""
        interessi = ""
        importo = ""
        scadenza = ""
        stato = ""
        for row in rows:
            nrata = row[0]
            interessi = row[1]
            importo = row[2]
            scadenza = row[3]
            stato = row[4]
            self.insert("", 'end', text=nrata, values=(nrata, interessi, importo, scadenza, stato))
    else:
        cur.execute("select ccliente from mutuo where cmutuo='%s';" % (cmutuo.get()))
        ccliente = cur.fetchone()
        contogetto = "('%s',)" % (conto.get())
        if str(ccliente) == str(contogetto):
            cur.execute("select * from rata where cmutuo='%s' and stato='pagato';" % (cmutuo.get()))
            total = cur.rowcount
            for record in self.get_children():
                self.delete(*self.get_children())
            print("Total Data Entries:" + str(total))
            rows = cur.fetchall()
            nrata = ""
            interessi = ""
            importo = ""
            scadenza = ""
            stato = ""
            for row in rows:
                nrata = row[0]
                interessi = row[1]
                importo = row[2]
                scadenza = row[3]
                stato = row[4]
                self.insert("", 'end', text=nrata, values=(nrata, interessi, importo, scadenza, stato))

#FUNZIONE QUERY PER RATE IN SCADENZA
def rinscadenza(self):
    con = pymysql.connect(host="localhost", user="admin", password="admin", database="banca")
    cur = con.cursor()
    contox = conto.get()
    for record in self.get_children():
        self.delete(*self.get_children())
    print(cmutuo.get())
    if cmutuo.get()=='':
        cur.execute("select * from rata where stato='in scadenza';")
        total = cur.rowcount
        for record in self.get_children():
            self.delete(*self.get_children())
        print("Total Data Entries:" + str(total))
        rows = cur.fetchall()
        nrata = ""
        interessi = ""
        importo = ""
        scadenza = ""
        stato = ""
        for row in rows:
            nrata = row[0]
            interessi = row[1]
            importo = row[2]
            scadenza = row[3]
            stato = row[4]
            self.insert("", 'end', text=nrata, values=(nrata, interessi, importo, scadenza, stato))
    else:
        cur.execute("select ccliente from mutuo where cmutuo='%s';" % (cmutuo.get()))
        ccliente = cur.fetchone()
        contogetto= "('%s',)"%(conto.get())
        if  str(ccliente) == str(contogetto):
            cur.execute("select * from rata where cmutuo='%s' and stato='in scadenza';" % (cmutuo.get()))
            total = cur.rowcount
            for record in self.get_children():
                self.delete(*self.get_children())
            print("Total Data Entries:" + str(total))
            rows = cur.fetchall()
            nrata = ""
            interessi = ""
            importo = ""
            scadenza = ""
            stato = ""
            for row in rows:
                nrata = row[0]
                interessi = row[1]
                importo = row[2]
                scadenza = row[3]
                stato = row[4]
                self.insert("", 'end', text=nrata, values=(nrata, interessi, importo, scadenza, stato))

#PROCEDURA PER AGGIORNARE GLI UTENTI
def aggiorna(self):
    con = pymysql.connect(host="localhost", user="admin", password="admin", database="banca")
    cur = con.cursor()
    for record in self.get_children():
        self.delete(*self.get_children())
    cur.execute("select * from cliente")
    total = cur.rowcount
    for record in self.get_children():
        self.delete(*self.get_children())
    print("Total Data Entries:" + str(total))
    rows = cur.fetchall()
    nome = ""
    cognome = ""
    anni = ""
    mail = ""
    citta = ""
    via = ""
    conto = ""
    for row in rows:
        nome = row[0]
        cognome = row[1]
        anni = row[2]
        mail = row[3]
        citta = row[4]
        via = row[5]
        conto = row[6]
        self.insert("", 'end', text=nome, values=(nome, cognome, anni, mail, citta, via, conto))

#PROCEDURA PER RIFIUTARE L'UTENTE
def rifiuta(self):
    con = pymysql.connect(host="localhost", user="admin", password="admin", database="banca")
    cur = con.cursor()
    MsgBox = messagebox.askquestion('Rifiutare utente', 'Sei sicuro di voler rifiutare questo utente?', icon='warning', parent=self)
    if MsgBox == 'yes':
        for item in self.selection():
            selconto = self.item(item, "values")
        elimina= selconto[6]
        if elimina=='':
            MsgBox2 = messagebox.showinfo("Errore", "Seleziona un utente")
        else:
            mess="Ci dispiace la sua iscrizione alla 'Banca Copa' non è stata approvata"
            dest= selconto[3]
            inviamail(mess, dest)
            cur.execute("delete from cliente WHERE conto = '%s';" % (elimina))
            con.commit()
            messagebox.showinfo("Information", "Utente rifiutato correttamente", parent=self)

#PROCEDURA PER ACCETTARE L'UTENTE
def accettare(self):
    con = pymysql.connect(host="localhost", user="admin", password="admin", database="banca")
    cur = con.cursor()
    MsgBox = messagebox.askquestion('Accettato utente', 'Sei sicuro di voler accettare questo utente?', icon='warning', parent=self)
    if MsgBox == 'yes':
        for item in self.selection():
            selconto = self.item(item, "values")
        approva= selconto[6]
        mess = "Congratulazioni la sua iscrizione alla 'Banca Copa' è stata approvata!ricorda che il tuo numero conto per accedere è: '%s'" %(approva)
        print(mess)
        dest = selconto[3]
        inviamail(mess, dest)
        cur.execute("INSERT INTO clientev (nome, cognome, anni, mail, citta, via, conto, password) SELECT nome, cognome, anni, mail, citta, via, conto, password FROM cliente WHERE conto = '%s';" % (approva))
        cur.execute("delete from cliente WHERE conto = '%s';" % (approva))
        con.commit()
        messagebox.showinfo("Information", "Utente accettato correttamente", parent=self)

#FUNZIONE DESHBOARD UTENTE
def deshboard():
    des = tk.Toplevel()
    des.title("Banca Copa")
    des.maxsize(width=1024, height=600)
    des.minsize(width=1024, height=600)
    des.bg = ImageTk.PhotoImage(file='immagini/bg4.jpg')
    bg = Label(des, image=des.bg).place(x=0, y=0, relwidth=1, relheight=1)
    heading = Label(des, text=f"Nr conto : {conto.get()}", font='Verdana 20 bold')
    heading.place(x=512, y=75, anchor='center')
    #CONNESSIONE AL DATABASE
    con = pymysql.connect(host="localhost", user="admin", password="admin", database="banca")
    cur = con.cursor()
    #CREAZIONE TABELLA
    columns = ("#1", "#2", "#3", "#4", "#5")
    tabella = ttk.Treeview(des, show="headings", height="13", columns=columns)
    tabella.heading('#1', text='Nr Rata', anchor='center')
    tabella.column('#1', width=204, anchor='center', stretch = False)
    tabella.heading('#2', text='Quota Interessi', anchor='center')
    tabella.column('#2', width=204, anchor='center', stretch = False)
    tabella.heading('#3', text='Importo Rata', anchor='center')
    tabella.column('#3', width=204, anchor='center', stretch = False)
    tabella.heading('#4', text='Scadenza rata', anchor='center')
    tabella.column('#4', width=204, anchor='center', stretch = False)
    tabella.heading('#5', text='STATO', anchor='center')
    tabella.column('#5', width=204, anchor='center', stretch=False)
    tabella.place(y=150)

    #FILTRO MUTUO
    global cmutuo
    mutuo = StringVar()
    cmutuo = Entry(des, width=15, textvariable=mutuo)
    cmutuo.place(x=140, y=130, anchor='center')

    #BOTTONE PER LE RATE NON PAGATE
    btn_npagate = tk.Button(des, text="Rate non pagate", font=("Verdana 10 bold", 11), command=(lambda: rnonpagate(tabella)))
    btn_npagate.place(x=140, y=490, anchor='center')
    btn_npagate.config(width=15)
    #BOTTONE PER LE RATE PAGATE
    btn_pagate = tk.Button(des, text="Rate pagate", font=("Verdana 10 bold", 11), command=(lambda: rpagate(tabella)))
    btn_pagate.place(x=396, y=490, anchor='center')
    btn_pagate.config(width=15)
    #BOTTONE PER LE RATE IN SCADENZA
    btn_scadenza = tk.Button(des, text="Rate in scadenza", font=("Verdana 10 bold", 11), command=(lambda: rinscadenza(tabella)))
    btn_scadenza.place(x=652, y=490, anchor='center')
    btn_scadenza.config(width=15)
    #BOTTONE PER TUTTE LE RATE
    btn_tutte = tk.Button(des, text="Tutte le rate", font=("Verdana 10 bold", 11),command=(lambda: tutte(tabella)))
    btn_tutte.place(x=908, y=490, anchor='center')
    btn_tutte.config(width=15)

#FUNZIONE DESHBOARD ADMIN
def admin_deshboard():
    des = tk.Toplevel()
    des.title("Banca Copa")
    #des.attributes('-topmost', True)
    des.maxsize(width=1024, height=600)
    des.minsize(width=1024, height=600)
    des.bg = ImageTk.PhotoImage(file='immagini/bg3.jpg')
    bg = Label(des, image=des.bg).place(x=0, y=0, relwidth=1, relheight=1)
    #CONNESSIONE AL DATABSE
    con = pymysql.connect(host="localhost", user="admin", password="admin", database="banca")
    cur = con.cursor()
    #CREAZIONE TABELLA
    columns = ("#1", "#2", "#3", "#4", "#5", "#6", "#7")
    tabella = ttk.Treeview(des, show="headings", height="13", columns=columns)
    tabella.heading('#1', text='Nome', anchor='center')
    tabella.column('#1', width=146, anchor='center', stretch = False)
    tabella.heading('#2', text='Cognome', anchor='center')
    tabella.column('#2', width=146, anchor='center', stretch = False)
    tabella.heading('#3', text='Anni', anchor='center')
    tabella.column('#3', width=146, anchor='center', stretch = False)
    tabella.heading('#4', text='mail', anchor='center')
    tabella.column('#4', width=146, anchor='center', stretch = False)
    tabella.heading('#5', text='Città', anchor='center')
    tabella.column('#5', width=146, anchor='center', stretch = False)
    tabella.heading('#6', text='Via', anchor='center')
    tabella.column('#6', width=146, anchor='center', stretch = False)
    tabella.heading('#7', text='Conto', anchor='center')
    tabella.column('#7', width=146, anchor='center', stretch=False)
    tabella.place(y=140)
    #BOTTONE APPROVAZIONE
    btn_search = tk.Button(des, text="Approva", font=("Verdana 10 bold", 11), command=(lambda: accettare(tabella)))
    btn_search.place(x=312, y=490, anchor='center')
    btn_search.config(width=15)
    #BOTTONE RIFIUTA
    btn_rifiuta = tk.Button(des, text="Rifiuta", font=("Verdana 10 bold", 11),command=(lambda: rifiuta(tabella)))
    btn_rifiuta.place(x=512, y=490, anchor='center')
    btn_rifiuta.config(width=15)
    #BOTTONE AGGIORNA
    btn_aggiorna = tk.Button(des, text="Aggiorna", font=("Verdana 10 bold", 11),command=(lambda: aggiorna(tabella)))
    btn_aggiorna.place(x=712, y=490, anchor='center')
    btn_aggiorna.config(width=15)

#FUNZIONE CHE GENERA IL CODICE/CONTO
def conto_generatore(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

#FUNZIONE DI REGISTRAZIONE
def signup():
    def action():
        if nome.get() == "" or cognome.get() == "" or anni.get() == "" or citta.get() == "" or via.get() == "" or conto.get() == "" or password.get() == "" or very_pass.get() == "":
            messagebox.showerror("Errore", "Inserisci tutti i campi", parent=winsignup)
        elif int(anni.get())<= 17:
            messagebox.showerror("Errore", "Devi essere maggiorenne per creare un conto", parent=winsignup)
        elif password.get() != very_pass.get():
            messagebox.showerror("Errore", "Le password non coincidono", parent=winsignup)
        else:
            try:
                con = pymysql.connect(host="localhost", user="admin", password="admin", database="banca")
                cur = con.cursor()
                cur.execute("select * from cliente where conto=%s", conto.get())
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Errore", "User Name Already Exits", parent=winsignup)
                else:
                    codice_ins()
            except Exception as es:
                messagebox.showerror("Errore", f"Error Dui to : {str(es)}", parent=winsignup)

    def switch():
        winsignup.destroy()

    def clear():
        nome.delete(0, END)
        cognome.delete(0, END)
        anni.delete(0, END)
        mail.delete(0, END)
        citta.delete(0, END)
        via.delete(0, END)
        conto.delete(0, END)
        password.delete(0, END)
        very_pass.delete(0, END)

    def codice_ins():
        wcodice = tk.Toplevel()
        wcodice.title("Banca Copa")
        wcodice.maxsize(width=550, height=200)
        wcodice.minsize(width=550, height=200)
        #wcodice.attributes('-topmost', True)
        wcodice.bg = ImageTk.PhotoImage(file='immagini/bg5.jpg')
        bg = Label(wcodice, image=wcodice.bg).place(x=0, y=0, relwidth=1, relheight=1.3)
        inscodice = StringVar()
        inscodice = Entry(wcodice, width=60, textvariable=inscodice)
        inscodice.place(x=275, y=100, anchor='center')
        destinatario = mail.get()
        codiceinviato = conto_generatore(5)
        messa = "Il tuo codice di conferma è '%s'" % (codiceinviato)
        inviamail(messa, destinatario)

        def verifica():
            if inscodice.get() == '':
                messagebox.showerror("Errore", "Inserisci il codice", parent=wcodice)
            elif inscodice.get() != codiceinviato:
                messagebox.showerror("Errore", "Codice non corretto", parent=wcodice)
            else:
                con = pymysql.connect(host="localhost", user="admin", password="admin", database="banca")
                cur = con.cursor()
                cur.execute(
                    "insert into cliente(nome,cognome,anni, mail,citta,via,conto,password) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        nome.get(),
                        cognome.get(),
                        anni.get(),
                        mail.get(),
                        citta.get(),
                        via.get(),
                        conto.get(),
                        password.get()
                    ))

                con.commit()
                con.close()
                messagebox.showinfo("Successo", "Ragistrato con successo, prima di accedere attendi che un nostro operatore approvi il suo account", parent=wcodice)
                clear()
                switch()
                wcodice.destroy()
        btn_conferma = Button(wcodice, text="Conferma", font='Verdana 10 bold', command=(lambda: verifica()))
        btn_conferma.place(x=275, y=145, anchor='center')
        btn_conferma.config(width=10)
        return inscodice.get()


#REGISTRAZIONE
    winsignup = tk.Toplevel()
    winsignup.title("Banca Copa")
    winsignup.maxsize(width=500, height=700)
    winsignup.minsize(width=500, height=700)

    winsignup.bg = ImageTk.PhotoImage(file='immagini/bg2.jpg')
    bg = Label(winsignup, image=winsignup.bg).place(x=0, y=0, relwidth=1, relheight=1)
    nome = StringVar()
    cognome = StringVar()
    anni = IntVar(winsignup, value='0')
    mail = StringVar()
    citta = StringVar()
    via = StringVar()
    conto = StringVar(winsignup, value=conto_generatore(16))
    password = StringVar()
    very_pass = StringVar()

    nome = Entry(winsignup, width=40, textvariable=nome)
    nome.place(x=250, y=133, anchor='center')

    cognome = Entry(winsignup, width=40, textvariable=cognome)
    cognome.place(x=250, y=183, anchor='center')

    anni = Entry(winsignup, width=40, textvariable=anni)
    anni.place(x=250, y=233, anchor='center')

    mail = Entry(winsignup, width=40, textvariable=mail)
    mail.place(x=250, y=283, anchor='center')

    citta = Entry(winsignup, width=40, textvariable=citta)
    citta.place(x=250, y=333, anchor='center')

    via = Entry(winsignup, width=40, textvariable=via)
    via.place(x=250, y=383, anchor='center')

    conto = Entry(winsignup, width=40, textvariable=conto)
    conto.place(x=250, y=433, anchor='center')
    conto.config(state= DISABLED)

    password = Entry(winsignup, width=40, show="*", textvariable=password)
    password.place(x=250, y=483, anchor='center')

    very_pass = Entry(winsignup, width=40, show="*", textvariable=very_pass)
    very_pass.place(x=250, y=533, anchor='center')

    # button login and clear
    btn_signup = Button(winsignup, text="Registrati", font='Verdana 10 bold', command=action)
    btn_signup.place(x=200, y=600, anchor='center')
    btn_signup.config(width=18)

    btn_login = Button(winsignup, text="Cancella", font='Verdana 10 bold', command=clear)
    btn_login.place(x=365, y=600, anchor='center')

    sign_up_btn = Button(winsignup, text="Login", font='Verdana 10 bold', command=switch)
    sign_up_btn.place(x=455, y=40, anchor='center')

    winsignup.mainloop()

#FUNZIONE DI LOGIN ADMIN
def admin_login():
    if conto.get() == "" or password.get() == "":
        messagebox.showerror("Errore", "Inerisci il conto e la password", parent=win)
    else:
        try:
            con = pymysql.connect(host="localhost", user="admin", password="admin", database="banca")
            cur = con.cursor()
            cur.execute("select * from admin where conto=%s and password = %s", (conto.get(), password.get()))
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Errore", "Conto o password errati", parent=win)
            else:
                messagebox.showinfo("Successo", "Login effettuato con successo ", parent=win)
                #close()
                clear()
                admin_deshboard()
            con.close()
        except Exception as es:
            messagebox.showerror("Errore", f"Error Dui to : {str(es)}", parent=win)

#MENU E CONFIGURAZIONE FINESTRA
win = Tk()
win.title("Banca Copa")
win.maxsize(width=1024, height=600)
win.minsize(width=1024, height=600)
win.bg=ImageTk.PhotoImage(file='immagini/bg1.jpg')
bg= Label(win, image=win.bg).place(x=0, y=0, relwidth= 1, relheight=1)

conto = Label(win, text="Numero conto :", font='Verdana 10 bold')
conto.place(x=90, y=211)

userpass = Label(win, text="Password :", font='Verdana 10 bold')
userpass.place(x=90, y=248)

conto = StringVar()
password = StringVar()

userentry = Entry(win, width=60, textvariable=conto)
userentry.focus()
userentry.place(x=512, y=223, anchor='center')

passentry = Entry(win, width=60, show="*", textvariable=password)
passentry.place(x=512, y=260, anchor='center')

#BUTTONE DI LOGIN
btn_login = Button(win, text="Login", font='Verdana 10 bold', command=login)
btn_login.place(x=355, y=305, anchor='center')
btn_login.config(width=10)
#BUTTONE DI LOGIN ADMIN
btn_alogin = Button(win, text="Admin Login", font='Verdana 10 bold', command=admin_login)
btn_alogin.place(x=512, y=305, anchor='center')
btn_alogin.config(width=10)
#BUTTONE CHE CANCELLA I DATI INSERITI
btn_canc = Button(win, text="Cancella", font='Verdana 10 bold', command=clear)
btn_canc.place(x=669, y=305, anchor='center')
btn_canc.config(width=10)
#BUTTONE DI REGISTRAZIONE
sign_up_btn = Button(win, text="Registrati", font='Verdana 10 bold', command=signup)
sign_up_btn.place(x=512, y=450, anchor='center')
sign_up_btn.config(width=10)

win.mainloop()   
