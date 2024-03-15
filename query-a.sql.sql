-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 10, 2022 at 10:12 AM
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
-- Database: `pollution-db2`
--

-- --------------------------------------------------------

--
-- Table structure for table `site`
--

CREATE TABLE `site` (
  `SiteID` int(10) NOT NULL,
  `Location` varchar(100) DEFAULT NULL,
  `geo_point_2d` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `site`
--

INSERT INTO `site` (`SiteID`, `Location`, `geo_point_2d`) VALUES
(203, 'Brislington Depot', '51.4417471802,-2.55995583224'),
(206, 'Rupert Street', '51.4554331987,-2.59626237324'),
(213, 'Old Market', '51.4560189999,-2.58348949026'),
(215, 'Parson Street School', '51.432675707,-2.60495665673'),
(270, 'Wells Road', '51.4278638883,-2.56374153315'),
(375, 'Newfoundland Road Police Station', '51.4606738207,-2.58225341824'),
(395, 'Shiner\'s Garage', '51.4577930324,-2.56271419977'),
(447, 'Bath Road', '51.4425372726,-2.57137536073'),
(452, 'AURN St Pauls', '51.4628294172,-2.58454081635'),
(459, 'Cheltenham Road \\ Station Road', '51.4689385901,-2.5927241667'),
(463, 'Fishponds Road', '51.4780449714,-2.53523027459'),
(481, 'CREATE Centre Roof', '51.447213417,-2.62247405516'),
(500, 'Temple Way', '51.4579497129,-2.58398909033'),
(501, 'Colston Avenue', '51.4552693825,-2.59664882861');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `site`
--
ALTER TABLE `site`
  ADD PRIMARY KEY (`SiteID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
