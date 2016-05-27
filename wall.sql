-- MySQL dump 10.13  Distrib 5.7.9, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: wall
-- ------------------------------------------------------
-- Server version	5.5.49-log

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
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `comment` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_comments_users_idx` (`user_id`),
  KEY `fk_comments_messages1_idx` (`message_id`),
  CONSTRAINT `fk_comments_messages1` FOREIGN KEY (`message_id`) REFERENCES `messages` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_comments_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (6,1,1,'test','2016-05-11 12:03:05','2016-05-11 12:03:05'),(7,1,2,'hola','2016-05-11 12:03:05','2016-05-11 12:03:05'),(8,3,1,'holoooooooooooooooooooooooooooooo','2016-05-11 14:23:25','2016-05-11 14:23:25'),(9,3,1,'testooooo','2016-05-11 18:32:19','2016-05-11 18:32:19'),(10,1,1,'fuck this shit','2016-05-11 19:18:43','2016-05-11 19:18:43'),(11,7,4,'dddddddduuuuuuuuuuuuuuuuuuse','2016-05-17 18:19:40','2016-05-17 18:19:40'),(12,8,4,'test','2016-05-17 18:39:09','2016-05-17 18:39:09'),(13,8,1,'he doesn\'t wanna answer apparently','2016-05-17 18:40:41','2016-05-17 18:40:41');
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `message` text,
  `reciever_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_messages_users1_idx` (`user_id`),
  CONSTRAINT `fk_messages_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,1,'Hello my name is wizwiz',4,'2016-05-11 00:17:43','2016-05-11 00:17:43'),(3,2,'Just un petit Coucou',4,'2016-05-11 01:05:41','2016-05-11 01:05:41'),(4,1,'Un nouveau bb',4,'2016-05-11 17:51:26','2016-05-11 17:51:26'),(5,1,'Hey today is great day',1,'2016-05-17 13:33:40','2016-05-17 13:33:40'),(6,4,'duuude',1,'2016-05-17 15:33:41','2016-05-17 15:33:41'),(7,4,'What\'s upppppp',1,'2016-05-17 15:35:20','2016-05-17 15:35:20'),(8,4,'hey dude what\'s up',7,'2016-05-17 17:29:12','2016-05-17 17:29:12');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `description` text,
  `password` varchar(255) DEFAULT NULL,
  `user_level` varchar(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Nazim','Bellahsene','1981-06-15','nazim.bellahsene@gmail.com','Hey everyone','$2b$12$tAOKlfZQLR8hGt//dBdZv.3DB1uQ7sqmxDsNwzJdyBNxc/oUVhLa2','9','2016-05-10 22:17:07','2016-05-18 01:29:45'),(2,'Wissam','Bellahsene','1976-02-05','agsous.w@outlook.com',NULL,'$2b$12$SF9WkWXkYqSut/rW6nzoZukn21eBFAUTM5JomPZHmbVR34Zhc.GKe','8','2016-05-11 00:48:37','2016-05-11 00:48:37'),(4,'Frank','Modic','1988-10-03','frank@modic.co',NULL,'$2b$12$A8mOR9ldcqolk9Zegi9xxejxv2nrq0FdyDFxdd4KtffDjKdQ.4u.S','8','2016-05-16 19:00:58','2016-05-16 19:00:58'),(5,'Ana','Argentina','1977-12-10','ana@bel.com',NULL,'$2b$12$r..LuFaeqqfkelbnPUZ5XuUq02xEinOnQxU13kLR8Vp9lTqLTbAZq','8','2016-05-16 19:23:02','2016-05-16 19:23:02'),(6,'Da Eun','Juliette','1999-12-12','juliette@daeun.com',NULL,'$2b$12$xl3Tc3QlMp37cfJxAVzmu.1N/8QH8UVQvR8dnzsM791qQzy7mlohy','8','2016-05-16 21:40:47','2016-05-16 21:40:47'),(7,'Grant','Hugh','1820-12-13','grant@dojo.com',NULL,'$2b$12$oYRvo9mp43DYW2dQnsV11uZr5ugV0c6JO.en1qY.BuX/tXB7DJsdi','8','2016-05-16 21:43:00','2016-05-16 21:43:00'),(8,'Danny','The Dog','1980-05-23','danny@hotdog.com',NULL,'$2b$12$gF7rV6nq0Lb9cQGzf.Jg7uRwa1kqO6gC6cWqAalGC4exKu4WlIBOy','8','2016-05-16 21:49:08','2016-05-16 21:49:08'),(9,'Derek','Doe','2016-05-27','derek@gmail.com',NULL,'$2b$12$zmvM3DjVYTGvG23Eq44lNeqW5DdE3fO.fp90OBDPzBTCe9LH4Ozjm','8','2016-05-21 14:22:31','2016-05-21 14:22:31'),(10,'Pikatchu','pokemon','2016-05-19','pikatchu@gmail.com',NULL,'$2b$12$FN0s3Rn2TV3pIU6s1QiAEem6HXjnlHZivvHwcOa9yqyR9odH65tLa','8','2016-05-21 15:07:36','2016-05-21 15:07:36'),(11,'Michael','Jordan','1994-12-29','michael@nike.com',NULL,'$2b$12$4LbBLevBoYkhut05GFI5vuoGLvNH/Sz7bcL06IXgAYCHMZY5x.wpC','8','2016-05-21 15:16:03','2016-05-21 15:16:03'),(12,'Kobe','Bryant','2016-06-29','kobe@bryant.com',NULL,'$2b$12$N5GEu0729sSfI6OYw/BlruSvYgHwDRpv9WH9fxb08ytr8ZF0AY14S','8','2016-05-21 15:19:08','2016-05-21 15:19:08'),(13,'test','testo','2016-05-26','test@test.col',NULL,'$2b$12$2K.QO4LlckWgOguUgXYesODE7RXwY4t8DnZkQiKZCd7mG2luLTS9W','8','2016-05-21 20:37:17','2016-05-21 20:37:17'),(14,'Deandre','harvey','2016-05-09','test@yomama.com',NULL,'$2b$12$ctsvkK0pNf.g2s9YWB7ig.wz3mWVwZeJXAC8ZtyoX/03xAzQMa/Qy','9','2016-05-26 09:45:26','2016-05-26 09:45:26');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-05-26 21:32:17
