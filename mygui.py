import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import os

# Get the current working directory
cwdi = str(os.getcwd())+"/img/"

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
        frame1 = tk.LabelFrame(self, frame_styles, text="Testing Aplikasi")
        frame1.place(rely=0.05, relx=0.02, height=500, width=500)

        frame2 = tk.LabelFrame(self, frame_styles, text="Image")
        frame2.place(rely=0.05, relx=0.45, height=500, width=500)

        labelv = tk.Label(text="temp untuk values")
        labellst = tk.Label(text="temp untuk list data image")
        label2 = tk.Label(frame1, font=("Verdana", 10), bg="#BEB2A7", text="Pilih gambar di list bawah ini")
        label2.pack(side="top")
        Lbox1 = tk.Listbox(frame1)
        
        Lbox1.pack(side="top")
        s = ttk.Separator(frame1, orient='horizontal')
        s.pack(fill='x')
        button1 = tk.Button(frame1, text="Tambah Gambar", bg="green", command=lambda: Add_img())
        button1.pack()
        label3 = tk.Label(frame1, font=("Verdana", 10), bg="#BEB2A7", text="Or")
        label3.pack(side="top")
        button2 = tk.Button(frame1, text="Delete", bg="red", command=lambda: Delete_img())
        button2.pack()
        w1 = tk.Label(frame2)
        button3 = tk.Button(frame2, text="Lihat Hasil", bg="blue", command=lambda: Hasil())

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
            labelv.configure(text=value)
            w1.pack()
            button3.pack()
            # print('You selected item %d: "%s"' % (index, value))
        Lbox1.bind('<<ListboxSelect>>', onselect)

        def Refresh_Data():
            Lbox1.delete(0, tk.END)
            data = os.listdir(cwdi+"ori")
            data.sort()
            dt = " ".join(data)
            labellst.configure(text=dt)
            for i in range(len(data)):
                Lbox1.insert(i+1, data[i])
        Refresh_Data()

        def Add_img():
            file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Image files", ("*.png","*.jpg","*.jpeg"))])
            if len(file_path) > 0:
                gambarcv2 = cv2.imread(file_path)
                gambarcv2 = cv2.resize(gambarcv2, (250, 250))
                imgname = "photo-1.png"
                data = str(labellst.cget("text"))
                data = data.split(" ")
                if len(data) > 0:
                    for i in range(len(data)):
                        spltstr = data[i].split("-")
                        index = spltstr[1].split(".")
                        imgname = "photo-"+str(i+2)+".png"
                        # print(index[0]+"dan"+str(i+1))
                        if index[0] != str(i+1):
                            imgname = "photo-"+str(i+1)+".png"
                            break
                cv2.imwrite(cwdi+"ori/"+imgname, gambarcv2)
                Refresh_Data()
        
        def Delete_img():
            fileimg = cwdi+"ori/"+str(labelv.cget("text"))
            if os.path.exists(fileimg):
                os.remove(fileimg)
            else:
                print("The file does not exist") 
            w1.pack_forget()
            button3.pack_forget()
            Refresh_Data()
        
        def Hasil():
            img_val = str(labelv.cget("text"))
            img_ori = cv2.imread(cwdi+"ori/"+img_val)
            denoised_image = cv2.fastNlMeansDenoisingColored(img_ori, None, h=15, hColor=10, templateWindowSize=7, searchWindowSize=21)
            psnr = cv2.PSNR(img_ori, denoised_image)
            psnr = f"{psnr:0.2f}"
            svriwayat = cwdi+"hasil/riwayat/"+img_val.split(".")[0]+" "+psnr+" .png"
            cv2.imwrite(cwdi+"hasil/ori.png", img_ori)
            cv2.imwrite(cwdi+"hasil/denoise.png", denoised_image)
            cv2.imwrite(svriwayat, denoised_image)
            OpenNewWindow()


class OpenNewWindow(tk.Toplevel):

    def __init__(self, *args, **kwargs):

        tk.Toplevel.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        self.title("Result Denoised Image")
        self.geometry("500x500")
        self.resizable(0, 0)

        label1 = tk.Label(main_frame, font=("Verdana", 20), text="Result")
        label1.pack(side="top")
        s = ttk.Separator(main_frame, orient='horizontal')
        s.pack(fill='x')

        frame1 = tk.Frame(main_frame)
        frame1.pack()
        frame2 = tk.Frame(main_frame)
        frame2.pack()

        label2 = tk.Label(frame1, text="Original Image")
        label2.pack(side="left")
        label3 = tk.Label(frame1, text="Denoised Image")
        label3.pack(side="right")
        gambararr = Image.open(cwdi+"hasil/ori.png")
        gambar = ImageTk.PhotoImage(image=gambararr)
        labeli1 = tk.Label(frame2, image=gambar)
        labeli1.pack(side="left")
        labeli1.image = gambar
        gambararr = Image.open(cwdi+"hasil/denoise.png")
        gambar = ImageTk.PhotoImage(image=gambararr)
        labeli2 = tk.Label(frame2, image=gambar)
        labeli2.pack(side="right")
        labeli2.image = gambar
        
        # PSNR
        img1 = cv2.imread(cwdi+"hasil/ori.png")
        img2 = cv2.imread(cwdi+"hasil/denoise.png")
        psnr = cv2.PSNR(img1, img2)
        label4 = tk.Label(main_frame, text=f"PSNR = {psnr:0.2f}")
        label4.pack(side="bottom")

class Riwayat(GUI):  # inherits from the GUI class
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        frame1 = tk.LabelFrame(self, frame_styles, text="Riwayat")
        frame1.place(rely=0.05, relx=0.02, height=400, width=400)

        frame2 = tk.LabelFrame(self, frame_styles, text="Image")
        frame2.place(rely=0.05, relx=0.45, height=500, width=500)
        frame3 = tk.Frame(frame2)
        frame3.pack(side="top")
        label2 = tk.Label(frame3, text="Original Image")
        label3 = tk.Label(frame3, text="Denoised Image")
        labeli1 = tk.Label(frame2)
        labeli2 = tk.Label(frame2)
        label4 = tk.Label(frame2)
        label4.pack(side="bottom")

        # This is a treeview.
        tv1 = ttk.Treeview(frame1)
        column_list_account = ["Image", "PSNR", "extension"]
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
            data = os.listdir(cwdi+"hasil/riwayat")
            data.sort()
            for row in data:
                tv1.insert("", "end", values=row)

        def Select_item(a):
            curItem = tv1.item(tv1.focus())
            label2.pack(side="left")
            label3.pack(side="right")
            gambararr = Image.open(cwdi+"ori/"+curItem['values'][0]+""+curItem['values'][2])
            gambar = ImageTk.PhotoImage(image=gambararr)
            labeli1.configure(image=gambar)
            labeli1.pack(side="left")
            labeli1.image = gambar
            riw = " ".join(curItem['values'])
            gambararr = Image.open(cwdi+"hasil/riwayat/"+riw)
            gambar = ImageTk.PhotoImage(image=gambararr)
            labeli2.configure(image=gambar)
            labeli2.pack(side="right")
            labeli2.image = gambar
            label4.configure(text="PSNR = "+curItem['values'][1])
        tv1.bind('<ButtonRelease-1>', Select_item)

        Load_data()
        # def Refresh_data():
        #     # Deletes the data in the current treeview and reinserts it.
        #     tv1.delete(*tv1.get_children())  # *=splat operator
        #     Load_data()
        # Var1 = tk.IntVar()
        # Var2 = tk.IntVar()
        # Cbutton1 = tk.Checkbutton(frame2, text="tk CheckButton1", variable=Var1, onvalue=1, offvalue=0)
        # Cbutton1.pack()
        # Cbutton2 = tk.Checkbutton(frame2, text="tk CheckButton2", variable=Var2, onvalue=1, offvalue=0)
        # Cbutton2.pack()

        # Cbutton3 = ttk.Checkbutton(frame2, text="ttk CheckButton1", variable=Var1, onvalue=1, offvalue=0)
        # Cbutton3.pack()
        # Cbutton3 = ttk.Checkbutton(frame2, text="ttk CheckButton2", variable=Var2, onvalue=1, offvalue=0)
        # Cbutton3.pack()

        # Var3 = tk.IntVar()
        # R1 = tk.Radiobutton(frame2, text="tk Radiobutton1", variable=Var3, value=1)
        # R1.pack()
        # R2 = tk.Radiobutton(frame2, text="tk Radiobutton2", variable=Var3, value=2)
        # R2.pack()
        # R3 = tk.Radiobutton(frame2, text="tk Radiobutton3", variable=Var3, value=3)
        # R3.pack()

        # R4 = tk.Radiobutton(frame2, text="ttk Radiobutton1", variable=Var3, value=1)
        # R4.pack()
        # R5 = tk.Radiobutton(frame2, text="ttk Radiobutton2", variable=Var3, value=2)
        # R5.pack()
        # R6 = tk.Radiobutton(frame2, text="ttk Radiobutton3", variable=Var3, value=3)
        # R6.pack()


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