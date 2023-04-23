# Automated HAZOP analysis & risk analysis
The concept of this automated HAZOP analysis & risk analysis tool is based on preHAZOP (see preHAZOP [^1]). 

Optimization points of automated preHAZOP:

- Based on pressure zones
- Analysis with a relational SQL database
- Process medium is considered
- Self-integrated scenarios such as reactor runaway scenario; corrosion scenario for piping and equipment

![HAZOP-Graph](https://github.com/TUDoAD/Abschlussarbeiten_Oeing/blob/main/Yang/pictures/Automated%20HAZOP%20analysis.png)

Figure 1: Automated HAZOP Analysis Flow Sheet

## Authors:
![TU-Do](https://github.com/TUDoAD/preHAZOP/blob/main/figures/TUDO_AD_logo.png)

Ruolan Yang, Jonas Oeing

TU Dortmund University, [Laboratory of Equipment Design](https://ad.bci.tu-dortmund.de/cms/en/laboratory/)

***
## Install:

- Install Python (anaconda) from https://www.anaconda.com/products/individual (Python 3.9.15)

- Install MySQL from https://dev.mysql.com/downloads/, for windows [^2]: 
    1. select *MySQL Installer for Windows*
    2. select first *Windows (x86, 32-bit), MSI Installer 2.4M* to *Download*, 
    3. select *No thanks, just start my download.*
    4. select Setup Type: *Custom*
    5. select Products: MySQL Server; MySQL Workbench; MySQL Shell (select the latest version)
    6. Next -> Excute -> Next
    7. Accont and Roles: select your password
    8. Next -> Finish
    9. Go to MySQL Workbench, Connect to MySQL Server, you need to enter your password
    10. You can now work with the SQL database.

- Load the following python libraries:
  - NetworkX (vers. 2.8.8) [^3]
  - Matplotlib (vers. 3.6.2) [^4]
  - mysql.connector (vers. 8.0.31) [^5]
  - Other libraries are included with Python.

- Load all_codes.zip from https://github.com/TUDoAD/Abschlussarbeiten_Oeing/blob/main/Yang/Results/Code/all_codes.zip

- Load XMLs from https://github.com/TUDoAD/Abschlussarbeiten_Oeing/tree/main/Yang/Results/XMLs

- Place scripts with XMLs in one folder

***
## Manual:

Here is the sequence of the HAZOP & risk analysis 

```mermaid
graph LR;
    Read_Simu_GraphML-->Druckraum_Detektion;
    Druckraum_Detektion-->HAZOP_analyse;
```
### *Read_Simu_GraphML* --- Integration of GraphML file and simulation results file

1. Run the script in Python
2. Enter file names for GraphML and simulation results. for example: *CSTR_plant_GraphML* and *CSTR_Simulation* 

![GUI for Data input](https://github.com/TUDoAD/Abschlussarbeiten_Oeing/blob/main/Yang/pictures/GUI_for_integration_RI.png)

Figure 2: Graphical user interface for the *Read_Simu_GraphML*

3. Click *Enter data*; if the files exist, the Messenger box will tell you that you can close the window.

4. The new file *XX_Graphl_Plus* is created.

* Notice, if you want to try a new process, please make sure:

  * In the first line of the simulation result, the *encoding* must be *utf-8*.
```xml
  <?xml version="1.0" encoding="utf-8"?>
```
  * In the simulation result, all flows (edges) around the equipment must be available, otherwise it is not possible to analyse the leakage risk of the equipment.

### *Druckraum_Detektion* --- Prepare pressure zones for HAZOP & risk analysis

1. Run the script in Python
2. Enter file name for *XX_Graphl_Plus*
































***
References:

[^1]: Oeing, J; Holtermann, T. online documentation,   https://github.com/TUDoAD/preHAZOP#user-content-fn-2-a8cb56aa2b9de8999506ceb333e4af1f, accessed on 22.04.2023

[^2]: MySQL Guide, online documentation, https://www.youtube.com/watch?v=gvRXjsrpCHw, accessed on 22.04.2023

[^3]: NetworkX, online documentation, https://networkx.org/, accessed on 22.04.2023

[^4]: matplotlib, https://matplotlib.org/, accessed on 22.04.2023

[^5]: MySQL Connectors, https://www.mysql.com/products/connector/, accessed on 22.04.2023