from tkinter import *
import pyautogui as pg
import time
import os







def delete_win10def():
    os.startfile('antivirusWin10def.reg', 'open')


    for i in range(2):
        time.sleep(0.5)
        pg.hotkey("enter")
def mem_install():
    os.startfile('memreduct-3.3.5-setup.exe', 'runas')


    for i in range(6):
        time.sleep(0.5)
        pg.hotkey("enter")
def mb_install():
    os.startfile('MBSetup.exe', 'open')
    time.sleep(1)


    pg.keyDown('alt')
    time.sleep(.2)
    pg.press('tab')
    time.sleep(.2)
    pg.keyUp('alt')





    pg.click(678, 442)
    pg.click(560, 401)
    pg.click(758, 554)
    pg.click(761, 490)










root = Tk()


root.title("Автоматизация оптимизации Windows 10")
root.minsize(width=500, height=400)




language = "Rus"

def lang_change(language=language):
    if language == "Rus":
        greeting.config(text="Welcome!")
        lang_but.config(text="English")
        start_and_go.config(text="Start optimize")
        ch0.config(text="Uninstall built-in Windows 10 Defender antivirus")
        ch1.config(text="Install the memreduct app to control RAM")
        ch2.config(text="Install MalwareBytes antivirus")
        about_project.config(text="About us")
        root.title("Automatic optimization Windows 10")

        language = "Eng"

    else:
        greeting.config(text="Добро пожаловать!")
        lang_but.config(text="Русский")
        start_and_go.config(text="Начать оптимизацию")
        ch0.config(text="Удалить встроенный антивирус Windows 10 Defender")
        ch1.config(text="Установить приложение memreduct для контроля ОЗУ")
        ch2.config(text="Установить антивирус MalwareBytes")
        root.title("Автоматизация оптимизации Windows 10")
        about_project.config(text="О нас")

        language = "Rus"





def main_code():
    abc = 0
    v0 = var0.get()
    v1 = var1.get()
    v2 = var2.get()
    if v0 == "1":
        delete_win10def()
        abc = 1
    if v1 == "1":
        mem_install()
        abc = 1
    if v2 == "1":
        mb_install()
        abc = 1
    if abc == 1:
        root_end = Tk()
        root_end.title("Optimization was successful")
        root_end.minsize(width=380, height=110)
        goodbye = Label(root_end, text="Thanks for using. Good luck!")
        goodbye.pack()
        root_end.mainloop()

        abc = 0

def apf():
    root_ap = Tk()
    root_ap.title("About us")
    root_ap.geometry('420x100')
    apl0 = Label(root_ap, text="This application is designed to help you optimize your Windows 10 "
                              )
    apl0.pack()
    apl1 = Label(root_ap, text=
                               "operating system. It will automatically increase your productivity and do it for free.  "
                              )
    apl1.pack()
    apl2 = Label(root_ap, text="The project itself was created for  "
                               )
    apl2.pack()
    apl3 = Label(root_ap, text=
                               "the Future Engineers conference.")
    apl3.pack()


    root_ap.mainloop()


lang_but = Button(text="Русский",
                  command=lang_change)
lang_but.pack()





greeting = Label(text="Добро пожаловать!",
                    font=('Times', '25', 'italic'))
greeting.pack()




start_and_go=Button(  text     = "Начать оптимизацию",
                         font     = ('Times', '20', 'italic'),
                         bg       = "green",
                         height   = 2,
                         width    = 20,
                         command  = main_code)

start_and_go.pack()




var0 = StringVar()
var1 = StringVar()
var2 = StringVar()





ch0 = Checkbutton(root, text="Удалить встроенный антивирус Windows 10 Defender", variable=var0, onvalue=True, offvalue=False)
ch1 = Checkbutton(root, text="Установить приложение memreduct для контроля ОЗУ", variable=var1, onvalue=True, offvalue=False)
ch2 = Checkbutton(root, text="Установить антивирус MalwareBytes", variable=var2, onvalue=True, offvalue=False)





ch0.select()
ch1.select()
ch2.deselect()





ch0.pack()
ch1.pack()
ch2.pack()





about_project = Button(text="О нас", command=apf)
about_project.pack()




root.mainloop()