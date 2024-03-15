-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 29, 2022 at 03:58 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pollution-db`
--

-- --------------------------------------------------------

--
-- Table structure for table `readings`
--

CREATE TABLE `readings` (
  `ReadingsID` int(11) NOT NULL,
  `Date Time` varchar(45) DEFAULT NULL,
  `NOx` varchar(45) DEFAULT NULL,
  `NO2` varchar(45) DEFAULT NULL,
  `NO` varchar(45) DEFAULT NULL,
  `SiteID` varchar(45) DEFAULT NULL,
  `PM10` varchar(45) DEFAULT NULL,
  `NVPM10` varchar(45) DEFAULT NULL,
  `VPM10` varchar(45) DEFAULT NULL,
  `NVPM2.5` varchar(45) DEFAULT NULL,
  `PM2.5` varchar(45) DEFAULT NULL,
  `VPM2.5` varchar(45) DEFAULT NULL,
  `CO` varchar(45) DEFAULT NULL,
  `O3` varchar(45) DEFAULT NULL,
  `SO2` varchar(45) DEFAULT NULL,
  `Temperature` varchar(45) DEFAULT NULL,
  `RH` varchar(45) DEFAULT NULL,
  `Air pressure` varchar(45) DEFAULT NULL,
  `Date start` varchar(45) DEFAULT NULL,
  `Date End` varchar(45) DEFAULT NULL,
  `Current` varchar(45) DEFAULT NULL,
  `Instrument` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `schema`
--

CREATE TABLE `schema` (
  `measures` int(11) NOT NULL,
  `desc` varchar(45) DEFAULT NULL,
  `units` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `site`
--

CREATE TABLE `site` (
  `SiteID` int(11) NOT NULL,
  `geo_point_2d` varchar(45) DEFAULT NULL,
  `Location` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `readings`
--
ALTER TABLE `readings`
  ADD PRIMARY KEY (`ReadingsID`);

--
-- Indexes for table `schema`
--
ALTER TABLE `schema`
  ADD PRIMARY KEY (`measures`);

--
-- Indexes for table `site`
--
ALTER TABLE `site`
  ADD PRIMARY KEY (`SiteID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `readings`
--
ALTER TABLE `readings`
  ADD CONSTRAINT `SiteID` FOREIGN KEY (`ReadingsID`) REFERENCES `mydb`.`site` (`SiteID`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
