/*
 Navicat Premium Data Transfer

 Source Server         : DBeric
 Source Server Type    : MySQL
 Source Server Version : 80015
 Source Host           : localhost:3306
 Source Schema         : carpool

 Target Server Type    : MySQL
 Target Server Version : 80015
 File Encoding         : 65001

 Date: 27/02/2019 20:05:04
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for car_info
-- ----------------------------
DROP TABLE IF EXISTS `car_info`;
CREATE TABLE `car_info` (
  `Lname` varchar(255) DEFAULT NULL,
  `Fname` varchar(255) DEFAULT NULL,
  `Plate` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Driver_license` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Unique_id` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `make` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `gender` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Unique_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for driver_info
-- ----------------------------
DROP TABLE IF EXISTS `driver_info`;
CREATE TABLE `driver_info` (
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `unique_id` int(10) NOT NULL,
  `departure` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `destination` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `time` datetime NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `capability` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`unique_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for passenger
-- ----------------------------
DROP TABLE IF EXISTS `passenger`;
CREATE TABLE `passenger` (
  `passenger_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `departure` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `destination` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `unique_id` int(10) NOT NULL,
  `num_passenger` int(255) DEFAULT NULL,
  PRIMARY KEY (`unique_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for usr_info
-- ----------------------------
DROP TABLE IF EXISTS `usr_info`;
CREATE TABLE `usr_info` (
  `usr_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `unique_id` int(10) NOT NULL,
  `phone_num` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `car_info` binary(1) NOT NULL,
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`unique_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

SET FOREIGN_KEY_CHECKS = 1;
