from tkinter import *
from tkcalendar import DateEntry
master = Tk()

#pack
#place
#grid
canvas = Canvas(master, height=450, width=750)
canvas.pack()
frame_ust=Frame(master, bg='#add8e6')
frame_ust.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

frame_alt_sol=Frame(master, bg='#add8e6')
frame_alt_sol.place(relx=0.1, rely=0.21, relwidth=0.23, relheight=0.5)

frame_alt_sag=Frame(master, bg='#add8e6')
frame_alt_sag.place(relx=0.34, rely=0.21, relwidth=0.56, relheight=0.5)

hatirlatma_tipi_etiket = Label(frame_ust, bg='#add8e6',text="Hatırlatma tipi",font="verdana 12 bold")
hatirlatma_tipi_etiket.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tipi_opsiyon= StringVar(frame_ust)
hatirlatma_tipi_opsiyon.set("\t")

hatirlatma_tipi_acilir_menu= OptionMenu(frame_ust,hatirlatma_tipi_opsiyon, "Doğum Günü", "Alışveriş", "Ödeme")
hatirlatma_tipi_acilir_menu.pack(padx=10,pady=10,side=LEFT)

hatirlatma_tarihi_etiket = Label(frame_ust, bg='#add8e6',text="Hatırlatma Tarihi",font="verdana 12 bold")
hatirlatma_tarihi_etiket.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tarih_secici = DateEntry(frame_ust, widh=12, background='orange', foreground='black', borderwidht=1, locale="de_DE")
hatirlatma_tarih_secici._top_cal.overrideredirect(False)
hatirlatma_tarih_secici.pack(padx=10, pady=10, side=LEFT)

Label(frame_alt_sol, bg='#add8e6', text="Hatırlatma Yöntemi",font="verdana 10 bold").pack(padx=10, pady=10, anchor=NW)

var= IntVar()

R1=Radiobutton(frame_alt_sol, text="Sisteme Kaydet", variable=var, value=1, bg='#add8e6', font="verdana 10" )
R1.pack(anchor=NW, pady=5, padx=15)

R2=Radiobutton(frame_alt_sol, text="E-posta gönder", variable=var, value=2, bg='#add8e6', font="verdana 10" )
R2.pack(anchor=NW, pady=5, padx=15)

var1=IntVar()
C1=Checkbutton(frame_alt_sol, text="Bir Hafta Önce", variable=var1, onvalue=1, offvalue=0,bg='#add8e6', font="verdana 10" )
C1.pack(anchor=NW, pady=2, padx=25)

var2=IntVar()
C2=Checkbutton(frame_alt_sol, text="Bir Gün Önce", variable=var2, onvalue=1, offvalue=0,bg='#add8e6', font="verdana 10" )
C2.pack(anchor=NW, pady=2, padx=25)

var3=IntVar()
C3=Checkbutton(frame_alt_sol, text="Aynı Gün", variable=var3, onvalue=1, offvalue=0,bg='#add8e6', font="verdana 10" )
C3.pack(anchor=NW, pady=2, padx=25)

def gonder():
    pass
    return

Label(frame_alt_sag, bg='#add8e6', text="Hatırlatma Mesajı",font="verdana 15 bold").pack(padx=10, pady=10, anchor=NW)

metin_alanı=Text(frame_alt_sag, height=9, width=50)
metin_alanı.tag_configure('style',foreground="#bfbfbf",font=('Verdena',7,'bold'))
metin_alanı.pack()
karilama_metni="Mesajını buraya gir"
metin_alanı.insert(END, karilama_metni,'style')

gonder_butonu=Button(frame_alt_sag, text="Gönder", command=gonder)

gonder_butonu.pack(anchor=S)

master.mainloop()
