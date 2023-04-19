# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 21:25:39 2023

@author: yangr
"""

import tkinter
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import networkx as nx
import math





#Verbinden mit den mySQl-Datenbank
connection = mysql.connector.connect(host = 'localhost',
                                     port = '3306',
                                     user = 'root',
                                     password = 'Master_Yang!2023',database='hazop_analyse')

cursor = connection.cursor()


connection_2 = mysql.connector.connect(host = 'localhost',
                                     port = '3306',
                                     user = 'root',
                                     password = 'Master_Yang!2023',database='hazop_analyse_result')

cursor_2 = connection_2.cursor()





info_sub = {}
info_ghss = {}
stoichio = {}



def enter_substance(substance):
    
    
    def maunu_enter_sub():
        #print("well done")
        #global subinfo1
        #global ghs_exist1
        
        molarmass = molarmass_entry.get()
        boilingpoint = boilingpoint_entry.get()
        flashpoint = flashpoint_entry.get()
        autotemp = autoitemperature_entry.get()
        heatcapa = heatcapa_entry.get()
        heatformation = heatformation_entry.get()
        maxdecompo = decompositionmax_entry.get()
        mindecompo = decompositionmin_entry.get()
        
        if heatcapa and heatformation and molarmass:
            subinfo1 = [substance, molarmass, boilingpoint, flashpoint, autotemp, heatcapa, heatformation, maxdecompo, mindecompo]
            print(subinfo1)
            ghs1 =  ghs1_status_var.get()
            ghs2 =  ghs2_status_var.get()
            ghs3 =  ghs3_status_var.get()
            ghs4 =  ghs4_status_var.get()
            ghs5 =  ghs5_status_var.get()
            ghs6 =  ghs6_status_var.get()
            ghs7 =  ghs7_status_var.get()
            ghs8 =  ghs8_status_var.get()
            ghs9 =  ghs9_status_var.get()
            ghs_information = [ghs1, ghs2, ghs3, ghs4, ghs5, ghs6, ghs7, ghs8, ghs9]
            ghs_exist1 = [x for x in ghs_information if x!='No']
            print(ghs_exist1)
            tkinter.messagebox.showinfo(title=" ", message="Submitted, you can close the substance input window and try again:)")
            info_sub[substance] = subinfo1
            info_ghss[substance] = ghs_exist1
        else:
            tkinter.messagebox.showwarning(title="Error", message="Heat Capacity, Heats of formation and Molar mass are required.")
            
    
    window2 = tkinter.Toplevel()
    #window = tkinter.Tk()
    window2.title("Please enter the " + substance + " information")
    
    frame2 = tkinter.Frame(window2)
    frame2.pack()
    
    #Saving Substance Information
    substance_frame = tkinter.LabelFrame(frame2)
    substance_frame.grid(row=0, column=0, padx=20, pady=10)
    
    name_label = tkinter.Label(substance_frame, text = substance)
    name_label.grid(row=1, column=0)
    
    molarmass_label = tkinter.Label(substance_frame, text = "Molar Mass [g/mol]")
    molarmass_label.grid(row=0, column=1)
    boilingpoint_label = tkinter.Label(substance_frame, text = "Boiling Point [°C]")
    boilingpoint_label.grid(row=0, column=2)
    flashpoint_label = tkinter.Label(substance_frame, text = "Flash Point [°C]")
    flashpoint_label.grid(row=0, column=3)
    autoitemperature_label = tkinter.Label(substance_frame, text = "Autoignition Temperature [°C]")
    autoitemperature_label.grid(row=0, column=4)
    heatcapa_label = tkinter.Label(substance_frame, text = "Heat Capacity [J/mol*K]")
    heatcapa_label.grid(row=0, column=5)
    heatformation_label = tkinter.Label(substance_frame, text = "Heat of Formations [kJ/mol]")
    heatformation_label.grid(row=2, column=5)
    decompositionmax_label = tkinter.Label(substance_frame, text = "Maximum Decomposition Temperature [°C]")
    decompositionmax_label.grid(row=2, column=2)
    decompositionmin_label = tkinter.Label(substance_frame, text = "Minimum Decomposition Temperature [°C]")
    decompositionmin_label.grid(row=2, column=4)
    
    molarmass_entry = tkinter.Entry(substance_frame)
    molarmass_entry.grid(row=1, column=1)
    boilingpoint_entry = tkinter.Entry(substance_frame)
    boilingpoint_entry.grid(row=1, column=2)
    flashpoint_entry = tkinter.Entry(substance_frame)
    flashpoint_entry.grid(row=1, column=3)
    autoitemperature_entry = tkinter.Entry(substance_frame)
    autoitemperature_entry.grid(row=1, column=4)
    heatcapa_entry = tkinter.Entry(substance_frame)
    heatcapa_entry.grid(row=1, column=5)
    heatformation_entry = tkinter.Entry(substance_frame)
    heatformation_entry.grid(row=3, column=5)
    decompositionmax_entry = tkinter.Entry(substance_frame)
    decompositionmax_entry.grid(row=3, column=2)
    decompositionmin_entry = tkinter.Entry(substance_frame)
    decompositionmin_entry.grid(row=3, column=4)
    
    for widget in substance_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)
        
    
    ghs_frame = tkinter.LabelFrame(frame2, text="GHS Inforamtion")
    ghs_frame.grid(row=1, column=0, padx=20, pady=10)
    
    #label for GHS 1
    image1 = Image.open(".\GUI_Picture\GHS01_explos.png")
    resize_image1 = image1.resize((60, 60))
    img1 = ImageTk.PhotoImage(resize_image1)
    
    explosive_label = tkinter.Label(ghs_frame, text="Explosive")
    explosive_label.grid(row=0, column=0)
    explosive_label.image = img1
    explosive_label["compound"] = tkinter.TOP
    explosive_label["image"] = img1
    
    #label for GHS 2
    image2 = Image.open(".\GUI_Picture\GHS02_flamme.png")
    resize_image2 = image2.resize((60, 60))
    img2 = ImageTk.PhotoImage(resize_image2)
    
    flammable_label = tkinter.Label(ghs_frame, text="Flammable")
    flammable_label.grid(row=0, column=1)
    flammable_label.image = img1
    flammable_label["compound"] = tkinter.TOP
    flammable_label["image"] = img2
    
    #label for GHS 3
    image3 = Image.open(".\GUI_Picture\GHS03_rondflam.png")
    resize_image3 = image3.resize((60, 60))
    img3 = ImageTk.PhotoImage(resize_image3)
    
    oxidizing_label = tkinter.Label(ghs_frame, text="Oxidizing")
    oxidizing_label.grid(row=0, column=2)
    oxidizing_label.image = img3
    oxidizing_label["compound"] = tkinter.TOP
    oxidizing_label["image"] = img3
    
    #label for GHS 4
    image4 = Image.open(".\GUI_Picture\GHS04_bottle.png")
    resize_image4 = image4.resize((60, 60))
    img4 = ImageTk.PhotoImage(resize_image4)
    
    compressedgas_label = tkinter.Label(ghs_frame, text="Compressed Gas")
    compressedgas_label.grid(row=0, column=3)
    compressedgas_label.image = img4
    compressedgas_label["compound"] = tkinter.TOP
    compressedgas_label["image"] = img4
    
    #label for GHS 5
    image5 = Image.open(".\GUI_Picture\GHS05_acid_red.png")
    resize_image5 = image5.resize((60, 60))
    img5 = ImageTk.PhotoImage(resize_image5)
    
    corrosive_label = tkinter.Label(ghs_frame, text="Corrosive")
    corrosive_label.grid(row=0, column=4)
    corrosive_label.image = img5
    corrosive_label["compound"] = tkinter.TOP
    corrosive_label["image"] = img5
    
    #label for GHS 6
    image6 = Image.open(".\GUI_Picture\GHS06_skull.png")
    resize_image6 = image6.resize((60, 60))
    img6 = ImageTk.PhotoImage(resize_image6)
    
    toxic_label = tkinter.Label(ghs_frame, text="Toxic")
    toxic_label.grid(row=0, column=5)
    toxic_label.image = img6
    toxic_label["compound"] = tkinter.TOP
    toxic_label["image"] = img6
    
    #label for GHS 7
    image7 = Image.open(".\GUI_Picture\GHS07_exclam.png")
    resize_image7 = image7.resize((60, 60))
    img7 = ImageTk.PhotoImage(resize_image7)
    
    harmful_label = tkinter.Label(ghs_frame, text="Harmful")
    harmful_label.grid(row=0, column=6)
    harmful_label.image = img4
    harmful_label["compound"] = tkinter.TOP
    harmful_label["image"] = img7
    
    #label for GHS 8
    image8 = Image.open(".\GUI_Picture\GHS08_silhouete.png")
    resize_image8 = image8.resize((60, 60))
    img8 = ImageTk.PhotoImage(resize_image8)
    
    healthhazard_label = tkinter.Label(ghs_frame, text="Health Hazard")
    healthhazard_label.grid(row=0, column=7)
    healthhazard_label.image = img8
    healthhazard_label["compound"] = tkinter.TOP
    healthhazard_label["image"] = img8
    
    #label for GHS 9
    image9 = Image.open(".\GUI_Picture\GHS09_aq-pollut.png")
    resize_image9 = image9.resize((60, 60))
    img9 = ImageTk.PhotoImage(resize_image9)
    
    enviromenthazard_label = tkinter.Label(ghs_frame, text="Enviroment Hazard")
    enviromenthazard_label.grid(row=0, column=8)
    enviromenthazard_label.image = img9
    enviromenthazard_label["compound"] = tkinter.TOP
    enviromenthazard_label["image"] = img9
    
    
    #Add check button
    ghs1_status_var = tkinter.StringVar(value="No")
    explosive_check = tkinter.Checkbutton(ghs_frame, text="Yes", variable=ghs1_status_var, onvalue="Explosive", offvalue="No")
    explosive_check.grid(row=1, column=0)
    
    ghs2_status_var = tkinter.StringVar(value="No")
    flammable_check = tkinter.Checkbutton(ghs_frame, text="Yes", variable=ghs2_status_var, onvalue="Flammable", offvalue="No")
    flammable_check.grid(row=1, column=1)
    
    ghs3_status_var = tkinter.StringVar(value="No")
    oxidizing_check = tkinter.Checkbutton(ghs_frame, text="Yes", variable=ghs3_status_var, onvalue="Oxidizing", offvalue="No")
    oxidizing_check.grid(row=1, column=2)
    
    ghs4_status_var = tkinter.StringVar(value="No")
    compressedgas_check = tkinter.Checkbutton(ghs_frame, text="Yes", variable=ghs4_status_var, onvalue="Compressed Gas", offvalue="No")
    compressedgas_check.grid(row=1, column=3)
    
    ghs5_status_var = tkinter.StringVar(value="No")
    corrosive_check = tkinter.Checkbutton(ghs_frame, text="Yes", variable=ghs5_status_var, onvalue="Corrosive", offvalue="No")
    corrosive_check.grid(row=1, column=4)
    
    ghs6_status_var = tkinter.StringVar(value="No")
    toxic_check = tkinter.Checkbutton(ghs_frame, text="Yes", variable=ghs6_status_var, onvalue="Toxic", offvalue="No")
    toxic_check.grid(row=1, column=5)
    
    ghs7_status_var = tkinter.StringVar(value="No")
    harmful_check = tkinter.Checkbutton(ghs_frame, text="Yes", variable=ghs7_status_var, onvalue="Harmful", offvalue="No")
    harmful_check.grid(row=1, column=6)
    
    ghs8_status_var = tkinter.StringVar(value="No")
    healthhazard_check = tkinter.Checkbutton(ghs_frame, text="Yes", variable=ghs8_status_var, onvalue="Health Hazard", offvalue="No")
    healthhazard_check.grid(row=1, column=7)
    
    ghs9_status_var = tkinter.StringVar(value="No")
    enviromenthazard_check = tkinter.Checkbutton(ghs_frame, text="Yes", variable=ghs9_status_var, onvalue="Enviroment Hazard", offvalue="No")
    enviromenthazard_check.grid(row=1, column=8)    
    
    for widget in ghs_frame.winfo_children():
        widget.grid_configure(padx=20, pady=5)


    #Reference
    quelle_frame = tkinter.LabelFrame(frame2, text="Reference")
    quelle_frame.grid(row=2, column=0, padx=20, pady=10)
    
    imagefrom_label = tkinter.Label(quelle_frame, text="Photos from https://www.reach-compliance.ch/ghsclp/neuegefahrenpiktogramme/ ")
    imagefrom_label.grid(row=0, column=0)         
        
    #Button
    button1 = tkinter.Button(frame2, text="Enter data", command= maunu_enter_sub)
    button1.grid(row=3, column=0, sticky="news", padx=20, pady=10)
    button2 = tkinter.Button(frame2, text="close window", command = window2.destroy)
    button2.grid(row=4, column=0, sticky="news", padx=20, pady=10)

    window2.mainloop()







def enter_data():
    #print("finish!")
    #global info_sub
    #global info_ghss
    global exist_stoff
    global exist_reaction_stoff
    global reaction_temp
    #global A_factor
    #global Ea
    #global Reactor_name
    atom_pressure = pressure_var.get()
    
    if atom_pressure == "Yes":
        
        reactant1 = reactant1_combobox.get()
        reactant2 = reactant2_combobox.get()
        reactant3 = reactant3_combobox.get()
        product1 = product1_combobox.get()
        product2 = product2_combobox.get()
        product3 = product3_combobox.get()
        solvent = solvent_combobox.get()
        
        v1 = v1_combobox.get()
        v2 = v2_combobox.get()
        v3 = v3_combobox.get()
        v4 = v4_combobox.get()
        v5 = v5_combobox.get()
        v6 = v6_combobox.get()
        
        
        reaction_temp = temperature_entry.get()
        #A_factor = A_faktor_entry.get()
        #Ea = Ea_entry.get()
        #Reactor_name = reactor_entry.get()
        
        reaction_stoff = [reactant1, reactant2, reactant3, product1, product2, product3]
        stoi_input_list = [-int(v1), -int(v2), -int(v3), int(v4), int(v5), int(v6)]
        
        
        for compo, vv in zip(reaction_stoff, stoi_input_list):
            if compo and vv != 0:
                stoichio[compo] = vv
        
               
        
        #print(stoff)
        stoff = [reactant1, reactant2, reactant3, product1, product2, product3, solvent]
        exist_stoff = [x for x in stoff if x]
        exist_reaction_stoff = [x for x in reaction_stoff if x]
        print(exist_stoff)
        #print(len(exist_stoff))
        #print(len(info_sub))
        #if len(exist_stoff) ==len(info_sub):
        #    
        
        #else:    
        for sub in exist_stoff:
            if sub not in info_sub:
                print(sub)
                query = "SELECT COUNT(Name) FROM stoffdaten WHERE Name=%s"
                cursor.execute(query, (sub,))
                exist = cursor.fetchone()
                exist_check = exist[0]
                print(exist_check)
                if exist_check == 1:
                    query_1 = "SELECT Name,MolarMass,BoilingPoint,FlashPoint,AutoignitionTemperature,Heat_capacity_Tn,Heats_of_Formations, Max_DecompositionTemperature, Min_DecompositionTemperature FROM stoffdaten WHERE Name = %s"
                    cursor.execute(query_1, (sub,))
                    results = cursor.fetchall()
                    for row in results:
                        subinfo = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]]
                        print(subinfo)
                    query_2 = "SELECT Explosive, Flammable, Oxidizing, CompressedGas, Corrosive, Toxic, Harmful, HealthHazard, EnviromenalHazard FROM stoffdaten_copy WHERE Name = %s"
                    cursor.execute(query_2, (sub,))
                    ghs_name = ["Explosive", "Flammable", "Oxidizing", "CompressedGas", "Corrosive", "Toxic", "Harmful", "Health Hazard", "Enviroment Hazard"]
                    result_ghs = cursor.fetchall()
                    for row in result_ghs:
                        ghs_info = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]]
                        
                    info_ghss[sub] = []
                    for x,y in zip(ghs_name,ghs_info):
                        if y == "Yes":
                            info_ghss[sub].append(x)
                    info_sub[sub] = subinfo

                    
                elif exist_check ==0:                
                    if sub not in info_sub:
                        tkinter.messagebox.showwarning(title="Error", message="The substance "+ sub + " is not in the database")
                        enter_substance(sub)
                #info_sub[sub] = subinfo1
                #info_ghss[sub] = ghs_exist1
        #print(info_sub)
        #print(info_ghss)
        #if len(info_sub) == len(exist_stoff):
        #    print("successful")
        #tkinter.messagebox.showinfo(title="Good", message="successful, you can close this window.")
                                
    else:
        tkinter.messagebox.showwarning(title="Sorry", message="analysing now only works at atmospheric pressure.")




def close_main_window():
    if len(info_sub) == len(exist_stoff):        
        window.destroy()
        print(info_sub)
        print(info_ghss)
        print("successful")
        #tkinter.messagebox.showinfo(title="Good", message="Well done")
        
    else:
        tkinter.messagebox.showerror(title="Error", message="Error, please try to enter again")
        #print("Error, please try to enter again")

















window = tkinter.Tk()
window.title("Reaction Entry Form")

frame1 = tkinter.Frame(window)
frame1.pack()

#Saving reaction Info
reaction_frame = tkinter.LabelFrame(frame1, text="Chemical equation")
reaction_frame.grid(row=0, column=0, padx=20, pady=10)



reactant1_label = tkinter.Label(reaction_frame, text="Reactant 1")
reactant1_label.grid(row=0, column=0)

plus1_label = tkinter.Label(reaction_frame, text="+")
plus1_label.grid(row=1, column=1)

reactant2_label = tkinter.Label(reaction_frame, text="Reactant 2")
reactant2_label.grid(row=0, column=2)

plus2_label = tkinter.Label(reaction_frame, text="+")
plus2_label.grid(row=1, column=3)

reactant3_label = tkinter.Label(reaction_frame, text="Reactant 3")
reactant3_label.grid(row=0, column=4)

plus2_label = tkinter.Label(reaction_frame, text="------>")
plus2_label.grid(row=1, column=5)

product1_label = tkinter.Label(reaction_frame, text="Product 1")
product1_label.grid(row=0, column=6)

plus3_label = tkinter.Label(reaction_frame, text="+")
plus3_label.grid(row=1, column=7)

product2_label = tkinter.Label(reaction_frame, text="Product 2")
product2_label.grid(row=0, column=8)

plus4_label = tkinter.Label(reaction_frame, text="+")
plus4_label.grid(row=1, column=9)

product3_label = tkinter.Label(reaction_frame, text="Product 3")
product3_label.grid(row=0, column=10)

Stofflist_combo = ['1,2-Propanediol', '1,3-Butadiene', '1-Butanol', '1-Butene', '2-Propanol', 'Acetic acid', 'Acetic anhydride', 'Acetone', 'Acetylene', 'Acrolein', 'Acrylic acid', 'Adipic acid', 'Ammonia, anhydrous', 'Aniline', 'Benzene', 'Carbon dioxide', 'Carbon monoxide', 'Chlorine', 'Chlorobenzene', 'Chloroform', 'Cumene', 'Cyclohexane', 'Ethanol', 'Ethyl acetate', 'Ethylbenzene', 'Ethylene', 'Ethylene dichloride', 'Ethylene glycol', 'Ethylene oxide', 'Formaldehyde', 'Formic acid', 'Hydrochloric acid solution', 'Hydrogen', 'Hydrogen cyanide', 'Hydrogen peroxide', 'Hydrogen sulfide', 'Mercury', 'Methane', 'Methanol', 'Methyl acetate', 'Methyl chloride', 'Methyl formate', 'Methylene chloride', 'N-butyl acetate', 'Nitrogen', 'Oxygen', 'Phenol', 'Phthalic anhydride', 'Propane', 'Propene', 'Propylene oxide', 'Sodium carbonate', 'Styrene', 'Sulfur', 'Sulfur dioxide', 'Sulfuric acid', 'Toluene', 'Vinyl chloride', 'Water', 'm-Xylene', 'n-Hexane', 'o-Xylene', 'p-Xylene']

reactant1_combobox = ttk.Combobox(reaction_frame, values=Stofflist_combo)
reactant2_combobox = ttk.Combobox(reaction_frame, values=Stofflist_combo)
reactant3_combobox = ttk.Combobox(reaction_frame, values=Stofflist_combo)
product1_combobox = ttk.Combobox(reaction_frame, values=Stofflist_combo)
product2_combobox = ttk.Combobox(reaction_frame, values=Stofflist_combo)
product3_combobox = ttk.Combobox(reaction_frame, values=Stofflist_combo)


reactant1_combobox.grid(row=1, column=0)
reactant2_combobox.grid(row=1, column=2)
reactant3_combobox.grid(row=1, column=4)
product1_combobox.grid(row=1, column=6)
product2_combobox.grid(row=1, column=8)
product3_combobox.grid(row=1, column=10)

for widget in reaction_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
    
    
#Saving Stoichiometry Info
stoichiometry_frame = tkinter.LabelFrame(frame1, text="Chemical equation stoichiometry")
stoichiometry_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)


v1_label = tkinter.Label(stoichiometry_frame, text=chr(957)+"1")
v1_label.grid(row=0, column=0)

blank1_label = tkinter.Label(stoichiometry_frame, text="      ")
blank1_label.grid(row=1, column=1)

v2_label = tkinter.Label(stoichiometry_frame, text=chr(957)+"2")
v2_label.grid(row=0, column=2)

blank2_label = tkinter.Label(stoichiometry_frame, text="      ")
blank2_label.grid(row=1, column=3)

v3_label = tkinter.Label(stoichiometry_frame, text=chr(957)+"3")
v3_label.grid(row=0, column=4)

blank3_label = tkinter.Label(stoichiometry_frame, text="               ")
blank3_label.grid(row=1, column=5)

v4_label = tkinter.Label(stoichiometry_frame, text=chr(957)+"4")
v4_label.grid(row=0, column=6)

blank4_label = tkinter.Label(stoichiometry_frame, text="      ")
blank4_label.grid(row=1, column=7)

v5_label = tkinter.Label(stoichiometry_frame, text=chr(957)+"5")
v5_label.grid(row=0, column=8)

blank5_label = tkinter.Label(stoichiometry_frame, text="      ")
blank5_label.grid(row=1, column=9)

v6_label = tkinter.Label(stoichiometry_frame, text=chr(957)+"6")
v6_label.grid(row=0, column=10)

v1_combobox = tkinter.Spinbox(stoichiometry_frame, from_=0, to=100)
v2_combobox = tkinter.Spinbox(stoichiometry_frame, from_=0, to=100)
v3_combobox = tkinter.Spinbox(stoichiometry_frame, from_=0, to=100)
v4_combobox = tkinter.Spinbox(stoichiometry_frame, from_=0, to=100)
v5_combobox = tkinter.Spinbox(stoichiometry_frame, from_=0, to=100)
v6_combobox = tkinter.Spinbox(stoichiometry_frame, from_=0, to=100)

v1_combobox.grid(row=1, column=0)
v2_combobox.grid(row=1, column=2)
v3_combobox.grid(row=1, column=4)
v4_combobox.grid(row=1, column=6)
v5_combobox.grid(row=1, column=8)
v6_combobox.grid(row=1, column=10)

for widget in stoichiometry_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Saving Reaction conditions
condition_frame = tkinter.LabelFrame(frame1, text="reaction conditions")
condition_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

temperature_label = tkinter.Label(condition_frame, text="reaction temperature [°C]")
temperature_label.grid(row=0, column=0)

temperature_entry = tkinter.Entry(condition_frame)
temperature_entry.grid(row=1, column=0)

#A_faktor_label = tkinter.Label(condition_frame, text="frequency factor A [L/mol*s]")
#A_faktor_label.grid(row=0, column=1)

#A_faktor_entry = tkinter.Entry(condition_frame)
#A_faktor_entry.grid(row=1, column=1)

#Ea_label = tkinter.Label(condition_frame, text="activation energy [J/mol]")
#Ea_label.grid(row=0, column=2)

#Ea_entry = tkinter.Entry(condition_frame)
#Ea_entry.grid(row=1, column=2)

pressure_var = tkinter.StringVar(value="No")
pressure_check = tkinter.Checkbutton(condition_frame, text="The reaction takes place at atmospheric pressure.", variable=pressure_var, onvalue="Yes", offvalue="No")
pressure_check.grid(row=1, column=4)

solvent_label = tkinter.Label(condition_frame, text="Solvent, if it exists")
solvent_label.grid(row=2, column=0)

solvent_combobox = ttk.Combobox(condition_frame, values=Stofflist_combo)
solvent_combobox.grid(row=3, column=0)

#reactor_label = tkinter.Label(condition_frame, text="Reactor node name")
#reactor_label.grid(row=2, column=1)

#reactor_entry = tkinter.Entry(condition_frame)
#reactor_entry.grid(row=3, column=1)




for widget in condition_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


#Button
button3 = tkinter.Button(frame1, text="Enter data", command=enter_data)
button3.grid(row=3, column=0, sticky="news", padx=20, pady=10)

button4 = tkinter.Button(frame1, text="Update and close", command =close_main_window)
button4.grid(row=4, column=0, sticky="news", padx=20, pady=10)



window.mainloop()



#print(stoichio)
#print(reaction_temp)
#print(exist_reaction_stoff)
#print(info_sub)
#print(info_ghss)


#Um die adiabate Temperaturerhöhung und MSTR zu rechnen
Qr = 0
mix_capa_top = 0
mix_capa_bottom = 0

for i in exist_reaction_stoff:
    Qr  = Qr + float(info_sub[i][6])*stoichio[i]
    if stoichio[i] > 0:
        c_p = float(info_sub[i][5])/float(info_sub[i][1])
        mol = float(info_sub[i][1])
        mix_capa_top = mix_capa_top + c_p*mol*stoichio[i]
        mix_capa_bottom = mix_capa_bottom + mol*stoichio[i]
        mix_capa = mix_capa_top/mix_capa_bottom

delta_Tr = -Qr*1000/(mix_capa*mix_capa_bottom)


#print(mix_capa)

delta_Tr = -Qr*1000/(mix_capa*mix_capa_bottom)
print("delta_Tr: " + str(delta_Tr))



MSTR = delta_Tr + float(reaction_temp)

print("MSTR: ")
print("delta_Tr: " + str(MSTR))



#Um die Hazop_Inhalte zu erstellendef severity_check (delta_Tr):
def severity_check (delta_Tr):
    if delta_Tr > 400:
        severity = 'Catastrophic'
    elif 400 > delta_Tr > 200:
        severity = 'Critical'
    elif 200 > delta_Tr > 50:
        severity = 'Low'
    else:
        severity = 'Negligible'

    description = severity + " runaway reaction"
    print("This is a " + description)
    return description
    


overpressure_risk = 0
toxic_risk = 0
flamm_risk = 0
ignition_risk = 0
no_possible = 0
safe_info = "Decompositions risk of "


for i in exist_stoff:
    if float(info_sub[i][2]) < MSTR:
        overpressure_risk = overpressure_risk + 1
        for ghs_check in info_ghss[i]:
            if ghs_check == "Toxic":
                toxic_risk = toxic_risk + 1
            elif ghs_check == "Flammable":
                flamm_risk = flamm_risk + 1
        
        
    if info_sub[i][7] != '-':
        if float(info_sub[i][7]) < MSTR:
            safe_info = safe_info + i + ','
            
    if float(info_sub[i][4]) < MSTR:
        ignition_risk = ignition_risk + 1
        
    if float(info_sub[i][2]) > MSTR:
        for y in exist_stoff:
            if MSTR > float(info_sub[i][7]):            
                no_possible = no_possible + 1



def consequence_safe_1(overpressure_risk, toxic_risk, flamm_risk):
    if overpressure_risk > 0 and toxic_risk > 0 and flamm_risk > 0:
        consequence_1 = "risk of boiling liquid expanding vapor explosion and formation of toxic and flammable clouds."
        safeguard_1 = "Install rupture disk burst or safety valve and the direktion, direction, location due to toxic substances must be very well considered."         
    elif overpressure_risk > 0 and toxic_risk > 0 and flamm_risk == 0:
        consequence_1 = "risk of boiling liquid expanding vapor explosion and formation of toxic clouds."
        safeguard_1 = "Install rupture disk burst and the highest level of safety protechtion must be provided to workers on site"
    
    elif overpressure_risk > 0 and toxic_risk == 0 and flamm_risk > 0:
        consequence_1 = "risk of boiling liquid expanding vapor explosion and formation of flammable clouds."
        safeguard_1 = "Install rupture disk burst and sources of fire must be avoided on site"
    elif overpressure_risk > 0 and toxic_risk == 0 and flamm_risk == 0:
        consequence_1 = "risk of boiling liquid expanding vapor explosion."
        safeguard_1 = "Install rupture disk burst"
        
    if no_possible > 0:
        consequence_1 = "No way to stop the reaction!"
        safeguard_1 = "Do not recommend running this process."
    return [consequence_1, safeguard_1]




def consequence_2(safe_info4):
    if safe_info4 != "Decompositions risk of ":
        consequence_2 = safe_info4.rstrip(',')        
    else:
        consequence_2 = '-'
    return consequence_2
  

      
def consequence_3(ignition_risk):
    if ignition_risk > 0:
        consequence_3 = "risk of explosion with fire"
    elif ignition_risk == 0:
        consequence_3 = "-"
    return consequence_3

descrip = severity_check (MSTR)


a = consequence_safe_1(overpressure_risk, toxic_risk, flamm_risk)
print("--------------------------------------------------------------------------")
print("Risks: ")
print(a[0])

con_2 = consequence_2(safe_info)
print(con_2)
    
con_3 = consequence_3(ignition_risk)
print(con_3)

subs_for_result = ','.join(exist_stoff)

print("---------------------------------------------------------------------------")
print("Safeguards: ")
print(a[1])







connection.commit()
connection.close()

connection_2.commit()
connection_2.close()




















