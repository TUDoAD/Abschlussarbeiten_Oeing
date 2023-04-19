# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 22:40:42 2023

@author: yangr
"""

#import xml.etree.ElementTree as ET
import tkinter
from tkinter import ttk
from tkinter import messagebox
import xml.etree.ElementTree as ET
import networkx as nx
import os
#import pandas as pd


def enter_data():
    global name1
    global name2
    #accepted = accept_var.get()
    xml_for_networkx = graphri_entry.get()
    simu_for_ET = simu_entry.get()
    path1 = './'+xml_for_networkx+'.xml'
    isExist1 = os.path.exists(path1)
    path2 = './'+simu_for_ET+'.xml'
    isExist2 = os.path.exists(path2)
        
    if isExist1 == 1 and isExist2 == 1:
        
        name1 = xml_for_networkx
        name2 = simu_for_ET
        
        """
        stoff1 = stoff1_combobox.get()
        stoff2 = stoff2_combobox.get()
        stoff3 = stoff3_combobox.get()
        stoff4 = stoff4_combobox.get()
        stoff5 = stoff5_combobox.get()
        stoff6 = stoff6_combobox.get()
        input_stoff__ = [stoff1, stoff2, stoff3, stoff4, stoff5, stoff6]
        input_stoff_exist = [x for x in input_stoff__ if x]
        print(input_stoff_exist)
        """
        tkinter.messagebox.showinfo(title="Successful", message="You can close the window")
    else:
        tkinter.messagebox.showerror(title="Error", message="Please check the file!")
        
        
        
        
        

window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()





link_input_frame = tkinter.LabelFrame(frame, text="Please enter the file name")
link_input_frame.grid(row = 0, column = 0, padx = 20, pady = 10)

graphri_label = tkinter.Label(link_input_frame, text="GraphML: ")
graphri_label.grid(row = 0, column = 0)

simu_label = tkinter.Label(link_input_frame, text="Simulation result: ")
simu_label.grid(row = 1, column = 0)

blank_label = tkinter.Label(link_input_frame, text=" ")
blank_label.grid(row = 0, column = 2)


graphri_entry = tkinter.Entry(link_input_frame, width=30)
graphri_entry.grid(row = 0, column = 1)
simu_entry = tkinter.Entry(link_input_frame, width=30)
simu_entry.grid(row = 1, column = 1)


"""
stoff_input_frame = tkinter.LabelFrame(frame, text="Please enter the substances of the processes, you can check it in DWSIM.")
stoff_input_frame.grid(row=1, column=0, padx=20, pady=20)


infobox_label = tkinter.Label(stoff_input_frame, text="                                                            ")
infobox_label.grid(row=0, column=1)
stoff1_label = tkinter.Label(stoff_input_frame, text="Substance 1")
stoff1_label.grid(row=1, column=0)
stoff2_label = tkinter.Label(stoff_input_frame, text="Substance 2")
stoff2_label.grid(row=2, column=0)
stoff3_label = tkinter.Label(stoff_input_frame, text="Substance 3")
stoff3_label.grid(row=3, column=0)
stoff4_label = tkinter.Label(stoff_input_frame, text="Substance 4")
stoff4_label.grid(row=1, column=2)
stoff5_label = tkinter.Label(stoff_input_frame, text="Substance 5")
stoff5_label.grid(row=2, column=2)
stoff6_label = tkinter.Label(stoff_input_frame, text="Substance 6")
stoff6_label.grid(row=3, column=2)
infobox2_label = tkinter.Label(stoff_input_frame, text="                                                            ")
infobox2_label.grid(row=4, column=1)
blank_label = tkinter.Label(stoff_input_frame, text=" ")
blank_label.grid(row=0, column=4)

listx = ['1,2-Propanediol', '1,3-Butadiene', '1-Butanol', '1-Butene', '2-Propanol', 'Acetic acid', 'Acetic anhydride', 'Acetone', 'Acetylene', 'Acrolein', 'Acrylic acid', 'Adipic acid', 'Ammonia, anhydrous', 'Aniline', 'Benzene', 'Carbon dioxide', 'Carbon monoxide', 'Chlorine', 'Chlorobenzene', 'Chloroform', 'Cumene', 'Cyclohexane', 'Ethanol', 'Ethyl acetate', 'Ethylbenzene', 'Ethylene', 'Ethylene dichloride', 'Ethylene glycol', 'Ethylene oxide', 'Formaldehyde', 'Formic acid', 'Hydrochloric acid solution', 'Hydrogen', 'Hydrogen cyanide', 'Hydrogen peroxide', 'Hydrogen sulfide', 'Mercury', 'Methane', 'Methanol', 'Methyl acetate', 'Methyl chloride', 'Methyl formate', 'Methylene chloride', 'N-butyl acetate', 'Nitrogen', 'Oxygen', 'Phenol', 'Phthalic anhydride', 'Propane', 'Propene', 'Propylene oxide', 'Sodium carbonate', 'Styrene', 'Sulfur', 'Sulfur dioxide', 'Sulfuric acid', 'Toluene', 'Vinyl chloride', 'Water', 'm-Xylene', 'n-Hexane', 'o-Xylene', 'p-Xylene']
stoff1_combobox = ttk.Combobox(stoff_input_frame, values=listx)
stoff2_combobox = ttk.Combobox(stoff_input_frame, values=listx)
stoff3_combobox = ttk.Combobox(stoff_input_frame, values=listx)
stoff4_combobox = ttk.Combobox(stoff_input_frame, values=listx)
stoff5_combobox = ttk.Combobox(stoff_input_frame, values=listx)
stoff6_combobox = ttk.Combobox(stoff_input_frame, values=listx)



stoff1_combobox.grid(row=1, column=1)
stoff2_combobox.grid(row=2, column=1)
stoff3_combobox.grid(row=3, column=1)
stoff4_combobox.grid(row=1, column=3)
stoff5_combobox.grid(row=2, column=3)
stoff6_combobox.grid(row=3, column=3)
"""




#Button
button = tkinter.Button(frame, text="Enter data", command= enter_data)
button.grid(row=2, column=0, padx=40, pady=10)


window.mainloop()





g = nx.read_graphml('./'+name1+'.xml')

tree = ET.parse(name2+".xml")



#Test
#g = nx.read_graphml('./CSTR_plant_GraphML.xml')
#tree = ET.parse("CSTR_simulation_2.xml")

edges_names = g.edges
#print(edges_names)
listx = ['1,2-Propanediol', '1,3-Butadiene', '1-Butanol', '1-Butene', '2-Propanol', 'Acetic acid', 'Acetic anhydride', 'Acetone', 'Acetylene', 'Acrolein', 'Acrylic acid', 'Adipic acid', 'Ammonia, anhydrous', 'Aniline', 'Benzene', 'Carbon dioxide', 'Carbon monoxide', 'Chlorine', 'Chlorobenzene', 'Chloroform', 'Cumene', 'Cyclohexane', 'Ethanol', 'Ethyl acetate', 'Ethylbenzene', 'Ethylene', 'Ethylene dichloride', 'Ethylene glycol', 'Ethylene oxide', 'Formaldehyde', 'Formic acid', 'Hydrochloric acid solution', 'Hydrogen', 'Hydrogen cyanide', 'Hydrogen peroxide', 'Hydrogen sulfide', 'Mercury', 'Methane', 'Methanol', 'Methyl acetate', 'Methyl chloride', 'Methyl formate', 'Methylene chloride', 'N-butyl acetate', 'Nitrogen', 'Oxygen', 'Phenol', 'Phthalic anhydride', 'Propane', 'Propene', 'Propylene oxide', 'Sodium carbonate', 'Styrene', 'Sulfur', 'Sulfur dioxide', 'Sulfuric acid', 'Toluene', 'Vinyl chloride', 'Water', 'm-Xylene', 'n-Hexane', 'o-Xylene', 'p-Xylene']

#input_stoff = input_stoff_exist

#input_stoff_ = [x.replace(' ', '_') for x in input_stoff]
#print(input_stoff_)



  
edge = []
substanz = []
mass_flow = []
mass_flow_unit = []
volume_flow = []
volume_flow_unit = []



input_stoff = []
for i in edges_names:
    object_name_1 = i[0] + ', ' + i[1]
    object_name_2 = i[1] + ', ' + i[0]
    if len(tree.findall(".//Object[@name="+'"'+object_name_1+'"'+"]/Property")) > 0:
        for prop in tree.findall(".//Object[@name="+'"'+object_name_1+'"'+"]/Property"):
            if prop.attrib['name'] in listx and prop.attrib['name'] not in input_stoff:
                input_stoff.append(prop.attrib['name'])
        break
print(input_stoff)           



molfraction = {}
for stoff in input_stoff:
    info_to_combi = {}
    name_in_xml = 'mol_fraction_' + stoff.replace(' ', '_')
    info_to_combi['Name'] = stoff
    info_to_combi['xml_name'] = name_in_xml
    info_to_combi['mol_fraction'] = []

    molfraction[stoff] =  info_to_combi
    
print(molfraction)



for x in edges_names:
    object_name_1 = x[0] + ', ' + x[1]
    object_name_2 = x[1] + ', ' + x[0]
    if len(tree.findall(".//Object[@name="+'"'+object_name_1+'"'+"]/Property")) > 0:
        edge.append(x)
        sub = []
        mol_fraction = {}
        for prop in tree.findall(".//Object[@name="+'"'+object_name_1+'"'+"]/Property"):
            if prop.attrib['name'] in input_stoff:
                if prop.attrib['value'] != "0" and prop.attrib['name'] not in sub:
                    sub.append(prop.attrib['name'])
                    mol_fraction[prop.attrib['name']] = prop.attrib['value'] 
                elif prop.attrib['value'] == "0" and prop.attrib['name'] not in sub:     
                    mol_fraction[prop.attrib['name']] = "0"                                
            elif prop.attrib['name'] == 'Mass Flow':
                mass_flow.append(prop.attrib['value'])
                mass_flow_unit.append(prop.attrib['units'])
            elif prop.attrib['name'] == 'Volumetric Flow':
                volume_flow.append(prop.attrib['value'])
                volume_flow_unit.append(prop.attrib['units'])
     
        stoff = ', '.join(sub)
        substanz.append(stoff)
        for i in input_stoff:
           molfraction[i]['mol_fraction'].append(mol_fraction[i])
        
List_for_attribute = [substanz, mass_flow, mass_flow_unit, volume_flow, volume_flow_unit]
for i in molfraction:
    List_for_attribute.append(molfraction[i]['mol_fraction'])





remain = [x for x in edges_names if x not in edge]

for x in remain:
    edge.append(x)
    for attri in List_for_attribute:
        attri.append("n.a.")


List_for_name = ['subs', 'Mass_flow', 'Mass_flow_unit', 'Volume_flow', 'Volume_flow_unit']

for i in molfraction:
    List_for_name.append(molfraction[i]['xml_name'])
#print(substanz)

for (attr,name) in zip(List_for_attribute, List_for_name):
    dic_attribute = dict(zip(edge, attr))
    #print(dic_attribute)
    nx.set_edge_attributes(g, dic_attribute, name)

###################################################################################################################################
    

#############################################################################################################################

dic_sub_process = {}
node_names = g.nodes()
for n in node_names:
    edges_in = list(g.in_edges(n))
    edges_out = list(g.out_edges(n))
    edges = edges_in + edges_out
    node_stoff = []
    for i in edges:
        #stoff = g.get_edge_data(*i)['subs']
        allstoff = list(g.get_edge_data(*i)['subs'].split(", "))
        #print(stoff)
        for stoff in allstoff:
            if stoff not in node_stoff and stoff not in ['n.a.', 'n.d.']:           
                node_stoff.append(stoff)
    if node_stoff != []:
        node_stoff = ', '.join(node_stoff)
    else:
        node_stoff = 'n.a.'        
    dic_sub_process[n] = node_stoff
      
#print(dic_sub_process)

dic_node = {}
node_for_V = []
V = []
V_unit = []
for n in node_names:
    if g._node[n]['group'] in ['Vessel', 'Reactor']:
        dic_in = {}
        if len(tree.findall(".//Object[@name="+'"'+n+'"'+"]/Property")) > 0:
            node_for_V.append(n)
            sub = []
            for prop in tree.findall(".//Object[@name="+'"'+n+'"'+"]/Property"):
                if prop.attrib['name'] == 'Volume':
                    dic_in['V'] = prop.attrib['value']
                    dic_in['V_unit'] = prop.attrib['units']
                
            dic_node[n] = dic_in
        

nx.set_node_attributes(g, dic_sub_process, 'Subs')

nx.set_node_attributes(g, dic_node)


   
name_for_save = name1[0:4]
nx.write_graphml_lxml(g, name_for_save+'_Graph_Plus.xml')


#nx.write_graphml_lxml(g, '1____Graph_Plus.xml')

