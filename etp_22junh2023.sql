-- MySQL dump 10.13  Distrib 8.0.33, for Linux (x86_64)
--
-- Host: localhost    Database: etp-tic
-- ------------------------------------------------------
-- Server version	8.0.33-0ubuntu0.20.04.2

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
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
  `name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `description` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (9,'ETP - 40','INFORMÁTICA GERAL'),(10,'ETP - 94','INFORMÁTICA ESPECIFICO'),(11,'ETP - 40 e ETP 94','TEM NAS DUAS ETP');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `etp40`
--

DROP TABLE IF EXISTS `etp40`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `etp40` (
  `id` int NOT NULL AUTO_INCREMENT,
  `informacao1_40` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `necessidade2_40` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `necessidade3_40` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `necessidade4_40` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `solucao5_40` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `solucao6_40` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `solucao7_40` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `solucao8_40` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `solucao9_40` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `solucao10_40` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `solucao11_40` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `planejamento12_40` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `planejamento13_40` text,
  `planejamento14_40` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `viabilidade15_40` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `viabilidade16_40` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `usuario_id` int DEFAULT NULL,
  `date_created` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `etp40_FK` (`usuario_id`),
  CONSTRAINT `etp40_FK` FOREIGN KEY (`usuario_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `etp40`
--

LOCK TABLES `etp40` WRITE;
/*!40000 ALTER TABLE `etp40` DISABLE KEYS */;
INSERT INTO `etp40` VALUES (1,'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16',7,'2023-06-21 01:37:00'),(4,'informação','234','543','456','567','678','789','089','6543','sdfsd','2343','234','234','234','234','23423',7,'2023-06-21 01:38:00'),(5,'42342','23423','23423','23423','234234','23423','234234','234234','234234','453435','756756','567567','345347','45645','756723','345345',7,'2023-06-21 01:44:00'),(6,'<p>teste hkj jk </p>','<p>234dsfsdhkl</p>','<p class=\"ql-align-center\"><strong>asdfasdf</strong> a</p><p>a</p><p>f</p><p>asdfasdfasf</p><p>as</p><p>fasdf</p>','<p>trwetert</p>','<p><br></p>','<p><br></p>','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','<p><br></p>','<p><br></p>','<p><br></p>','<p>teste123</p>',7,'2023-06-21 22:50:56'),(7,'<p>teste hkj jk </p>','<p>234dsfsdhkl</p>','<p class=\"ql-align-center\"><strong>asdfasdf</strong> a</p><p>a</p><p>f</p><p>asdfasdfasf</p><p>as</p><p>fasdf</p>','<p>trwetert</p>','<p><br></p>','<p><br></p>','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','<p><br></p>','<p><br></p>','<p><br></p>','<p>teste123</p>',7,'2023-06-21 22:51:33'),(8,'<p>teste hkj jk </p>','<p>234dsfsdhkl</p>','<p class=\"ql-align-center\"><strong>asdfasdf</strong> a</p><p>a</p><p>f</p><p>asdfasdfasf</p><p>as</p><p>fasdf</p>','<p>trwetert</p>','<p><br></p>','<p><br></p>','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','<p><br></p>','<p><br></p>','<p><br></p>','<p>teste123</p>',7,'2023-06-21 23:16:19');
/*!40000 ALTER TABLE `etp40` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Table structure for table `etp94`
--

DROP TABLE IF EXISTS `etp94`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `etp94` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `informacao1_94` text,
  `necessidade2_94` text,
  `necessidade3_94` text,
  `necessidade4_94` text,
  `necessidade5_94` text,
  `necessidade6_94` text,
  `necessidade7_94` text,
  `solucao8_94` text,
  `solucao9_94` text,
  `solucao10_94` text,
  `solucao11_94` text,
  `solucao12_94` text,
  `solucao13_94` text,
  `solucao14_94` text,
  `solucao15_94` text,
  `planejamento16_94` text,
  `planejamento17_94` text,
  `viabilidade18_94` text,
  `viabilidade19_94` text,
  `usuario_id` int(11) DEFAULT NULL,
  `date_created` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `etp94_FK` (`usuario_id`),
  CONSTRAINT `etp94_FK` FOREIGN KEY (`usuario_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `etp94`
--

LOCK TABLES `etp94` WRITE;
/*!40000 ALTER TABLE `etp94` DISABLE KEYS */;
INSERT INTO `etp94` VALUES (9,'23','23','23','','','','','','','','','','','','113\r\n12','','','','',13,'2023-06-28 08:01:00'),(10,'Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','rerere',13,'2023-06-28 08:50:31'),(11,'Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','rerere',13,'2023-06-28 08:56:26'),(12,'Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','rerere',13,'2023-06-28 09:00:44'),(13,'Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação',13,'2023-06-28 09:09:44'),(14,'Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação',13,'2023-06-28 09:15:46'),(15,'Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação',13,'2023-06-28 09:19:14'),(16,'Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','Não Constar Informação','oioioo',13,'2023-06-28 09:35:25');
/*!40000 ALTER TABLE `etp94` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;
--
-- Table structure for table `paginas`
--

DROP TABLE IF EXISTS `paginas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paginas` (
  `nome` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `descricao` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paginas`
--

LOCK TABLES `paginas` WRITE;
/*!40000 ALTER TABLE `paginas` DISABLE KEYS */;
INSERT INTO `paginas` VALUES ('informacao',1,''),('necessidade',2,'Descrever as necessidades');
/*!40000 ALTER TABLE `paginas` ENABLE KEYS */;
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
  `status` int DEFAULT NULL,
  `user_created` int NOT NULL,
  `category` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `category` (`category`),
  KEY `user_created` (`user_created`),
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`category`) REFERENCES `category` (`id`),
  CONSTRAINT `product_ibfk_2` FOREIGN KEY (`user_created`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (11,'Informação básica','Nesta etapa, faculta-se informar o Processo Administrativo correspondente às demandas geradas para a condução da futura contratação',NULL,7,11),(12,'3. Área Requisitante','Aqui você deve informar o nome do(s) órgão(s), setor(es) ou área(s) que solicitou(aram) a contratação.',NULL,7,11);
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (1,'Admin'),(2,'Gerente'),(3,'usuário restrito'),(4,'usuários');
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
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (7,'Pr Jorge','jorge0302@gmail.com','$pbkdf2-sha256$29000$9H7PmfM.Z2xNiRGCUGoN4Q$vZCozBH3OUJCQeuHzOscu2SPK4ftuP0wVUFGU0yoZXw','2023-05-22 00:06:48','2023-05-31 00:06:51',1,1,NULL,'Av Armindo Moura, 581, QD E, BL 8 APT 101','2023-05-30','81-986452028'),(11,'jorge0302@gmail.com','homero@etpdigital.com','$pbkdf2-sha256$29000$5pyzVgqBECKkVMr5PydkrA$8xhqoJF6wYO1ueUonPXkgX9pM94LTiU0CQFQfNP6wlM','2023-05-24 23:49:00','2023-05-31 02:50:16',1,1,NULL,'5434','2023-05-30','34534534'),(12,'ADMIN','admin@admin','$pbkdf2-sha256$29000$HQNgrNVaaw2h1Nq7F2Ks1Q$1SxfzdxwRCqcJ2Ya6OUO4KR93XusiKWJAQaT0UHpPfE','2023-05-31 16:12:00','2023-05-31 00:07:19',1,1,NULL,'123',NULL,'543512'),(13,'araujo','araujo@email','$pbkdf2-sha256$29000$6p3zPgegVIrxnhOCEOIcww$ZB9GQHzgKxUlbARWefIYVFzlWK53GG8gp0AmhiPpF0A','2023-05-31 02:50:00',NULL,1,1,NULL,'teste',NULL,'423423');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'etp-tic'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-21 23:20:26
