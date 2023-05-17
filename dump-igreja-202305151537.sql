-- MySQL dump 10.13  Distrib 8.0.33, for Linux (x86_64)
--
-- Host: 191.252.185.216    Database: igreja
-- ------------------------------------------------------
-- Server version	8.0.32-0ubuntu0.20.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('c0e7f698ff99');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `description` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'Calçados',''),(2,'Ortopédico','Materiais usado na ortopedia '),(3,'Aluguel','Informação sobre o alugueis'),(4,'Energia','Celpe'),(5,'Água','gasto com águas.'),(6,'Pastores','Despensas com pastores e auxiliares'),(7,'ação social','Gasto com ajuda financeira');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `description` text NOT NULL,
  `qtd` int DEFAULT NULL,
  `image` text,
  `price` decimal(10,2) NOT NULL,
  `date_created` datetime NOT NULL,
  `last_update` datetime DEFAULT NULL,
  `status` int DEFAULT NULL,
  `user_created` int NOT NULL,
  `category` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `category` (`category`),
  KEY `user_created` (`user_created`),
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`category`) REFERENCES `category` (`id`),
  CONSTRAINT `product_ibfk_2` FOREIGN KEY (`user_created`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'Tênis','Calçado',20,'',149.90,'2019-03-02 19:32:00','2019-03-02 19:32:00',1,2,1),(2,'Sapato Social','Calçado',38,'',249.90,'2019-03-02 21:17:00','2023-03-28 16:34:19',1,2,1),(3,'Sapatênis','Calçado',200,NULL,350.00,'2019-03-04 12:09:42','2019-03-02 21:20:26',1,2,1),(4,'Sandália','Calçado',30,'',300.00,'2019-03-04 22:53:00','2019-03-04 22:53:00',1,2,1),(5,'Chinelo','Calçado',40,'',1900.00,'2019-03-04 22:54:00','2019-03-04 22:54:00',1,2,1),(6,'Teste ortopedista ','Teste',5,'',260.00,'2023-03-28 13:30:00','2023-03-28 13:30:00',1,2,2),(7,'teste 1','teste12',22,'',25.00,'2023-03-29 14:10:00','2023-03-29 14:10:00',1,5,1),(8,'Aluguel do Cajá ','mês de julho',1,'comprovante',600.00,'2023-03-29 14:44:00','2023-03-29 14:44:00',1,2,3);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `role` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (1,'Admin'),(2,'Administração'),(3,'Diáconos'),(4,'membros');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(40) NOT NULL,
  `email` varchar(120) NOT NULL,
  `password` varchar(200) NOT NULL,
  `date_created` datetime NOT NULL,
  `last_update` datetime DEFAULT NULL,
  `role` int NOT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `recovery_code` varchar(200) DEFAULT NULL,
  `endereco` varchar(420) DEFAULT NULL,
  `data_nascimento` date DEFAULT NULL,
  `celular` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `username` (`username`),
  KEY `role` (`role`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`role`) REFERENCES `role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (2,'admin','admin@email.com','$pbkdf2-sha256$29000$4vwf41zL.V/rvTcmxLj33g$KiPwlnxJFJUK5EB1qD3cotArGsl8oYaVv3qN1ZQJjr0','2019-03-02 13:33:00','2019-03-10 15:59:55',1,1,'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MiwidXNlcm5hbWUiOiJ0aWFnb2x1aXpycyIsImV4cCI6MTU1MjI0NDQ5Mn0.S0L7LiRIWgNRT3Mf16-g1ZU6azeSF0QINyw8zVzlJyY',NULL,NULL,NULL),(4,'gerente','gerente@email','$pbkdf2-sha256$29000$KKX0HsN4b60VwnjPmZNSig$C3M1g9k6w/ETive5KK1RgoidALPodfUZhs1ofehBSP4','2019-03-07 17:53:00','2023-03-28 16:29:41',2,1,NULL,NULL,NULL,NULL),(5,'loginsta','logista@email','$pbkdf2-sha256$29000$4vwf41zL.V/rvTcmxLj33g$KiPwlnxJFJUK5EB1qD3cotArGsl8oYaVv3qN1ZQJjr0','2019-03-07 17:53:00','2019-03-08 09:23:27',3,1,NULL,NULL,NULL,NULL),(6,'admin@email.com','usuario@email','$pbkdf2-sha256$29000$9D7nvLfWeq81ptS69x6DsA$bcjYayfbN/w6HIMZjZa4rQj9w2V3UF.Cgu1K5IK1xkw','2019-03-07 17:53:00','2023-03-28 16:31:58',4,1,'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NiwidXNlcm5hbWUiOiJ1c3VhcmlvIiwiZXhwIjoxNTU1MzU2NDI3fQ.Huf6P-pr4qsfLsiVowvm3ZRSsRmNszJmxG_ezD_m2U8',NULL,NULL,NULL),(7,'Pr Jorge','jorge0302@gmail.com','$pbkdf2-sha256$29000$Vqo1pvQeY.z9/x9DqDWmdA$jThCCT.e7yac23K34u1KUcx7Dehf1Gm6scctFeOExDA','2023-03-29 11:58:00',NULL,1,1,NULL,'Av Armindo Moura, 581, QD E, BL 8 APT 101',NULL,'81-986452028'),(8,'Maiara','bilongavendas@gmail.com','$pbkdf2-sha256$29000$I6T0HgNA6L2X0ppTyrl3jg$zTr4cvLFHDVSQZxi4arQhpHccg38JrDtTFHfq7y4jck','2023-03-29 12:51:00',NULL,2,1,NULL,'Av Armindo Moura, 581, QD E bl 8 AP 101','1993-05-22','81945204094'),(9,'Missionária Eunides','misseunides@gmail.com','$pbkdf2-sha256$29000$CMGYU4qxtnYuhTAmxNibcw$IJMik.QPD8ZxbZAZj2vIoc/TFa0gwH4bIkWXdgl9Ktw','2023-03-29 14:15:00',NULL,2,1,NULL,'Ibura','1973-03-07','81-9999999'),(10,'teste','teste@email.com','$pbkdf2-sha256$29000$Tqn1/r/3fg.hdC5lDCGE0A$Rue42ovqRIUFTatBhRobtwov8Wb/dH4vKwVgagbEtRk','2023-03-29 14:36:00',NULL,4,1,NULL,'teste','2023-03-29','teste');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'igreja'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-15 15:37:08
