/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : aumentos

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2017-07-13 12:37:54
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for augment_attribute
-- ----------------------------
DROP TABLE IF EXISTS `augment_attribute`;
CREATE TABLE `augment_attribute` (
  `id` int(11) NOT NULL,
  `description` text,
  `type` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
