# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 11:28:27 2022

@author: yangr
"""

import networkx as nx
import mysql.connector
import os
#import pandas as pd
import tkinter
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk


#Verbinden mit den mySQl-Datenbank
connection_1 = mysql.connector.connect(host = 'localhost',
                                     port = '3306',
                                     user = 'root',
                                     password = 'Master_Yang!2023',database='hazop_analyse')

cursor_1 = connection_1.cursor()

connection_2 = mysql.connector.connect(host = 'localhost',
                                     port = '3306',
                                     user = 'root',
                                     password = 'Master_Yang!2023',database='hazop_analyse_result')
cursor_2 = connection_2.cursor()

#g = nx.read_graphml('./1____Graph_Plus.xml')



Input_name = 'cstr_024'
Table_Name = 'hazop_analyse_' + Input_name
Input_Ordner_name = "Druckraum_CSTR_Graph_Plus"

# Für die Druckrüme der Pumpe, Bypass zu überprüfen
comp_g = nx.read_graphml("./CSTR_Graph_Plus.xml")



# Funktion, um die Austrittsmenge zu beurteilen und mit Hilfe von Signalword zu 
def Einstufen_des_Ausmaßes(Austrittsmenge, Signalword):
    if Signalword == 'Danger':
        if Austrittsmenge <= 4.5:
            return 'S3'
        elif 4.5 < Austrittsmenge <= 45:
            return 'S2'
        elif 45 < Austrittsmenge <= 4500:
            return 'S1'
        elif Austrittsmenge > 4500:
            return 'S0'
    elif Signalword == 'Warning':
        if Austrittsmenge <= 4.5:
            return 'S4'
        elif 4.5 < Austrittsmenge <= 45:
            return 'S3'
        elif 45 < Austrittsmenge <= 4500:
            return 'S2'
        elif 4500 < Austrittsmenge <= 45000:
            return 'S1'
        else:
            return 'S0'
    else:
        if Austrittsmenge <= 450:
            return 'S4'
        elif 450 < Austrittsmenge <= 45000:
            return 'S3'
        else:
            return 'S2'


# Funktion, um die richtige Stufe einzugeben, wenn zwei Stufen exisieren. 
def finden_Stufen(x,y):
    number_x = int(x[1])
    number_y = int(y[1])
    if number_x > number_y:
        return y
    else:
        return x
    

# Funktion, um die richtige Stufe von einer List einzugeben.
def finden_Stufen_in_List(stufen):
    s = list(set(stufen))
    if s != ['-'] and s != [None] and s != ['']:
        x = [int(x[1]) for x in stufen if x != '-']
        k = min(x)
        stufe = 'S'+str(k)
        return stufe
    else:
        return '-'    

# Funktion zur Bestimmung der Gefahrenstufen des Gemisches in der Rohrleitung
def finde_Stufen_Mischung(g, edge):
    stoffnames = g.get_edge_data(*edge)['subs']
    
    
    if stoffnames not in ['n.d.', 'n.a.']:
        allstoff = list(g.get_edge_data(*edge)['subs'].split(", "))
        molfraction = {}
        for stoff in allstoff:
            mol_fraction_name_1 = 'mol_fraction_' + stoff
            mol_fraction_name = mol_fraction_name_1.replace(" ", "_")
            molfraction[stoff] = float(g.get_edge_data(*edge)[mol_fraction_name].replace(',','.'))
        
        if g.get_edge_data(*edge)['Mass_flow_unit'] == 'g/s':
            massflow = float(g.get_edge_data(*edge)['Mass_flow'].replace(',','.')) * 60 * 20 * 0.001
        elif g.get_edge_data(*edge)['Mass_flow_unit'] == 'kg/h':
            massflow = float(g.get_edge_data(*edge)['Mass_flow'].replace(',','.')) * 1 / 3
        stoffinfo = {} 
        wi_unten = 0
        for i in allstoff:
            #print(i)
            query = "SELECT MolarMass, Signalword FROM stoffdaten WHERE Name = %s"
            cursor_1.execute(query, (i,))
            result = cursor_1.fetchone()
            info = {}
            info['Molar mass'] = float(result[0])
            info['Signalword'] = result[1]
            stoffinfo[i] = info
            wi_unten = wi_unten + info['Molar mass'] * molfraction[i]
            
        danger_mass = 0
        warning_mass = 0
        for i in allstoff:
            wi = stoffinfo[i]['Molar mass'] * molfraction[i] / wi_unten
            mi = wi * massflow
            stoffinfo[i]['mi'] = mi
            if stoffinfo[i]['Signalword'] == 'Danger':
                danger_mass = danger_mass + mi
            elif stoffinfo[i]['Signalword'] == 'Warning':
                warning_mass = warning_mass + mi
        
        stufe1 = Einstufen_des_Ausmaßes(danger_mass, 'Danger')
        stufe2 = Einstufen_des_Ausmaßes(warning_mass, 'Warning')
        stufe = finden_Stufen(stufe1, stufe2)
        #print(stufe)
        return stufe
            #wi = molfraction[i] * float(info['Molar mass']) / ()
        

# Identifizieren der Gefährdungsstufen für Apparate wie Reaktor, Behälter
def finde_Stufen_in_Vessel(g,node):
    edges_out = list(g.out_edges(node))
    edges_in = list(g.in_edges(node))
    
    piping_out = [x for x in edges_out if g.get_edge_data(*x)['Class'] in ['Piping', 'Pipe'] and g.get_edge_data(*x)['subs'] not in ['n.a.', 'n.d']]
    piping_in = [x for x in edges_in if g.get_edge_data(*x)['Class'] in ['Piping', 'Pipe'] and g.get_edge_data(*x)['subs'] not in ['n.a.', 'n.d']]
    print(piping_out)
    print(node)
    print(piping_in)
    print("-----------------")
    if piping_out != [] and piping_in !=[]:
        edge = piping_out[0]
    elif piping_out != []:
        edge = piping_out[0]
    elif piping_in != []:
        edge = piping_in[0]
    #elif piping_in != [] and piping_out == []:
        #edge = piping_in[0]
    else:
        print(piping_out)
        print(piping_in)
        edge = 'None'

 
    if edge != 'None':
        molfraction = {}
        stoff_vessel = list(g.get_edge_data(*edge)['subs'].split(", "))
        density = float(g.get_edge_data(*edge)['Mass_flow'].replace(',','.')) / float(g.get_edge_data(*edge)['Volume_flow'].replace(',','.'))
        Massen_i = 0
        if g._node[node]['V'] not in ['n.a.', 'n.d.']:
            if g.get_edge_data(*edge)['Volume_flow_unit'] == 'm3/h':
                V = float(g._node[node]['V'].replace(',','.')) 
                Massen_i = V * density + Massen_i
    
            elif g.get_edge_data(*edge)['Volume_flow_unit'] == 'L/min':
                V = float(g._node[node]['V'].replace(',','.'))            
                Massen_i = V * density * 60 * 0.001 + Massen_i
                
        Massen = Massen_i

        if Massen != 0:
            for stoff in stoff_vessel:
                mol_fraction_name_2 = 'mol_fraction_' + stoff
                mol_fraction_name_vessel = mol_fraction_name_2.replace(" ", "_")
                molfraction[stoff] = float(g.get_edge_data(*edge)[mol_fraction_name_vessel].replace(',','.'))
            stoffinfo = {}
            wi_unten = 0
            for i in stoff_vessel:
                query = "SELECT MolarMass, Signalword FROM stoffdaten WHERE Name = %s"
                cursor_1.execute(query, (i,))
                result = cursor_1.fetchone()
                info = {}
                #print(result[0])
                info['Molar mass'] = float(result[0])
                info['Signalword'] = result[1]
                stoffinfo[i] = info
                wi_unten = wi_unten + info['Molar mass'] * molfraction[i]
                #vi_unten = vi_unten + info['Molar mass'] * molfraction[i] / info['Density']
            # 1.5 L 
        
            danger_mass = 0
            warning_mass = 0
            if Massen != 0:
                for i in stoff_vessel:
                    #print(i)
                    wi = stoffinfo[i]['Molar mass'] * molfraction[i] / wi_unten
                    mi = wi * Massen
                    stoffinfo[i]['mi'] = mi
                    if stoffinfo[i]['Signalword'] == 'Danger':
                        danger_mass = danger_mass + mi
                    elif stoffinfo[i]['Signalword'] == 'Warning':
                        warning_mass = warning_mass + mi
                
                stufe1 = Einstufen_des_Ausmaßes(danger_mass, 'Danger')
                stufe2 = Einstufen_des_Ausmaßes(warning_mass, 'Warning')
                stufe = finden_Stufen(stufe1, stufe2)
                print(stufe)
                return stufe

##############################################################################################################
#Hazop-Analyse
# Neue Tabelle erstellen
cursor_2.execute("CREATE TABLE " + Table_Name +\
               " (`Nodes` VARCHAR(255),\
                `Index` int,\
                Description VARCHAR(255),\
                Guideword VARCHAR(255),\
                Parameter VARCHAR(255),\
                Cause_1 VARCHAR(255),\
                Cause_2 VARCHAR(255),\
                Cause_3 VARCHAR(255),\
                Consequence_1 VARCHAR(255),\
                Consequence_2 VARCHAR(255),\
                Consequence_3 VARCHAR(255),\
                Substance VARCHAR(255),\
                `Danger of leakage` VARCHAR(255),\
                `Dangerous level` VARCHAR(255),\
                Safeguard_1 VARCHAR(255),\
                Safeguard_2 VARCHAR(255),\
                `References` VARCHAR(255), Primary Key(`Nodes`, `Index`))")

# Durchführung der HAZOP-Analyse nacheinander in den Druckräumen
# Szenarien in der Datenbank anzuwenden

for dirpath, dirnames, filenames in os.walk('./'+ Input_Ordner_name):
    for filename in filenames:
        n = os.path.join(dirpath, filename)
        file = filename
        if os.path.splitext(file)[-1][1:] == "xml" :
            """Get Datei Name"""
            inputx = os.path.splitext(file)[0] 
            g = nx.read_graphml(n)


            # Wenn man direkt g.nodes() benutzt, funktioniert die Iterator nicht, return Null...man kann nur einzeln kopieren
            nodes_name = []
            nodes = g.nodes()
            for n in nodes:
                nodes_name.append(n)
            
            Listx = []
            for n in nodes_name:
                #Node_name = n
                Substance_name = g._node[n]['Subs']
                Class = g._node[n]['group']
                Subclass = g._node[n]['Sub_class']
                                   
                if Class in ['Column', 'Pump', 'Heat exchanger', 'Vessel', 'Reactor']:
                    Tabel_name_to_check = '`'+Class+'`'
                    query = "SELECT * FROM "+ Tabel_name_to_check + "WHERE Description LIKE '%(general)'"
                    cursor_1.execute(query)
                    result = cursor_1.fetchall()
    
                    for x in result:
                        m = list(x)
                        m.insert(0,n)
                        m[11] = Substance_name
                        m = tuple(m)
                        Listx.append(m)
                    
                    if Subclass in ['Heat exchanger with straight tubes', 'Pump, centrifugal type', 'Column with bubble cap trays']:
                        Tabel_name_to_check = '`'+Class+'`'
                        query = "SELECT * FROM "+ Tabel_name_to_check + "WHERE Description LIKE %s"
                        cursor_1.execute(query,("%" + Subclass + "%",))
                        result_sub = cursor_1.fetchall()
        
                        for x in result_sub:
                            m = list(x)
                            m.insert(0,n)
                            m[11] = Substance_name
                            m = tuple(m)
                            Listx.append(m)
                        

            #print(Listx)
                    
            sql = "INSERT INTO " + Table_Name + "(`Nodes`, `Index`, Description, Guideword, Parameter, Cause_1, Cause_2, Cause_3, Consequence_1, Consequence_2, Consequence_3, Substance, `Danger of leakage`, `Dangerous level`, Safeguard_1, Safeguard_2, `References`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"            
            cursor_2.executemany(sql, Listx)


##################################################################################################################################################################
# Bewertung des Leckagerisikos
##################################################################################################################################################################

           
            #nodes = g.nodes()
            main_nodes_1 = [n for n in nodes if g._node[n]['group'] in ['Column', 'Pump', 'Heat exchanger']]
            main_nodes_2 = [n for n in nodes if  g._node[n]['group'] in ['Reactor', 'Vessel']]
            #print(main_nodes_1)            

            stufe_dict = {}
            for n in main_nodes_1:
                edges_in = list(g.in_edges(n))
                piping_in = [x for x in edges_in if g.get_edge_data(*x)['Class'] in ['Piping', 'Pipe']]
                edges_out = list(g.out_edges(n))
                piping_out = [x for x in edges_out if g.get_edge_data(*x)['Class'] in ['Piping', 'Pipe']]
                piping = piping_in + piping_out
                #print(piping)
                piping_stufe = []
                for i in piping:
                    if g.get_edge_data(*i)['subs'] not in ['n.a.', 'n.d.']:
                        stoff = list(g.get_edge_data(*i)['subs'].split(", "))
                        #print(stoff)
                        signal_word = {}
                        for sub in stoff:
                            query = "SELECT Signalword FROM stoffdaten WHERE Name = %s"
                            cursor_1.execute(query, (sub,))
                            result = cursor_1.fetchone()
                            signal_word[sub] = result[0]
                        mass_flow = g.get_edge_data(*i)['Mass_flow']
                        if len(stoff) == 1:                
                            if mass_flow not in ['n.a.', 'n.d.']:
                                if g.get_edge_data(*i)['Mass_flow_unit'] == 'g/s':
                                    mass_flow_in_20 = float(g.get_edge_data(*i)['Mass_flow'].replace(',','.')) * 60 * 20 * 0.001
                                elif g.get_edge_data(*i)['Mass_flow_unit'] == 'kg/h':
                                    mass_flow_in_20 = float(g.get_edge_data(*i)['Mass_flow'].replace(',','.')) * 1 / 3

                                #print(mass_flow_in_20)
                                stufe = Einstufen_des_Ausmaßes(mass_flow_in_20, signal_word[sub])
                                piping_stufe.append(stufe)
                                #print(stufe)
                        elif len(stoff) > 1:
                            stufe = finde_Stufen_Mischung(g, i)
                            piping_stufe.append(stufe)
                if piping_stufe != []:
                    node_stufe = finden_Stufen_in_List(piping_stufe)
                    stufe_dict[n] = node_stufe
                else:
                    node_stufe = '-'
                    stufe_dict[n] = node_stufe
                    #print(node_stufe)




            for n in main_nodes_2:
                #print(n)
                stufe = finde_Stufen_in_Vessel(g, n)
                stufe_dict[n] = stufe

            #print(stufe_dict)


            for i in stufe_dict.keys():
                cursor_2.execute("UPDATE " + Table_Name + " SET `Dangerous level`='%s' WHERE `Nodes`='%s' AND `Danger of leakage`='%s'"%(stufe_dict[i], i, 'Yes'))
            
            
add_safeguard = "ALTER TABLE " + Table_Name + " ADD `Safeguard_1 exists` VARCHAR(20) AFTER Safeguard_1, ADD `Safeguard_2 exists` VARCHAR(20) AFTER Safeguard_2"
cursor_2.execute(add_safeguard)             


######################################################################################################################################################################
#Reaktor Runaway_Szenarien
info_sub = {}
info_ghss = {}
stoichio = {}

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
        #print(exist_stoff)
        #print(len(exist_stoff))
        #print(len(info_sub))
        #if len(exist_stoff) ==len(info_sub):
        #    
        
        #else:    
        for sub in exist_stoff:
            #print(sub)
            if sub not in info_sub:
                #print("sub for select: "+ sub)
                query = "SELECT COUNT(Name) FROM stoffdaten WHERE Name=%s"
                cursor_1.execute(query, (sub,))
                exist = cursor_1.fetchone()
                exist_check = exist[0]
                #print(exist_check)
                if exist_check == 1:
                    query_1 = "SELECT Name,MolarMass,BoilingPoint,FlashPoint,AutoignitionTemperature,Heat_capacity_Tn,Heats_of_Formations, Max_DecompositionTemperature, Min_DecompositionTemperature FROM stoffdaten WHERE Name = %s"
                    cursor_1.execute(query_1, (sub,))
                    results = cursor_1.fetchall()
                    for row in results:
                        subinfo = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]]
                        print(subinfo)
                    query_2 = "SELECT Explosive, Flammable, Oxidizing, CompressedGas, Corrosive, Toxic, Harmful, HealthHazard, EnviromenalHazard FROM stoffdaten_copy WHERE Name = %s"
                    cursor_1.execute(query_2, (sub,))
                    ghs_name = ["Explosive", "Flammable", "Oxidizing", "CompressedGas", "Corrosive", "Toxic", "Harmful", "Health Hazard", "Enviroment Hazard"]
                    result_ghs = cursor_1.fetchall()
                    for row in result_ghs:
                        ghs_info = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]]
                        
                    info_ghss[sub] = []
                    for x,y in zip(ghs_name,ghs_info):
                        if y == "Yes":
                            info_ghss[sub].append(x)
                    info_sub[sub] = subinfo
                    #print(subinfo)
                    
                elif exist_check ==0:                
                    if sub not in info_sub:
                        tkinter.messagebox.showwarning(title="Error", message="The substance "+ sub + " is not in the database")
                                
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

for dirpath, dirnames, filenames in os.walk('./'+ Input_Ordner_name):
    for filename in filenames:
        n = os.path.join(dirpath, filename)
        file = filename
        if os.path.splitext(file)[-1][1:] == "xml" :
            #Get Datei Name
            inputx = os.path.splitext(file)[0] 
            g = nx.read_graphml(n)


            #wenn man direkt g.nodes() benutzt, funktioniert die Iterator nicht, return Null...man kann nur einzeln kopieren
            nodes_name = []
            nodes = g.nodes()
            for n in nodes:
                if g._node[n]['group'] == 'Reactor':

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
                
                    Stofflist_combo = ['Acetic acid', 'Acetic anhydride', 'Ethanol', 'Ethylene oxide', 'Hydrogen peroxide', 'Methanol', 'Methyl acetate', 'Sulfuric acid']
                
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
                    
                    Qr = 0
                    mix_capa_top = 0
                    mix_capa_bottom = 0

                    # zur Berechnung von Delta T (Kelvin)
                    for i in exist_reaction_stoff:
                        Qr  = Qr + float(info_sub[i][6])*stoichio[i]
                        if stoichio[i] > 0:
                            c_p = float(info_sub[i][5])/float(info_sub[i][1])
                            mol = float(info_sub[i][1])
                            mix_capa_top = mix_capa_top + c_p*mol*stoichio[i]
                            mix_capa_bottom = mix_capa_bottom + mol*stoichio[i]
                            mix_capa = mix_capa_top/mix_capa_bottom

                    delta_Tr = -Qr*1000/(mix_capa*mix_capa_bottom)


                    print(mix_capa)

                    delta_Tr = -Qr*1000/(mix_capa*mix_capa_bottom)
                    print("delta_Tr: " + str(delta_Tr))



                    MSTR = delta_Tr + float(reaction_temp)

                    print(MSTR)



                    # Um die Severity zu bewerten
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
                        return description

                    # Zur Abschätzung der Auswirkungen des Runaway-Szenarios
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
                            #print(info_sub[i][4])
                            #print("Autoignition: "+i)
                            ignition_risk = ignition_risk + 1
                            
                        if float(info_sub[i][2]) > MSTR:
                            for y in exist_stoff:
                                if MSTR > float(info_sub[i][7]):            
                                    no_possible = no_possible + 1



                    def consequence_safe_1(overpressure_risk, toxic_risk, flamm_risk):
                        if overpressure_risk > 0 and toxic_risk > 0 and flamm_risk > 0:
                            consequence_1 = "risk of boiling liquid expanding vapor explosion and formation of toxic and flammable clouds."
                            safeguard_1 = "Install rupture disk burst or safety valve, the direction, location due to toxic substances must be very well considered."         
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
                    print(a)
                    con_1 = a[0]
                    safe_1 = a[1]

                    con_2 = consequence_2(safe_info)

                        
                    con_3 = consequence_3(ignition_risk)


                    subs_for_result = ','.join(exist_stoff)



                    print(con_1)
                    print(safe_1)

                    Listx = [(n, '48', descrip, 'Higher', 'Temperature', 'loss of power', 'cooling jacket not working', 'too much reactants', con_1, con_2, con_3, subs_for_result, 'Yes', '-', safe_1, '-', 'Please calculate TMRad value to learn more about SIL','- ', 'Yang_auto'),]
                    sql = "INSERT INTO " + Table_Name + "(`Nodes`, `Index`, Description, Guideword, Parameter, Cause_1, Cause_2, Cause_3, Consequence_1, Consequence_2, Consequence_3, Substance, `Danger of leakage`, `Dangerous level`, Safeguard_1, `Safeguard_1 exists`, Safeguard_2, `Safeguard_2 exists`, `References`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"            
                    cursor_2.executemany(sql, Listx)

###################################################################################################################################################################
#Korrosion_Überprüfung 
          
corrosion_resistant = {'stainless steel': 'No', 'Glass': 'Good', 'PP': 'Good', 'Aluminum alloy': 'Good'}


for dirpath, dirnames, filenames in os.walk('./'+ Input_Ordner_name):
    for filename in filenames:
        n = os.path.join(dirpath, filename)
        file = filename
        if os.path.splitext(file)[-1][1:] == "xml" :
            #Get Datei Name
            inputx = os.path.splitext(file)[0] 
            g = nx.read_graphml(n)
            

            #wenn man direkt g.nodes() benutzt, funktioniert die Iterator nicht, return Null...man kann nur einzeln kopieren
            nodes_name = []
            nodes = g.nodes()            
            
            material_dict = {}
            for n in nodes:
                if g._node[n]['material'] not in ['n.d.', 'n.a.']:
                    material_info = {}
                    corrosive_sub = []
                    material_info['Substanz'] = list(g._node[n]['Subs'].split(", "))
                    #print(material_info)
                    

                    for sub in material_info['Substanz']:
                        #print(sub)
                        if sub not in ['n.a.', 'n.d.']:
                            query = "SELECT Corrosive FROM stoffdaten WHERE Name = %s"
                            cursor_1.execute(query, (sub,))

                            result = cursor_1.fetchone()
                            #print(result[0])
                        
                            if result[0] == 'Yes':
                                corrosive_sub.append(sub)
                                material_info['Corrosive Substanz'] = corrosive_sub       
                                material_info['Material'] = g._node[n]['material']
                                material_info['Corrosion_check'] = corrosion_resistant[g._node[n]['material']]
                                material_dict[n] = material_info
                    
            #print(material_dict)
            # Auswirkungen, Ursachen und Sicherheitsmaßnahmen nach dem Algorithmus anzugeben
            for n in material_dict.keys():
                if material_dict[n]['Corrosive Substanz'] != []:
                    cause_1 = 'because of the corrosive substance(s): ' + ', '.join(material_dict[n]['Corrosive Substanz'])
                    consequence_1 = g._node[n]['group'] + ' damage'
                    consequence_2 = 'reduce the operation life period of the ' + g._node[n]['group']
                    consequence_3 = 'risk of leakage' 
                    Substance = ', '.join(material_dict[n]['Substanz'])
                    safe1_exist = material_dict[n]['Corrosion_check']
                    if material_dict[n]['Corrosion_check'] == 'No':
                        safe1_exist = 'No'
                        safe2 = 'The corrosion protection of the ' + material_dict[n]['Material'] + ' is unsatisfactory and it is recommended to replace the material or add a coating'
                        safe2_exist = 'No'
                        danger = 'Yes'
                        danger_stufe = finde_Stufen_in_Vessel(g, n)
                    else:
                        safe1_exist = 'Yes'
                        safe2 = 'The corrosion protection of the ' + material_dict[n]['Material'] + ' is ' + material_dict[n]['Corrosion_check']
                        safe2_exist = 'Yes'
                        danger = ' '
                        danger_stufe = ' '
                    Listx = [(n, '47', 'Chemical corrosion due to corrosive substance', 'Higher', 'Corrosion', cause_1, '-', '-', consequence_1, consequence_2, consequence_3, Substance, danger, danger_stufe, 'Use of corrosion resistant materials', safe1_exist, safe2, safe2_exist, 'Yang_auto'),]
                    print(Listx)
                    sql = "INSERT INTO " + Table_Name + "(`Nodes`, `Index`, Description, Guideword, Parameter, Cause_1, Cause_2, Cause_3, Consequence_1, Consequence_2, Consequence_3, Substance, `Danger of leakage`, `Dangerous level`, Safeguard_1, `Safeguard_1 exists`, Safeguard_2, `Safeguard_2 exists`, `References`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"            
                    cursor_2.executemany(sql, Listx)
            
            edges = g.edges()
            edges_info = {}
            for i in edges:
                if g.get_edge_data(*i)['Class'] == 'Piping' and  g.get_edge_data(*i)['subs'] != 'n.a.':
                    info = {}
                    stoff = list(g.get_edge_data(*i)['subs'].split(", "))
                    #print(stoff)        
                    corrosive_sub = []
                    for sub in stoff:
                        query = "SELECT Corrosive FROM stoffdaten WHERE Name = %s"
                        cursor_1.execute(query, (sub,))
                        result = cursor_1.fetchone()
                        if result[0] == 'Yes':
                            corrosive_sub.append(sub)
                            
                    if corrosive_sub != []:
                        info['Substance'] = stoff
                        info['Corrosive Substanz'] = corrosive_sub
                        info['Material'] = g.get_edge_data(*i)['material']
                        if g.get_edge_data(*i)['material'] in corrosion_resistant:
                            info['Corrosion_check'] = corrosion_resistant[g.get_edge_data(*i)['material']]
                        else:
                            info['Corrosion_check'] = 'not verified'
                        edges_info[i] = info
                            
            #print(edges_info)

            for n in edges_info.keys():
                name = 'Piping from node ' + n[0] + ' to node ' +n[1]
                cause_1 = 'because of the corrosive substance(s): ' + ', '.join(edges_info[n]['Corrosive Substanz'])
                consequence_1 = 'Piping damage'
                consequence_2 = 'risk of leakage'
                substance =', '.join(edges_info[n]['Substance'])
                if edges_info[n]['Corrosion_check'] == 'No':
                    safe1_exist = 'No'
                    safe2 = 'The corrosion protection of the ' + edges_info[n]['Material'] + ' is unsatisfactory and it is recommended to replace the material or add a coating'
                    safe2_exist = 'No'
                    danger_leck = 'Yes'
                    stage_danger = finde_Stufen_Mischung(g, n)
                elif edges_info[n]['Corrosion_check'] == 'not verified':
                    safe1_exist = 'No'
                    safe2 = 'The corrosion protection of the ' + edges_info[n]['Material'] + ' is ' + edges_info[n]['Corrosion_check']
                    safe2_exist = 'No'
                    danger_leck = 'Yes'
                    stage_danger = finde_Stufen_Mischung(g, n)
                else:
                    safe1_exist = 'Yes'
                    safe2 = 'The corrosion protection of the ' + edges_info[n]['Material'] + ' is ' + edges_info[n]['Corrosion_check']
                    danger_leck = 'No'
                    stage_danger = ' '
                    safe2_exist = 'Yes'
                
                Listx = [(name, '47', 'Chemical corrosion of the piping due to corrosive substance', 'Higher', 'Corrosion', cause_1, '-', '-', consequence_1, consequence_2, '-', substance, 'Yes', stage_danger, 'Use of corrosion resistant materials', safe1_exist, safe2, safe2_exist, 'Yang_auto'),]
                sql = "INSERT INTO " + Table_Name + "(`Nodes`, `Index`, Description, Guideword, Parameter, Cause_1, Cause_2, Cause_3, Consequence_1, Consequence_2, Consequence_3, Substance, `Danger of leakage`, `Dangerous level`, Safeguard_1, `Safeguard_1 exists`, Safeguard_2, `Safeguard_2 exists`, `References`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"            
                cursor_2.executemany(sql, Listx)
                
                
###############################################################################################################################################################################################################################################################################################################
# Es gibt verschiedene Algorithmen zur Sicherheitsüberprüfung in Abhängigkeit von der Anzahl der Hauptanlagen und der Anzahl der Pumpen


Haput_teil = ["Column", "Heat exchanger, detailed","Heat exchanger", "Vessel", "Silo", "Reactor"]

dic_safe = {}
Pump_schnittpunkte = {}
for dirpath, dirnames, filenames in os.walk('./'+ Input_Ordner_name):
    for filename in filenames:
        n = os.path.join(dirpath, filename)
        file = filename
        if os.path.splitext(file)[-1][1:] == "xml" :
            #Get Datei Name
            inputx = os.path.splitext(file)[0] 
            g = nx.read_graphml(n)
            node_names = g.nodes()
            Main_node = [x for x in node_names if g._node[x]['group'] in Haput_teil]
            Pump = [x for x in node_names if g._node[x]['group'] == 'Pump']
            Hauput_number = len(Main_node) + len(Pump)

            if Hauput_number == 1 and len(Main_node) == 1:
                dic_safe_check = {'safety valve': 'no', 'pressure sensor': 'no', 'temperature sensor': 'no', 'high level alarm': 'no', 'low level alarm': 'no', 'high pressure alarm': 'no', 'low pressure alarm': 'no', 'low temperature alarm': 'no', 'high temperature alarm': 'no', 'controlled': 'no'}
                for n in node_names:
                    if g._node[n]['sub_group_2'] == 'Safety valves':
                        dic_safe_check['safety valve'] = n
                    if g._node[n]['request'] == 'TI':
                        dic_safe_check['temperature sensor'] = n
                    if g._node[n]['request'] == 'PI':
                        dic_safe_check['pressure sensor'] = n
                    if g._node[n]['request'] in ['LLA-/+', 'LRCA+-', 'LIA+-']:
                        dic_safe_check['high level alarm'] = n
                        dic_safe_check['low level alarm'] = n
                    if g._node[n]['request'] in ['LLA-', 'LRCA-', 'LIA-']:
                        dic_safe_check['low level alarm'] = n
                    if g._node[n]['request'] in ['LLA+', 'LRCA+', 'LIA+', 'LICA+']:
                        dic_safe_check['high level alarm'] = n
                    if g._node[n]['request'] in ['PRCA+-', 'PIA+-']:
                        dic_safe_check['high pressure alarm'] = n
                        dic_safe_check['low pressure alarm'] = n
                    if g._node[n]['request'] in ['PRCA+', 'PIA+']:
                        dic_safe_check['high pressure alarm'] = n
                    if g._node[n]['request'] in ['PRCA-', 'PIA-']:
                        dic_safe_check['low pressure alarm'] = n
                    if g._node[n]['request'] in ['FRC', 'TR', 'TC', 'LIC', 'PIC', 'PC', 'LC', 'FC', 'FR']:   
                        dic_safe_check['controlled'] = n
                    if g._node[n]['request'] in ['TRCA+-', 'TIA+-', 'TTA+-']:
                        dic_safe_check['high temperature alarm'] = n
                        dic_safe_check['low temperature alarm'] = n
                    if g._node[n]['request'] in ['TRCA+', 'TIA+', 'TTA+']:
                        dic_safe_check['high temperature alarm'] = n
                    if g._node[n]['request'] in ['TRCA-', 'TIA-', 'TTA-']:
                        dic_safe_check['low temperature alarm'] = n       
                dic_safe[Main_node[0]] = dic_safe_check
            if Hauput_number == 1 and len(Pump)==1:
                dic_safe_pump = {'check valve': 'no', 'pressure sensor': 'no', 'temperature sensor': 'no', 'controlled': 'no', 'Valves before and after pumps': 'Yes', 'bypass': 'No'}
                node_to_check = []
                for n in node_names:
                    if g._node[n]['sub_group_2'] == 'Check valves': 
                        dic_safe_pump['check valve'] = n
                    if g._node[n]['request'] == 'PI':
                        dic_safe_pump['pressure sensor'] = n
                    if g._node[n]['request'] == 'TI':
                        dic_safe_pump['temperature sensor'] = n
                    if g._node[n]['request'] in ['FRC', 'TR', 'TC', 'FICR', 'FC', 'FR']:   
                        dic_safe_pump['controlled'] = n
                    if g._node[n]['group'] == 'Valves': 
                        neighbors_out = list(g.out_edges(n))
                        neighbors_in = list(g.in_edges(n))
                        neighbors = neighbors_out + neighbors_in
                        if len(neighbors) == 1:
                            neighbor = neighbors[0]
                            if g.get_edge_data(*neighbor)['Class'] in ['Piping', 'Pipe']:
                                neighbors = n
                                neighbor_in_ri = list(nx.all_neighbors(comp_g, n))
                                neighbor_to_check = [x for x in neighbor_in_ri if x not in node_names]
                                for i in neighbor_to_check:
                                    node_to_check.append(i)
                                #print(neighbor_to_check)
                            
                dic_safe[Pump[0]] = dic_safe_pump
                Pump_schnittpunkte[Pump[0]] = node_to_check
            
            if Hauput_number > 1:
                for n in Main_node:
                    dic_safe_check_i = {'safety valve': 'no', 'pressure sensor': 'no', 'temperature sensor': 'no', 'high level alarm': 'no', 'low level alarm': 'no', 'high pressure alarm': 'no', 'low pressure alarm': 'no', 'low temperature alarm': 'no', 'high temperature alarm': 'no', 'controlled': 'no'}
                    main_neigh = list(nx.all_neighbors(g,n))
                    safe_neigh = [x for x in main_neigh if g._node[x]['sub_group_2'] == 'Safety valves']
                    #print(safe_neigh)
                    if safe_neigh != []:
                        dic_safe_check_i['safety valve'] = safe_neigh[0]
                    msr_neighs = [x for x in main_neigh if g._node[x]['group'] =='MSR']
                    for msr in msr_neighs:
                        if g._node[msr]['request'] == 'TI':
                            dic_safe_check_i['temperature sensor'] = msr
                        if g._node[msr]['request'] == 'PI':
                            dic_safe_check_i['pressure sensor'] = msr
                        if g._node[msr]['request'] in ['LLA-/+', 'LRCA+-', 'LIA+-']:
                            dic_safe_check_i['high level alarm'] = msr
                            dic_safe_check_i['low level alarm'] = msr
                        if g._node[msr]['request'] in ['LLA-', 'LRCA-', 'LIA-']:
                            dic_safe_check_i['low level alarm'] = msr
                        if g._node[msr]['request'] in ['LLA+', 'LRCA+', 'LIA+', 'LICA+']:
                            dic_safe_check_i['high level alarm'] = msr
                        if g._node[msr]['request'] in ['PRCA+-', 'PIA+-']:
                            dic_safe_check_i['high pressure alarm'] = msr
                            dic_safe_check_i['low pressure alarm'] = msr
                        if g._node[msr]['request'] in ['PRCA+', 'PIA+']:
                            dic_safe_check_i['high pressure alarm'] = msr
                        if g._node[msr]['request'] in ['PRCA-', 'PIA-']:
                            dic_safe_check_i['low pressure alarm'] = msr
                        if g._node[msr]['request'] in ['FRC', 'TR', 'TC', 'LIC', 'PIC', 'PC', 'LC', 'FC', 'FR']:   
                            dic_safe_check_i['controlled'] = msr
                        if g._node[msr]['request'] in ['TRCA+-', 'TIA+-', 'TTA+-']:
                            dic_safe_check_i['high temperature alarm'] = msr
                            dic_safe_check_i['low temperature alarm'] = msr 
                        if g._node[msr]['request'] in ['TRCA+', 'TIA+', 'TTA+']:
                            dic_safe_check_i['high temperature alarm'] = msr
                        if g._node[msr]['request'] in ['TRCA-', 'TIA-', 'TTA-']:
                            dic_safe_check_i['low temperature alarm'] = msr 
                    dic_safe[n] = dic_safe_check_i
                    
                if len(Pump) == 1:
                    for i in Pump:
                        dic_safe_pump_i = {'check valve': 'no', 'pressure sensor': 'no', 'temperature sensor': 'no', 'controlled': 'no', 'Valves before and after pumps': 'No', 'bypass': 'No'}
                        neigh_pump = list(nx.all_neighbors(g,i))
                        for n in neigh_pump:
                            if g._node[n]['sub_group_2'] == 'Check valves': 
                                dic_safe_pump_i['check valve'] = n
                            if g._node[n]['request'] == 'PI':
                                dic_safe_pump_i['pressure sensor'] = n
                            if g._node[n]['request'] == 'TI':
                                dic_safe_pump_i['temperature sensor'] = n
                            if g._node[n]['request'] in ['FRC', 'TR', 'TC', 'FICR', 'FC', 'FIC', 'TIC', 'PC', 'PIC', 'FR']:   
                                dic_safe_pump_i['controlled'] = n
                        dic_safe[i] = dic_safe_pump_i
                        
                if len(Pump) > 1:
                    for i in Pump:
                        dic_safe_pump_ii = {'check valve': 'no', 'pressure sensor': 'no', 'temperature sensor': 'no', 'controlled': 'no', 'Valves before and after pumps': 'No', 'bypass': 'no'}
                        neigh_pump = list(nx.all_neighbors(g,i))
                        for n in neigh_pump:
                            if g._node[n]['sub_group_2'] == 'Check valves': 
                                dic_safe_pump_ii['check valve'] = n
                            if g._node[n]['request'] == 'PI':
                                dic_safe_pump_ii['pressure sensor'] = n
                            if g._node[n]['request'] == 'TI':
                                dic_safe_pump_ii['temperature sensor'] = n
                            if g._node[n]['request'] in ['FRC', 'TR', 'TC', 'FICR', 'FC', 'FIC', 'TIC', 'PC', 'PIC', 'FR']:   
                                dic_safe_pump_ii['controlled'] = n
                        
                        neigh_pump_has_1 = [x for x in neigh_pump if g.has_edge(x,i)]
                        neigh_pump_not_msr_1 = [x for x in neigh_pump_has_1 if g.get_edge_data(x,i)['Class'] in ['Pipe', 'Piping', 'Heat transfer medium']]
                        
                        neigh_pump_has_2 = [x for x in neigh_pump if g.has_edge(i,x)]
                        neigh_pump_not_msr_2 = [x for x in neigh_pump_has_2 if g.get_edge_data(i,x)['Class'] in ['Pipe', 'Piping', 'Heat transfer medium']]
                        
                        #print(neigh_pump_not_msr)
                        for x in Pump:
                            if x != i:
                                paths1 = nx.has_path(g, source = neigh_pump_not_msr_1[0], target = x)
                                paths2 = nx.has_path(g, source = x, target = neigh_pump_not_msr_2[0])
                                if paths1 or paths2:
                                    dic_safe_pump_ii['bypass'] = "Please check again"
                                if paths1 and paths2:
                                    dic_safe_pump_ii['bypass'] = x
                                
                        dic_safe[i] = dic_safe_pump_ii




if len(Pump_schnittpunkte) != {}:
    for i in Pump_schnittpunkte:
        list1 = Pump_schnittpunkte[i]
        for x in Pump_schnittpunkte:
            list2 = Pump_schnittpunkte[x]
            if x != i and len(list1) == len(list2) and all(x in list2 for x in list1):
                dic_safe[i]['bypass'] = x

print(dic_safe)            
#print(Pump_schnittpunkte)


for i in dic_safe:
    for safe_check in dic_safe[i]:
        cursor_2.execute("UPDATE " + Table_Name + " SET `Safeguard_1 exists`='%s' WHERE `Nodes`='%s' AND `Safeguard_1` LIKE'%s'" %(dic_safe[i][safe_check], i, "%" + safe_check + "%"))
        cursor_2.execute("UPDATE " + Table_Name + " SET `Safeguard_2 exists`='%s' WHERE `Nodes`='%s' AND `Safeguard_2` LIKE'%s'" %(dic_safe[i][safe_check], i, "%" + safe_check + "%"))

###########################################################################################################################################################################################


# Verbindung zu MySQL abbrechen
connection_1.commit()
connection_1.close()

connection_2.commit()
connection_2.close()

