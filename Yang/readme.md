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

## Install:

>- Install Python (anaconda) from https://www.anaconda.com/products/individual [^1]

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






































References:
[^1]: Oeing, J; Holtermann, T. online documentation,   https://github.com/TUDoAD/preHAZOP#user-content-fn-2-a8cb56aa2b9de8999506ceb333e4af1f, accessed on 22.04.2023