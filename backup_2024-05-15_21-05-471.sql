-- MariaDB dump 10.19-11.2.0-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: otra
-- ------------------------------------------------------
-- Server version	11.2.0-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin_interface_theme`
--

DROP TABLE IF EXISTS `admin_interface_theme`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_interface_theme` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `title` varchar(50) NOT NULL,
  `title_visible` tinyint(1) NOT NULL,
  `logo` varchar(100) NOT NULL,
  `logo_visible` tinyint(1) NOT NULL,
  `css_header_background_color` varchar(10) NOT NULL,
  `title_color` varchar(10) NOT NULL,
  `css_header_text_color` varchar(10) NOT NULL,
  `css_header_link_color` varchar(10) NOT NULL,
  `css_header_link_hover_color` varchar(10) NOT NULL,
  `css_module_background_color` varchar(10) NOT NULL,
  `css_module_text_color` varchar(10) NOT NULL,
  `css_module_link_color` varchar(10) NOT NULL,
  `css_module_link_hover_color` varchar(10) NOT NULL,
  `css_module_rounded_corners` tinyint(1) NOT NULL,
  `css_generic_link_color` varchar(10) NOT NULL,
  `css_generic_link_hover_color` varchar(10) NOT NULL,
  `css_save_button_background_color` varchar(10) NOT NULL,
  `css_save_button_background_hover_color` varchar(10) NOT NULL,
  `css_save_button_text_color` varchar(10) NOT NULL,
  `css_delete_button_background_color` varchar(10) NOT NULL,
  `css_delete_button_background_hover_color` varchar(10) NOT NULL,
  `css_delete_button_text_color` varchar(10) NOT NULL,
  `list_filter_dropdown` tinyint(1) NOT NULL,
  `related_modal_active` tinyint(1) NOT NULL,
  `related_modal_background_color` varchar(10) NOT NULL,
  `related_modal_rounded_corners` tinyint(1) NOT NULL,
  `logo_color` varchar(10) NOT NULL,
  `recent_actions_visible` tinyint(1) NOT NULL,
  `favicon` varchar(100) NOT NULL,
  `related_modal_background_opacity` varchar(5) NOT NULL,
  `env_name` varchar(50) NOT NULL,
  `env_visible_in_header` tinyint(1) NOT NULL,
  `env_color` varchar(10) NOT NULL,
  `env_visible_in_favicon` tinyint(1) NOT NULL,
  `related_modal_close_button_visible` tinyint(1) NOT NULL,
  `language_chooser_active` tinyint(1) NOT NULL,
  `language_chooser_display` varchar(10) NOT NULL,
  `list_filter_sticky` tinyint(1) NOT NULL,
  `form_pagination_sticky` tinyint(1) NOT NULL,
  `form_submit_sticky` tinyint(1) NOT NULL,
  `css_module_background_selected_color` varchar(10) NOT NULL,
  `css_module_link_selected_color` varchar(10) NOT NULL,
  `logo_max_height` smallint(5) unsigned NOT NULL CHECK (`logo_max_height` >= 0),
  `logo_max_width` smallint(5) unsigned NOT NULL CHECK (`logo_max_width` >= 0),
  `foldable_apps` tinyint(1) NOT NULL,
  `language_chooser_control` varchar(20) NOT NULL,
  `list_filter_highlight` tinyint(1) NOT NULL,
  `list_filter_removal_links` tinyint(1) NOT NULL,
  `show_fieldsets_as_tabs` tinyint(1) NOT NULL,
  `show_inlines_as_tabs` tinyint(1) NOT NULL,
  `css_generic_link_active_color` varchar(10) NOT NULL,
  `collapsible_stacked_inlines` tinyint(1) NOT NULL,
  `collapsible_stacked_inlines_collapsed` tinyint(1) NOT NULL,
  `collapsible_tabular_inlines` tinyint(1) NOT NULL,
  `collapsible_tabular_inlines_collapsed` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_interface_theme_name_30bda70f_uniq` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_interface_theme`
--

LOCK TABLES `admin_interface_theme` WRITE;
/*!40000 ALTER TABLE `admin_interface_theme` DISABLE KEYS */;
/*!40000 ALTER TABLE `admin_interface_theme` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `aso_benef`
--

DROP TABLE IF EXISTS `aso_benef`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `aso_benef` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cla_doc` varchar(1) NOT NULL,
  `doc_ide` varchar(12) NOT NULL,
  `nombre` varchar(64) NOT NULL,
  `agno_nac` int(11) DEFAULT NULL,
  `parentesco` varchar(1) NOT NULL,
  `porcentaje` double DEFAULT NULL,
  `asociado_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `aso_benef_asociado_id_doc_ide_3deff567_uniq` (`asociado_id`,`doc_ide`),
  CONSTRAINT `aso_benef_asociado_id_7e0109c6_fk_asociados_id` FOREIGN KEY (`asociado_id`) REFERENCES `asociados` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aso_benef`
--

LOCK TABLES `aso_benef` WRITE;
/*!40000 ALTER TABLE `aso_benef` DISABLE KEYS */;
/*!40000 ALTER TABLE `aso_benef` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `aso_referencias`
--

DROP TABLE IF EXISTS `aso_referencias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `aso_referencias` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `tipo_ref` varchar(1) NOT NULL,
  `parentesco` varchar(1) NOT NULL,
  `nombre` varchar(64) NOT NULL,
  `ocupacion` varchar(32) NOT NULL,
  `empresa` varchar(40) NOT NULL,
  `direccion` varchar(64) NOT NULL,
  `tel_fijo` varchar(10) NOT NULL,
  `tel_cel` varchar(10) NOT NULL,
  `tel_emp` varchar(10) NOT NULL,
  `asociado_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `aso_referencias_asociado_id_nombre_487d281b_uniq` (`asociado_id`,`nombre`),
  CONSTRAINT `aso_referencias_asociado_id_72372c1d_fk_asociados_id` FOREIGN KEY (`asociado_id`) REFERENCES `asociados` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aso_referencias`
--

LOCK TABLES `aso_referencias` WRITE;
/*!40000 ALTER TABLE `aso_referencias` DISABLE KEYS */;
/*!40000 ALTER TABLE `aso_referencias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `asociados`
--

DROP TABLE IF EXISTS `asociados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `asociados` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cod_aso` varchar(12) NOT NULL,
  `sexo` varchar(1) NOT NULL,
  `est_civ` varchar(1) NOT NULL,
  `fec_nac` date DEFAULT NULL,
  `zona` varchar(16) DEFAULT NULL,
  `profesion` varchar(48) DEFAULT NULL,
  `ocupacion` varchar(40) DEFAULT NULL,
  `ocupacion_cod` varchar(3) DEFAULT NULL,
  `estrato` varchar(1) DEFAULT NULL,
  `niv_est` varchar(1) NOT NULL,
  `cab_fam` varchar(1) NOT NULL,
  `fec_afi` date DEFAULT NULL,
  `cargo_emp` varchar(36) DEFAULT NULL,
  `per_a_cargo` int(11) DEFAULT NULL,
  `num_hij_men` int(11) DEFAULT NULL,
  `num_hij_may` int(11) DEFAULT NULL,
  `tip_viv` varchar(24) DEFAULT NULL,
  `tie_en_ciu` int(11) DEFAULT NULL,
  `med_con` varchar(48) DEFAULT NULL,
  `fec_ing_tra` date DEFAULT NULL,
  `tel_tra` varchar(10) DEFAULT NULL,
  `tip_sal` varchar(18) DEFAULT NULL,
  `act_eco` varchar(24) DEFAULT NULL,
  `cod_ciiu` varchar(12) DEFAULT NULL,
  `tip_con` varchar(18) DEFAULT NULL,
  `nom_emp` varchar(40) DEFAULT NULL,
  `nit_emp` varchar(12) DEFAULT NULL,
  `dir_emp` varchar(50) DEFAULT NULL,
  `email_emp` varchar(254) DEFAULT NULL,
  `sector_emp` varchar(12) DEFAULT NULL,
  `empresa_ant` int(11) DEFAULT NULL,
  `emp_num_emp` int(11) DEFAULT NULL,
  `negocio_pro` varchar(1) NOT NULL,
  `negocio_nom` varchar(48) DEFAULT NULL,
  `negocio_tel` varchar(10) DEFAULT NULL,
  `negocio_loc_pro` varchar(1) NOT NULL,
  `negocio_cam_com` varchar(1) NOT NULL,
  `negocio_ant` int(11) DEFAULT NULL,
  `pension_ent` varchar(36) DEFAULT NULL,
  `pension_tie` int(11) DEFAULT NULL,
  `pension_otr` varchar(1) NOT NULL,
  `pension_ent_otr` varchar(36) DEFAULT NULL,
  `pep_es_fam` varchar(1) NOT NULL,
  `pep_fam_par` varchar(1) NOT NULL,
  `pep_fam_nom` varchar(36) DEFAULT NULL,
  `pep_car_pub` varchar(1) NOT NULL,
  `pep_cargo` varchar(36) DEFAULT NULL,
  `pep_eje_pod` varchar(1) NOT NULL,
  `pep_adm_rec_est` varchar(1) NOT NULL,
  `tie_gre_car` varchar(1) NOT NULL,
  `recibe_pag_ext` varchar(1) NOT NULL,
  `recide_ext_mas_186` varchar(1) NOT NULL,
  `recibe_ing_ext` varchar(1) NOT NULL,
  `estado_anteia` varchar(1) NOT NULL,
  `ciu_tra_id` bigint(20) DEFAULT NULL,
  `id_pag_id` bigint(20) DEFAULT NULL,
  `oficina_id` bigint(20) DEFAULT NULL,
  `tercero_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `asociados_oficina_id_cod_aso_6bb3f49a_uniq` (`oficina_id`,`cod_aso`),
  KEY `asociados_ciu_tra_id_daf65bec_fk_localidades_id` (`ciu_tra_id`),
  KEY `asociados_id_pag_id_3bc8e7a5_fk_pagadores_id` (`id_pag_id`),
  KEY `asociados_tercero_id_5b396400_fk_terceros_id` (`tercero_id`),
  CONSTRAINT `asociados_ciu_tra_id_daf65bec_fk_localidades_id` FOREIGN KEY (`ciu_tra_id`) REFERENCES `localidades` (`id`),
  CONSTRAINT `asociados_id_pag_id_3bc8e7a5_fk_pagadores_id` FOREIGN KEY (`id_pag_id`) REFERENCES `pagadores` (`id`),
  CONSTRAINT `asociados_oficina_id_acba896d_fk_oficinas_id` FOREIGN KEY (`oficina_id`) REFERENCES `oficinas` (`id`),
  CONSTRAINT `asociados_tercero_id_5b396400_fk_terceros_id` FOREIGN KEY (`tercero_id`) REFERENCES `terceros` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asociados`
--

LOCK TABLES `asociados` WRITE;
/*!40000 ALTER TABLE `asociados` DISABLE KEYS */;
/*!40000 ALTER TABLE `asociados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=193 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES
(1,'Can add Theme',1,'add_theme'),
(2,'Can change Theme',1,'change_theme'),
(3,'Can delete Theme',1,'delete_theme'),
(4,'Can view Theme',1,'view_theme'),
(5,'Can add log entry',2,'add_logentry'),
(6,'Can change log entry',2,'change_logentry'),
(7,'Can delete log entry',2,'delete_logentry'),
(8,'Can view log entry',2,'view_logentry'),
(9,'Can add permission',3,'add_permission'),
(10,'Can change permission',3,'change_permission'),
(11,'Can delete permission',3,'delete_permission'),
(12,'Can view permission',3,'view_permission'),
(13,'Can add group',4,'add_group'),
(14,'Can change group',4,'change_group'),
(15,'Can delete group',4,'delete_group'),
(16,'Can view group',4,'view_group'),
(17,'Can add user',5,'add_user'),
(18,'Can change user',5,'change_user'),
(19,'Can delete user',5,'delete_user'),
(20,'Can view user',5,'view_user'),
(21,'Can add content type',6,'add_contenttype'),
(22,'Can change content type',6,'change_contenttype'),
(23,'Can delete content type',6,'delete_contenttype'),
(24,'Can view content type',6,'view_contenttype'),
(25,'Can add session',7,'add_session'),
(26,'Can change session',7,'change_session'),
(27,'Can delete session',7,'delete_session'),
(28,'Can view session',7,'view_session'),
(29,'Can add ct a_cda t_amp',8,'add_cta_cdat_amp'),
(30,'Can change ct a_cda t_amp',8,'change_cta_cdat_amp'),
(31,'Can delete ct a_cda t_amp',8,'delete_cta_cdat_amp'),
(32,'Can view ct a_cda t_amp',8,'view_cta_cdat_amp'),
(33,'Can add pla n_aportes',9,'add_plan_aportes'),
(34,'Can change pla n_aportes',9,'change_plan_aportes'),
(35,'Can delete pla n_aportes',9,'delete_plan_aportes'),
(36,'Can view pla n_aportes',9,'view_plan_aportes'),
(37,'Can add asociados',10,'add_asociados'),
(38,'Can change asociados',10,'change_asociados'),
(39,'Can delete asociados',10,'delete_asociados'),
(40,'Can view asociados',10,'view_asociados'),
(41,'Can add as o_referencias',11,'add_aso_referencias'),
(42,'Can change as o_referencias',11,'change_aso_referencias'),
(43,'Can delete as o_referencias',11,'delete_aso_referencias'),
(44,'Can view as o_referencias',11,'view_aso_referencias'),
(45,'Can add as o_benef',12,'add_aso_benef'),
(46,'Can change as o_benef',12,'change_aso_benef'),
(47,'Can delete as o_benef',12,'delete_aso_benef'),
(48,'Can view as o_benef',12,'view_aso_benef'),
(49,'Can add backup',13,'add_backup'),
(50,'Can change backup',13,'change_backup'),
(51,'Can delete backup',13,'delete_backup'),
(52,'Can view backup',13,'view_backup'),
(53,'Can add cambio s_cre',14,'add_cambios_cre'),
(54,'Can change cambio s_cre',14,'change_cambios_cre'),
(55,'Can delete cambio s_cre',14,'delete_cambios_cre'),
(56,'Can view cambio s_cre',14,'view_cambios_cre'),
(57,'Can add ca t_de s_di a_cre',15,'add_cat_des_dia_cre'),
(58,'Can change ca t_de s_di a_cre',15,'change_cat_des_dia_cre'),
(59,'Can delete ca t_de s_di a_cre',15,'delete_cat_des_dia_cre'),
(60,'Can view ca t_de s_di a_cre',15,'view_cat_des_dia_cre'),
(61,'Can add credito s_causa',16,'add_creditos_causa'),
(62,'Can change credito s_causa',16,'change_creditos_causa'),
(63,'Can delete credito s_causa',16,'delete_creditos_causa'),
(64,'Can view credito s_causa',16,'view_creditos_causa'),
(65,'Can add ct a_cdat',17,'add_cta_cdat'),
(66,'Can change ct a_cdat',17,'change_cta_cdat'),
(67,'Can delete ct a_cdat',17,'delete_cta_cdat'),
(68,'Can view ct a_cdat',17,'view_cta_cdat'),
(69,'Can add centrocostos',18,'add_centrocostos'),
(70,'Can change centrocostos',18,'change_centrocostos'),
(71,'Can delete centrocostos',18,'delete_centrocostos'),
(72,'Can view centrocostos',18,'view_centrocostos'),
(73,'Can add cierr e_mes',19,'add_cierre_mes'),
(74,'Can change cierr e_mes',19,'change_cierre_mes'),
(75,'Can delete cierr e_mes',19,'delete_cierre_mes'),
(76,'Can view cierr e_mes',19,'view_cierre_mes'),
(77,'Can add clientes',20,'add_clientes'),
(78,'Can change clientes',20,'change_clientes'),
(79,'Can delete clientes',20,'delete_clientes'),
(80,'Can view clientes',20,'view_clientes'),
(81,'Can add conceptos',21,'add_conceptos'),
(82,'Can change conceptos',21,'change_conceptos'),
(83,'Can delete conceptos',21,'delete_conceptos'),
(84,'Can view conceptos',21,'view_conceptos'),
(85,'Can add im p_co n_cre',22,'add_imp_con_cre'),
(86,'Can change im p_co n_cre',22,'change_imp_con_cre'),
(87,'Can delete im p_co n_cre',22,'delete_imp_con_cre'),
(88,'Can view im p_co n_cre',22,'view_imp_con_cre'),
(89,'Can add im p_co n_cr e_int',23,'add_imp_con_cre_int'),
(90,'Can change im p_co n_cr e_int',23,'change_imp_con_cre_int'),
(91,'Can delete im p_co n_cr e_int',23,'delete_imp_con_cre_int'),
(92,'Can view im p_co n_cr e_int',23,'view_imp_con_cre_int'),
(93,'Can add im p_co n_li n_aho',24,'add_imp_con_lin_aho'),
(94,'Can change im p_co n_li n_aho',24,'change_imp_con_lin_aho'),
(95,'Can delete im p_co n_li n_aho',24,'delete_imp_con_lin_aho'),
(96,'Can view im p_co n_li n_aho',24,'view_imp_con_lin_aho'),
(97,'Can add creditos',25,'add_creditos'),
(98,'Can change creditos',25,'change_creditos'),
(99,'Can delete creditos',25,'delete_creditos'),
(100,'Can view creditos',25,'view_creditos'),
(101,'Can add codeudores',26,'add_codeudores'),
(102,'Can change codeudores',26,'change_codeudores'),
(103,'Can delete codeudores',26,'delete_codeudores'),
(104,'Can view codeudores',26,'view_codeudores'),
(105,'Can add cta s_ahorro',27,'add_ctas_ahorro'),
(106,'Can change cta s_ahorro',27,'change_ctas_ahorro'),
(107,'Can delete cta s_ahorro',27,'delete_ctas_ahorro'),
(108,'Can view cta s_ahorro',27,'view_ctas_ahorro'),
(109,'Can add pla n_ctas',28,'add_plan_ctas'),
(110,'Can change pla n_ctas',28,'change_plan_ctas'),
(111,'Can delete pla n_ctas',28,'delete_plan_ctas'),
(112,'Can view pla n_ctas',28,'view_plan_ctas'),
(113,'Can add destin o_cre',29,'add_destino_cre'),
(114,'Can change destin o_cre',29,'change_destino_cre'),
(115,'Can delete destin o_cre',29,'delete_destino_cre'),
(116,'Can view destin o_cre',29,'view_destino_cre'),
(117,'Can add detall e_econo',30,'add_detalle_econo'),
(118,'Can change detall e_econo',30,'change_detalle_econo'),
(119,'Can delete detall e_econo',30,'delete_detalle_econo'),
(120,'Can view detall e_econo',30,'view_detalle_econo'),
(121,'Can add detall e_prod',31,'add_detalle_prod'),
(122,'Can change detall e_prod',31,'change_detalle_prod'),
(123,'Can delete detall e_prod',31,'delete_detalle_prod'),
(124,'Can view detall e_prod',31,'view_detalle_prod'),
(125,'Can add doct o_conta',32,'add_docto_conta'),
(126,'Can change doct o_conta',32,'change_docto_conta'),
(127,'Can delete doct o_conta',32,'delete_docto_conta'),
(128,'Can view doct o_conta',32,'view_docto_conta'),
(129,'Can add xdo c_zep',33,'add_xdoc_zep'),
(130,'Can change xdo c_zep',33,'change_xdoc_zep'),
(131,'Can delete xdo c_zep',33,'delete_xdoc_zep'),
(132,'Can view xdo c_zep',33,'view_xdoc_zep'),
(133,'Can add estado s_fin',34,'add_estados_fin'),
(134,'Can change estado s_fin',34,'change_estados_fin'),
(135,'Can delete estado s_fin',34,'delete_estados_fin'),
(136,'Can view estado s_fin',34,'view_estados_fin'),
(137,'Can add hech o_econo',35,'add_hecho_econo'),
(138,'Can change hech o_econo',35,'change_hecho_econo'),
(139,'Can delete hech o_econo',35,'delete_hecho_econo'),
(140,'Can view hech o_econo',35,'view_hecho_econo'),
(141,'Can add ct a_ah o_es t_his',36,'add_cta_aho_est_his'),
(142,'Can change ct a_ah o_es t_his',36,'change_cta_aho_est_his'),
(143,'Can delete ct a_ah o_es t_his',36,'delete_cta_aho_est_his'),
(144,'Can view ct a_ah o_es t_his',36,'view_cta_aho_est_his'),
(145,'Can add linea s_ahorro',37,'add_lineas_ahorro'),
(146,'Can change linea s_ahorro',37,'change_lineas_ahorro'),
(147,'Can delete linea s_ahorro',37,'delete_lineas_ahorro'),
(148,'Can view linea s_ahorro',37,'view_lineas_ahorro'),
(149,'Can add linea s_credito',38,'add_lineas_credito'),
(150,'Can change linea s_credito',38,'change_lineas_credito'),
(151,'Can delete linea s_credito',38,'delete_lineas_credito'),
(152,'Can view linea s_credito',38,'view_lineas_credito'),
(153,'Can add ct a_cda t_liq',39,'add_cta_cdat_liq'),
(154,'Can change ct a_cda t_liq',39,'change_cta_cdat_liq'),
(155,'Can delete ct a_cda t_liq',39,'delete_cta_cdat_liq'),
(156,'Can view ct a_cda t_liq',39,'view_cta_cdat_liq'),
(157,'Can add localidades',40,'add_localidades'),
(158,'Can change localidades',40,'change_localidades'),
(159,'Can delete localidades',40,'delete_localidades'),
(160,'Can view localidades',40,'view_localidades'),
(161,'Can add mo v_caja',41,'add_mov_caja'),
(162,'Can change mo v_caja',41,'change_mov_caja'),
(163,'Can delete mo v_caja',41,'delete_mov_caja'),
(164,'Can view mo v_caja',41,'view_mov_caja'),
(165,'Can add oficinas',42,'add_oficinas'),
(166,'Can change oficinas',42,'change_oficinas'),
(167,'Can delete oficinas',42,'delete_oficinas'),
(168,'Can view oficinas',42,'view_oficinas'),
(169,'Can add originacion',43,'add_originacion'),
(170,'Can change originacion',43,'change_originacion'),
(171,'Can delete originacion',43,'delete_originacion'),
(172,'Can view originacion',43,'view_originacion'),
(173,'Can add pagadores',44,'add_pagadores'),
(174,'Can change pagadores',44,'change_pagadores'),
(175,'Can delete pagadores',44,'delete_pagadores'),
(176,'Can view pagadores',44,'view_pagadores'),
(177,'Can add re t_fu e_aho',45,'add_ret_fue_aho'),
(178,'Can change re t_fu e_aho',45,'change_ret_fue_aho'),
(179,'Can delete re t_fu e_aho',45,'delete_ret_fue_aho'),
(180,'Can view re t_fu e_aho',45,'view_ret_fue_aho'),
(181,'Can add ta s_li n_aho',46,'add_tas_lin_aho'),
(182,'Can change ta s_li n_aho',46,'change_tas_lin_aho'),
(183,'Can delete ta s_li n_aho',46,'delete_tas_lin_aho'),
(184,'Can view ta s_li n_aho',46,'view_tas_lin_aho'),
(185,'Can add terceros',47,'add_terceros'),
(186,'Can change terceros',47,'change_terceros'),
(187,'Can delete terceros',47,'delete_terceros'),
(188,'Can view terceros',47,'view_terceros'),
(189,'Can add usuarios',48,'add_usuarios'),
(190,'Can change usuarios',48,'change_usuarios'),
(191,'Can delete usuarios',48,'delete_usuarios'),
(192,'Can view usuarios',48,'view_usuarios');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backup`
--

DROP TABLE IF EXISTS `backup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `backup` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `timestamp` datetime(6) NOT NULL,
  `filename` varchar(100) NOT NULL,
  `usuario` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `backup_timestamp_b90c276c_uniq` (`timestamp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backup`
--

LOCK TABLES `backup` WRITE;
/*!40000 ALTER TABLE `backup` DISABLE KEYS */;
/*!40000 ALTER TABLE `backup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cambios_cre`
--

DROP TABLE IF EXISTS `cambios_cre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cambios_cre` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `tip_cam` varchar(1) DEFAULT NULL,
  `capital` double DEFAULT NULL,
  `int_cor` double DEFAULT NULL,
  `int_mor` double DEFAULT NULL,
  `pol_seg` double DEFAULT NULL,
  `des_pp` double DEFAULT NULL,
  `acreedor` double DEFAULT NULL,
  `det_pro_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cambios_cre_det_pro_id_tip_cam_067edefb_uniq` (`det_pro_id`,`tip_cam`),
  CONSTRAINT `cambios_cre_det_pro_id_68d1b399_fk_detalle_prod_id` FOREIGN KEY (`det_pro_id`) REFERENCES `detalle_prod` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cambios_cre`
--

LOCK TABLES `cambios_cre` WRITE;
/*!40000 ALTER TABLE `cambios_cre` DISABLE KEYS */;
/*!40000 ALTER TABLE `cambios_cre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cat_des_dia_cre`
--

DROP TABLE IF EXISTS `cat_des_dia_cre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cat_des_dia_cre` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `codigo` int(11) NOT NULL,
  `categoria` varchar(1) NOT NULL,
  `minimo_dias` int(11) DEFAULT NULL,
  `maximo_dias` int(11) DEFAULT NULL,
  `cliente_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cat_des_dia_cre_cliente_id_codigo_categoria_a56a2855_uniq` (`cliente_id`,`codigo`,`categoria`),
  CONSTRAINT `cat_des_dia_cre_cliente_id_7adbb96e_fk_clientes_id` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cat_des_dia_cre`
--

LOCK TABLES `cat_des_dia_cre` WRITE;
/*!40000 ALTER TABLE `cat_des_dia_cre` DISABLE KEYS */;
/*!40000 ALTER TABLE `cat_des_dia_cre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `centro_costos`
--

DROP TABLE IF EXISTS `centro_costos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `centro_costos` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(5) NOT NULL,
  `centro_costo` longtext NOT NULL,
  `oficina_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `centro_costos_oficina_id_codigo_93aeb005_uniq` (`oficina_id`,`codigo`),
  CONSTRAINT `centro_costos_oficina_id_a8f34bb1_fk_oficinas_id` FOREIGN KEY (`oficina_id`) REFERENCES `oficinas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `centro_costos`
--

LOCK TABLES `centro_costos` WRITE;
/*!40000 ALTER TABLE `centro_costos` DISABLE KEYS */;
/*!40000 ALTER TABLE `centro_costos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cierre_mes`
--

DROP TABLE IF EXISTS `cierre_mes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cierre_mes` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fecha` date DEFAULT NULL,
  `protegido` varchar(1) NOT NULL,
  `tot_deb` double DEFAULT NULL,
  `tot_cre` double DEFAULT NULL,
  `fec_cie` datetime(6) DEFAULT NULL,
  `usuario` varchar(16) NOT NULL,
  `oficina_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cierre_mes_oficina_id_fecha_05d8659c_uniq` (`oficina_id`,`fecha`),
  CONSTRAINT `cierre_mes_oficina_id_0cc19944_fk_oficinas_id` FOREIGN KEY (`oficina_id`) REFERENCES `oficinas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cierre_mes`
--

LOCK TABLES `cierre_mes` WRITE;
/*!40000 ALTER TABLE `cierre_mes` DISABLE KEYS */;
/*!40000 ALTER TABLE `cierre_mes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `clientes` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(1) NOT NULL,
  `doc_ide` varchar(12) NOT NULL,
  `dv` varchar(1) DEFAULT NULL,
  `sigla` varchar(36) NOT NULL,
  `nombre` varchar(120) NOT NULL,
  `clase_coop` varchar(8) NOT NULL,
  `direccion` varchar(128) DEFAULT NULL,
  `telefono` varchar(12) DEFAULT NULL,
  `celular` varchar(10) DEFAULT NULL,
  `ciudad` varchar(32) DEFAULT NULL,
  `email` varchar(254) NOT NULL,
  `dominio` varchar(200) NOT NULL,
  `nit_ger` varchar(10) DEFAULT NULL,
  `nom_ger` varchar(100) DEFAULT NULL,
  `nit_con` varchar(10) DEFAULT NULL,
  `nom_con` varchar(100) DEFAULT NULL,
  `tp_con` varchar(16) DEFAULT NULL,
  `nit_rev_fis` varchar(10) DEFAULT NULL,
  `nom_rev_fis` varchar(100) DEFAULT NULL,
  `tp_rev_fis` varchar(16) DEFAULT NULL,
  `age_ret` varchar(1) NOT NULL,
  `ret_iva` varchar(1) NOT NULL,
  `aut_ret` varchar(1) NOT NULL,
  `logo` varchar(254) DEFAULT NULL,
  `num_lic` varchar(8) NOT NULL,
  `lic_act` varchar(1) NOT NULL,
  `ini_lic` date NOT NULL,
  `fin_lic` date NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `clientes_codigo_2488c54d_uniq` (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `codeudores`
--

DROP TABLE IF EXISTS `codeudores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `codeudores` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `credito_id` bigint(20) NOT NULL,
  `oficina_id` bigint(20) NOT NULL,
  `tercero_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `codeudores_oficina_id_credito_id_tercero_id_26cae9fc_uniq` (`oficina_id`,`credito_id`,`tercero_id`),
  KEY `codeudores_credito_id_845096a3_fk_creditos_id` (`credito_id`),
  KEY `codeudores_tercero_id_92710901_fk_terceros_id` (`tercero_id`),
  CONSTRAINT `codeudores_credito_id_845096a3_fk_creditos_id` FOREIGN KEY (`credito_id`) REFERENCES `creditos` (`id`),
  CONSTRAINT `codeudores_oficina_id_b4575af0_fk_oficinas_id` FOREIGN KEY (`oficina_id`) REFERENCES `oficinas` (`id`),
  CONSTRAINT `codeudores_tercero_id_92710901_fk_terceros_id` FOREIGN KEY (`tercero_id`) REFERENCES `terceros` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `codeudores`
--

LOCK TABLES `codeudores` WRITE;
/*!40000 ALTER TABLE `codeudores` DISABLE KEYS */;
/*!40000 ALTER TABLE `codeudores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `conceptos`
--

DROP TABLE IF EXISTS `conceptos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `conceptos` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cod_con` varchar(8) NOT NULL,
  `con_justo` varchar(1) NOT NULL,
  `descripcion` varchar(44) NOT NULL,
  `tip_dev_ap` varchar(1) NOT NULL,
  `tip_con` varchar(1) NOT NULL,
  `tip_sis` varchar(1) NOT NULL,
  `cta_con` varchar(10) NOT NULL,
  `cta_con_pas` varchar(10) NOT NULL,
  `debito` varchar(1) NOT NULL,
  `credito` varchar(1) NOT NULL,
  `por_tercero` varchar(1) NOT NULL,
  `por_ret_fue` double DEFAULT NULL,
  `cliente_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `conceptos_cliente_id_cod_con_45709994_uniq` (`cliente_id`,`cod_con`),
  CONSTRAINT `conceptos_cliente_id_677184f4_fk_clientes_id` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conceptos`
--

LOCK TABLES `conceptos` WRITE;
/*!40000 ALTER TABLE `conceptos` DISABLE KEYS */;
/*!40000 ALTER TABLE `conceptos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `creditos`
--

DROP TABLE IF EXISTS `creditos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `creditos` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cod_cre` varchar(10) DEFAULT NULL,
  `libranza` varchar(10) DEFAULT NULL,
  `pagare` varchar(16) DEFAULT NULL,
  `termino` varchar(1) NOT NULL,
  `for_pag` varchar(1) NOT NULL,
  `tip_gar` varchar(2) NOT NULL,
  `cap_ini` double DEFAULT NULL,
  `fec_des` date DEFAULT NULL,
  `fec_pag_ini` date DEFAULT NULL,
  `fec_ree` date DEFAULT NULL,
  `fec_ven` date DEFAULT NULL,
  `fec_ult_pag` date DEFAULT NULL,
  `val_cuo_ini` double DEFAULT NULL,
  `val_cuo_act` double DEFAULT NULL,
  `num_cuo_ini` int(11) DEFAULT NULL,
  `num_cuo_act` int(11) DEFAULT NULL,
  `num_cuo_gra` int(11) DEFAULT NULL,
  `per_ano` int(11) DEFAULT NULL,
  `tian_ic_ini` double DEFAULT NULL,
  `tian_ic_act` double DEFAULT NULL,
  `tian_im` double DEFAULT NULL,
  `tian_pol_seg` double DEFAULT NULL,
  `por_des_pro_pag` double DEFAULT NULL,
  `decreciente` varchar(1) NOT NULL,
  `estado` varchar(1) NOT NULL,
  `est_jur` varchar(1) NOT NULL,
  `cat_nue` varchar(1) NOT NULL,
  `rep_cen_rie` varchar(1) NOT NULL,
  `val_gar_hip` double DEFAULT NULL,
  `mat_inm_gar` varchar(12) DEFAULT NULL,
  `num_pol_gar_hip` varchar(16) DEFAULT NULL,
  `figarantias` varchar(1) NOT NULL,
  `cod_lin_cre_id` bigint(20) DEFAULT NULL,
  `com_des_id` bigint(20) DEFAULT NULL,
  `imputacion_id` bigint(20) DEFAULT NULL,
  `oficina_id` bigint(20) NOT NULL,
  `socio_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `creditos_oficina_id_cod_cre_b9120ad4_uniq` (`oficina_id`,`cod_cre`),
  KEY `creditos_cod_lin_cre_id_026f7da2_fk_lineas_credito_id` (`cod_lin_cre_id`),
  KEY `creditos_com_des_id_d9a5de2c_fk_detalle_prod_id` (`com_des_id`),
  KEY `creditos_imputacion_id_5769b745_fk_imp_con_cre_id` (`imputacion_id`),
  KEY `creditos_socio_id_96f7d74d_fk_asociados_id` (`socio_id`),
  CONSTRAINT `creditos_cod_lin_cre_id_026f7da2_fk_lineas_credito_id` FOREIGN KEY (`cod_lin_cre_id`) REFERENCES `lineas_credito` (`id`),
  CONSTRAINT `creditos_com_des_id_d9a5de2c_fk_detalle_prod_id` FOREIGN KEY (`com_des_id`) REFERENCES `detalle_prod` (`id`),
  CONSTRAINT `creditos_imputacion_id_5769b745_fk_imp_con_cre_id` FOREIGN KEY (`imputacion_id`) REFERENCES `imp_con_cre` (`id`),
  CONSTRAINT `creditos_oficina_id_8735d2ed_fk_oficinas_id` FOREIGN KEY (`oficina_id`) REFERENCES `oficinas` (`id`),
  CONSTRAINT `creditos_socio_id_96f7d74d_fk_asociados_id` FOREIGN KEY (`socio_id`) REFERENCES `asociados` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `creditos`
--

LOCK TABLES `creditos` WRITE;
/*!40000 ALTER TABLE `creditos` DISABLE KEYS */;
/*!40000 ALTER TABLE `creditos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `creditos_causa`
--

DROP TABLE IF EXISTS `creditos_causa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `creditos_causa` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cod_cre` varchar(10) DEFAULT NULL,
  `cuota` int(11) NOT NULL,
  `fecha` date DEFAULT NULL,
  `capital` double DEFAULT NULL,
  `int_cor` double DEFAULT NULL,
  `comprobante_id` bigint(20) DEFAULT NULL,
  `oficina_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `creditos_causa_oficina_id_cod_cre_compr_01aba2ea_uniq` (`oficina_id`,`cod_cre`,`comprobante_id`,`cuota`),
  KEY `creditos_causa_comprobante_id_9dfab115_fk_detalle_prod_id` (`comprobante_id`),
  CONSTRAINT `creditos_causa_comprobante_id_9dfab115_fk_detalle_prod_id` FOREIGN KEY (`comprobante_id`) REFERENCES `detalle_prod` (`id`),
  CONSTRAINT `creditos_causa_oficina_id_1f874be4_fk_oficinas_id` FOREIGN KEY (`oficina_id`) REFERENCES `oficinas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `creditos_causa`
--

LOCK TABLES `creditos_causa` WRITE;
/*!40000 ALTER TABLE `creditos_causa` DISABLE KEYS */;
/*!40000 ALTER TABLE `creditos_causa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cta_aho_est_his`
--

DROP TABLE IF EXISTS `cta_aho_est_his`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cta_aho_est_his` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fecha` date DEFAULT NULL,
  `est_cta_ant` varchar(1) NOT NULL,
  `cta_aho_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cta_aho_est_his_cta_aho_id_fecha_a571e139_uniq` (`cta_aho_id`,`fecha`),
  CONSTRAINT `cta_aho_est_his_cta_aho_id_69d3b9a2_fk_ctas_ahorro_id` FOREIGN KEY (`cta_aho_id`) REFERENCES `ctas_ahorro` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cta_aho_est_his`
--

LOCK TABLES `cta_aho_est_his` WRITE;
/*!40000 ALTER TABLE `cta_aho_est_his` DISABLE KEYS */;
/*!40000 ALTER TABLE `cta_aho_est_his` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cta_cdat`
--

DROP TABLE IF EXISTS `cta_cdat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cta_cdat` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `ampliacion` int(11) NOT NULL,
  `valor` double DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `plazo_mes` int(11) DEFAULT NULL,
  `tiae` double DEFAULT NULL,
  `Periodicidad` int(11) DEFAULT NULL,
  `cta_int_ret` varchar(10) DEFAULT NULL,
  `aplicado` varchar(1) NOT NULL,
  `cta_aho_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cta_cdat_cta_aho_id_ampliacion_ebfe2acf_uniq` (`cta_aho_id`,`ampliacion`),
  CONSTRAINT `cta_cdat_cta_aho_id_a43a8864_fk_ctas_ahorro_id` FOREIGN KEY (`cta_aho_id`) REFERENCES `ctas_ahorro` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cta_cdat`
--

LOCK TABLES `cta_cdat` WRITE;
/*!40000 ALTER TABLE `cta_cdat` DISABLE KEYS */;
/*!40000 ALTER TABLE `cta_cdat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cta_cdat_amp`
--

DROP TABLE IF EXISTS `cta_cdat_amp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cta_cdat_amp` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fecha` date DEFAULT NULL,
  `num_liq` int(11) DEFAULT NULL,
  `valor` double DEFAULT NULL,
  `cta_aho_afe` varchar(10) DEFAULT NULL,
  `clase` varchar(1) NOT NULL,
  `documento` varchar(10) DEFAULT NULL,
  `aplicado` varchar(1) NOT NULL,
  `cta_aho_id` bigint(20) NOT NULL,
  `cta_amp_id` bigint(20) NOT NULL,
  `docto_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cta_cdat_amp_cta_aho_id_cta_amp_id_fecha_a4074715_uniq` (`cta_aho_id`,`cta_amp_id`,`fecha`),
  KEY `cta_cdat_amp_cta_amp_id_982f548b_fk_cta_cdat_id` (`cta_amp_id`),
  KEY `cta_cdat_amp_docto_id_34d223cd_fk_hecho_econo_id` (`docto_id`),
  CONSTRAINT `cta_cdat_amp_cta_aho_id_e2006d93_fk_ctas_ahorro_id` FOREIGN KEY (`cta_aho_id`) REFERENCES `ctas_ahorro` (`id`),
  CONSTRAINT `cta_cdat_amp_cta_amp_id_982f548b_fk_cta_cdat_id` FOREIGN KEY (`cta_amp_id`) REFERENCES `cta_cdat` (`id`),
  CONSTRAINT `cta_cdat_amp_docto_id_34d223cd_fk_hecho_econo_id` FOREIGN KEY (`docto_id`) REFERENCES `hecho_econo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cta_cdat_amp`
--

LOCK TABLES `cta_cdat_amp` WRITE;
/*!40000 ALTER TABLE `cta_cdat_amp` DISABLE KEYS */;
/*!40000 ALTER TABLE `cta_cdat_amp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cta_cdat_liq`
--

DROP TABLE IF EXISTS `cta_cdat_liq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cta_cdat_liq` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fecha` date DEFAULT NULL,
  `tip_liq` varchar(1) NOT NULL,
  `val_int` double DEFAULT NULL,
  `val_ret` double DEFAULT NULL,
  `val_ret_nue` double DEFAULT NULL,
  `aplicado` varchar(1) NOT NULL,
  `cta_aho_id` bigint(20) NOT NULL,
  `cta_amp_id` bigint(20) NOT NULL,
  `docto_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cta_cdat_liq_cta_aho_id_cta_amp_id_fecha_tip_liq_a45ec347_uniq` (`cta_aho_id`,`cta_amp_id`,`fecha`,`tip_liq`),
  KEY `cta_cdat_liq_cta_amp_id_bdad1f65_fk_cta_cdat_amp_id` (`cta_amp_id`),
  KEY `cta_cdat_liq_docto_id_057b04fb_fk_hecho_econo_id` (`docto_id`),
  CONSTRAINT `cta_cdat_liq_cta_aho_id_c056a2d4_fk_ctas_ahorro_id` FOREIGN KEY (`cta_aho_id`) REFERENCES `ctas_ahorro` (`id`),
  CONSTRAINT `cta_cdat_liq_cta_amp_id_bdad1f65_fk_cta_cdat_amp_id` FOREIGN KEY (`cta_amp_id`) REFERENCES `cta_cdat_amp` (`id`),
  CONSTRAINT `cta_cdat_liq_docto_id_057b04fb_fk_hecho_econo_id` FOREIGN KEY (`docto_id`) REFERENCES `hecho_econo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cta_cdat_liq`
--

LOCK TABLES `cta_cdat_liq` WRITE;
/*!40000 ALTER TABLE `cta_cdat_liq` DISABLE KEYS */;
/*!40000 ALTER TABLE `cta_cdat_liq` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ctas_ahorro`
--

DROP TABLE IF EXISTS `ctas_ahorro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ctas_ahorro` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `num_cta` varchar(10) DEFAULT NULL,
  `est_cta` varchar(1) NOT NULL,
  `fec_apertura` date DEFAULT NULL,
  `fec_cancela` date DEFAULT NULL,
  `exc_tas_mil` varchar(1) NOT NULL,
  `fec_ini_exc` date DEFAULT NULL,
  `asociado_id` bigint(20) NOT NULL,
  `lin_aho_id` bigint(20) NOT NULL,
  `oficina_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ctas_ahorro_oficina_id_num_cta_35981a38_uniq` (`oficina_id`,`num_cta`),
  KEY `ctas_ahorro_asociado_id_cac2cc15_fk_asociados_id` (`asociado_id`),
  KEY `ctas_ahorro_lin_aho_id_4841d086_fk_lineas_ahorro_id` (`lin_aho_id`),
  CONSTRAINT `ctas_ahorro_asociado_id_cac2cc15_fk_asociados_id` FOREIGN KEY (`asociado_id`) REFERENCES `asociados` (`id`),
  CONSTRAINT `ctas_ahorro_lin_aho_id_4841d086_fk_lineas_ahorro_id` FOREIGN KEY (`lin_aho_id`) REFERENCES `lineas_ahorro` (`id`),
  CONSTRAINT `ctas_ahorro_oficina_id_c6601d86_fk_oficinas_id` FOREIGN KEY (`oficina_id`) REFERENCES `oficinas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ctas_ahorro`
--

LOCK TABLES `ctas_ahorro` WRITE;
/*!40000 ALTER TABLE `ctas_ahorro` DISABLE KEYS */;
/*!40000 ALTER TABLE `ctas_ahorro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `destino_cre`
--

DROP TABLE IF EXISTS `destino_cre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `destino_cre` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `codigo` int(11) NOT NULL,
  `descripcion` varchar(50) DEFAULT NULL,
  `cliente_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `destino_cre_cliente_id_codigo_b562c7c5_uniq` (`cliente_id`,`codigo`),
  CONSTRAINT `destino_cre_cliente_id_d38384cc_fk_clientes_id` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `destino_cre`
--

LOCK TABLES `destino_cre` WRITE;
/*!40000 ALTER TABLE `destino_cre` DISABLE KEYS */;
/*!40000 ALTER TABLE `destino_cre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_econo`
--

DROP TABLE IF EXISTS `detalle_econo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `detalle_econo` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `item_concepto` varchar(6) DEFAULT NULL,
  `detalle` longtext DEFAULT NULL,
  `debito` double DEFAULT NULL,
  `credito` double DEFAULT NULL,
  `valor_1` double DEFAULT NULL,
  `valor_2` double DEFAULT NULL,
  `id_ds` bigint(20) DEFAULT NULL,
  `cuenta_id` bigint(20) NOT NULL,
  `detalle_prod_id` bigint(20) DEFAULT NULL,
  `hecho_econo_id` bigint(20) NOT NULL,
  `tercero_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `detalle_econo_cuenta_id_e633eb1e_fk_plan_ctas_id` (`cuenta_id`),
  KEY `detalle_econo_detalle_prod_id_a14728b6_fk_detalle_prod_id` (`detalle_prod_id`),
  KEY `detalle_econo_tercero_id_7ca1d7ec_fk_terceros_id` (`tercero_id`),
  KEY `detalle_eco_hecho_e_534ad7_idx` (`hecho_econo_id`,`cuenta_id`,`tercero_id`,`detalle_prod_id`),
  CONSTRAINT `detalle_econo_cuenta_id_e633eb1e_fk_plan_ctas_id` FOREIGN KEY (`cuenta_id`) REFERENCES `plan_ctas` (`id`),
  CONSTRAINT `detalle_econo_detalle_prod_id_a14728b6_fk_detalle_prod_id` FOREIGN KEY (`detalle_prod_id`) REFERENCES `detalle_prod` (`id`),
  CONSTRAINT `detalle_econo_hecho_econo_id_40cee328_fk_hecho_econo_id` FOREIGN KEY (`hecho_econo_id`) REFERENCES `hecho_econo` (`id`),
  CONSTRAINT `detalle_econo_tercero_id_7ca1d7ec_fk_terceros_id` FOREIGN KEY (`tercero_id`) REFERENCES `terceros` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_econo`
--

LOCK TABLES `detalle_econo` WRITE;
/*!40000 ALTER TABLE `detalle_econo` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_econo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_prod`
--

DROP TABLE IF EXISTS `detalle_prod`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `detalle_prod` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `producto` varchar(2) NOT NULL,
  `subcuenta` varchar(12) DEFAULT NULL,
  `concepto` varchar(8) DEFAULT NULL,
  `valor` double DEFAULT NULL,
  `usuario` varchar(12) DEFAULT NULL,
  `fecha_creacion` datetime(6) NOT NULL,
  `fecha_actualizacion` datetime(6) NOT NULL,
  `centro_costo_id` bigint(20) DEFAULT NULL,
  `hecho_econo_id` bigint(20) NOT NULL,
  `oficina_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `detalle_prod_hecho_econo_id_producto__8ad7a390_uniq` (`hecho_econo_id`,`producto`,`subcuenta`,`concepto`),
  KEY `detalle_prod_centro_costo_id_a3fb0dcb_fk_centro_costos_id` (`centro_costo_id`),
  KEY `detalle_pro_oficina_9a63d9_idx` (`oficina_id`,`producto`,`subcuenta`),
  CONSTRAINT `detalle_prod_centro_costo_id_a3fb0dcb_fk_centro_costos_id` FOREIGN KEY (`centro_costo_id`) REFERENCES `centro_costos` (`id`),
  CONSTRAINT `detalle_prod_hecho_econo_id_a21f864a_fk_hecho_econo_id` FOREIGN KEY (`hecho_econo_id`) REFERENCES `hecho_econo` (`id`),
  CONSTRAINT `detalle_prod_oficina_id_df1f1463_fk_oficinas_id` FOREIGN KEY (`oficina_id`) REFERENCES `oficinas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_prod`
--

LOCK TABLES `detalle_prod` WRITE;
/*!40000 ALTER TABLE `detalle_prod` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_prod` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES
(2,'admin','logentry'),
(1,'admin_interface','theme'),
(8,'ampliacion_cdat_app','cta_cdat_amp'),
(9,'aportes_app','plan_aportes'),
(12,'asociados_app','aso_benef'),
(11,'asociados_app','aso_referencias'),
(10,'asociados_app','asociados'),
(4,'auth','group'),
(3,'auth','permission'),
(5,'auth','user'),
(13,'backup_bd','backup'),
(14,'cambios_creditos_app','cambios_cre'),
(15,'categorias_creditos_app','cat_des_dia_cre'),
(16,'causacion_creditos_app','creditos_causa'),
(17,'cdat_app','cta_cdat'),
(18,'centrocostos_app','centrocostos'),
(19,'cierre_mensual_app','cierre_mes'),
(20,'clientes_app','clientes'),
(21,'conceptos_app','conceptos'),
(22,'contabilizacion_capital_creditos_app','imp_con_cre'),
(23,'contabilizacion_intereses_creditos_app','imp_con_cre_int'),
(24,'contabilizacion_lineas_ahorros_app','imp_con_lin_aho'),
(6,'contenttypes','contenttype'),
(26,'creditos_app','codeudores'),
(25,'creditos_app','creditos'),
(27,'ctas_ahorros_app','ctas_ahorro'),
(28,'cuentas_app','plan_ctas'),
(29,'destino_credito_app','destino_cre'),
(30,'detalle_economico_app','detalle_econo'),
(31,'detalle_producto_app','detalle_prod'),
(32,'documentos_app','docto_conta'),
(33,'documentos_app','xdoc_zep'),
(34,'estados_financieros_app','estados_fin'),
(35,'hecho_economico_app','hecho_econo'),
(36,'historico_ctas_ahorros_app','cta_aho_est_his'),
(37,'lineas_ahorro_app','lineas_ahorro'),
(38,'lineas_credito_app','lineas_credito'),
(39,'liquidacion_cdat_app','cta_cdat_liq'),
(40,'localidades_app','localidades'),
(41,'movimiento_caja_app','mov_caja'),
(42,'oficinas_app','oficinas'),
(43,'originacion_app','originacion'),
(44,'pagadores_app','pagadores'),
(45,'retefuente_ahorros_app','ret_fue_aho'),
(7,'sessions','session'),
(46,'tasas_lin_aho_app','tas_lin_aho'),
(47,'terceros_app','terceros'),
(48,'usuarios_app','usuarios');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES
(1,'contenttypes','0001_initial','2024-05-15 21:03:22.209697'),
(2,'auth','0001_initial','2024-05-15 21:03:29.655645'),
(3,'admin','0001_initial','2024-05-15 21:03:31.317753'),
(4,'admin','0002_logentry_remove_auto_add','2024-05-15 21:03:31.489297'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-05-15 21:03:31.608380'),
(6,'admin_interface','0001_initial','2024-05-15 21:03:32.391959'),
(7,'admin_interface','0002_add_related_modal','2024-05-15 21:03:35.600504'),
(8,'admin_interface','0003_add_logo_color','2024-05-15 21:03:36.502994'),
(9,'admin_interface','0004_rename_title_color','2024-05-15 21:03:36.858244'),
(10,'admin_interface','0005_add_recent_actions_visible','2024-05-15 21:03:37.708577'),
(11,'admin_interface','0006_bytes_to_str','2024-05-15 21:03:37.932742'),
(12,'admin_interface','0007_add_favicon','2024-05-15 21:03:38.535197'),
(13,'admin_interface','0008_change_related_modal_background_opacity_type','2024-05-15 21:03:39.590070'),
(14,'admin_interface','0009_add_enviroment','2024-05-15 21:03:41.099567'),
(15,'admin_interface','0010_add_localization','2024-05-15 21:03:41.163671'),
(16,'admin_interface','0011_add_environment_options','2024-05-15 21:03:43.549905'),
(17,'admin_interface','0012_update_verbose_names','2024-05-15 21:03:43.585396'),
(18,'admin_interface','0013_add_related_modal_close_button','2024-05-15 21:03:44.416766'),
(19,'admin_interface','0014_name_unique','2024-05-15 21:03:44.774754'),
(20,'admin_interface','0015_add_language_chooser_active','2024-05-15 21:03:45.449817'),
(21,'admin_interface','0016_add_language_chooser_display','2024-05-15 21:03:46.099422'),
(22,'admin_interface','0017_change_list_filter_dropdown','2024-05-15 21:03:46.126968'),
(23,'admin_interface','0018_theme_list_filter_sticky','2024-05-15 21:03:46.808159'),
(24,'admin_interface','0019_add_form_sticky','2024-05-15 21:03:48.016841'),
(25,'admin_interface','0020_module_selected_colors','2024-05-15 21:03:49.376337'),
(26,'admin_interface','0021_file_extension_validator','2024-05-15 21:03:49.411340'),
(27,'admin_interface','0022_add_logo_max_width_and_height','2024-05-15 21:03:50.658134'),
(28,'admin_interface','0023_theme_foldable_apps','2024-05-15 21:03:51.216606'),
(29,'admin_interface','0024_remove_theme_css','2024-05-15 21:03:51.549764'),
(30,'admin_interface','0025_theme_language_chooser_control','2024-05-15 21:03:52.224460'),
(31,'admin_interface','0026_theme_list_filter_highlight','2024-05-15 21:03:52.841849'),
(32,'admin_interface','0027_theme_list_filter_removal_links','2024-05-15 21:03:53.466449'),
(33,'admin_interface','0028_theme_show_fieldsets_as_tabs_and_more','2024-05-15 21:03:54.716716'),
(34,'admin_interface','0029_theme_css_generic_link_active_color','2024-05-15 21:03:55.491038'),
(35,'admin_interface','0030_theme_collapsible_stacked_inlines_and_more','2024-05-15 21:03:58.149794'),
(36,'clientes_app','0001_initial','2024-05-15 21:03:58.766085'),
(37,'localidades_app','0001_initial','2024-05-15 21:03:59.982299'),
(38,'oficinas_app','0001_initial','2024-05-15 21:04:01.966969'),
(39,'documentos_app','0001_initial','2024-05-15 21:04:03.599775'),
(40,'hecho_economico_app','0001_initial','2024-05-15 21:04:05.166198'),
(41,'lineas_ahorro_app','0001_initial','2024-05-15 21:04:06.383243'),
(42,'terceros_app','0001_initial','2024-05-15 21:04:08.866477'),
(43,'pagadores_app','0001_initial','2024-05-15 21:04:10.490660'),
(44,'asociados_app','0001_initial','2024-05-15 21:04:15.776107'),
(45,'ctas_ahorros_app','0001_initial','2024-05-15 21:04:17.891321'),
(46,'cdat_app','0001_initial','2024-05-15 21:04:19.124709'),
(47,'ampliacion_cdat_app','0001_initial','2024-05-15 21:04:21.207739'),
(48,'aportes_app','0001_initial','2024-05-15 21:04:22.274754'),
(49,'contenttypes','0002_remove_content_type_name','2024-05-15 21:04:23.141479'),
(50,'auth','0002_alter_permission_name_max_length','2024-05-15 21:04:23.749974'),
(51,'auth','0003_alter_user_email_max_length','2024-05-15 21:04:24.091716'),
(52,'auth','0004_alter_user_username_opts','2024-05-15 21:04:24.136776'),
(53,'auth','0005_alter_user_last_login_null','2024-05-15 21:04:24.641018'),
(54,'auth','0006_require_contenttypes_0002','2024-05-15 21:04:24.663556'),
(55,'auth','0007_alter_validators_add_error_messages','2024-05-15 21:04:24.706551'),
(56,'auth','0008_alter_user_username_max_length','2024-05-15 21:04:25.090966'),
(57,'auth','0009_alter_user_last_name_max_length','2024-05-15 21:04:25.407775'),
(58,'auth','0010_alter_group_name_max_length','2024-05-15 21:04:25.766329'),
(59,'auth','0011_update_proxy_permissions','2024-05-15 21:04:25.868405'),
(60,'auth','0012_alter_user_first_name_max_length','2024-05-15 21:04:26.358291'),
(61,'backup_bd','0001_initial','2024-05-15 21:04:27.065874'),
(62,'centrocostos_app','0001_initial','2024-05-15 21:04:28.173994'),
(63,'detalle_producto_app','0001_initial','2024-05-15 21:04:31.090854'),
(64,'cambios_creditos_app','0001_initial','2024-05-15 21:04:32.399010'),
(65,'categorias_creditos_app','0001_initial','2024-05-15 21:04:33.590545'),
(66,'causacion_creditos_app','0001_initial','2024-05-15 21:04:35.382581'),
(67,'cierre_mensual_app','0001_initial','2024-05-15 21:04:36.499193'),
(68,'conceptos_app','0001_initial','2024-05-15 21:04:37.766077'),
(69,'conceptos_app','0002_alter_conceptos_por_ret_fue','2024-05-15 21:04:38.790541'),
(70,'contabilizacion_capital_creditos_app','0001_initial','2024-05-15 21:04:39.990598'),
(71,'contabilizacion_intereses_creditos_app','0001_initial','2024-05-15 21:04:41.183591'),
(72,'contabilizacion_lineas_ahorros_app','0001_initial','2024-05-15 21:04:42.390943'),
(73,'lineas_credito_app','0001_initial','2024-05-15 21:04:43.817238'),
(74,'creditos_app','0001_initial','2024-05-15 21:04:49.392079'),
(75,'cuentas_app','0001_initial','2024-05-15 21:04:50.959421'),
(76,'destino_credito_app','0001_initial','2024-05-15 21:04:52.140896'),
(77,'detalle_economico_app','0001_initial','2024-05-15 21:04:54.965638'),
(78,'documentos_app','0002_xdoc_zep','2024-05-15 21:04:55.790598'),
(79,'estados_financieros_app','0001_initial','2024-05-15 21:04:57.474303'),
(80,'hecho_economico_app','0002_alter_hecho_econo_anulado_alter_hecho_econo_canal_and_more','2024-05-15 21:04:57.589879'),
(81,'historico_ctas_ahorros_app','0001_initial','2024-05-15 21:04:59.024754'),
(82,'liquidacion_cdat_app','0001_initial','2024-05-15 21:05:01.743715'),
(83,'movimiento_caja_app','0001_initial','2024-05-15 21:05:03.382685'),
(84,'originacion_app','0001_initial','2024-05-15 21:05:04.891056'),
(85,'retefuente_ahorros_app','0001_initial','2024-05-15 21:05:06.382269'),
(86,'sessions','0001_initial','2024-05-15 21:05:06.997804'),
(87,'tasas_lin_aho_app','0001_initial','2024-05-15 21:05:08.307124'),
(88,'usuarios_app','0001_initial','2024-05-15 21:05:09.550403');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `docto_conta`
--

DROP TABLE IF EXISTS `docto_conta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `docto_conta` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `per_con` int(11) DEFAULT NULL,
  `codigo` int(11) NOT NULL,
  `nom_cto` varchar(12) NOT NULL,
  `nombre` varchar(44) NOT NULL,
  `doc_admin` varchar(1) DEFAULT NULL,
  `doc_caja` varchar(1) DEFAULT NULL,
  `inicio_nuevo_per` varchar(1) NOT NULL,
  `consecutivo` int(11) DEFAULT NULL,
  `id_ds` bigint(20) DEFAULT NULL,
  `oficina_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `docto_conta_oficina_id_per_con_codigo_933a642d_uniq` (`oficina_id`,`per_con`,`codigo`),
  KEY `docto_conta_id_ds_440a2920` (`id_ds`),
  CONSTRAINT `docto_conta_oficina_id_8998d390_fk_oficinas_id` FOREIGN KEY (`oficina_id`) REFERENCES `oficinas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `docto_conta`
--

LOCK TABLES `docto_conta` WRITE;
/*!40000 ALTER TABLE `docto_conta` DISABLE KEYS */;
/*!40000 ALTER TABLE `docto_conta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estados_fin`
--

DROP TABLE IF EXISTS `estados_fin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `estados_fin` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fec_inf` date DEFAULT NULL,
  `ing_sal_fij` double DEFAULT NULL,
  `ing_hon` double DEFAULT NULL,
  `ing_pen` double DEFAULT NULL,
  `ing_arr` double DEFAULT NULL,
  `ing_com` double DEFAULT NULL,
  `ing_ext` double DEFAULT NULL,
  `ing_otr` varchar(1) DEFAULT NULL,
  `ing_tot` double DEFAULT NULL,
  `egr_sec_fin` double DEFAULT NULL,
  `egr_cuo_hip` double DEFAULT NULL,
  `egr_des_nom` varchar(1) DEFAULT NULL,
  `egr_gas_fam` double DEFAULT NULL,
  `egr_otr_cre` double DEFAULT NULL,
  `egr_arr` double DEFAULT NULL,
  `egr_otr_gas` double DEFAULT NULL,
  `egr_tot` double DEFAULT NULL,
  `act_otr_egr` double DEFAULT NULL,
  `act_tip_bien` varchar(20) DEFAULT NULL,
  `act_vei` double DEFAULT NULL,
  `act_otr` varchar(1) DEFAULT NULL,
  `tot_act` double DEFAULT NULL,
  `act_fin_rai` double DEFAULT NULL,
  `act_inv` double DEFAULT NULL,
  `escritura` varchar(20) DEFAULT NULL,
  `pas_otr` varchar(1) DEFAULT NULL,
  `pas_tip` varchar(24) DEFAULT NULL,
  `tot_pat` double DEFAULT NULL,
  `pas_val` double DEFAULT NULL,
  `tot_pas` double DEFAULT NULL,
  `pas_des` varchar(40) DEFAULT NULL,
  `dec_ren` varchar(1) NOT NULL,
  `tip_pas` varchar(40) DEFAULT NULL,
  `des_pas` varchar(40) DEFAULT NULL,
  `val_pas` double DEFAULT NULL,
  `ope_mon_ext` varchar(1) NOT NULL,
  `nom_ban_ext` varchar(40) DEFAULT NULL,
  `ope_pais_ext` varchar(1) NOT NULL,
  `ope_monto_ext` varchar(1) NOT NULL,
  `num_cta_ext` varchar(20) DEFAULT NULL,
  `tip_ope_ext` varchar(20) DEFAULT NULL,
  `mon_ope_ext` varchar(1) NOT NULL,
  `prod_mon_ext` varchar(1) NOT NULL,
  `des_prod_ext` varchar(40) DEFAULT NULL,
  `mon_prod_ext` varchar(20) DEFAULT NULL,
  `pais_prod_ext` varchar(20) DEFAULT NULL,
  `ciu_prod_ext` varchar(20) DEFAULT NULL,
  `prom_prod_ext` double DEFAULT NULL,
  `cliente_id` bigint(20) NOT NULL,
  `tercero_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `estados_fin_cliente_id_tercero_id_fec_inf_c0f42941_uniq` (`cliente_id`,`tercero_id`,`fec_inf`),
  KEY `estados_fin_tercero_id_23e9036c_fk_terceros_id` (`tercero_id`),
  CONSTRAINT `estados_fin_cliente_id_dc3a9784_fk_clientes_id` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id`),
  CONSTRAINT `estados_fin_tercero_id_23e9036c_fk_terceros_id` FOREIGN KEY (`tercero_id`) REFERENCES `terceros` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estados_fin`
--

LOCK TABLES `estados_fin` WRITE;
/*!40000 ALTER TABLE `estados_fin` DISABLE KEYS */;
/*!40000 ALTER TABLE `estados_fin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hecho_econo`
--

DROP TABLE IF EXISTS `hecho_econo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hecho_econo` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `numero` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `descripcion` varchar(64) DEFAULT NULL,
  `anulado` varchar(1) NOT NULL,
  `protegido` varchar(1) NOT NULL,
  `fecha_prot` datetime(6) NOT NULL,
  `usuario` varchar(16) DEFAULT NULL,
  `canal` varchar(3) NOT NULL,
  `id_ds` bigint(20) DEFAULT NULL,
  `docto_conta_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hecho_econo_docto_conta_id_numero_13c3e9fc_uniq` (`docto_conta_id`,`numero`),
  KEY `hecho_econo_id_ds_bdf079c2` (`id_ds`),
  CONSTRAINT `hecho_econo_docto_conta_id_d2f5d394_fk_docto_conta_id` FOREIGN KEY (`docto_conta_id`) REFERENCES `docto_conta` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hecho_econo`
--

LOCK TABLES `hecho_econo` WRITE;
/*!40000 ALTER TABLE `hecho_econo` DISABLE KEYS */;
/*!40000 ALTER TABLE `hecho_econo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `imp_con_cre`
--

DROP TABLE IF EXISTS `imp_con_cre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `imp_con_cre` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cod_imp` varchar(2) DEFAULT NULL,
  `descripcion` varchar(40) DEFAULT NULL,
  `kpte_cap` varchar(10) DEFAULT NULL,
  `kdet_gen_adi` varchar(10) DEFAULT NULL,
  `kdet_gen` varchar(10) DEFAULT NULL,
  `kdet_gen_gas` varchar(10) DEFAULT NULL,
  `kdet_gen_rec` varchar(10) DEFAULT NULL,
  `kdet_ind_gas` varchar(10) DEFAULT NULL,
  `kdet_ind_rec` varchar(10) DEFAULT NULL,
  `kdpp_ic` varchar(10) DEFAULT NULL,
  `kpte_ic` varchar(10) DEFAULT NULL,
  `cta_val` varchar(10) DEFAULT NULL,
  `kcta_ingreso` varchar(10) DEFAULT NULL,
  `kic_orden_i` varchar(10) DEFAULT NULL,
  `cliente_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `imp_con_cre_cliente_id_cod_imp_6a5aff0f_uniq` (`cliente_id`,`cod_imp`),
  CONSTRAINT `imp_con_cre_cliente_id_f12bb555_fk_clientes_id` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `imp_con_cre`
--

LOCK TABLES `imp_con_cre` WRITE;
/*!40000 ALTER TABLE `imp_con_cre` DISABLE KEYS */;
/*!40000 ALTER TABLE `imp_con_cre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `imp_con_cre_int`
--

DROP TABLE IF EXISTS `imp_con_cre_int`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `imp_con_cre_int` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cod_imp` varchar(2) DEFAULT NULL,
  `categoria` varchar(1) NOT NULL,
  `kcta_con` varchar(10) DEFAULT NULL,
  `kcta_pro_ind` varchar(10) DEFAULT NULL,
  `kporcentaje` double DEFAULT NULL,
  `cta_int` varchar(10) DEFAULT NULL,
  `cta_ord_int` varchar(10) DEFAULT NULL,
  `cliente_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `imp_con_cre_int_cliente_id_cod_imp_categoria_bf1938bf_uniq` (`cliente_id`,`cod_imp`,`categoria`),
  CONSTRAINT `imp_con_cre_int_cliente_id_377a7b14_fk_clientes_id` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `imp_con_cre_int`
--

LOCK TABLES `imp_con_cre_int` WRITE;
/*!40000 ALTER TABLE `imp_con_cre_int` DISABLE KEYS */;
/*!40000 ALTER TABLE `imp_con_cre_int` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `imp_con_lin_aho`
--

DROP TABLE IF EXISTS `imp_con_lin_aho`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `imp_con_lin_aho` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cod_imp` varchar(2) DEFAULT NULL,
  `descripcion` varchar(40) DEFAULT NULL,
  `ctaafeact` varchar(10) DEFAULT NULL,
  `ctaafeina` varchar(10) DEFAULT NULL,
  `ctaafeint` varchar(10) DEFAULT NULL,
  `ctaretfue` varchar(10) DEFAULT NULL,
  `linea_ahorro_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `imp_con_lin_aho_linea_ahorro_id_cod_imp_9aa67cd0_uniq` (`linea_ahorro_id`,`cod_imp`),
  CONSTRAINT `imp_con_lin_aho_linea_ahorro_id_45e35007_fk_lineas_ahorro_id` FOREIGN KEY (`linea_ahorro_id`) REFERENCES `lineas_ahorro` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `imp_con_lin_aho`
--

LOCK TABLES `imp_con_lin_aho` WRITE;
/*!40000 ALTER TABLE `imp_con_lin_aho` DISABLE KEYS */;
/*!40000 ALTER TABLE `imp_con_lin_aho` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lineas_ahorro`
--

DROP TABLE IF EXISTS `lineas_ahorro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lineas_ahorro` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cod_lin_aho` varchar(2) DEFAULT NULL,
  `nombre` varchar(30) DEFAULT NULL,
  `termino` varchar(1) NOT NULL,
  `per_liq_int` varchar(1) NOT NULL,
  `cta_por_pas` varchar(10) DEFAULT NULL,
  `fec_ult_liq_int` date DEFAULT NULL,
  `saldo_minimo` double DEFAULT NULL,
  `cliente_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `lineas_ahorro_cliente_id_cod_lin_aho_4a95e06c_uniq` (`cliente_id`,`cod_lin_aho`),
  CONSTRAINT `lineas_ahorro_cliente_id_a447e541_fk_clientes_id` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lineas_ahorro`
--

LOCK TABLES `lineas_ahorro` WRITE;
/*!40000 ALTER TABLE `lineas_ahorro` DISABLE KEYS */;
/*!40000 ALTER TABLE `lineas_ahorro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lineas_credito`
--

DROP TABLE IF EXISTS `lineas_credito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lineas_credito` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cod_lin_cre` int(11) NOT NULL,
  `descripcion` varchar(44) DEFAULT NULL,
  `tas_int_anu` double DEFAULT NULL,
  `tas_int_mor` double DEFAULT NULL,
  `por_pol` double DEFAULT NULL,
  `por_des_pp` double DEFAULT NULL,
  `dia_con_int_mor` int(11) DEFAULT NULL,
  `cliente_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `lineas_credito_cliente_id_cod_lin_cre_7aff1685_uniq` (`cliente_id`,`cod_lin_cre`),
  CONSTRAINT `lineas_credito_cliente_id_db569c63_fk_clientes_id` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lineas_credito`
--

LOCK TABLES `lineas_credito` WRITE;
/*!40000 ALTER TABLE `lineas_credito` DISABLE KEYS */;
/*!40000 ALTER TABLE `lineas_credito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `localidades`
--

DROP TABLE IF EXISTS `localidades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `localidades` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(8) NOT NULL,
  `nombre` varchar(36) NOT NULL,
  `cod_pos` varchar(12) DEFAULT NULL,
  `departamento` varchar(36) DEFAULT NULL,
  `cliente_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `localidades_cliente_id_codigo_4e0f3dfc_uniq` (`cliente_id`,`codigo`),
  CONSTRAINT `localidades_cliente_id_91adb0f5_fk_clientes_id` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `localidades`
--

LOCK TABLES `localidades` WRITE;
/*!40000 ALTER TABLE `localidades` DISABLE KEYS */;
/*!40000 ALTER TABLE `localidades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mov_caja`
--

DROP TABLE IF EXISTS `mov_caja`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mov_caja` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fecha` date DEFAULT NULL,
  `cod_caj` varchar(2) NOT NULL,
  `jornada` varchar(1) NOT NULL,
  `saldo_ini` double DEFAULT NULL,
  `debitos` double DEFAULT NULL,
  `creditos` double DEFAULT NULL,
  `val_che_dev` double DEFAULT NULL,
  `saldo_fin` double DEFAULT NULL,
  `diferencia` double DEFAULT NULL,
  `val_cheques` double DEFAULT NULL,
  `val_vales` double DEFAULT NULL,
  `cerrado` varchar(1) NOT NULL,
  `monedas` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`monedas`)),
  `oficina_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mov_caja_oficina_id_fecha_cod_caj_jornada_21847f57_uniq` (`oficina_id`,`fecha`,`cod_caj`,`jornada`),
  CONSTRAINT `mov_caja_oficina_id_fb7c071e_fk_oficinas_id` FOREIGN KEY (`oficina_id`) REFERENCES `oficinas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mov_caja`
--

LOCK TABLES `mov_caja` WRITE;
/*!40000 ALTER TABLE `mov_caja` DISABLE KEYS */;
/*!40000 ALTER TABLE `mov_caja` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oficinas`
--

DROP TABLE IF EXISTS `oficinas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oficinas` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(5) NOT NULL,
  `contabiliza` varchar(1) NOT NULL,
  `nombre_oficina` longtext NOT NULL,
  `responsable` longtext NOT NULL,
  `celular` varchar(10) DEFAULT NULL,
  `email` varchar(254) NOT NULL,
  `direccion` varchar(80) DEFAULT NULL,
  `ciudad_id` bigint(20) DEFAULT NULL,
  `cliente_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `oficinas_cliente_id_codigo_1ed09afc_uniq` (`cliente_id`,`codigo`),
  KEY `oficinas_ciudad_id_7ded3061_fk_localidades_id` (`ciudad_id`),
  CONSTRAINT `oficinas_ciudad_id_7ded3061_fk_localidades_id` FOREIGN KEY (`ciudad_id`) REFERENCES `localidades` (`id`),
  CONSTRAINT `oficinas_cliente_id_04a02d4d_fk_clientes_id` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oficinas`
--

LOCK TABLES `oficinas` WRITE;
/*!40000 ALTER TABLE `oficinas` DISABLE KEYS */;
/*!40000 ALTER TABLE `oficinas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `originacion`
--

DROP TABLE IF EXISTS `originacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `originacion` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `lin_cre` varchar(80) NOT NULL,
  `monto` double DEFAULT NULL,
  `plazo` int(11) DEFAULT NULL,
  `gar_cre_sol` varchar(1) NOT NULL,
  `lin_cre_sol` varchar(1) NOT NULL,
  `mod_cre_sol` varchar(1) NOT NULL,
  `asociado_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `originacion_asociado_id_caf78405_uniq` (`asociado_id`),
  CONSTRAINT `originacion_asociado_id_caf78405_fk_asociados_id` FOREIGN KEY (`asociado_id`) REFERENCES `asociados` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `originacion`
--

LOCK TABLES `originacion` WRITE;
/*!40000 ALTER TABLE `originacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `originacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pagadores`
--

DROP TABLE IF EXISTS `pagadores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pagadores` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(5) DEFAULT NULL,
  `nombre` varchar(40) NOT NULL,
  `pagador` varchar(72) DEFAULT NULL,
  `tel_cel` varchar(10) DEFAULT NULL,
  `ciudad_id` bigint(20) DEFAULT NULL,
  `cliente_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `pagadores_cliente_id_codigo_5ad72127_uniq` (`cliente_id`,`codigo`),
  KEY `pagadores_ciudad_id_18d84c42_fk_localidades_id` (`ciudad_id`),
  CONSTRAINT `pagadores_ciudad_id_18d84c42_fk_localidades_id` FOREIGN KEY (`ciudad_id`) REFERENCES `localidades` (`id`),
  CONSTRAINT `pagadores_cliente_id_60aee58a_fk_clientes_id` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagadores`
--

LOCK TABLES `pagadores` WRITE;
/*!40000 ALTER TABLE `pagadores` DISABLE KEYS */;
/*!40000 ALTER TABLE `pagadores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plan_aportes`
--

DROP TABLE IF EXISTS `plan_aportes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `plan_aportes` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `agno` int(11) DEFAULT NULL,
  `meses` int(11) DEFAULT NULL,
  `iniadu` double DEFAULT NULL,
  `totadu` double DEFAULT NULL,
  `inichi1` double DEFAULT NULL,
  `totchi1` double DEFAULT NULL,
  `inichi2` double DEFAULT NULL,
  `totchi2` double DEFAULT NULL,
  `inijur` double DEFAULT NULL,
  `totjur` double DEFAULT NULL,
  `oficina_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `plan_aportes_oficina_id_agno_e98bee9a_uniq` (`oficina_id`,`agno`),
  CONSTRAINT `plan_aportes_oficina_id_1ceef028_fk_oficinas_id` FOREIGN KEY (`oficina_id`) REFERENCES `oficinas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plan_aportes`
--

LOCK TABLES `plan_aportes` WRITE;
/*!40000 ALTER TABLE `plan_aportes` DISABLE KEYS */;
/*!40000 ALTER TABLE `plan_aportes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plan_ctas`
--

DROP TABLE IF EXISTS `plan_ctas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `plan_ctas` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `per_con` int(11) DEFAULT NULL,
  `cod_cta` varchar(10) DEFAULT NULL,
  `nom_cta` varchar(64) DEFAULT NULL,
  `tip_cta` varchar(1) DEFAULT NULL,
  `dinamica` longtext NOT NULL,
  `naturaleza` varchar(1) NOT NULL,
  `activa` varchar(1) NOT NULL,
  `por_tercero` varchar(1) NOT NULL,
  `cta_act_fij` varchar(1) NOT NULL,
  `cta_pre` varchar(1) NOT NULL,
  `cta_bal` varchar(1) NOT NULL,
  `cta_res` varchar(1) NOT NULL,
  `cta_ord` varchar(1) NOT NULL,
  `cta_ban` varchar(1) NOT NULL,
  `cta_gan_per` varchar(1) NOT NULL,
  `cta_per_gan` varchar(1) NOT NULL,
  `cta_dep` varchar(1) NOT NULL,
  `cta_ing_ret` varchar(1) NOT NULL,
  `cta_ret_iva` varchar(1) NOT NULL,
  `cta_rec` varchar(1) NOT NULL,
  `id_ds` bigint(20) DEFAULT NULL,
  `cliente_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `plan_ctas_cliente_id_per_con_cod_cta_f24165f0_uniq` (`cliente_id`,`per_con`,`cod_cta`),
  KEY `plan_ctas_id_ds_64720be2` (`id_ds`),
  CONSTRAINT `plan_ctas_cliente_id_e341a598_fk_clientes_id` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plan_ctas`
--

LOCK TABLES `plan_ctas` WRITE;
/*!40000 ALTER TABLE `plan_ctas` DISABLE KEYS */;
/*!40000 ALTER TABLE `plan_ctas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ret_fue_aho`
--

DROP TABLE IF EXISTS `ret_fue_aho`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ret_fue_aho` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fecha_inicial` date DEFAULT NULL,
  `fecha_final` date DEFAULT NULL,
  `bas_liq_int` double DEFAULT NULL,
  `tas_liq_rf` double DEFAULT NULL,
  `lin_aho_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `RET_FUE_AHO_lin_aho_id_fecha_inicial_54ff9997_uniq` (`lin_aho_id`,`fecha_inicial`),
  CONSTRAINT `RET_FUE_AHO_lin_aho_id_a1a3df63_fk_lineas_ahorro_id` FOREIGN KEY (`lin_aho_id`) REFERENCES `lineas_ahorro` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ret_fue_aho`
--

LOCK TABLES `ret_fue_aho` WRITE;
/*!40000 ALTER TABLE `ret_fue_aho` DISABLE KEYS */;
/*!40000 ALTER TABLE `ret_fue_aho` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tas_lin_aho`
--

DROP TABLE IF EXISTS `tas_lin_aho`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tas_lin_aho` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fecha_inicial` date DEFAULT NULL,
  `fecha_final` date DEFAULT NULL,
  `tiae` double NOT NULL,
  `lin_aho_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tas_lin_aho_lin_aho_id_fecha_inicial_9d919388_uniq` (`lin_aho_id`,`fecha_inicial`),
  CONSTRAINT `tas_lin_aho_lin_aho_id_6eebff26_fk_lineas_ahorro_id` FOREIGN KEY (`lin_aho_id`) REFERENCES `lineas_ahorro` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tas_lin_aho`
--

LOCK TABLES `tas_lin_aho` WRITE;
/*!40000 ALTER TABLE `tas_lin_aho` DISABLE KEYS */;
/*!40000 ALTER TABLE `tas_lin_aho` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `terceros`
--

DROP TABLE IF EXISTS `terceros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `terceros` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cla_doc` varchar(1) NOT NULL,
  `doc_ide` varchar(12) NOT NULL,
  `dig_ver` varchar(1) NOT NULL,
  `nit_rap` varchar(12) NOT NULL,
  `regimen` varchar(12) NOT NULL,
  `fec_exp_ced` date DEFAULT NULL,
  `tip_ter` varchar(12) NOT NULL,
  `pri_ape` varchar(28) DEFAULT NULL,
  `seg_ape` varchar(28) NOT NULL,
  `pri_nom` varchar(28) DEFAULT NULL,
  `seg_nom` varchar(28) NOT NULL,
  `raz_soc` varchar(120) NOT NULL,
  `direccion` varchar(80) DEFAULT NULL,
  `cod_pos` varchar(8) DEFAULT NULL,
  `tel_ofi` varchar(10) DEFAULT NULL,
  `tel_res` varchar(10) DEFAULT NULL,
  `id_ds` bigint(20) DEFAULT NULL,
  `celular1` varchar(10) DEFAULT NULL,
  `celular2` varchar(10) DEFAULT NULL,
  `fax` varchar(10) DEFAULT NULL,
  `email` varchar(254) NOT NULL,
  `nombre` varchar(120) NOT NULL,
  `fec_act` date DEFAULT NULL,
  `observacion` varchar(255) NOT NULL,
  `per_pub_exp` varchar(1) NOT NULL,
  `nit_interno` varchar(1) NOT NULL,
  `cliente_id` bigint(20) NOT NULL,
  `cod_ciu_exp_id` bigint(20) DEFAULT NULL,
  `cod_ciu_res_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `terceros_cliente_id_cla_doc_doc_ide_28ea5f9a_uniq` (`cliente_id`,`cla_doc`,`doc_ide`),
  KEY `terceros_cod_ciu_exp_id_c385237b_fk_localidades_id` (`cod_ciu_exp_id`),
  KEY `terceros_cod_ciu_res_id_89ac61f6_fk_localidades_id` (`cod_ciu_res_id`),
  KEY `terceros_id_ds_05fe5933` (`id_ds`),
  CONSTRAINT `terceros_cliente_id_f854f5d1_fk_clientes_id` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id`),
  CONSTRAINT `terceros_cod_ciu_exp_id_c385237b_fk_localidades_id` FOREIGN KEY (`cod_ciu_exp_id`) REFERENCES `localidades` (`id`),
  CONSTRAINT `terceros_cod_ciu_res_id_89ac61f6_fk_localidades_id` FOREIGN KEY (`cod_ciu_res_id`) REFERENCES `localidades` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `terceros`
--

LOCK TABLES `terceros` WRITE;
/*!40000 ALTER TABLE `terceros` DISABLE KEYS */;
/*!40000 ALTER TABLE `terceros` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuarios` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `login` varchar(16) NOT NULL,
  `nit` varchar(12) DEFAULT NULL,
  `nombre` varchar(44) DEFAULT NULL,
  `fec_ing` date DEFAULT NULL,
  `es_cajero` varchar(1) NOT NULL,
  `cod_caj` varchar(2) DEFAULT NULL,
  `fec_sal` date DEFAULT NULL,
  `cta_con_acr` varchar(10) DEFAULT NULL,
  `activo` varchar(1) NOT NULL,
  `oficina_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuarios_oficina_id_login_34c6551a_uniq` (`oficina_id`,`login`),
  CONSTRAINT `usuarios_oficina_id_b33d5dbd_fk_oficinas_id` FOREIGN KEY (`oficina_id`) REFERENCES `oficinas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xdoc_zep`
--

DROP TABLE IF EXISTS `xdoc_zep`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `xdoc_zep` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `per_con` int(11) NOT NULL,
  `clase_zep` varchar(1) NOT NULL,
  `doc_ds` int(11) DEFAULT NULL,
  `nombre` varchar(16) NOT NULL,
  `descripcion` varchar(36) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `xdoc_zep_per_con_clase_zep_4d1efbfd_uniq` (`per_con`,`clase_zep`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xdoc_zep`
--

LOCK TABLES `xdoc_zep` WRITE;
/*!40000 ALTER TABLE `xdoc_zep` DISABLE KEYS */;
/*!40000 ALTER TABLE `xdoc_zep` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-15 16:05:57
