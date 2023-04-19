-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: hazop_analyse_result
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `hazop_analyse_cstr_024`
--

DROP TABLE IF EXISTS `hazop_analyse_cstr_024`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hazop_analyse_cstr_024` (
  `Nodes` varchar(255) NOT NULL,
  `Index` int NOT NULL,
  `Description` varchar(255) DEFAULT NULL,
  `Guideword` varchar(255) DEFAULT NULL,
  `Parameter` varchar(255) DEFAULT NULL,
  `Cause_1` varchar(255) DEFAULT NULL,
  `Cause_2` varchar(255) DEFAULT NULL,
  `Cause_3` varchar(255) DEFAULT NULL,
  `Consequence_1` varchar(255) DEFAULT NULL,
  `Consequence_2` varchar(255) DEFAULT NULL,
  `Consequence_3` varchar(255) DEFAULT NULL,
  `Substance` varchar(255) DEFAULT NULL,
  `Danger of leakage` varchar(255) DEFAULT NULL,
  `Dangerous level` varchar(255) DEFAULT NULL,
  `Safeguard_1` varchar(255) DEFAULT NULL,
  `Safeguard_1 exists` varchar(20) DEFAULT NULL,
  `Safeguard_2` varchar(255) DEFAULT NULL,
  `Safeguard_2 exists` varchar(20) DEFAULT NULL,
  `References` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Nodes`,`Index`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hazop_analyse_cstr_024`
--

LOCK TABLES `hazop_analyse_cstr_024` WRITE;
/*!40000 ALTER TABLE `hazop_analyse_cstr_024` DISABLE KEYS */;
INSERT INTO `hazop_analyse_cstr_024` VALUES ('B-01',26,'High pressure in vessel (general)','Higher','Pressure','high Temperatur','exothermic reaction in the vessel','-','risk of leakage','burst','-','Acetic anhydride','Yes','S3','install high pressure alarm','no','install safety valve','V-S-B-01','Kletz_what went wrong and Yang'),('B-01',27,'High level in vessel (general)','Higher','Level','human error','operation error','indicates the level in the vessel is almost twice the actual level.','overflow in the tank','risk of leakage','-','Acetic anhydride','Yes','S3','install high level alarm','LLA-/+ L-B-01','installation of more than one measurement for the vessel',NULL,'Kletz_what went wrong and Yang'),('B-01',28,'Low level in vessel (general)','Lower','Level','vessel defect','operation error',NULL,'risk of leakage','-','-','Acetic anhydride','Yes','S3','install low level alarm','LLA-/+ L-B-01','-',NULL,'Yang'),('B-01',29,'Low pressure in vessel (general)','Lower','Pressure','fire in the tank','the temperature in the vessel is too low','-','vessel defect','-','-','Acetic anhydride',NULL,NULL,'install pressure sensor','PI PI-B-01','-',NULL,'Yang'),('B-01',30,'High temperature in vessel (general)','Higher','Temperature','high temperature of feeding','exothermic reaction in the vessel','-','risk of leakage','vessel defect','-','Acetic anhydride',NULL,NULL,'install temperature sensor','TI TI-B-01','install high temperature alarm','no','Yang'),('B-01',31,'Low temperature in vessel (general)','Lower','Temperature','evaporation of the stored chemicals','low temperature of the environment','-','risk of freezing','change of product quality','-','Acetic anhydride',NULL,NULL,'install temperature sensor','TI TI-B-01','install low temperature alarm','no','Yang'),('B-01',32,'More flow from outlet pipe into tank (general)','Reverse','Flow','operation error','lower pressure in vessel','-','risk of overflow in the tank','-',NULL,'Acetic anhydride',NULL,NULL,'install check valve on the outlet',NULL,'-',NULL,'Yang'),('B-01',47,'Chemical corrosion due to corrosive substance','Higher','Corrosion','because of the corrosive substance(s): Acetic anhydride','-','-','Vessel damage','reduce the operation life period of the Vessel','risk of leakage','Acetic anhydride',' ',' ','Use of corrosion resistant materials','Yes','The corrosion protection of the Glass is Good','Yes','Yang_auto'),('B-02',26,'High pressure in vessel (general)','Higher','Pressure','high Temperatur','exothermic reaction in the vessel','-','risk of leakage','burst','-','Methanol','Yes','S3','install high pressure alarm','no','install safety valve','V-S-B-02','Kletz_what went wrong and Yang'),('B-02',27,'High level in vessel (general)','Higher','Level','human error','operation error','indicates the level in the vessel is almost twice the actual level.','overflow in the tank','risk of leakage','-','Methanol','Yes','S3','install high level alarm','LLA-/+ L-B-02','installation of more than one measurement for the vessel',NULL,'Kletz_what went wrong and Yang'),('B-02',28,'Low level in vessel (general)','Lower','Level','vessel defect','operation error',NULL,'risk of leakage','-','-','Methanol','Yes','S3','install low level alarm','LLA-/+ L-B-02','-',NULL,'Yang'),('B-02',29,'Low pressure in vessel (general)','Lower','Pressure','fire in the tank','the temperature in the vessel is too low','-','vessel defect','-','-','Methanol',NULL,NULL,'install pressure sensor','PI PI-B-02','-',NULL,'Yang'),('B-02',30,'High temperature in vessel (general)','Higher','Temperature','high temperature of feeding','exothermic reaction in the vessel','-','risk of leakage','vessel defect','-','Methanol',NULL,NULL,'install temperature sensor','TI TI-B-02','install high temperature alarm','no','Yang'),('B-02',31,'Low temperature in vessel (general)','Lower','Temperature','evaporation of the stored chemicals','low temperature of the environment','-','risk of freezing','change of product quality','-','Methanol',NULL,NULL,'install temperature sensor','TI TI-B-02','install low temperature alarm','no','Yang'),('B-02',32,'More flow from outlet pipe into tank (general)','Reverse','Flow','operation error','lower pressure in vessel','-','risk of overflow in the tank','-',NULL,'Methanol',NULL,NULL,'install check valve on the outlet',NULL,'-',NULL,'Yang'),('B-03',26,'High pressure in vessel (general)','Higher','Pressure','high Temperatur','exothermic reaction in the vessel','-','risk of leakage','burst','-','Acetic anhydride, Methanol, Acetic acid, Methyl acetate','Yes','S3','install high pressure alarm','no','install safety valve','V-S-B-03','Kletz_what went wrong and Yang'),('B-03',27,'High level in vessel (general)','Higher','Level','human error','operation error','indicates the level in the vessel is almost twice the actual level.','overflow in the tank','risk of leakage','-','Acetic anhydride, Methanol, Acetic acid, Methyl acetate','Yes','S3','install high level alarm','LLA-/+ L-B-03','installation of more than one measurement for the vessel',NULL,'Kletz_what went wrong and Yang'),('B-03',28,'Low level in vessel (general)','Lower','Level','vessel defect','operation error',NULL,'risk of leakage','-','-','Acetic anhydride, Methanol, Acetic acid, Methyl acetate','Yes','S3','install low level alarm','LLA-/+ L-B-03','-',NULL,'Yang'),('B-03',29,'Low pressure in vessel (general)','Lower','Pressure','fire in the tank','the temperature in the vessel is too low','-','vessel defect','-','-','Acetic anhydride, Methanol, Acetic acid, Methyl acetate',NULL,NULL,'install pressure sensor','PI PI-B-03','-',NULL,'Yang'),('B-03',30,'High temperature in vessel (general)','Higher','Temperature','high temperature of feeding','exothermic reaction in the vessel','-','risk of leakage','vessel defect','-','Acetic anhydride, Methanol, Acetic acid, Methyl acetate',NULL,NULL,'install temperature sensor','TI TI-B-03','install high temperature alarm','no','Yang'),('B-03',31,'Low temperature in vessel (general)','Lower','Temperature','evaporation of the stored chemicals','low temperature of the environment','-','risk of freezing','change of product quality','-','Acetic anhydride, Methanol, Acetic acid, Methyl acetate',NULL,NULL,'install temperature sensor','TI TI-B-03','install low temperature alarm','no','Yang'),('B-03',32,'More flow from outlet pipe into tank (general)','Reverse','Flow','operation error','lower pressure in vessel','-','risk of overflow in the tank','-',NULL,'Acetic anhydride, Methanol, Acetic acid, Methyl acetate',NULL,NULL,'install check valve on the outlet',NULL,'-',NULL,'Yang'),('B-03',47,'Chemical corrosion due to corrosive substance','Higher','Corrosion','because of the corrosive substance(s): Acetic anhydride, Acetic acid','-','-','Vessel damage','reduce the operation life period of the Vessel','risk of leakage','Acetic anhydride, Methanol, Acetic acid, Methyl acetate','Yes','S3','Use of corrosion resistant materials','No','The corrosion protection of the stainless steel is unsatisfactory and it is recommended to replace the material or add a coating','No','Yang_auto'),('P-G-01-1',1,'Failure of the seal (general)','Lower','Pressure','bearing failure','-','-','leak of chemicals','-','-','Acetic anhydride','Yes','S3','install pressure sensor','no','install check valve in the delivery line','no','Kletz_what went wrong'),('P-G-01-1',2,'Bearing failure (general)','Lower','Flow','lack of lubrication','-','-','failure of the seal','-','-','Acetic anhydride',NULL,NULL,'install pressure sensor','no','install check valve in the delivery line','no','Kletz_what went wrong'),('P-G-01-1',3,'Pumping against wrongly closed valve results in damage of pump  (general)','Higher','Temperature','valve wrongly closed','-','-','damage to the seals','leak of chemicals','-','Acetic anhydride','Yes','S3','bypass','P-G-01-2','install remotely operated valves (controlled)','FICR F-F-01','Holtermann_Masterarbeit'),('P-G-01-1',4,'Mechanical failure of the pump (general)','No','Flow','mechanical failure','power outage','-','damage','continuous process disturbed','-','Acetic anhydride',NULL,NULL,'bypass','P-G-01-2','-',NULL,'Holtermann_Masterarbeit with change from Yang'),('P-G-01-1',5,'Bursting of a pump (general)','Higher','Temperature','operating error, wrongly started between closed valves','pump housing made of brittle material','operating error went unnoticed','vapor pressure of the liquid raised','pump burst','-','Acetic anhydride','Yes','S3','install pressure sensor','no','install remotely operated valves (controlled)','FICR F-F-01','DECHEMA Ereignis-Datenbank'),('P-G-01-1',7,'Failure in the cooling system  (general)','Lower','Temperature','low flow rates','failure in the cooling system (open more)','-','fat lose its viscosity','change of lubricant characteristic','damage to the bearings','Acetic anhydride',NULL,NULL,'install temperature sensor','no','check the cooling system',NULL,'www.researchgate.net/publication/291334094'),('P-G-01-1',8,'Pump damage due to high pressure (general)','Higher','Pressure','vaporizing liquid','blockage in the valve outlet','-','explosion','stop production',NULL,'Acetic anhydride','Yes','S3','check and drain pipes and drain system',NULL,'replace the gasket and check the damage',NULL,'www.researchgate.net/publication/291334094'),('P-G-01-1',9,'Pump does not work  (general)','No','Pressure','pump failure','power outage','faulty pressure sensor','stop production','stop the pump','-','Acetic anhydride',NULL,NULL,'check the types of liquids that can be used with the pump',NULL,'install pressure sensor','no','www.researchgate.net/publication/291334094, Yang'),('P-G-01-1',10,'high flow rate in the pump (general)','Higher','Flow','blockage in the valve outlet','operating fault','too high engine power','overheating of the pump','destruction of the internal pump','cavitation','Acetic anhydride',NULL,NULL,'install remotely operated valves (controlled)','FICR F-F-01','check density of liquid that differens from the nominal density',NULL,'www.researchgate.net/publication/291334094'),('P-G-01-2',1,'Failure of the seal (general)','Lower','Pressure','bearing failure','-','-','leak of chemicals','-','-','n.a.','Yes','-','install pressure sensor','no','install check valve in the delivery line','no','Kletz_what went wrong'),('P-G-01-2',2,'Bearing failure (general)','Lower','Flow','lack of lubrication','-','-','failure of the seal','-','-','n.a.',NULL,NULL,'install pressure sensor','no','install check valve in the delivery line','no','Kletz_what went wrong'),('P-G-01-2',3,'Pumping against wrongly closed valve results in damage of pump  (general)','Higher','Temperature','valve wrongly closed','-','-','damage to the seals','leak of chemicals','-','n.a.','Yes','-','bypass','P-G-01-1','install remotely operated valves (controlled)','FICR F-F-01','Holtermann_Masterarbeit'),('P-G-01-2',4,'Mechanical failure of the pump (general)','No','Flow','mechanical failure','power outage','-','damage','continuous process disturbed','-','n.a.',NULL,NULL,'bypass','P-G-01-1','-',NULL,'Holtermann_Masterarbeit with change from Yang'),('P-G-01-2',5,'Bursting of a pump (general)','Higher','Temperature','operating error, wrongly started between closed valves','pump housing made of brittle material','operating error went unnoticed','vapor pressure of the liquid raised','pump burst','-','n.a.','Yes','-','install pressure sensor','no','install remotely operated valves (controlled)','FICR F-F-01','DECHEMA Ereignis-Datenbank'),('P-G-01-2',7,'Failure in the cooling system  (general)','Lower','Temperature','low flow rates','failure in the cooling system (open more)','-','fat lose its viscosity','change of lubricant characteristic','damage to the bearings','n.a.',NULL,NULL,'install temperature sensor','no','check the cooling system',NULL,'www.researchgate.net/publication/291334094'),('P-G-01-2',8,'Pump damage due to high pressure (general)','Higher','Pressure','vaporizing liquid','blockage in the valve outlet','-','explosion','stop production',NULL,'n.a.','Yes','-','check and drain pipes and drain system',NULL,'replace the gasket and check the damage',NULL,'www.researchgate.net/publication/291334094'),('P-G-01-2',9,'Pump does not work  (general)','No','Pressure','pump failure','power outage','faulty pressure sensor','stop production','stop the pump','-','n.a.',NULL,NULL,'check the types of liquids that can be used with the pump',NULL,'install pressure sensor','no','www.researchgate.net/publication/291334094, Yang'),('P-G-01-2',10,'high flow rate in the pump (general)','Higher','Flow','blockage in the valve outlet','operating fault','too high engine power','overheating of the pump','destruction of the internal pump','cavitation','n.a.',NULL,NULL,'install remotely operated valves (controlled)','FICR F-F-01','check density of liquid that differens from the nominal density',NULL,'www.researchgate.net/publication/291334094'),('P-G-02-1',1,'Failure of the seal (general)','Lower','Pressure','bearing failure','-','-','leak of chemicals','-','-','Methanol','Yes','S3','install pressure sensor','no','install check valve in the delivery line','no','Kletz_what went wrong'),('P-G-02-1',2,'Bearing failure (general)','Lower','Flow','lack of lubrication','-','-','failure of the seal','-','-','Methanol',NULL,NULL,'install pressure sensor','no','install check valve in the delivery line','no','Kletz_what went wrong'),('P-G-02-1',3,'Pumping against wrongly closed valve results in damage of pump  (general)','Higher','Temperature','valve wrongly closed','-','-','damage to the seals','leak of chemicals','-','Methanol','Yes','S3','bypass','P-G-02-2','install remotely operated valves (controlled)','FICR F-F-02','Holtermann_Masterarbeit'),('P-G-02-1',4,'Mechanical failure of the pump (general)','No','Flow','mechanical failure','power outage','-','damage','continuous process disturbed','-','Methanol',NULL,NULL,'bypass','P-G-02-2','-',NULL,'Holtermann_Masterarbeit with change from Yang'),('P-G-02-1',5,'Bursting of a pump (general)','Higher','Temperature','operating error, wrongly started between closed valves','pump housing made of brittle material','operating error went unnoticed','vapor pressure of the liquid raised','pump burst','-','Methanol','Yes','S3','install pressure sensor','no','install remotely operated valves (controlled)','FICR F-F-02','DECHEMA Ereignis-Datenbank'),('P-G-02-1',7,'Failure in the cooling system  (general)','Lower','Temperature','low flow rates','failure in the cooling system (open more)','-','fat lose its viscosity','change of lubricant characteristic','damage to the bearings','Methanol',NULL,NULL,'install temperature sensor','no','check the cooling system',NULL,'www.researchgate.net/publication/291334094'),('P-G-02-1',8,'Pump damage due to high pressure (general)','Higher','Pressure','vaporizing liquid','blockage in the valve outlet','-','explosion','stop production',NULL,'Methanol','Yes','S3','check and drain pipes and drain system',NULL,'replace the gasket and check the damage',NULL,'www.researchgate.net/publication/291334094'),('P-G-02-1',9,'Pump does not work  (general)','No','Pressure','pump failure','power outage','faulty pressure sensor','stop production','stop the pump','-','Methanol',NULL,NULL,'check the types of liquids that can be used with the pump',NULL,'install pressure sensor','no','www.researchgate.net/publication/291334094, Yang'),('P-G-02-1',10,'high flow rate in the pump (general)','Higher','Flow','blockage in the valve outlet','operating fault','too high engine power','overheating of the pump','destruction of the internal pump','cavitation','Methanol',NULL,NULL,'install remotely operated valves (controlled)','FICR F-F-02','check density of liquid that differens from the nominal density',NULL,'www.researchgate.net/publication/291334094'),('P-G-02-2',1,'Failure of the seal (general)','Lower','Pressure','bearing failure','-','-','leak of chemicals','-','-','n.a.','Yes','-','install pressure sensor','no','install check valve in the delivery line','no','Kletz_what went wrong'),('P-G-02-2',2,'Bearing failure (general)','Lower','Flow','lack of lubrication','-','-','failure of the seal','-','-','n.a.',NULL,NULL,'install pressure sensor','no','install check valve in the delivery line','no','Kletz_what went wrong'),('P-G-02-2',3,'Pumping against wrongly closed valve results in damage of pump  (general)','Higher','Temperature','valve wrongly closed','-','-','damage to the seals','leak of chemicals','-','n.a.','Yes','-','bypass','P-G-02-1','install remotely operated valves (controlled)','FICR F-F-02','Holtermann_Masterarbeit'),('P-G-02-2',4,'Mechanical failure of the pump (general)','No','Flow','mechanical failure','power outage','-','damage','continuous process disturbed','-','n.a.',NULL,NULL,'bypass','P-G-02-1','-',NULL,'Holtermann_Masterarbeit with change from Yang'),('P-G-02-2',5,'Bursting of a pump (general)','Higher','Temperature','operating error, wrongly started between closed valves','pump housing made of brittle material','operating error went unnoticed','vapor pressure of the liquid raised','pump burst','-','n.a.','Yes','-','install pressure sensor','no','install remotely operated valves (controlled)','FICR F-F-02','DECHEMA Ereignis-Datenbank'),('P-G-02-2',7,'Failure in the cooling system  (general)','Lower','Temperature','low flow rates','failure in the cooling system (open more)','-','fat lose its viscosity','change of lubricant characteristic','damage to the bearings','n.a.',NULL,NULL,'install temperature sensor','no','check the cooling system',NULL,'www.researchgate.net/publication/291334094'),('P-G-02-2',8,'Pump damage due to high pressure (general)','Higher','Pressure','vaporizing liquid','blockage in the valve outlet','-','explosion','stop production',NULL,'n.a.','Yes','-','check and drain pipes and drain system',NULL,'replace the gasket and check the damage',NULL,'www.researchgate.net/publication/291334094'),('P-G-02-2',9,'Pump does not work  (general)','No','Pressure','pump failure','power outage','faulty pressure sensor','stop production','stop the pump','-','n.a.',NULL,NULL,'check the types of liquids that can be used with the pump',NULL,'install pressure sensor','no','www.researchgate.net/publication/291334094, Yang'),('P-G-02-2',10,'high flow rate in the pump (general)','Higher','Flow','blockage in the valve outlet','operating fault','too high engine power','overheating of the pump','destruction of the internal pump','cavitation','n.a.',NULL,NULL,'install remotely operated valves (controlled)','FICR F-F-02','check density of liquid that differens from the nominal density',NULL,'www.researchgate.net/publication/291334094'),('Piping from node B-01 to node T13',47,'Chemical corrosion of the piping due to corrosive substance','Higher','Corrosion','because of the corrosive substance(s): Acetic anhydride','-','-','Piping damage','risk of leakage','-','Acetic anhydride','Yes','S3','Use of corrosion resistant materials','No','The corrosion protection of the stainless steel is unsatisfactory and it is recommended to replace the material or add a coating','No','Yang_auto'),('Piping from node B-03 to node V-S-B-03',47,'Chemical corrosion of the piping due to corrosive substance','Higher','Corrosion','because of the corrosive substance(s): Acetic anhydride, Acetic acid','-','-','Piping damage','risk of leakage','-','Acetic anhydride, Methanol, Acetic acid, Methyl acetate','Yes','S3','Use of corrosion resistant materials','No','The corrosion protection of the stainless steel is unsatisfactory and it is recommended to replace the material or add a coating','No','Yang_auto'),('Piping from node P-G-01-1 to node F-P-1',47,'Chemical corrosion of the piping due to corrosive substance','Higher','Corrosion','because of the corrosive substance(s): Acetic anhydride','-','-','Piping damage','risk of leakage','-','Acetic anhydride','Yes','S3','Use of corrosion resistant materials','No','The corrosion protection of the n.d. is not verified','No','Yang_auto'),('Piping from node R-01 to node T1',47,'Chemical corrosion of the piping due to corrosive substance','Higher','Corrosion','because of the corrosive substance(s): Acetic anhydride, Acetic acid','-','-','Piping damage','risk of leakage','-','Acetic anhydride, Methanol, Acetic acid, Methyl acetate','Yes','S3','Use of corrosion resistant materials','No','The corrosion protection of the stainless steel is unsatisfactory and it is recommended to replace the material or add a coating','No','Yang_auto'),('Piping from node T11 to node R-01',47,'Chemical corrosion of the piping due to corrosive substance','Higher','Corrosion','because of the corrosive substance(s): Acetic anhydride','-','-','Piping damage','risk of leakage','-','Acetic anhydride, Methanol','Yes','S3','Use of corrosion resistant materials','No','The corrosion protection of the stainless steel is unsatisfactory and it is recommended to replace the material or add a coating','No','Yang_auto'),('Piping from node T13 to node V-03',47,'Chemical corrosion of the piping due to corrosive substance','Higher','Corrosion','because of the corrosive substance(s): Acetic anhydride','-','-','Piping damage','risk of leakage','-','Acetic anhydride','Yes','S3','Use of corrosion resistant materials','No','The corrosion protection of the n.d. is not verified','No','Yang_auto'),('Piping from node V-03 to node P-G-01-1',47,'Chemical corrosion of the piping due to corrosive substance','Higher','Corrosion','because of the corrosive substance(s): Acetic anhydride','-','-','Piping damage','risk of leakage','-','Acetic anhydride','Yes','S3','Use of corrosion resistant materials','No','The corrosion protection of the stainless steel is unsatisfactory and it is recommended to replace the material or add a coating','No','Yang_auto'),('Piping from node V-SE-01 to node B-01',47,'Chemical corrosion of the piping due to corrosive substance','Higher','Corrosion','because of the corrosive substance(s): Acetic anhydride','-','-','Piping damage','risk of leakage','-','Acetic anhydride','Yes','S3','Use of corrosion resistant materials','No','The corrosion protection of the n.d. is not verified','No','Yang_auto'),('R-01',20,'High pressure in reactor (general)','Higher','Pressure','uncontrolled reaction occurs','too much reactant into reactor','too littel product flow out of reactor','reactor material could weaken','causing leak or explosion','-','Acetic anhydride, Methanol, Acetic acid, Methyl acetate','Yes','S3','install high pressure alarm','no','install safety valve','V-S-R-01','Hazard and Operability Analysis of an Enthylene Oxide Production Plant'),('R-01',21,'Low pressure in reactor (general)','Lower','Pressure','too much product flow leaving the reactor','temperature dramatically decreases','-','uncontroll reactant and product flow into reactor','-','-','Acetic anhydride, Methanol, Acetic acid, Methyl acetate',NULL,NULL,'install pressure sensor','no','add valve controls onto product and reactant lines',NULL,'Hazard and Operability Analysis of an Enthylene Oxide Production Plant'),('R-01',22,'High temperature in reactor (general)','Higher','Temperature','incoming reactant temperature is too high','reaction thermodynamics proceed in an uncontrolled fashion','-','reactor could overheat','reactor pressure could increase','-','Acetic anhydride, Methanol, Acetic acid, Methyl acetate',NULL,NULL,'install temperature sensor ','TI TIR-R-01','add thermal control jacket to reactor',NULL,'Hazard and Operability Analysis of an Enthylene Oxide Production Plant'),('R-01',23,'Low temperature in reactor (general)','Lower','Temperature','incoming reactant temperature is too low','heat jacket to reactor out','-','reaction kinetics would be affected','reactor pressure could decrease','-','Acetic anhydride, Methanol, Acetic acid, Methyl acetate',NULL,NULL,'install temperature sensor','TI TIR-R-01','add thermal control jacket to reactor',NULL,'Hazard and Operability Analysis of an Enthylene Oxide Production Plant'),('R-01',24,'Low level in reactor (general)','Lower','Level','incorrect operation','low feed in reacor',NULL,'reduced amount of product ',NULL,NULL,'Acetic anhydride, Methanol, Acetic acid, Methyl acetate',NULL,NULL,'install remote valves on the feed',NULL,'install low level alarm','LLA-/+ L-R-01','Yang'),('R-01',25,'High level in reactor (general)','Higher','Level','incorrect operation','more feed in reactor','output valve incorrectly closed','high conversion in reactor','high temperature','-','Acetic anhydride, Methanol, Acetic acid, Methyl acetate',NULL,NULL,'install remote valves on the feed',NULL,'install high level alarm','LLA-/+ L-R-01','Yang'),('R-01',47,'Chemical corrosion due to corrosive substance','Higher','Corrosion','because of the corrosive substance(s): Acetic anhydride, Acetic acid','-','-','Reactor damage','reduce the operation life period of the Reactor','risk of leakage','Acetic anhydride, Methanol, Acetic acid, Methyl acetate','Yes','S3','Use of corrosion resistant materials','No','The corrosion protection of the stainless steel is unsatisfactory and it is recommended to replace the material or add a coating','No','Yang_auto'),('R-01',48,'Critical runaway reaction','Higher','Temperature','loss of power','cooling jacket not working','too much reactants','risk of boiling liquid expanding vapor explosion and formation of toxic and flammable clouds.','-','-','Acetic anhydride,Methanol,Acetic acid,Methyl acetate','Yes','-','Install rupture disk burst or safety valve, the direction, location due to toxic substances must be very well considered.','V-S-R-01','Please calculate TMRad value to learn more about SIL','- ','Yang_auto');
/*!40000 ALTER TABLE `hazop_analyse_cstr_024` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-19 22:19:54
