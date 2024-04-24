-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: dcbcdb
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `bakeditem`
--

DROP TABLE IF EXISTS `bakeditem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bakeditem` (
  `baked_id` int NOT NULL AUTO_INCREMENT,
  `baked_name` varchar(40) NOT NULL,
  `price` float(5,2) NOT NULL,
  `stock` int NOT NULL,
  PRIMARY KEY (`baked_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bakeditem`
--

LOCK TABLES `bakeditem` WRITE;
/*!40000 ALTER TABLE `bakeditem` DISABLE KEYS */;
INSERT INTO `bakeditem` VALUES (1,'Chocolate Chip Scone',3.99,7),(2,'Lemon Scone',3.99,6),(3,'Peanut Butter Cookie',3.29,12),(4,'Chocolate Chip Macadamia Cookie',3.49,9);
/*!40000 ALTER TABLE `bakeditem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bakeditempurchase`
--

DROP TABLE IF EXISTS `bakeditempurchase`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bakeditempurchase` (
  `baked_id` int DEFAULT NULL,
  `purchase_id` int DEFAULT NULL,
  `quantity` int NOT NULL,
  KEY `baked_id` (`baked_id`),
  KEY `purchase_id` (`purchase_id`),
  CONSTRAINT `bakeditempurchase_ibfk_1` FOREIGN KEY (`baked_id`) REFERENCES `bakeditem` (`baked_id`),
  CONSTRAINT `bakeditempurchase_ibfk_2` FOREIGN KEY (`purchase_id`) REFERENCES `purchase` (`purchase_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bakeditempurchase`
--

LOCK TABLES `bakeditempurchase` WRITE;
/*!40000 ALTER TABLE `bakeditempurchase` DISABLE KEYS */;
INSERT INTO `bakeditempurchase` VALUES (2,5,1),(4,6,1);
/*!40000 ALTER TABLE `bakeditempurchase` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book` (
  `book_id` int NOT NULL AUTO_INCREMENT,
  `isbn` varchar(13) NOT NULL,
  `title` varchar(100) NOT NULL,
  `author_lname` varchar(30) NOT NULL,
  `author_fname` varchar(30) DEFAULT NULL,
  `stock` int NOT NULL,
  `price` float(5,2) NOT NULL,
  PRIMARY KEY (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES (1,'9780765326362','Words of Radiance','Sanderson','Brandon',3,18.99),(2,'9783453270381','Oathbringer','Sanderson','Brandon',2,18.99),(3,'9780060652951','The Great Divorce','Lewis','C.S.',6,9.99),(4,'978804397410','Murder on the Orient Express','Christie','Agatha',3,8.99);
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookpurchase`
--

DROP TABLE IF EXISTS `bookpurchase`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookpurchase` (
  `book_id` int DEFAULT NULL,
  `purchase_id` int DEFAULT NULL,
  `quantity` int NOT NULL,
  KEY `book_id` (`book_id`),
  KEY `purchase_id` (`purchase_id`),
  CONSTRAINT `bookpurchase_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `book` (`book_id`),
  CONSTRAINT `bookpurchase_ibfk_2` FOREIGN KEY (`purchase_id`) REFERENCES `purchase` (`purchase_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookpurchase`
--

LOCK TABLES `bookpurchase` WRITE;
/*!40000 ALTER TABLE `bookpurchase` DISABLE KEYS */;
INSERT INTO `bookpurchase` VALUES (1,5,1),(3,7,1),(4,8,1);
/*!40000 ALTER TABLE `bookpurchase` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coffeedrink`
--

DROP TABLE IF EXISTS `coffeedrink`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coffeedrink` (
  `drink_id` int NOT NULL AUTO_INCREMENT,
  `drink_name` varchar(40) NOT NULL,
  `price` float(5,2) NOT NULL,
  PRIMARY KEY (`drink_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coffeedrink`
--

LOCK TABLES `coffeedrink` WRITE;
/*!40000 ALTER TABLE `coffeedrink` DISABLE KEYS */;
INSERT INTO `coffeedrink` VALUES (1,'Caramel Macchiato',4.49),(2,'Mocha',4.29),(3,'London Fog',4.19),(4,'Caramel Latte',4.29);
/*!40000 ALTER TABLE `coffeedrink` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coffeedrinkpurchase`
--

DROP TABLE IF EXISTS `coffeedrinkpurchase`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coffeedrinkpurchase` (
  `drink_id` int DEFAULT NULL,
  `purchase_id` int DEFAULT NULL,
  `quantity` int NOT NULL,
  KEY `drink_id` (`drink_id`),
  KEY `purchase_id` (`purchase_id`),
  CONSTRAINT `coffeedrinkpurchase_ibfk_1` FOREIGN KEY (`drink_id`) REFERENCES `coffeedrink` (`drink_id`),
  CONSTRAINT `coffeedrinkpurchase_ibfk_2` FOREIGN KEY (`purchase_id`) REFERENCES `purchase` (`purchase_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coffeedrinkpurchase`
--

LOCK TABLES `coffeedrinkpurchase` WRITE;
/*!40000 ALTER TABLE `coffeedrinkpurchase` DISABLE KEYS */;
INSERT INTO `coffeedrinkpurchase` VALUES (1,5,1),(2,7,1),(4,8,1);
/*!40000 ALTER TABLE `coffeedrinkpurchase` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coffeeingredient`
--

DROP TABLE IF EXISTS `coffeeingredient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coffeeingredient` (
  `ingredient_id` int NOT NULL AUTO_INCREMENT,
  `ingredient_name` varchar(40) NOT NULL,
  `stock` int NOT NULL,
  PRIMARY KEY (`ingredient_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coffeeingredient`
--

LOCK TABLES `coffeeingredient` WRITE;
/*!40000 ALTER TABLE `coffeeingredient` DISABLE KEYS */;
INSERT INTO `coffeeingredient` VALUES (1,'Coffee beans',5),(2,'Caramel syrup',2),(3,'Milk',3),(4,'Vanilla syrup',2),(5,'Earl Grey tea bags',14),(6,'Chocolate syrup',3);
/*!40000 ALTER TABLE `coffeeingredient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `cust_id` int NOT NULL AUTO_INCREMENT,
  `cust_fname` varchar(30) NOT NULL,
  `cust_lname` varchar(30) NOT NULL,
  `cust_reward` int DEFAULT NULL,
  PRIMARY KEY (`cust_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Evan','Hedlund',0),(2,'Crissy','Sanders',20),(3,'Ken','Driver',10),(4,'Noah','Gleason',5);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customeremail`
--

DROP TABLE IF EXISTS `customeremail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customeremail` (
  `email_id` int NOT NULL AUTO_INCREMENT,
  `cust_id` int DEFAULT NULL,
  `email_address` varchar(60) NOT NULL,
  `is_primary` tinyint(1) NOT NULL,
  PRIMARY KEY (`email_id`),
  KEY `cust_id` (`cust_id`),
  CONSTRAINT `customeremail_ibfk_1` FOREIGN KEY (`cust_id`) REFERENCES `customer` (`cust_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customeremail`
--

LOCK TABLES `customeremail` WRITE;
/*!40000 ALTER TABLE `customeremail` DISABLE KEYS */;
INSERT INTO `customeremail` VALUES (5,1,'ehedlund@corban.edu',1),(6,2,'carissasanders@corban.edu',0),(7,3,'kdriver@corban.edu',1),(8,4,'noahgleason@corban.edu',0);
/*!40000 ALTER TABLE `customeremail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customerphonenum`
--

DROP TABLE IF EXISTS `customerphonenum`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customerphonenum` (
  `phone_id` int NOT NULL AUTO_INCREMENT,
  `cust_id` int DEFAULT NULL,
  `phone_num` varchar(11) NOT NULL,
  `phone_type` varchar(20) DEFAULT NULL,
  `is_primary` tinyint(1) NOT NULL,
  PRIMARY KEY (`phone_id`),
  KEY `cust_id` (`cust_id`),
  CONSTRAINT `customerphonenum_ibfk_1` FOREIGN KEY (`cust_id`) REFERENCES `customer` (`cust_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customerphonenum`
--

LOCK TABLES `customerphonenum` WRITE;
/*!40000 ALTER TABLE `customerphonenum` DISABLE KEYS */;
INSERT INTO `customerphonenum` VALUES (1,1,'13604961316','Mobile',1),(2,2,'15039904856','Mobile',1),(3,3,'12345678910','Home',0),(4,4,'15037131425','Mobile',1);
/*!40000 ALTER TABLE `customerphonenum` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `employee_id` int NOT NULL AUTO_INCREMENT,
  `manager` tinyint(1) NOT NULL,
  `managed_by` int DEFAULT NULL,
  `position` varchar(50) DEFAULT NULL,
  `employee_lname` varchar(30) NOT NULL,
  `employee_fname` varchar(30) NOT NULL,
  `employee_wage` float(7,2) DEFAULT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,1,NULL,'Owner','Cline','DC',59000.99),(2,0,0,'Barista','Gleason','Seth',32999.99),(3,0,0,'Teller','Nakamura','Ailsie',33999.99),(4,0,0,'Floor Staff','James','LeAnna',32999.99);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employeephonenum`
--

DROP TABLE IF EXISTS `employeephonenum`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employeephonenum` (
  `phone_id` int NOT NULL AUTO_INCREMENT,
  `employee_id` int DEFAULT NULL,
  `phone_num` varchar(11) NOT NULL,
  `phone_type` varchar(20) DEFAULT NULL,
  `is_primary` tinyint(1) NOT NULL,
  PRIMARY KEY (`phone_id`),
  KEY `employee_id` (`employee_id`),
  CONSTRAINT `employeephonenum_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employeephonenum`
--

LOCK TABLES `employeephonenum` WRITE;
/*!40000 ALTER TABLE `employeephonenum` DISABLE KEYS */;
INSERT INTO `employeephonenum` VALUES (1,1,'15093024997','Mobile',1),(2,2,'19713864734','Mobile',1),(3,3,'18083084309','Mobile',1),(4,4,'12345678910','Home',0);
/*!40000 ALTER TABLE `employeephonenum` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ingredientlist`
--

DROP TABLE IF EXISTS `ingredientlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingredientlist` (
  `drink_id` int DEFAULT NULL,
  `ingredient_id` int DEFAULT NULL,
  KEY `drink_id` (`drink_id`),
  KEY `ingredient_id` (`ingredient_id`),
  CONSTRAINT `ingredientlist_ibfk_1` FOREIGN KEY (`drink_id`) REFERENCES `coffeedrink` (`drink_id`),
  CONSTRAINT `ingredientlist_ibfk_2` FOREIGN KEY (`ingredient_id`) REFERENCES `coffeeingredient` (`ingredient_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredientlist`
--

LOCK TABLES `ingredientlist` WRITE;
/*!40000 ALTER TABLE `ingredientlist` DISABLE KEYS */;
INSERT INTO `ingredientlist` VALUES (1,1),(1,2),(1,3),(2,1),(2,3),(2,6),(3,3),(3,4),(3,5),(4,1),(4,2),(4,3);
/*!40000 ALTER TABLE `ingredientlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchase`
--

DROP TABLE IF EXISTS `purchase`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchase` (
  `purchase_id` int NOT NULL AUTO_INCREMENT,
  `cust_id` int DEFAULT NULL,
  `employee_id` int DEFAULT NULL,
  `total_cost` float(7,2) NOT NULL,
  PRIMARY KEY (`purchase_id`),
  KEY `cust_id` (`cust_id`),
  KEY `employee_id` (`employee_id`),
  CONSTRAINT `purchase_ibfk_1` FOREIGN KEY (`cust_id`) REFERENCES `customer` (`cust_id`),
  CONSTRAINT `purchase_ibfk_2` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchase`
--

LOCK TABLES `purchase` WRITE;
/*!40000 ALTER TABLE `purchase` DISABLE KEYS */;
INSERT INTO `purchase` VALUES (5,1,2,27.47),(6,2,3,13.48),(7,3,2,4.29),(8,4,3,13.18);
/*!40000 ALTER TABLE `purchase` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-24 10:40:35
