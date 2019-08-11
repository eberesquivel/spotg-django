/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : aumentos

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2017-07-13 12:37:47
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for augment_type
-- ----------------------------
DROP TABLE IF EXISTS `augment_type`;
CREATE TABLE `augment_type` (
  `id` int(11) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `aumentos`.`augment_type` (`id`, `type`) VALUES ('1', 'active');
INSERT INTO `aumentos`.`augment_type` (`id`, `type`) VALUES ('2', 'chance');
INSERT INTO `aumentos`.`augment_type` (`id`, `type`) VALUES ('3', 'passive');

