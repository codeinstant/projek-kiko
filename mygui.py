import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import os

# Get the current working directory
cwdi = str(os.getcwd())+"/img/"

pokemon_info = [['Bulbasaur', 'Grass', '318'], ['Ivysaur', 'Grass', '405'], ['Venusaur', 'Grass', '525'], ['Charmander', 'Fire', '309'], ['Charmeleon', 'Fire', '405'], ['Charizard', 'Fire', '534'], ['Squirtle', 'Water', '314'], ['Wartortle', 'Water', '405'], ['Blastoise', 'Water', '530'], ['Caterpie', 'Bug', '195'], ['Metapod', 'Bug', '205'], ['Butterfree', 'Bug', '395'], ['Weedle', 'Bug', '195'], ['Kakuna', 'Bug', '205'], ['Beedrill', 'Bug', '395'], ['Pidgey', 'Normal', '251'], ['Pidgeotto', 'Normal', '349'], ['Pidgeot', 'Normal', '479'], ['Rattata', 'Normal', '253'], ['Raticate', 'Normal', '413'], ['Spearow', 'Normal', '262'], ['Fearow', 'Normal', '442'], ['Ekans', 'Poison', '288'], ['Arbok', 'Poison', '448'], ['Pikachu', 'Electric', '320'], ['Raichu', 'Electric', '485'], ['Sandshrew', 'Ground', '300'], ['Sandslash', 'Ground', '450'], ['Nidoran?', 'Poison', '275'], ['Nidorina', 'Poison', '365'], ['Nidoqueen', 'Poison', '505'], ['Nidoran?', 'Poison', '273'], ['Nidorino', 'Poison', '365'], ['Nidoking', 'Poison', '505'], ['Clefairy', 'Fairy', '323'], ['Clefable', 'Fairy', '483'], ['Vulpix', 'Fire', '299'], ['Ninetales', 'Fire', '505'], ['Jigglypuff', 'Normal', '270'], ['Wigglytuff', 'Normal', '435'], ['Zubat', 'Poison', '245'], ['Golbat', 'Poison', '455'], ['Oddish', 'Grass', '320'], ['Gloom', 'Grass', '395'], ['Vileplume', 'Grass', '490'], ['Paras', 'Bug', '285'], ['Parasect', 'Bug', '405'], ['Venonat', 'Bug', '305'], ['Venomoth', 'Bug', '450'], ['Diglett', 'Ground', '265'], ['Dugtrio', 'Ground', '425'], ['Meowth', 'Normal', '290'], ['Persian', 'Normal', '440'], ['Psyduck', 'Water', '320'], ['Golduck', 'Water', '500'], ['Mankey', 'Fighting', '305'], ['Primeape', 'Fighting', '455'], ['Growlithe', 'Fire', '350'], ['Arcanine', 'Fire', '555'], ['Poliwag', 'Water', '300'], ['Poliwhirl', 'Water', '385'], ['Poliwrath', 'Water', '510'], ['Abra', 'Psychic', '310'], ['Kadabra', 'Psychic', '400'], ['Alakazam', 'Psychic', '500'], ['Machop', 'Fighting', '305'], ['Machoke', 'Fighting', '405'], ['Machamp', 'Fighting', '505'], ['Bellsprout', 'Grass', '300'], ['Weepinbell', 'Grass', '390'], ['Victreebel', 'Grass', '490'], ['Tentacool', 'Water', '335'], ['Tentacruel', 'Water', '515'], ['Geodude', 'Rock', '300'], ['Graveler', 'Rock', '390'], ['Golem', 'Rock', '495'], ['Ponyta', 'Fire', '410'], ['Rapidash', 'Fire', '500'], ['Slowpoke', 'Water', '315'], ['Slowbro', 'Water', '490'], ['Magnemite', 'Electric', '325'], ['Magneton', 'Electric', '465'], ["Farfetch'd", 'Normal', '377'], ['Doduo', 'Normal', '310'], ['Dodrio', 'Normal', '470'], ['Seel', 'Water', '325'], ['Dewgong', 'Water', '475'], ['Grimer', 'Poison', '325'], ['Muk', 'Poison', '500'], ['Shellder', 'Water', '305'], ['Cloyster', 'Water', '525'], ['Gastly', 'Ghost', '310'], ['Haunter', 'Ghost', '405'], ['Gengar', 'Ghost', '500'], ['Onix', 'Rock', '385'], ['Drowzee', 'Psychic', '328'], ['Hypno', 'Psychic', '483'], ['Krabby', 'Water', '325'], ['Kingler', 'Water', '475'], ['Voltorb', 'Electric', '330'], ['Electrode', 'Electric', '490'], ['Exeggcute', 'Grass', '325'], ['Exeggutor', 'Grass', '530'], ['Cubone', 'Ground', '320'], ['Marowak', 'Ground', '425'], ['Hitmonlee', 'Fighting', '455'], ['Hitmonchan', 'Fighting', '455'], ['Lickitung', 'Normal', '385'], ['Koffing', 'Poison', '340'], ['Weezing', 'Poison', '490'], ['Rhyhorn', 'Ground', '345'], ['Rhydon', 'Ground', '485'], ['Chansey', 'Normal', '450'], ['Tangela', 'Grass', '435'], ['Kangaskhan', 'Normal', '490'], ['Horsea', 'Water', '295'], ['Seadra', 'Water', '440'], ['Goldeen', 'Water', '320'], ['Seaking', 'Water', '450'], ['Staryu', 'Water', '340'], ['Starmie', 'Water', '520'], ['Scyther', 'Bug', '500'], ['Jynx', 'Ice', '455'], ['Electabuzz', 'Electric', '490'], ['Magmar', 'Fire', '495'], ['Pinsir', 'Bug', '500'], ['Tauros', 'Normal', '490'], ['Magikarp', 'Water', '200'], ['Gyarados', 'Water', '540'], ['Lapras', 'Water', '535'], ['Ditto', 'Normal', '288'], ['Eevee', 'Normal', '325'], ['Vaporeon', 'Water', '525'], ['Jolteon', 'Electric', '525'], ['Flareon', 'Fire', '525'], ['Porygon', 'Normal', '395'], ['Omanyte', 'Rock', '355'], ['Omastar', 'Rock', '495'], ['Kabuto', 'Rock', '355'], ['Kabutops', 'Rock', '495'], ['Aerodactyl', 'Rock', '515'], ['Snorlax', 'Normal', '540'], ['Articuno', 'Ice', '580'], ['Zapdos', 'Electric', '580'], ['Moltres', 'Fire', '580'], ['Dratini', 'Dragon', '300'], ['Dragonair', 'Dragon', '420'], ['Dragonite', 'Dragon', '600'], ['Mewtwo', 'Psychic', '680'], ['Mew', 'Psychic', '600']]

frame_styles = {"relief": "groove",
                "bd": 3, "bg": "#BEB2A7",
                "fg": "#073bb3", "font": ("Arial", 9, "bold")}

class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)

        menu_file = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Menu", menu=menu_file)
        menu_file.add_command(label="Testing", command=lambda: parent.show_frame(Testing))
        menu_file.add_command(label="Riwayat", command=lambda: parent.show_frame(Riwayat))
        menu_file.add_separator()
        menu_file.add_command(label="Exit Application", command=lambda: parent.Quit_application())

class MyApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        main_frame = tk.Frame(self, bg="#84CEEB", height=600, width=1024)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        # self.resizable(0, 0) prevents the app from being resized
        # self.geometry("1024x600") fixes the applications size
        self.frames = {}
        pages = (Testing, Riwayat)
        for F in pages:
            frame = F(main_frame, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Testing)
        menubar = MenuBar(self)
        tk.Tk.config(self, menu=menubar)

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def OpenNewWindow(self):
        OpenNewWindow()

    def Quit_application(self):
        self.destroy()


class GUI(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.main_frame = tk.Frame(self, bg="#BEB2A7", height=600, width=1024)
        # self.main_frame.pack_propagate(0)
        self.main_frame.pack(fill="both", expand="true")
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

class Testing(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)
        global data
        
        data = os.listdir(cwdi+"ori")
        data.sort()
        label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Pilih Gambar atau Tambah Gambar")
        label1.pack(side="top")
        label2 = tk.Label(self.main_frame, font=("Verdana", 10), bg="#BEB2A7", text="Pilih gambar di list bawah ini")
        label2.pack(side="top")
        Lbox1 = tk.Listbox(self.main_frame)
        
        Lbox1.pack(side="top")
        button1 = tk.Button(self.main_frame, text="Tambah Gambar", bg="green", command=lambda: Add_img())
        button1.pack()
        w1 = tk.Label(self.main_frame)
        w1.pack(side="top")

        def onselect(evt):
            # Note here that T kinter passes an event object to onselect()
            w = evt.widget
            index = int(w.curselection()[0])
            value = w.get(index)
            gambarcv2 = cv2.imread(cwdi+"ori/"+value)
            gambarcv2 = cv2.resize(gambarcv2, (250, 250))
            gambarcv2 = cv2.cvtColor(gambarcv2, cv2.COLOR_BGR2RGB)
            gambararr = Image.fromarray(gambarcv2)
            gambar = ImageTk.PhotoImage(image=gambararr)
            w1.configure(image=gambar)
            w1.gambar = gambar
            # print('You selected item %d: "%s"' % (index, value))
        Lbox1.bind('<<ListboxSelect>>', onselect)

        def Refresh_Data():
            Lbox1.delete(0, tk.END)
            data = os.listdir(cwdi+"ori")
            data.sort()
            print(data)
            for i in range(len(data)):
                Lbox1.insert(i+1, data[i])
        Refresh_Data()
        def Add_img():
            file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Image files", ("*.png","*.jpg","*.jpeg"))])
            # print(file_path)
            gambarcv2 = cv2.imread(file_path)
            gambarcv2 = cv2.resize(gambarcv2, (250, 250))
            imgname = "photo-1.png"
            if len(data) > 0:
                for i in range(len(data)):
                    spltstr = data[i].split("-")
                    index = spltstr[1].split(".")
                    imgname = "photo-"+str(i+2)+".png"
                    print(index[0]+"dan"+str(i+1))
                    if index[0] != str(i+1):
                        imgname = "photo-"+str(i+1)+".png"
                        break
            cv2.imwrite(cwdi+"ori/"+imgname, gambarcv2)
            Refresh_Data()

class OpenNewWindow(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        self.title("Here is the Title of the Window")
        self.geometry("500x500")
        self.resizable(0, 0)

        frame1 = ttk.LabelFrame(main_frame, text="This is a ttk LabelFrame")
        frame1.pack(expand=True, fill="both")

        label1 = tk.Label(frame1, font=("Verdana", 20), text="OpenNewWindow Page")
        label1.pack(side="top")

class Riwayat(GUI):  # inherits from the GUI class
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        frame1 = tk.LabelFrame(self, frame_styles, text="This is a LabelFrame containing a Treeview")
        frame1.place(rely=0.05, relx=0.02, height=400, width=400)

        frame2 = tk.LabelFrame(self, frame_styles, text="Some widgets")
        frame2.place(rely=0.05, relx=0.45, height=500, width=500)

        button1 = tk.Button(frame2, text="tk button", command=lambda: Refresh_data())
        button1.pack()
        button2 = ttk.Button(frame2, text="ttk button", command=lambda: Refresh_data())
        button2.pack()

        Var1 = tk.IntVar()
        Var2 = tk.IntVar()
        Cbutton1 = tk.Checkbutton(frame2, text="tk CheckButton1", variable=Var1, onvalue=1, offvalue=0)
        Cbutton1.pack()
        Cbutton2 = tk.Checkbutton(frame2, text="tk CheckButton2", variable=Var2, onvalue=1, offvalue=0)
        Cbutton2.pack()

        Cbutton3 = ttk.Checkbutton(frame2, text="ttk CheckButton1", variable=Var1, onvalue=1, offvalue=0)
        Cbutton3.pack()
        Cbutton3 = ttk.Checkbutton(frame2, text="ttk CheckButton2", variable=Var2, onvalue=1, offvalue=0)
        Cbutton3.pack()

        Lbox1 = tk.Listbox(frame2, selectmode="multiple")
        Lbox1.insert(1, "This is a tk ListBox")
        Lbox1.insert(2, "Github")
        Lbox1.insert(3, "Python")
        Lbox1.insert(3, "StackOverflow")
        Lbox1.pack(side="left")

        Var3 = tk.IntVar()
        R1 = tk.Radiobutton(frame2, text="tk Radiobutton1", variable=Var3, value=1)
        R1.pack()
        R2 = tk.Radiobutton(frame2, text="tk Radiobutton2", variable=Var3, value=2)
        R2.pack()
        R3 = tk.Radiobutton(frame2, text="tk Radiobutton3", variable=Var3, value=3)
        R3.pack()

        R4 = tk.Radiobutton(frame2, text="ttk Radiobutton1", variable=Var3, value=1)
        R4.pack()
        R5 = tk.Radiobutton(frame2, text="ttk Radiobutton2", variable=Var3, value=2)
        R5.pack()
        R6 = tk.Radiobutton(frame2, text="ttk Radiobutton3", variable=Var3, value=3)
        R6.pack()

        # This is a treeview.
        tv1 = ttk.Treeview(frame1)
        column_list_account = ["Name", "Type", "Base Stat Total"]
        tv1['columns'] = column_list_account
        tv1["show"] = "headings"  # removes empty column
        for column in column_list_account:
            tv1.heading(column, text=column)
            tv1.column(column, width=50)
        tv1.place(relheight=1, relwidth=0.995)
        treescroll = tk.Scrollbar(frame1)
        treescroll.configure(command=tv1.yview)
        tv1.configure(yscrollcommand=treescroll.set)
        treescroll.pack(side="right", fill="y")

        def Load_data():
            for row in pokemon_info:
                tv1.insert("", "end", values=row)

        def Refresh_data():
            # Deletes the data in the current treeview and reinserts it.
            tv1.delete(*tv1.get_children())  # *=splat operator
            Load_data()

        Load_data()


class PageOne(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Page One")
        label1.pack(side="top")


class PageThree(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Page Three")
        label1.pack(side="top")


class PageFour(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Page Four")
        label1.pack(side="top")