from tkinter import *
from tkinter import ttk
import sqlite3

class mood_Backend:

    def __init__(self):
        self = self

    def set_conn(self):
        f = 1

        self.conn = sqlite3.connect('mood_baro.db')

        self.c = self.conn.cursor()

        self.c.execute("""CREATE TABLE IF NOT EXISTS moodBarometer ('usr_name' TEXT,
                        'date' TEXT, 'day_Rate' INTEGER, 'mood_Rate' INTEGER, 'sleep_Rate' INTEGER,
                        'anxiety_Rate' INTEGER, 'depression_Rate' INTEGER, 'obsession_Rate' INTEGER,
                        'spiritual_Rate' INTEGER, 'hygiene_Rate' INTEGER, 'diet_Rate' INTEGER, workout_Rate INTEGER, 
                        'total' INTEGER);""")
        
        self.conn.commit()

        while f != 1:
            self.conn.close()

    def add_Vals(self, a, b, c, d, e, x, h, i, j, k, l, m, n ):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.x = x
        self.h = h
        self.i = i
        self.j = j
        self.k = k
        self.l = l
        self.m = m
        self.n = n
        self.c = self.conn.cursor()
        self.data = (a, b, c, d, e, x, h, i, j, k, l, m, n)
        self.query = "INSERT INTO moodBarometer VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
        self.c.execute(self.query, self.data)
        self.conn.commit()
        f = 1
    
    def view_log(self):    
        window_2 = Tk()
        frame_1 = Frame(window_2)
        frame_2 = Frame(window_2)
        frame_1.pack()
        frame_2.pack()
        lbl_one = Label(frame_1, text="CONFIRM NUMBERIC VALUES \n And Jot down your thoughts")
        lbl_one.pack()
        txt_display = Text(frame_2)
        txt_display.pack()
        self.c = self.conn.cursor()
        for self.row in self.c.execute("SELECT * FROM moodBarometer;"):
            data = self.c.fetchall()
        txt_display.insert("1.0", data)
        get_log = txt_display.get("1.0", END)
        
        def add_to_txtFile():
            file_1 = open("mood_log.txt","a")
            file_1.write(get_log)
            file_1.close

        enter_button = Button(frame_2, text="Log in data", command=add_to_txtFile)
        enter_button.pack()









