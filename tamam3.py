import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json

aktif_kullanici = None

root = tk.Tk()
root.title("Film Listeleme Uygulamasi")
root.geometry("800x600")
root.configure(bg="#2c3e50")

baslik_label = tk.Label(root, text="Film Listeleme Uygulamasi", font=("Arial", 18, "bold"), fg="#ffffff", bg="#2c3e50")
baslik_label.pack(pady=20)

giris_frame = tk.Frame(root, bg="#34495e", bd=5)
giris_frame.pack(pady=20, padx=20, fill="both", expand=True)

kullanici_adi_label = tk.Label(giris_frame, text="Kullanici adi:", font=("Arial", 14), fg="#ffffff", bg="#34495e")
kullanici_adi_label.grid(row=0, column=0, pady=10, padx=20, sticky="nsew")
kullanici_adi_entry = ttk.Entry(giris_frame, font=("Arial", 12))
kullanici_adi_entry.grid(row=0, column=1, pady=10, padx=10, sticky="nsew")

sifre_label = tk.Label(giris_frame, text="Sifre:", font=("Arial", 14), fg="#ffffff", bg="#34495e")
sifre_label.grid(row=1, column=0, pady=10, padx=20, sticky="nsew")
sifre_entry = ttk.Entry(giris_frame, font=("Arial", 12), show="*")
sifre_entry.grid(row=1, column=1, pady=10, padx=10, sticky="nsew")

def giris_yap():
    global aktif_kullanici
    kadi = kullanici_adi_entry.get().strip()
    sif = sifre_entry.get().strip()
    try:
        with open("users.json", "r", encoding="utf-8") as f:
            users_data = json.load(f)
    except FileNotFoundError:
        users_data = {}
    if kadi in users_data and users_data[kadi]["password"] == sif:
        aktif_kullanici = kadi
        messagebox.showinfo("Giris Basarili", "Hos geldin, " + kadi + "!")
        giris_frame.pack_forget()
        kayit_label.place_forget()
        sifremi_unuttum_label.place_forget()
        eserlerim_ekrani()
    else:
        messagebox.showerror("Hatali", "Kullanici adi veya sifre hatali!")

def hesap_olustur_ekrani():
    giris_frame.pack_forget()
    kayit_label.place_forget()
    sifremi_unuttum_label.place_forget()
    kayit_frame = tk.Frame(root, bg="#34495e", bd=5)
    kayit_frame.pack(pady=20, padx=20, fill="both", expand=True)

    tk.Label(kayit_frame, text="Kullanici adi:", font=("Arial", 12), fg="#ffffff", bg="#34495e").grid(row=0, column=0, pady=10, padx=10, sticky="e")
    yeni_kadi_entry = ttk.Entry(kayit_frame, font=("Arial", 12))
    yeni_kadi_entry.grid(row=0, column=1, pady=10, padx=10, sticky="ew")

    tk.Label(kayit_frame, text="Sifre:", font=("Arial", 12), fg="#ffffff", bg="#34495e").grid(row=1, column=0, pady=10, padx=10, sticky="e")
    yeni_sifre_entry = ttk.Entry(kayit_frame, font=("Arial", 12), show="*")
    yeni_sifre_entry.grid(row=1, column=1, pady=10, padx=10, sticky="ew")

    tk.Label(kayit_frame, text="En sevdiginiz hayvan:", font=("Arial", 12), fg="#ffffff", bg="#34495e").grid(row=2, column=0, pady=10, padx=10, sticky="e")
    yeni_hayvan_entry = ttk.Entry(kayit_frame, font=("Arial", 12))
    yeni_hayvan_entry.grid(row=2, column=1, pady=10, padx=10, sticky="ew")

    def kaydet_hesap():
        kadi = yeni_kadi_entry.get().strip()
        sifr = yeni_sifre_entry.get().strip()
        hayv = yeni_hayvan_entry.get().strip()
        if not kadi or not sifr or not hayv:
            messagebox.showerror("Hata", "Tum alanlari doldurmalisiniz!")
            return
        try:
            with open("users.json", "r", encoding="utf-8") as f:
                users_data = json.load(f)
        except FileNotFoundError:
            users_data = {}
        if kadi in users_data:
            messagebox.showerror("Hata", "Bu kullanici adi zaten var!")
        else:
            users_data[kadi] = {"password": sifr, "favorite_animal": hayv}
            with open("users.json", "w", encoding="utf-8") as f:
                json.dump(users_data, f, indent=4, ensure_ascii=False)
            messagebox.showinfo("Basarili", "Hesap basariyla olusturuldu!")
            kayit_frame.pack_forget()
            giris_frame.pack(pady=20, padx=20, fill="both", expand=True)
            kayit_label.place(relx=0.95, rely=0.95, anchor="se")
            sifremi_unuttum_label.place(relx=0.05, rely=0.95, anchor="sw")

    def geri():
        kayit_frame.pack_forget()
        giris_frame.pack(pady=20, padx=20, fill="both", expand=True)
        kayit_label.place(relx=0.95, rely=0.95, anchor="se")
        sifremi_unuttum_label.place(relx=0.05, rely=0.95, anchor="sw")

    ttk.Button(kayit_frame, text="Hesap Olustur", command=kaydet_hesap).grid(row=3, column=0, columnspan=2, pady=20)
    ttk.Button(kayit_frame, text="Geri", command=geri).grid(row=4, column=0, columnspan=2, pady=10)

def sifremi_unuttum_ekrani():
    giris_frame.pack_forget()
    kayit_label.place_forget()
    sifremi_unuttum_label.place_forget()
    sifre_unuttum_frame = tk.Frame(root, bg="#34495e", bd=5)
    sifre_unuttum_frame.pack(pady=20, padx=20, fill="both", expand=True)

    tk.Label(sifre_unuttum_frame, text="Kullanici adi:", font=("Arial", 12), fg="#ffffff", bg="#34495e").grid(row=0, column=0, pady=10, padx=10, sticky="e")
    kadi_fp_entry = ttk.Entry(sifre_unuttum_frame, font=("Arial", 12))
    kadi_fp_entry.grid(row=0, column=1, pady=10, padx=10, sticky="ew")

    tk.Label(sifre_unuttum_frame, text="En sevdiginiz hayvan:", font=("Arial", 12), fg="#ffffff", bg="#34495e").grid(row=1, column=0, pady=10, padx=10, sticky="e")
    hayvan_fp_entry = ttk.Entry(sifre_unuttum_frame, font=("Arial", 12))
    hayvan_fp_entry.grid(row=1, column=1, pady=10, padx=10, sticky="ew")

    def dogrula_bilgiler():
        kadi = kadi_fp_entry.get().strip()
        hayv = hayvan_fp_entry.get().strip()
        try:
            with open("users.json", "r", encoding="utf-8") as f:
                users_data = json.load(f)
        except FileNotFoundError:
            users_data = {}
        if kadi in users_data and users_data[kadi]["favorite_animal"] == hayv:
            sifre_unuttum_frame.pack_forget()
            sifre_sifirla_frame = tk.Frame(root, bg="#34495e", bd=5)
            sifre_sifirla_frame.pack(pady=20, padx=20, fill="both", expand=True)

            tk.Label(sifre_sifirla_frame, text="Yeni sifre:", font=("Arial", 12), fg="#ffffff", bg="#34495e").grid(row=0, column=0, pady=10, padx=10, sticky="e")
            yeni_s1_entry = ttk.Entry(sifre_sifirla_frame, font=("Arial", 12), show="*")
            yeni_s1_entry.grid(row=0, column=1, pady=10, padx=10, sticky="ew")

            tk.Label(sifre_sifirla_frame, text="Yeni sifre (tekrar):", font=("Arial", 12), fg="#ffffff", bg="#34495e").grid(row=1, column=0, pady=10, padx=10, sticky="e")
            yeni_s2_entry = ttk.Entry(sifre_sifirla_frame, font=("Arial", 12), show="*")
            yeni_s2_entry.grid(row=1, column=1, pady=10, padx=10, sticky="ew")

            def sifre_degistir():
                s1 = yeni_s1_entry.get().strip()
                s2 = yeni_s2_entry.get().strip()
                if s1 != s2:
                    messagebox.showerror("Hata", "Sifreler eslesmiyor!")
                    return
                users_data[kadi]["password"] = s1
                with open("users.json", "w", encoding="utf-8") as fw:
                    json.dump(users_data, fw, indent=4, ensure_ascii=False)
                messagebox.showinfo("Basarili", "Sifre basariyla degistirildi!")
                sifre_sifirla_frame.pack_forget()
                giris_frame.pack(pady=20, padx=20, fill="both", expand=True)
                kayit_label.place(relx=0.95, rely=0.95, anchor="se")
                sifremi_unuttum_label.place(relx=0.05, rely=0.95, anchor="sw")
        else:
            messagebox.showerror("Hata", "Bilgiler hatali!")

    def geri():
        sifre_unuttum_frame.pack_forget()
        giris_frame.pack(pady=20, padx=20, fill="both", expand=True)
        kayit_label.place(relx=0.95, rely=0.95, anchor="se")
        sifremi_unuttum_label.place(relx=0.05, rely=0.95, anchor="sw")

    ttk.Button(sifre_unuttum_frame, text="Dogrula", command=dogrula_bilgiler).grid(row=2, column=0, columnspan=2, pady=20)
    ttk.Button(sifre_unuttum_frame, text="Geri", command=geri).grid(row=3, column=0, columnspan=2, pady=10)

def eserlerim_ekrani():
    global aktif_kullanici
    try:
        with open("collection.json", "r", encoding="utf-8") as f:
            collection_data = json.load(f)
    except FileNotFoundError:
        collection_data = {}
    if aktif_kullanici not in collection_data:
        collection_data[aktif_kullanici] = []
        with open("collection.json", "w", encoding="utf-8") as f:
            json.dump(collection_data, f, indent=4, ensure_ascii=False)
    try:
        with open("movies.json", "r", encoding="utf-8") as fm:
            tum_filmler = json.load(fm)
    except FileNotFoundError:
        tum_filmler = []

    eserler_frame = tk.Frame(root, bg="#34495e", bd=5)
    eserler_frame.pack(pady=20, padx=20, fill="both", expand=True)

    ust_frame = tk.Frame(eserler_frame, bg="#34495e")
    ust_frame.pack(fill="x", pady=(0,10))
    ust_frame.columnconfigure(0, weight=0)
    ust_frame.columnconfigure(1, weight=1)

    def ana_menuye_don():
        eserler_frame.pack_forget()
        giris_frame.pack(pady=20, padx=20, fill="both", expand=True)
        kayit_label.place(relx=0.95, rely=0.95, anchor="se")
        sifremi_unuttum_label.place(relx=0.05, rely=0.95, anchor="sw")

    geri_buton = ttk.Button(ust_frame, text="Ana menuye don", command=ana_menuye_don)
    geri_buton.grid(row=0, column=0, sticky="w", padx=5)

    baslik_eserler_label = tk.Label(ust_frame, text="Eserlerim", font=("Arial", 18, "bold"), fg="#ffffff", bg="#34495e")
    baslik_eserler_label.grid(row=0, column=1, pady=5)

    kolonlar = ("adi","k_durum","IMBDpuani","turu","k_puan","k_not","yili")
    eser_tree = ttk.Treeview(eserler_frame, columns=kolonlar, show="headings")
    eser_tree.pack(pady=10, padx=10, fill="both", expand=True)

    eser_tree.heading("adi", text="Adi")
    eser_tree.heading("k_durum", text="Durum")
    eser_tree.heading("IMBDpuani", text="IMBD Puani")
    eser_tree.heading("turu", text="Turu")
    eser_tree.heading("k_puan", text="Puan")
    eser_tree.heading("k_not", text="Not")
    eser_tree.heading("yili", text="Yili")

    eser_tree.column("adi", width=160)
    eser_tree.column("k_durum", width=90)
    eser_tree.column("IMBDpuani", width=80)
    eser_tree.column("turu", width=80)
    eser_tree.column("k_puan", width=70)
    eser_tree.column("k_not", width=150)
    eser_tree.column("yili", width=80)

    def tabloyu_guncelle():
        for item in eser_tree.get_children():
            eser_tree.delete(item)
        for kayit in collection_data[aktif_kullanici]:
            mid = kayit.get("movie_id")
            kd = kayit.get("k_durum","Bilinmiyor")
            kp = kayit.get("k_puan","Belirtilmemis")
            kn = kayit.get("k_not","Not yok")
            hedef = None
            for mv in tum_filmler:
                if mv.get("id") == mid:
                    hedef = mv
                    break
            if hedef:
                eser_tree.insert("", tk.END, values=(
                    hedef.get("adi",""),
                    kd,
                    hedef.get("IMBDpuani",""),
                    hedef.get("turu",""),
                    kp,
                    kn,
                    hedef.get("yili","")
                ))

    def eser_ekle():
        eserler_frame.pack_forget()
        tur_secimi_ekrani()

    def eser_sil():
        secili = eser_tree.selection()
        if not secili:
            messagebox.showerror("Hata", "Silmek icin bir kayit secmelisiniz!")
            return
        index = eser_tree.index(secili)
        confirm = messagebox.askyesno("Emin misiniz?", "Secili eseri silmek istiyor musunuz?")
        if confirm:
            eser_tree.delete(secili)
            del collection_data[aktif_kullanici][index]
            with open("collection.json", "w", encoding="utf-8") as f:
                json.dump(collection_data, f, indent=4, ensure_ascii=False)

    def eser_duzenle():
        secili = eser_tree.selection()
        if not secili:
            messagebox.showerror("Hata", "Duzenlemek icin bir kayit secmelisiniz!")
            return
        index = eser_tree.index(secili)
        mevcut = collection_data[aktif_kullanici][index]
        k_durum = mevcut.get("k_durum","Bilinmiyor")
        k_puan  = mevcut.get("k_puan","Belirtilmemis")
        k_not   = mevcut.get("k_not","Not yok")

        duzen_pencere = tk.Toplevel(root)
        duzen_pencere.title("Eser Duzenle")
        duzen_pencere.geometry("300x300")
        duzen_pencere.configure(bg="#34495e")

        tk.Label(duzen_pencere, text="Durum:", bg="#34495e", fg="white", font=("Arial", 12)).pack(pady=5)
        durum_combobox = ttk.Combobox(duzen_pencere, values=["Izlenecek", "Izleniyor", "Izlendi", "Bilinmiyor"], state="readonly")
        durum_combobox.set(k_durum)
        durum_combobox.pack()

        tk.Label(duzen_pencere, text="Puan (1-5):", bg="#34495e", fg="white", font=("Arial", 12)).pack(pady=5)
        puan_combobox = ttk.Combobox(duzen_pencere, values=["1","2","3","4","5","Belirtilmemis"], state="readonly")
        puan_combobox.set(k_puan)
        puan_combobox.pack()

        tk.Label(duzen_pencere, text="Not:", bg="#34495e", fg="white", font=("Arial", 12)).pack(pady=5)
        not_text = tk.Text(duzen_pencere, font=("Arial", 12), height=4, width=25)
        not_text.pack()
        not_text.insert("1.0", k_not if k_not != "Not yok" else "")

        def kaydet_degisim():
            yeni_durum = durum_combobox.get()
            yeni_puan = puan_combobox.get()
            yeni_not = not_text.get("1.0","end").strip()
            if not yeni_not:
                yeni_not = "Not yok"
            collection_data[aktif_kullanici][index]["k_durum"] = yeni_durum
            collection_data[aktif_kullanici][index]["k_puan"]  = yeni_puan
            collection_data[aktif_kullanici][index]["k_not"]   = yeni_not
            with open("collection.json", "w", encoding="utf-8") as fcw:
                json.dump(collection_data, fcw, indent=4, ensure_ascii=False)
            duzen_pencere.destroy()
            tabloyu_guncelle()
            messagebox.showinfo("Basarili", "Degisiklikler kaydedildi!")

        ttk.Button(duzen_pencere, text="Kaydet", command=kaydet_degisim).pack(pady=20)

    buton_frame = tk.Frame(eserler_frame, bg="#34495e")
    buton_frame.pack(side="left", fill="y", padx=10, pady=10)

    ttk.Button(buton_frame, text="Eser Ekle", command=eser_ekle).pack(anchor="w", pady=5)
    ttk.Button(buton_frame, text="Eser Sil", command=eser_sil).pack(anchor="w", pady=5)

    duzenle_buton_frame = tk.Frame(eserler_frame, bg="#34495e")
    duzenle_buton_frame.pack(side="right", fill="y", padx=10, pady=10)
    ttk.Button(duzenle_buton_frame, text="Eser Duzenle", command=eser_duzenle).pack(anchor="e", pady=5)

    tabloyu_guncelle()

def tur_secimi_ekrani():
    secim_frame = tk.Frame(root, bg="#34495e", bd=5)
    secim_frame.pack(pady=20, padx=20, fill="both", expand=True)

    lbl = tk.Label(secim_frame, text="Tur seciniz (film/dizi):", font=("Arial", 14), bg="#34495e", fg="#ffffff")
    lbl.pack(pady=20)

    tur_combobox = ttk.Combobox(secim_frame, values=["film", "dizi"], font=("Arial", 12), state="readonly")
    tur_combobox.pack()

    def ileri():
        secili_tur = tur_combobox.get()
        if not secili_tur:
            messagebox.showerror("Hata", "Lutfen tur seciniz (film veya dizi)!")
            return
        secim_frame.pack_forget()
        film_dizi_listele(secili_tur)

    def geri():
        secim_frame.pack_forget()
        eserlerim_ekrani()

    ttk.Button(secim_frame, text="Ileri", command=ileri).pack(pady=10)
    ttk.Button(secim_frame, text="Geri", command=geri).pack(pady=10)

def film_dizi_listele(secili_tur):
    global aktif_kullanici
    liste_frame = tk.Frame(root, bg="#34495e", bd=5)
    liste_frame.pack(pady=20, padx=20, fill="both", expand=True)

    try:
        with open("movies.json", "r", encoding="utf-8") as f:
            tum_filmler = json.load(f)
    except FileNotFoundError:
        tum_filmler = []

    filtreli = [m for m in tum_filmler if m.get("turu") == secili_tur]

    arama_frame = tk.Frame(liste_frame, bg="#34495e")
    arama_frame.pack(side="top", fill="x", padx=5, pady=5)

    tk.Label(arama_frame, text="Arama:", font=("Arial", 12), bg="#34495e", fg="#ffffff").pack(side="left", padx=5)
    arama_entry = ttk.Entry(arama_frame, font=("Arial", 12))
    arama_entry.pack(side="left", padx=5)

    def arama_yap():
        query = arama_entry.get().lower().strip()
        sonuc = []
        for mv in filtreli:
            if query in mv.get("adi", "").lower():
                sonuc.append(mv)
        tablo_doldur(sonuc)

    ttk.Button(arama_frame, text="Ara", command=arama_yap).pack(side="left", padx=5)

    kolonlar = ("adi","yili","IMBDpuani","id")
    film_tree = ttk.Treeview(liste_frame, columns=kolonlar, show="headings")
    film_tree.pack(fill="both", expand=True, padx=5, pady=5)

    film_tree.heading("adi", text="Adi")
    film_tree.heading("yili", text="Yili")
    film_tree.heading("IMBDpuani", text="IMBD Puani")
    film_tree.heading("id", text="ID")

    film_tree.column("adi", width=200)
    film_tree.column("yili", width=100)
    film_tree.column("IMBDpuani", width=80)
    film_tree.column("id", width=50)

    def tablo_doldur(dizi):
        for item in film_tree.get_children():
            film_tree.delete(item)
        for mv in dizi:
            film_tree.insert("", "end", values=(
                mv.get("adi", ""),
                mv.get("yili", ""),
                mv.get("IMBDpuani", ""),
                mv.get("id", "")
            ))

    tablo_doldur(filtreli)

    alt_frame = tk.Frame(liste_frame, bg="#34495e")
    alt_frame.pack(side="bottom", fill="x", padx=5, pady=5)

    def geri():
        liste_frame.pack_forget()
        eserlerim_ekrani()

    def ekle():
        secili = film_tree.selection()
        if not secili:
            messagebox.showerror("Hata", "Lutfen eklemek icin bir kayit secin!")
            return
        item_values = film_tree.item(secili, "values")
        secili_id = int(item_values[3])
        try:
            with open("collection.json", "r", encoding="utf-8") as f:
                collection_data = json.load(f)
        except FileNotFoundError:
            collection_data = {}
        if aktif_kullanici not in collection_data:
            collection_data[aktif_kullanici] = []
        yeni_kayit = {
            "movie_id": secili_id,
            "k_durum": "Bilinmiyor",
            "k_puan": "Belirtilmemis",
            "k_not": "Not yok"
        }
        collection_data[aktif_kullanici].append(yeni_kayit)
        with open("collection.json", "w", encoding="utf-8") as f:
            json.dump(collection_data, f, indent=4, ensure_ascii=False)
        messagebox.showinfo("Basarili", f"Secili ID ({secili_id}) listeye eklendi.")
        geri()

    def duzenle_ve_ekle():
        secili = film_tree.selection()
        if not secili:
            messagebox.showerror("Hata", "Lutfen duzenleyip eklemek icin bir kayit secin!")
            return
        item_values = film_tree.item(secili, "values")
        secili_id = int(item_values[3])

        duzen_pencere = tk.Toplevel(root)
        duzen_pencere.title("Kisisel Bilgiler")
        duzen_pencere.geometry("300x300")
        duzen_pencere.configure(bg="#34495e")

        tk.Label(duzen_pencere, text="Durum:", bg="#34495e", fg="white", font=("Arial", 12)).pack(pady=5)
        durum_combobox = ttk.Combobox(duzen_pencere, values=["Izlenecek", "Izleniyor", "Izlendi"], state="readonly")
        durum_combobox.set("Izlenecek")
        durum_combobox.pack()

        tk.Label(duzen_pencere, text="Puan (1-5):", bg="#34495e", fg="white", font=("Arial", 12)).pack(pady=5)
        puan_combobox = ttk.Combobox(duzen_pencere, values=["1","2","3","4","5"], state="readonly")
        puan_combobox.set("1")
        puan_combobox.pack()

        tk.Label(duzen_pencere, text="Not:", bg="#34495e", fg="white", font=("Arial", 12)).pack(pady=5)
        not_text = tk.Text(duzen_pencere, font=("Arial", 12), height=4, width=25)
        not_text.pack()

        def kaydet_ve_ekle():
            kd = durum_combobox.get()
            kp = puan_combobox.get()
            kn = not_text.get("1.0","end").strip()
            if not kn:
                kn = "Not yok"
            try:
                with open("collection.json", "r", encoding="utf-8") as fc:
                    collection_data = json.load(fc)
            except FileNotFoundError:
                collection_data = {}
            if aktif_kullanici not in collection_data:
                collection_data[aktif_kullanici] = []
            yeni_kayit = {
                "movie_id": secili_id,
                "k_durum": kd,
                "k_puan": kp,
                "k_not": kn
            }
            collection_data[aktif_kullanici].append(yeni_kayit)
            with open("collection.json", "w", encoding="utf-8") as fcw:
                json.dump(collection_data, fcw, indent=4, ensure_ascii=False)
            messagebox.showinfo("Basarili", f"Secili ID ({secili_id}) guncel bilgilerle eklendi.")
            duzen_pencere.destroy()
            geri()

        ttk.Button(duzen_pencere, text="Kaydet ve Ekle", command=kaydet_ve_ekle).pack(pady=20)

    ttk.Button(alt_frame, text="Geri", command=geri).pack(side="left", padx=5, pady=5)
    ttk.Button(alt_frame, text="Ekle", command=ekle).pack(side="right", padx=5, pady=5)
    ttk.Button(alt_frame, text="Duzenleyip Ekle", command=duzenle_ve_ekle).pack(side="right", padx=5, pady=5)

giris_buton = ttk.Button(giris_frame, text="Giris Yap", command=giris_yap)
giris_buton.grid(row=2, column=0, columnspan=2, padx=40, pady=40)

kayit_label = tk.Label(root, text="Hesabiniz yok mu? Kayit Olusturun.", fg="#3498db", bg="#2c3e50", font=("Arial", 10, "italic"), cursor="hand2")
kayit_label.place(relx=0.95, rely=0.95, anchor="se")
kayit_label.bind("<Button-1>", lambda e: hesap_olustur_ekrani())

sifremi_unuttum_label = tk.Label(root, text="Sifremi Unuttum", fg="#3498db", bg="#2c3e50", font=("Arial", 10, "italic"), cursor="hand2")
sifremi_unuttum_label.place(relx=0.05, rely=0.95, anchor="sw")
sifremi_unuttum_label.bind("<Button-1>", lambda e: sifremi_unuttum_ekrani())

style = ttk.Style()
style.configure("TButton", font=("Arial", 10), padding=5)
style.configure("TEntry", padding=5)

root.mainloop()
