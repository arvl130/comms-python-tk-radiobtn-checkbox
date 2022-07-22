import tkinter
from tkinter import ttk
from tkinter import *


ws = tkinter.Tk()
ws.title("RadioButton & CheckBox")

frame = tkinter.Frame(ws)
frame.pack()

#
# TV items section
#
tv_items_frame = tkinter.LabelFrame(frame, text="Select Items here:", width=24)
tv_items_frame.grid(row = 0, column = 0, padx = 12, pady = 12)

tv_items_checked = []
for i in range(3):
    tv_items_checked.append(tkinter.IntVar())

big_tv_checkbox = ttk.Checkbutton(tv_items_frame, text = "TV 21\" PHP 15,000.00", variable = tv_items_checked[0], width=20)
big_tv_checkbox.pack(padx=(24, 40))

mid_tv_checkbox = ttk.Checkbutton(tv_items_frame, text = "TV 14\" PHP 7,500.00", variable = tv_items_checked[1], width=20)
mid_tv_checkbox.pack(padx=(24, 40))

sml_tv_checkbox = ttk.Checkbutton(tv_items_frame, text = "TV 12\" PHP 5,000.00", variable = tv_items_checked[2], width=20)
sml_tv_checkbox.pack(padx=(24, 40))

#
# Discount section
#
discount_rates_frame = tkinter.LabelFrame(frame, text="Discount")
discount_rates_frame.grid(row = 0, column = 1, padx = (0, 12), pady = 12)

discount_rates_selected = tkinter.IntVar(value = 5)

sml_discount_radiobtn = ttk.Radiobutton(discount_rates_frame, text='5%', value = 5, variable = discount_rates_selected, width=10)
sml_discount_radiobtn.pack(padx=(12, 0))

mid_discount_radiobtn = ttk.Radiobutton(discount_rates_frame, text='10%', value = 10, variable = discount_rates_selected, width=10)
mid_discount_radiobtn.pack(padx=(12, 0))

big_discount_radiobtn = ttk.Radiobutton(discount_rates_frame, text='15%', value = 15, variable = discount_rates_selected, width=10)
big_discount_radiobtn.pack(padx=(12, 0))

#
# Results section
#
results_frame = tkinter.Frame(frame)
results_frame.grid(row = 1, column = 1, pady=(0, 12), padx=(0, 12))

subtotal_textbox = Entry(results_frame, state=tkinter.DISABLED, width=16, disabledforeground="black")
subtotal_textbox.grid(row = 0, column = 0, pady=3)

discount_textbox = Entry(results_frame, state=tkinter.DISABLED, width=16, disabledforeground="black")
discount_textbox.grid(row = 1, column = 0, pady=3)

net_amount_textbox = Entry(results_frame, state=tkinter.DISABLED, width=16, disabledforeground="black")
net_amount_textbox.grid(row = 2, column = 0, pady=3)

def set_text(widget, text):
  widget.configure(state='normal')
  widget.delete(0, tkinter.END)
  widget.insert(0, text)
  widget.configure(state='disabled')

def do_compute():
  subtotal = 0.0
  if tv_items_checked[0].get() == 1:
    subtotal += 10_000

  if tv_items_checked[1].get() == 1:
    subtotal += 7_500

  if tv_items_checked[2].get() == 1:
    subtotal += 5_000
  
  discount = subtotal * (discount_rates_selected.get() / 100)
  net_amount = subtotal - discount
  
  set_text(subtotal_textbox, str(subtotal))
  set_text(discount_textbox, str(discount))
  set_text(net_amount_textbox, str(net_amount))

def do_clear():
  set_text(subtotal_textbox, "")
  set_text(discount_textbox, "")
  set_text(net_amount_textbox, "")

def do_close():
  ws.destroy()

#
# Controls section
#
controls_frame = tkinter.Frame(frame)
controls_frame.grid(row = 1, column = 0, pady=(0, 12))

compute_btn = ttk.Button(controls_frame, text="Compute", width=20, command=do_compute)
compute_btn.grid(row = 0, column = 0, padx=12)

clear_all_btn = ttk.Button(controls_frame, text="Clear All", width=20, command=do_clear)
clear_all_btn.grid(row = 1, column = 0, padx=12)

close_btn = ttk.Button(controls_frame, text="Close", width=20, command=do_close)
close_btn.grid(row = 2, column = 0, padx=12)

subtotal_label = ttk.Label(controls_frame, text="Sub-Total:", width=12, anchor="w")
subtotal_label.grid(row = 0, column = 1)

discount_label = ttk.Label(controls_frame, text="Discount:", width=12, anchor="w")
discount_label.grid(row = 1, column = 1)

net_amount_label = ttk.Label(controls_frame, text="Net Amount:", width=12, anchor="w")
net_amount_label.grid(row = 2, column = 1)

ws.mainloop()