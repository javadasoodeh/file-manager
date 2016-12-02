-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Dec 02, 2016 at 08:45 AM
-- Server version: 5.6.21
-- PHP Version: 5.6.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `filemanager`
--

-- --------------------------------------------------------

--
-- Table structure for table `file`
--

CREATE TABLE IF NOT EXISTS `file` (
  `fileid` varchar(50) COLLATE utf8_persian_ci NOT NULL,
  `name_main` varchar(50) COLLATE utf8_persian_ci NOT NULL,
  `content_type` varchar(50) COLLATE utf8_persian_ci NOT NULL,
  `size` int(11) NOT NULL,
  `extension` varchar(15) COLLATE utf8_persian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_persian_ci;

--
-- Dumping data for table `file`
--

INSERT INTO `file` (`fileid`, `name_main`, `content_type`, `size`, `extension`) VALUES
('21b5142b-af85-43e5-8267-580e0e2a9843', '01 (1).jpg', 'image/jpeg', 159462, 'jpg'),
('21ecb0f8-d8b0-44e6-b2a2-0470c79043f1', '01 (1).jpg', 'image/jpeg', 159462, 'jpg'),
('24df6f42-7591-4d6b-8364-f61091a048e0', '01 (1).jpg', 'image/jpeg', 159462, 'jpg'),
('37b9af98-7075-4c40-af1f-2954ea5224c4', 'Capture.PNG', 'image/png', 10641, 'PNG'),
('46c6ae7c-c542-4891-bc58-201c61c0141e', 'Ebru Gundes - Seni Istiyorum - HD .mp4', 'video/mp4', 68267394, 'mp4'),
('4ce06a44-4a26-4cbb-b6ff-9ab75db244b2', 'Ebru Gundes - Yaparim Bilirsin - HD .mp4', 'video/mp4', 52642018, 'mp4'),
('6e3e4acd-37d1-4632-8d9e-c0ee336a3159', '12.jpg', 'image/jpeg', 295454, 'jpg'),
('74f739af-6cde-492c-80f0-40873d4cb5b1', '01 (1).jpg', 'image/jpeg', 159462, 'jpg'),
('8e01ed08-443d-4f44-bf99-089c6b048175', 'computerChart.jpg', 'image/jpeg', 205559, 'jpg'),
('b273dc07-1f7c-497e-8c21-c2f815ad7286', 'Capture.PNG', 'image/png', 10641, 'PNG');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `file`
--
ALTER TABLE `file`
 ADD PRIMARY KEY (`fileid`), ADD UNIQUE KEY `name_UNIQUE` (`fileid`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
