-- MySQL dump 10.13  Distrib 5.7.42, for Linux (x86_64)
--
-- Host: localhost    Database: etp-tic
-- ------------------------------------------------------
-- Server version	5.7.42-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `description` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'ETP - 40','ETP '),(2,'ETP - 94','ETP TIC'),(3,'ETP - 40 e ETP 94','TEM NAS DUAS ETP');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paginas`
--

DROP TABLE IF EXISTS `paginas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `paginas` (
  `nome` varchar(15) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descricao` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `etapa` int(11) DEFAULT NULL,
  `name` varchar(200) CHARACTER SET utf8 NOT NULL,
  `description` text CHARACTER SET utf8 NOT NULL,
  `obrigatorio` int(11) DEFAULT NULL,
  `user_created` int(11) NOT NULL,
  `category` int(11) NOT NULL,
  `date_created` datetime NOT NULL,
  `observacao` text COLLATE utf8_icelandic_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `category` (`category`),
  KEY `user_created` (`user_created`),
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`category`) REFERENCES `category` (`id`),
  CONSTRAINT `product_ibfk_2` FOREIGN KEY (`user_created`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8 COLLATE=utf8_icelandic_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,1,'Informação Basica','Nesta etapa, faculta-se informar o Processo Administrativo correspondente às demandas geradas para a condução da futura contratação',0,7,1,'2023-05-30 10:49:00',''),(2,2,'Descrição da Necessidade','Neste item, você deve descrever a necessidade da compra/contratação, evidenciando o problema identificado e a real necessidade que ele gera, bem como o que se almeja alcançar com a contratação. (inciso I, art. 7°, IN 40/2020). De acordo com o art. 7°, §2°, este campo é obrigatório.',1,7,1,'2023-05-30 10:49:00',''),(3,3,'Área Requisitante','Aqui você deve informar o nome do(s) órgão(s), setor(es) ou área(s) que solicitou(aram) a contratação.',0,7,1,'2023-05-30 10:49:00',''),(4,4,'Requisitos da Contratação','Aqui você deve especificar quais são os requisitos indispensáveis de que o  objeto a adquirir/contratar deve dispor para atender à demanda, incluindo padrões mínimos de qualidade, de forma a permitir a seleção da proposta  mais vantajosa. Incluir, se possível, critérios e práticas de sustentabilidade  que devem ser veiculados como especificações técnicas do objeto ou  como obrigação da contratada. (inciso II, art. 7°, IN 40/2020). De acordo com o art. 7°, §2°, em caso do não preenchimento deste campo, devem ser apresentadas as devidas justificativas.',0,7,1,'2023-05-30 10:49:00',''),(5,1,'Informação Basica','Nesta etapa, faculta-se informar o Processo Administrativo correspondente às demandas geradas para a condução da futura contratação',0,7,2,'2023-05-30 10:49:00',''),(6,2,'Descrição da Necessidade','Neste item, você deve descrever a necessidade da compra/contratação, evidenciando o problema identificado e a real necessidade que ele gera, bem como o que se almeja alcançar com a contratação. (inciso I, art. 7°, IN 40/2020). De acordo com o art. 7°, §2°, este campo é obrigatório.',0,7,2,'2023-05-30 10:49:00',''),(7,3,'Área Requisitante','Aqui você deve informar o nome do(s) órgão(s), setor(es) ou área(s) que solicitou(aram) a contratação.',0,7,2,'2023-05-30 10:49:00',''),(15,5,'Levantamento de Mercado','Neste item, você deve informar o levantamento de mercado realizado, com a prospecção e análise das alternativas possíveis de soluções, podendo, entre outras opções:\r\na) ser consideradas contratações similares feitas por outros órgãos e  entidades, com objetivo de identificar a existência de novas  metodologias, tecnologias ou inovações que melhor atendam às  necessidades da administração; e\r\nb)	ser realizada consulta, audiência pública ou realizar diálogo transparente com potenciais contratadas, para coleta de contribuições. Caso, após o levantamento do mercado de que trata o inciso III, a quantidade de fornecedores for considerada restrita, deve-se verificar se os requisitos que limitam a participação são realmente indispensáveis, flexibilizando-os sempre que possível. (inciso III, art. 7°, c/c §1°, art. 7°, IN 40/2020). De acordo com o art. 7°, §2°, em caso do não preenchimento deste campo, devem ser apresentadas as devidas justificativas.',1,7,1,'2023-05-30 10:49:00','');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (1,'Admin'),(2,'Gerente'),(3,'Secretaria'),(4,'Usuarios');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(40) NOT NULL,
  `email` varchar(120) NOT NULL,
  `password` varchar(200) NOT NULL,
  `date_created` datetime NOT NULL,
  `last_update` datetime DEFAULT NULL,
  `role` int(11) NOT NULL,
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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (7,'Pr Jorge','jorge0302@gmail.com','$pbkdf2-sha256$29000$4XwvxbhXijGm9F7r/V8rBQ$J/onXMu4Kzfrjp9LqIAeeMg4n44Bx6JJCsSf/N2sVcg','2023-03-29 11:58:00','2023-06-05 11:01:49',1,1,NULL,'Av Armindo Moura, 581, QD E, BL 8 APT 101',NULL,'81-986452028'),(8,'admin','admin@admin','$pbkdf2-sha256$29000$X2vN.R.j1Prfe6815rz3Xg$7pHwjqXoHwZrXS/5DfuwN48Cg3dThcLNsuz4H1jntmk','2023-05-29 16:01:00',NULL,1,1,NULL,NULL,'2023-05-29','81 000000000'),(9,'Homero','homero@etpdigital.com','$pbkdf2-sha256$29000$vfd.j7H23tv7P.cc49ybsw$KMYme65JpUR5WcX2W/tYYKqeMD9J72McikyYxw3rmjU','2023-05-29 23:49:00','2023-05-29 23:49:00',1,1,NULL,'5434','2023-05-30','34534534');
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

-- Dump completed on 2023-06-05 11:29:18
