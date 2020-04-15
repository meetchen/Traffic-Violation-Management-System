/*
Navicat MySQL Data Transfer

Source Server         : sql
Source Server Version : 50553
Source Host           : localhost:3306
Source Database       : sql

Target Server Type    : MYSQL
Target Server Version : 50553
File Encoding         : 65001

Date: 2019-11-26 20:10:13
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for driver
-- ----------------------------
DROP TABLE IF EXISTS `driver`;
CREATE TABLE `driver` (
  `driver_id` int(64) NOT NULL AUTO_INCREMENT COMMENT '驾照号\r\n',
  `driver_name` varchar(255) DEFAULT NULL COMMENT '司机姓名',
  `driver_phone` varchar(255) DEFAULT NULL COMMENT '司机电话',
  `driver_address` varchar(255) DEFAULT NULL COMMENT '司机地址',
  `driver_post_code` varchar(255) DEFAULT NULL COMMENT '司机邮编',
  PRIMARY KEY (`driver_id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8 COMMENT='司机表\r\n';

-- ----------------------------
-- Records of driver
-- ----------------------------
INSERT INTO `driver` VALUES ('13', '南海深', '南田', '西安科技大学临潼校区', '1215');
INSERT INTO `driver` VALUES ('18', '南天阙', '18787988778', '北海十里深蔚之区', '588484');
INSERT INTO `driver` VALUES ('19', '北平', '151515', '北京', '151515');

-- ----------------------------
-- Table structure for notice
-- ----------------------------
DROP TABLE IF EXISTS `notice`;
CREATE TABLE `notice` (
  `notice_id` int(64) NOT NULL AUTO_INCREMENT COMMENT '通知单编号',
  `notice_time` varchar(64) NOT NULL COMMENT '通知单时间',
  `notice_date` varchar(64) NOT NULL COMMENT '通知日期',
  `notice_place` varchar(64) NOT NULL COMMENT '违章地点',
  `notice_record` varchar(64) NOT NULL COMMENT '违章记录',
  PRIMARY KEY (`notice_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COMMENT='通知单';

-- ----------------------------
-- Records of notice
-- ----------------------------
INSERT INTO `notice` VALUES ('1', '9：28', '2019-6-7', '15-13', '追尾');
INSERT INTO `notice` VALUES ('2', '9：26', '2016-6-6', '北平路', '追尾');

-- ----------------------------
-- Table structure for police
-- ----------------------------
DROP TABLE IF EXISTS `police`;
CREATE TABLE `police` (
  `police_id` int(64) NOT NULL AUTO_INCREMENT COMMENT '警察号',
  `police_name` varchar(255) DEFAULT NULL COMMENT '警察姓名',
  PRIMARY KEY (`police_id`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of police
-- ----------------------------
INSERT INTO `police` VALUES ('7', '北恋心');

-- ----------------------------
-- Table structure for punish
-- ----------------------------
DROP TABLE IF EXISTS `punish`;
CREATE TABLE `punish` (
  `punish_id` int(64) NOT NULL AUTO_INCREMENT COMMENT '处罚方式编号',
  `punish_type` varchar(64) NOT NULL COMMENT '处罚方式',
  PRIMARY KEY (`punish_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COMMENT='处罚表';

-- ----------------------------
-- Records of punish
-- ----------------------------
INSERT INTO `punish` VALUES ('1', '警告');
INSERT INTO `punish` VALUES ('5', '大');
INSERT INTO `punish` VALUES ('3', '扣留驾照');
INSERT INTO `punish` VALUES ('7', '大大大');

-- ----------------------------
-- Table structure for usertable
-- ----------------------------
DROP TABLE IF EXISTS `usertable`;
CREATE TABLE `usertable` (
  `user` varchar(255) NOT NULL,
  `user_password` varchar(255) NOT NULL,
  `user_identity` tinyint(1) NOT NULL COMMENT '1=police，0=driver',
  PRIMARY KEY (`user`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of usertable
-- ----------------------------
INSERT INTO `usertable` VALUES ('cjc', 'cjc', '1');
INSERT INTO `usertable` VALUES ('driver', 'driver', '0');

-- ----------------------------
-- Table structure for vehicle
-- ----------------------------
DROP TABLE IF EXISTS `vehicle`;
CREATE TABLE `vehicle` (
  `vehicle_license_plate` varchar(128) NOT NULL DEFAULT '' COMMENT '车牌号',
  `vehicle_date` varchar(255) DEFAULT NULL COMMENT '生产日期',
  `vehicle_type` varchar(255) DEFAULT NULL COMMENT '车辆型号',
  `vehicle_manufacturer` varchar(255) DEFAULT NULL COMMENT '车辆制造商',
  PRIMARY KEY (`vehicle_license_plate`(4))
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='机动车表\r\n';

-- ----------------------------
-- Records of vehicle
-- ----------------------------
INSERT INTO `vehicle` VALUES ('陕C6666', '2019-6-3', '超跑', '梅赛德斯');
INSERT INTO `vehicle` VALUES ('陕C8888', '2013-3-5', '面包车', '凯越');
INSERT INTO `vehicle` VALUES ('陕C8967', '2019-6-9\\', '上海通用', '商务车');
