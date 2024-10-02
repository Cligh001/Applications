from tkinter import *
BACKGROUND = "#D5E7B8"
FOREGROUND = "#f09eae"
FONT = "Arial"
SIZE = 14
TYPE = "bold"

#~~~~~~~~~~~~~~~~~~~~DESTROY~~~~~~~~~~~~~~~~~~~~~~~
def destroy_existing_content():
    # Destroy all widgets except dropdown menu and canvas
    for widget in wn.winfo_children():
        if widget != drop and widget != canv and widget != change_button and widget != main_title:  # Exclude dropdown menu and canvas from destruction
            widget.destroy()

#~~~~~~~~~~~~~~~~~~~~Menu~~~~~~~~~~~~~~~~~~~~~~~
def show(): 
    main_title.config(text = clicked.get())
    view = clicked.get()
    if view == "Dilution Calculator":
        destroy_existing_content()
        default_view()
    elif view == "Powder Calculator":
        destroy_existing_content()
        powder_view()
    elif view == "Liquid Calculator":
        destroy_existing_content()
        liquid_view()
    elif view == "DNA Copy # Calculator":
        destroy_existing_content()
        dcn_view()

#~~~~~~~~~~~~~~~~~~~~CALCULATE~~~~~~~~~~~~~~~~~~~~~~~
def calc():
    stock = int(stock_conc_input.get())
    needed = int(needed_conc_input.get())
    overall = int(overall_vol_input.get())
    
    df = stock / needed
    vol_stock_needed_ml = overall / df
    vol_stock_needed_l = vol_stock_needed_ml / 1000
    
    vol_ml_output.delete(0, END)
    vol_l_output.delete(0, END)
    vol_ml_output.insert(0, str(f"{vol_stock_needed_ml} mL"))
    vol_l_output.insert(0, str(f"{vol_stock_needed_l} L"))
    
#~~~~~~~~~~~~~~~~~~~~CLEAR~~~~~~~~~~~~~~~~~~~~~~~
def clear():
    stock_conc_input.delete(0, END)
    needed_conc_input.delete(0, END)
    overall_vol_input.delete(0, END)
    vol_ml_output.delete(0, END)
    vol_l_output.delete(0, END)
    vol_ml_output.insert(0, "˚⊹♡⊹˚₊˚⊹♡⊹˚")
    vol_l_output.insert(0, "˚⊹♡⊹˚₊˚⊹♡⊹˚")

#~~~~~~~~~~~~~~~~~~~~UI~~~~~~~~~~~~~~~~~~~~~~~
#window
wn = Tk()
wn.title("All-in-One Dilutions Calculator🧪")
wn.config(padx=50,pady=50,bg=BACKGROUND)

#image
canv = Canvas(width=300,height=300,bg=BACKGROUND,highlightthickness=0)
tube_img = PhotoImage(file="cute_tube.png")
canv.create_image(150,150,image=tube_img)
canv.grid(row=2, column=0, columnspan=2)

#----------Dropdown Menu----------

options = [ 
    "Dilution Calculator", 
    "Powder Calculator", 
    "Liquid Calculator",
    "DNA Copy # Calculator"
]

# datatype of menu text 
clicked = StringVar()

# initial menu text 
clicked.set("Dilution Calculator") 

# Create Dropdown menu 
drop = OptionMenu( wn , clicked , *options ) 
drop.grid(row=0, column=0) 
drop.config(highlightbackground=BACKGROUND, highlightthickness=0, background=BACKGROUND)


#----------LABELS----------
    #----------title label----------
main_title = Label( wn , text = "Dilution Calculator" ) 
main_title.grid(row=1, column=0, columnspan=2)
main_title.config(background=BACKGROUND, foreground=FOREGROUND, padx=10, pady=10, font=(FONT, 18, TYPE))

    #----------[stock] labels----------
stock_conc = Label(text="[Stock]:")
stock_conc.grid(row=3,column=0, sticky="E")
stock_conc.config(background=BACKGROUND,foreground=FOREGROUND ,padx=2, pady=2, font=(FONT, SIZE, TYPE))

    #----------[needed] labels----------
needed_conc = Label(text="[Needed]:")
needed_conc.grid(row=4,column=0, sticky="E")
needed_conc.config(background=BACKGROUND, foreground=FOREGROUND,padx=2, pady=2, font=(FONT, SIZE, TYPE))

    #----------overall vol. labels----------
overall_vol = Label(text="Overall Vol. (ml):")
overall_vol.grid(row=5,column=0, sticky="E")
overall_vol.config(background=BACKGROUND, foreground=FOREGROUND,padx=2, pady=2, font=(FONT, SIZE, TYPE))

    #----------stock vol needed labels----------
vol_stock_ml = Label(text="Vol. Stock (ml):")
vol_stock_ml.grid(row=6,column=0, sticky="E")
vol_stock_ml.config(background=BACKGROUND, foreground=FOREGROUND, padx=2, pady=2, font=(FONT, SIZE, TYPE))

vol_stock_l = Label(text="Vol. Stock (l):")
vol_stock_l.grid(row=7,column=0, sticky="E")
vol_stock_l.config(background=BACKGROUND, foreground=FOREGROUND, padx=2, pady=2, font=(FONT, SIZE, TYPE))

    #----------stock vol needed labels----------
note = Label(text="Note: [ ] means concentration. So, [stock] = stock concentration")
note.grid(row=9, column=0, columnspan=2, sticky="N")
note.config(background=BACKGROUND, foreground=FOREGROUND, padx=2, pady=2, font=(FONT, 10, TYPE))

#entrys
stock_conc_input = Entry(width=10)
stock_conc_input.grid(row=3,column=1,sticky="W", padx=2, pady=2)
stock_conc_input.config(highlightbackground=BACKGROUND, highlightthickness=0)

needed_conc_input = Entry(width=10)
needed_conc_input.grid(row=4,column=1,sticky="W", padx=2, pady=2)
needed_conc_input.config(highlightbackground=BACKGROUND, highlightthickness=0)

overall_vol_input = Entry(width=10)
overall_vol_input.grid(row=5,column=1,sticky="W", padx=2, pady=2)
overall_vol_input.config(highlightbackground=BACKGROUND, highlightthickness=0)

vol_ml_output = Entry(width=10)
vol_ml_output.grid(row=6,column=1,sticky="W", padx=2, pady=2)
vol_ml_output.config(highlightbackground=BACKGROUND, highlightthickness=0)
vol_ml_output.insert(0, "˚⊹♡⊹˚₊˚⊹♡⊹˚")

vol_l_output = Entry(width=10)
vol_l_output.grid(row=7,column=1,sticky="W", padx=2, pady=2)
vol_l_output.config(highlightbackground=BACKGROUND, highlightthickness=0)
vol_l_output.insert(0, "˚⊹♡⊹˚₊˚⊹♡⊹˚")

#buttons

change_button = Button( wn , text = "change" , command = show )
change_button.grid(row=0,column=1)
change_button.config(highlightbackground=BACKGROUND, highlightthickness=0)

calc_button = Button(text="calculate", width=10, command=calc)
calc_button.grid(row=8, column=1, padx=2, pady=2)
calc_button.config(highlightbackground=BACKGROUND, highlightthickness=0)

clear_button = Button(text="clear", width=10, command=clear)
clear_button.grid(row=8, column=0, padx=2, pady=2)
clear_button.config(highlightbackground=BACKGROUND, highlightthickness=0)

#--------------------DEFAULT VIEW--------------------
def default_view():
        #~~~~~~~~~~~~~~~~~~~~CALCULATE~~~~~~~~~~~~~~~~~~~~~~~
    def calc():
        stock = int(stock_conc_input.get())
        needed = int(needed_conc_input.get())
        overall = int(overall_vol_input.get())
        
        df = stock / needed
        vol_stock_needed_ml = overall / df
        vol_stock_needed_l = vol_stock_needed_ml / 1000
        
        vol_ml_output.delete(0, END)
        vol_l_output.delete(0, END)
        vol_ml_output.insert(0, str(f"{vol_stock_needed_ml} mL"))
        vol_l_output.insert(0, str(f"{vol_stock_needed_l} L"))
        
    #~~~~~~~~~~~~~~~~~~~~CLEAR~~~~~~~~~~~~~~~~~~~~~~~
    def clear():
        stock_conc_input.delete(0, END)
        needed_conc_input.delete(0, END)
        overall_vol_input.delete(0, END)
        vol_ml_output.delete(0, END)
        vol_l_output.delete(0, END)
        vol_ml_output.insert(0, "˚⊹♡⊹˚₊˚⊹♡⊹˚")
        vol_l_output.insert(0, "˚⊹♡⊹˚₊˚⊹♡⊹˚")

    #----------LABELS----------

        #----------[stock] labels----------
    stock_conc = Label(text="[Stock]:")
    stock_conc.grid(row=3,column=0, sticky="E")
    stock_conc.config(background=BACKGROUND,foreground=FOREGROUND ,padx=2, pady=2, font=(FONT, SIZE, TYPE))

        #----------[needed] labels----------
    needed_conc = Label(text="[Needed]:")
    needed_conc.grid(row=4,column=0, sticky="E")
    needed_conc.config(background=BACKGROUND, foreground=FOREGROUND,padx=2, pady=2, font=(FONT, SIZE, TYPE))

        #----------overall vol. labels----------
    overall_vol = Label(text="Overall Vol. (ml):")
    overall_vol.grid(row=5,column=0, sticky="E")
    overall_vol.config(background=BACKGROUND, foreground=FOREGROUND,padx=2, pady=2, font=(FONT, SIZE, TYPE))

        #----------stock vol needed labels----------
    vol_stock_ml = Label(text="Vol. Stock (ml):")
    vol_stock_ml.grid(row=6,column=0, sticky="E")
    vol_stock_ml.config(background=BACKGROUND, foreground=FOREGROUND, padx=2, pady=2, font=(FONT, SIZE, TYPE))

    vol_stock_l = Label(text="Vol. Stock (l):")
    vol_stock_l.grid(row=7,column=0, sticky="E")
    vol_stock_l.config(background=BACKGROUND, foreground=FOREGROUND, padx=2, pady=2, font=(FONT, SIZE, TYPE))

        #----------stock vol needed labels----------
    note = Label(text="Note: [ ] means concentration. So, [stock] = stock concentration")
    note.grid(row=9, column=0, columnspan=2, sticky="N")
    note.config(background=BACKGROUND, foreground=FOREGROUND, padx=2, pady=2, font=(FONT, 10, TYPE))

    #entrys
    stock_conc_input = Entry(width=10)
    stock_conc_input.grid(row=3,column=1,sticky="W", padx=2, pady=2)
    stock_conc_input.config(highlightbackground=BACKGROUND, highlightthickness=0)

    needed_conc_input = Entry(width=10)
    needed_conc_input.grid(row=4,column=1,sticky="W", padx=2, pady=2)
    needed_conc_input.config(highlightbackground=BACKGROUND, highlightthickness=0)

    overall_vol_input = Entry(width=10)
    overall_vol_input.grid(row=5,column=1,sticky="W", padx=2, pady=2)
    overall_vol_input.config(highlightbackground=BACKGROUND, highlightthickness=0)

    vol_ml_output = Entry(width=10)
    vol_ml_output.grid(row=6,column=1,sticky="W", padx=2, pady=2)
    vol_ml_output.config(highlightbackground=BACKGROUND, highlightthickness=0)
    vol_ml_output.insert(0, "˚⊹♡⊹˚₊˚⊹♡⊹˚")

    vol_l_output = Entry(width=10)
    vol_l_output.grid(row=7,column=1,sticky="W", padx=2, pady=2)
    vol_l_output.config(highlightbackground=BACKGROUND, highlightthickness=0)
    vol_l_output.insert(0, "˚⊹♡⊹˚₊˚⊹♡⊹˚")

    #buttons

    calc_button = Button(text="calculate", width=10, command=calc)
    calc_button.grid(row=8, column=1, padx=2, pady=2)
    calc_button.config(highlightbackground=BACKGROUND, highlightthickness=0)

    clear_button = Button(text="clear", width=10, command=clear)
    clear_button.grid(row=8, column=0, padx=2, pady=2)
    clear_button.config(highlightbackground=BACKGROUND, highlightthickness=0)

#--------------------g/mol VIEW--------------------

def powder_view():
    #~~~~~~~~~~~~~~~~~~~~CALCULATE~~~~~~~~~~~~~~~~~~~~~~~
        def calc():
            mw = float(mol_weight_input.get())
            cons_vol = float(in_vol_input.get()) #stands for constant volume = 1000ml unless said otherwise
            vol_need = float(vol_needed_input.get())
            mol_have = float(have_mol_input.get()) #kept at constant 1 unless said otherwise
            mol_need = float(need_mol_input.get())
            #this does calculations
            divide_first_step = (mw/cons_vol)
            first_overall = divide_first_step * vol_need
            
            df = mol_have / mol_need
            
            #another calculation if mols need to be converted
            final_overall = round((first_overall / df),2)
            
            powder_needed_output.delete(0, END)
            powder_needed_output.insert(0, str(f"{final_overall} g/mol"))
            
        #~~~~~~~~~~~~~~~~~~~~CLEAR~~~~~~~~~~~~~~~~~~~~~~~
        def clear():
            mol_weight_input.delete(0, END)
            in_vol_input.delete(0, END)
            vol_needed_input.delete(0, END)
            have_mol_input.delete(0, END)
            need_mol_input.delete(0, END)
            powder_needed_output.delete(0, END)
            powder_needed_output.insert(0, "˚⊹♡⊹˚₊˚⊹♡⊹˚")
            in_vol_input.insert(0, "1000")
            have_mol_input.insert(0, "1")

        #----------LABELS----------
            #----------[stock] labels----------
        mol_weight = Label(text="MW (g/mol):")
        mol_weight.grid(row=3,column=0, sticky="E")
        mol_weight.config(background=BACKGROUND,foreground=FOREGROUND ,padx=2, pady=2, font=(FONT, SIZE, TYPE))

            #----------[needed] labels----------
        in_vol = Label(text="In vol. (ml):")
        in_vol.grid(row=4,column=0, sticky="E")
        in_vol.config(background=BACKGROUND, foreground=FOREGROUND,padx=2, pady=2, font=(FONT, SIZE, TYPE))

            #----------overall vol. labels----------
        vol_needed = Label(text="Vol. Needed (ml):")
        vol_needed.grid(row=5,column=0, sticky="E")
        vol_needed.config(background=BACKGROUND, foreground=FOREGROUND,padx=2, pady=2, font=(FONT, SIZE, TYPE))

            #----------stock vol needed labels----------
        have_mol = Label(text="Mol Have (M):")
        have_mol.grid(row=6,column=0, sticky="E")
        have_mol.config(background=BACKGROUND, foreground=FOREGROUND, padx=2, pady=2, font=(FONT, SIZE, TYPE))

        need_mol = Label(text="Mol Need (M):")
        need_mol.grid(row=7,column=0, sticky="E")
        need_mol.config(background=BACKGROUND, foreground=FOREGROUND, padx=2, pady=2, font=(FONT, SIZE, TYPE))
        
        powder_needed = Label(text="Grams Needed (g/mol):")
        powder_needed.grid(row=8,column=0, sticky="E")
        powder_needed.config(background=BACKGROUND, foreground=FOREGROUND, padx=2, pady=2, font=(FONT, SIZE, TYPE))
        
            #----------stock vol needed labels----------
        note = Label(text='Note: Default values are due to MW for chemicals being 1M/1L.')
        note.grid(row=10, column=0, columnspan=2, sticky="N")
        note.config(background=BACKGROUND, foreground=FOREGROUND, padx=2, pady=2, font=(FONT, 10, TYPE))

        #entrys
        mol_weight_input = Entry(width=10)
        mol_weight_input.grid(row=3,column=1,sticky="W", padx=2, pady=2)
        mol_weight_input.config(highlightbackground=BACKGROUND, highlightthickness=0)

        in_vol_input = Entry(width=10)
        in_vol_input.grid(row=4,column=1,sticky="W", padx=2, pady=2)
        in_vol_input.config(highlightbackground=BACKGROUND, highlightthickness=0)
        in_vol_input.insert(0, "1000")

        vol_needed_input = Entry(width=10)
        vol_needed_input.grid(row=5,column=1,sticky="W", padx=2, pady=2)
        vol_needed_input.config(highlightbackground=BACKGROUND, highlightthickness=0)

        have_mol_input = Entry(width=10)
        have_mol_input.grid(row=6,column=1,sticky="W", padx=2, pady=2)
        have_mol_input.config(highlightbackground=BACKGROUND, highlightthickness=0)
        have_mol_input.insert(0, "1")

        need_mol_input = Entry(width=10)
        need_mol_input.grid(row=7,column=1,sticky="W", padx=2, pady=2)
        need_mol_input.config(highlightbackground=BACKGROUND, highlightthickness=0)
        
        powder_needed_output = Entry(width=10)
        powder_needed_output.grid(row=8,column=1,sticky="W", padx=2, pady=2)
        powder_needed_output.config(highlightbackground=BACKGROUND, highlightthickness=0)
        powder_needed_output.insert(0, "˚⊹♡⊹˚₊˚⊹♡⊹˚")

        #buttons

        calc_button = Button(text="calculate", width=10, command=calc)
        calc_button.grid(row=9, column=1, padx=2, pady=2)
        calc_button.config(highlightbackground=BACKGROUND, highlightthickness=0)

        clear_button = Button(text="clear", width=10, command=clear)
        clear_button.grid(row=9, column=0, padx=2, pady=2)
        clear_button.config(highlightbackground=BACKGROUND, highlightthickness=0)

#--------------------moles in Solution--------------------
def liquid_view():
    #~~~~~~~~~~~~~~~~~~~~CALCULATE~~~~~~~~~~~~~~~~~~~~~~~
    def calc():
        mol = float(mol_have_input.get())
        bottle_vol = float(in_vol_input.get()) 
        vol_need = float(vol_needed_input.get())
        mol_need = float(need_mol_input.get())
        
        #this does calculations
        divide_first_step = (mol/bottle_vol)
        first_overall = divide_first_step * vol_need
        
        df = mol / mol_need
        
        #another calculation if mols need to be converted
        final_overall_ml = first_overall / df
        final_overall_ul = round((final_overall_ml * 1000), 2)
            
        stock_needed_ml_output.delete(0, END)
        stock_needed_ul_output.delete(0, END)
        
        stock_needed_ml_output.insert(0, str(f"{final_overall_ml} mL"))
        stock_needed_ul_output.insert(0, str(f"{final_overall_ul} uL"))
        
    #~~~~~~~~~~~~~~~~~~~~CLEAR~~~~~~~~~~~~~~~~~~~~~~~
    def clear():
        mol_have_input.delete(0, END)
        in_vol_input.delete(0, END)
        vol_needed_input.delete(0, END)
        need_mol_input.delete(0, END)
        stock_needed_ml_output.delete(0, END)
        stock_needed_ul_output.delete(0, END)
        stock_needed_ml_output.insert(0, "˚⊹♡⊹˚₊˚⊹♡⊹˚")
        stock_needed_ul_output.insert(0, "˚⊹♡⊹˚₊˚⊹♡⊹˚")
        

    #----------LABELS----------
        #----------[stock] labels----------
    mol_have = Label(text="Mol Stock (M):")
    mol_have.grid(row=3,column=0, sticky="E")
    mol_have.config(background=BACKGROUND,foreground=FOREGROUND ,padx=2, pady=2, font=(FONT, SIZE, TYPE))

        #----------[needed] labels----------
    in_vol = Label(text="Vol. Stock (ml):")
    in_vol.grid(row=4,column=0, sticky="E")
    in_vol.config(background=BACKGROUND, foreground=FOREGROUND,padx=2, pady=2, font=(FONT, SIZE, TYPE))

        #----------overall vol. labels----------
    vol_needed = Label(text="Vol. Needed (ml):")
    vol_needed.grid(row=5,column=0, sticky="E")
    vol_needed.config(background=BACKGROUND, foreground=FOREGROUND,padx=2, pady=2, font=(FONT, SIZE, TYPE))

        #----------stock vol needed labels----------

    need_mol = Label(text="Mol Need (M):")
    need_mol.grid(row=6,column=0, sticky="E")
    need_mol.config(background=BACKGROUND, foreground=FOREGROUND, padx=2, pady=2, font=(FONT, SIZE, TYPE))
        
    stock_needed_ml = Label(text="Vol. Stock Needed (ml):")
    stock_needed_ml.grid(row=7,column=0, sticky="E")
    stock_needed_ml.config(background=BACKGROUND, foreground=FOREGROUND, padx=2, pady=2, font=(FONT, SIZE, TYPE))
    
    stock_needed_ul = Label(text="Vol. Stock Needed (ul):")
    stock_needed_ul.grid(row=8,column=0, sticky="E")
    stock_needed_ul.config(background=BACKGROUND, foreground=FOREGROUND, padx=2, pady=2, font=(FONT, SIZE, TYPE))
        
        #----------stock vol needed labels----------
    note = Label(text='Note: Make sure to pay attention to the units!')
    note.grid(row=10, column=0, columnspan=2, sticky="N")
    note.config(background=BACKGROUND, foreground=FOREGROUND, padx=2, pady=2, font=(FONT, 10, TYPE))

    #entrys
    mol_have_input = Entry(width=10)
    mol_have_input.grid(row=3,column=1,sticky="W", padx=2, pady=2)
    mol_have_input.config(highlightbackground=BACKGROUND, highlightthickness=0)

    in_vol_input = Entry(width=10)
    in_vol_input.grid(row=4,column=1,sticky="W", padx=2, pady=2)
    in_vol_input.config(highlightbackground=BACKGROUND, highlightthickness=0)


    vol_needed_input = Entry(width=10)
    vol_needed_input.grid(row=5,column=1,sticky="W", padx=2, pady=2)
    vol_needed_input.config(highlightbackground=BACKGROUND, highlightthickness=0)

    need_mol_input = Entry(width=10)
    need_mol_input.grid(row=6,column=1,sticky="W", padx=2, pady=2)
    need_mol_input.config(highlightbackground=BACKGROUND, highlightthickness=0)

    stock_needed_ml_output = Entry(width=10)
    stock_needed_ml_output.grid(row=7,column=1,sticky="W", padx=2, pady=2)
    stock_needed_ml_output.config(highlightbackground=BACKGROUND, highlightthickness=0)
    stock_needed_ml_output.insert(0, "˚⊹♡⊹˚₊˚⊹♡⊹˚")
    
    stock_needed_ul_output = Entry(width=10)
    stock_needed_ul_output.grid(row=8,column=1,sticky="W", padx=2, pady=2)
    stock_needed_ul_output.config(highlightbackground=BACKGROUND, highlightthickness=0)
    stock_needed_ul_output.insert(0, "˚⊹♡⊹˚₊˚⊹♡⊹˚")

    #buttons

    calc_button = Button(text="calculate", width=10, command=calc)
    calc_button.grid(row=9, column=1, padx=2, pady=2)
    calc_button.config(highlightbackground=BACKGROUND, highlightthickness=0)

    clear_button = Button(text="clear", width=10, command=clear)
    clear_button.grid(row=9, column=0, padx=2, pady=2)
    clear_button.config(highlightbackground=BACKGROUND, highlightthickness=0)
    
#--------------------DNA Copy Number--------------------
def dcn_view(): ##CHRISTINE LEFT OFF HERE
    #~~~~~~~~~~~~~~~~~~~~CALCULATE~~~~~~~~~~~~~~~~~~~~~~~
    def calc():
        temp_len = float(temp_len_input.get()) #LENGTH OF TEMPLATE *good*
        dna_conc = float(dna_conc_input.get()) #DNA CONCENTRATION
        
        #this does calculations
        mult_avo_first_step = (dna_conc * 6.022e23)
        mult_sec_step = (temp_len * 1e9 * 650)
        
        copy_num = mult_avo_first_step / mult_sec_step
        final_copy_num = "{:.4e}".format(copy_num)
        
        num_cop_ul_output.delete(0, END)
        
        num_cop_ul_output.insert(0, str(f"{final_copy_num}"))
        
    #~~~~~~~~~~~~~~~~~~~~CLEAR~~~~~~~~~~~~~~~~~~~~~~~
    def clear():
        temp_len_input.delete(0, END)
        dna_conc_input.delete(0, END)
        num_cop_ul_output.delete(0, END)
        num_cop_ul_output.insert(0, "˚⊹♡⊹˚₊˚⊹♡⊹˚")

    #----------LABELS----------
        #----------Template Length labels----------
    temp_len_have = Label(text="Template Length(bp):")
    temp_len_have.grid(row=3,column=0, sticky="E")
    temp_len_have.config(background=BACKGROUND,foreground=FOREGROUND ,padx=2, pady=2, font=(FONT, SIZE, TYPE))

        #----------DNA Concentration labels----------
    dna_conc_have = Label(text="DNA Concentration(ng/ul):")
    dna_conc_have.grid(row=4,column=0, sticky="E")
    dna_conc_have.config(background=BACKGROUND, foreground=FOREGROUND,padx=2, pady=2, font=(FONT, SIZE, TYPE))

        #----------stock vol needed labels----------
        
    num_cop_ul = Label(text="# of Copies (per ul):")
    num_cop_ul.grid(row=7,column=0, sticky="E")
    num_cop_ul.config(background=BACKGROUND, foreground=FOREGROUND, padx=2, pady=2, font=(FONT, SIZE, TYPE))

        #----------stock vol needed labels----------
    note = Label(text='Note: Make sure to verify your calculations!')
    note.grid(row=10, column=0, columnspan=2, sticky="N")
    note.config(background=BACKGROUND, foreground=FOREGROUND, padx=2, pady=2, font=(FONT, 10, TYPE))

    #entrys
    temp_len_input = Entry(width=10)
    temp_len_input.grid(row=3,column=1,sticky="W", padx=2, pady=2)
    temp_len_input.config(highlightbackground=BACKGROUND, highlightthickness=0)

    dna_conc_input = Entry(width=10)
    dna_conc_input.grid(row=4,column=1,sticky="W", padx=2, pady=2)
    dna_conc_input.config(highlightbackground=BACKGROUND, highlightthickness=0)


    num_cop_ul_output = Entry(width=10)
    num_cop_ul_output.grid(row=7,column=1,sticky="W", padx=2, pady=2)
    num_cop_ul_output.config(highlightbackground=BACKGROUND, highlightthickness=0)
    num_cop_ul_output.insert(0, "˚⊹♡⊹˚₊˚⊹♡⊹˚")

    #buttons

    calc_button = Button(text="calculate", width=10, command=calc)
    calc_button.grid(row=9, column=1, padx=2, pady=2)
    calc_button.config(highlightbackground=BACKGROUND, highlightthickness=0)

    clear_button = Button(text="clear", width=10, command=clear)
    clear_button.grid(row=9, column=0, padx=2, pady=2)
    clear_button.config(highlightbackground=BACKGROUND, highlightthickness=0)

wn.mainloop()