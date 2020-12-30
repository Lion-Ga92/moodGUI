from tkinter import *
from tkinter import ttk
from datetime import date

root = Tk()
frame_1 = Frame(root)
frame_1.grid(row=1, column=1)
frame_2 = Frame(root)
frame_2.grid(row=2, column=1)
frame_3 = Frame(root, borderwidth=2, relief="raised")
frame_3.grid(row=3, column=1)
lbl_greet = Label(frame_1, text="Hello!!! And welcome user:    ")
lbl_greet.grid(row=1, column=1)
ent_usr = Entry(frame_1, width="10")
ent_usr.grid(row=1, column=2)
date_get = date.today()
ent_date = Entry(frame_1, width="10")
ent_date.grid(row=1, column=3)
ent_date.insert(0, date_get)

bttn_ent1 = Button(frame_1, text="Enter")
bttn_ent1.grid(row=1, column=4)

#frame_2 widgets

lbl_day_stat = Label(frame_2, text="Good day- Bad day\n FOR THE VALUE SCALES 1=GOOD 3=STRESSED OUT 5=CRISIS IN CATEGORY")
lbl_day_stat.grid(row=1, column=1)

num_1 = DoubleVar()
# MY QUESTION IS THIS HOW DO I PUT THE SELECTED VALUE AND STORE IT IN THE NUM_1 Variable as this is the syntax as far as i understand it. 
day_scal = Scale(frame_2, orient=HORIZONTAL, length=500, from_=0, to=5, command=lambda x: day_scal.get())
day_scal.grid(row=2, column=1)

def show_day():
    stoppit = "to stop this you need the number" + str(day_scal)
    print(stoppit)

show_day()



print(day_scal)


lbl_mood = Label(frame_2, text="Mood:", width="16")
lbl_mood.grid(row=3, column=1)

mood_scal = Scale(frame_2, orient=HORIZONTAL, length=500, from_=0.0, to=5)
mood_scal.grid(row=4, column=1)

lbl_sleep = Label(frame_2, text="Sleep:", width="16")
lbl_sleep.grid(row=5, column=1)

sleep_sc = Scale(frame_2, orient=HORIZONTAL, length=500, from_=0.0, to=5)
sleep_sc.grid(row=6, column=1)

lbl_anxiet = Label(frame_2, text="Anxiety", width="16")
lbl_anxiet.grid(row=7, column=1)

scal_anx = Scale(frame_2, orient=HORIZONTAL, length=500, from_=0.0, to=5)
scal_anx.grid(row=8, column=1)

lbl_depre = Label(frame_2, text="Depression", width="16")
lbl_depre.grid(row=9, column=1)

depr_scal = Scale(frame_2, orient=HORIZONTAL, length=500, from_=0.0, to=5)
depr_scal.grid(row=10, column=1)

lbl_obsess = Label(frame_2, text="Obessesion", width="16")
lbl_obsess.grid(row=11, column=1)

obsess_scal = Scale(frame_2, orient=HORIZONTAL, length=500, from_=0.0, to=5)
obsess_scal.grid(row=12, column=1)

lbl_spirit = Label(frame_2, text="Spirituality", width="16")
lbl_spirit.grid(row=13, column=1)

sprt_scal = Scale(frame_2, orient=HORIZONTAL, length=500, from_=0.0, to=5)
sprt_scal.grid(row=14, column=1)

lbl_hygiea= Label(frame_2, text="Hygiene", width="16")
lbl_hygiea.grid(row=15, column=1)

hygiea_scal = Scale(frame_2, orient=HORIZONTAL, length=500, from_=0.0, to=5)
hygiea_scal.grid(row=16, column=1)

lbl_diet = Label(frame_2, text="diet", width="16")
lbl_diet.grid(row=17, column=1)

diet_scal = Scale(frame_2, orient=HORIZONTAL, length=500, from_=0.0, to=5)
diet_scal.grid(row=18, column=1)

lbl_exercise = Label(frame_2, text="Exercise", width="16")
lbl_exercise.grid(row=19, column=1)

workout_scal = Scale(frame_2, orient=HORIZONTAL, length=500, from_=1, to=5)
workout_scal.grid(row=20, column=1)

lbl_scale_mssg = Label(frame_2, text="score ratings: <20% You are having a good day!\n 20% >= you <= 50% You are stressed, but manageable. \n > 50% You are stressed out and risking a crisis \n 100% CRISIS!!! CALL SOMEONE")
lbl_scale_mssg.grid(row=21, column=1)

ent_totals = Entry(frame_2, widt=10)
ent_totals.grid(row=22, column=1)


lbl_totals = Label(frame_2, text="Out of 50")
lbl_totals.grid(row=23, column=1)
#FRAME 3 WIDGETS:

lbl_main_dis = Label(frame_3, text="Main")
lbl_main_dis.grid(row=2, column=1)
lbl_drink = Label(frame_3, text="Drink")
lbl_drink.grid(row=3, column=1)
lbl_snk1 = Label(frame_3, text="Snack")
lbl_snk1.grid(row=4, column=1)
lbl_snk2 = Label(frame_3, text="Other snack")
lbl_snk2.grid(row=5, column=1)
lbl_breakf = Label(frame_3, text="Breakfast")
lbl_breakf.grid(row=1, column=2)
ent_bf_main = Entry(frame_3, width=20)
ent_bf_main.grid(row=2, column=2)
ent_bf_dr = Entry(frame_3, width=20)
ent_bf_dr.grid(row=3, column=2)
ent_bf_sn1 = Entry(frame_3, width=20)
ent_bf_sn1.grid(row=4, column=2)
ent_dinr_sna2 = Entry(frame_3, width=20)
ent_dinr_sna2.grid(row=5, column=2)


#FRAME 4 WIDGETS:
lbl_lunch = Label(frame_3, text="Lunch")
lbl_lunch.grid(row=1, column=3)
ent_lunch_main = Entry(frame_3, width=20)
ent_lunch_main.grid(row=2, column=3)
ent_lunch_dr = Entry(frame_3, width=20)
ent_lunch_dr.grid(row=3, column=3)
ent_lunch_sn1 = Entry(frame_3, width=20)
ent_lunch_sn1.grid(row=4, column=3)
ent_dinr_sna2 = Entry(frame_3, width=20)
ent_dinr_sna2.grid(row=5, column=3)


#FRAME 5 WIDGETS
lbl_dinner = Label(frame_3, text="Dinner")
lbl_dinner.grid(row=1, column=4)
ent_dinr_main = Entry(frame_3, width=20)
ent_dinr_main.grid(row=2, column=4)
ent_dinr_dr = Entry(frame_3, width=20)
ent_dinr_dr.grid(row=3, column=4)
ent_dinr_sna1 = Entry(frame_3, width=20)
ent_dinr_sna1.grid(row=4, column=4)
ent_dinr_sna2 = Entry(frame_3, width=20)
ent_dinr_sna2.grid(row=5, column=4)
root.mainloop()
