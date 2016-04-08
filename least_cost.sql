-- phpMyAdmin SQL Dump
-- version 4.5.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Apr 08, 2016 at 08:39 AM
-- Server version: 5.6.17
-- PHP Version: 5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `least_cost`
--

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('68ff22e10145');

-- --------------------------------------------------------

--
-- Table structure for table `buyer`
--

CREATE TABLE `buyer` (
  `buyer_id` int(11) NOT NULL,
  `buyer_name` varchar(120) NOT NULL,
  `state_id` int(11) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `buyer`
--

INSERT INTO `buyer` (`buyer_id`, `buyer_name`, `state_id`, `created_at`) VALUES
(1, 'Kumaran', 31, '2016-04-07 23:04:52'),
(2, 'Ezhil', 16, '2016-04-07 23:05:15'),
(3, 'Ijaz', 25, '2016-04-07 23:05:24');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`product_id`, `product_name`, `created_at`) VALUES
(1, 'MacBook Air', '2016-04-07 22:15:55'),
(2, 'iPad Pro', '2016-04-07 22:16:33'),
(3, 'Surface Book Pro', '2016-04-07 22:16:47'),
(4, 'Sandisk 8GB', '2016-04-07 22:16:54'),
(5, 'Sandisk 16GB', '2016-04-07 22:16:59'),
(6, 'Sandisk OTG 32GB', '2016-04-07 22:17:07'),
(7, 'USB-C cable', '2016-04-07 22:17:31'),
(8, 'Transcend SSD 1TB', '2016-04-07 22:18:02'),
(9, 'Transcend HDD 1TB', '2016-04-07 22:18:10'),
(10, 'iPhone SE', '2016-04-07 22:18:39');

-- --------------------------------------------------------

--
-- Table structure for table `seller`
--

CREATE TABLE `seller` (
  `seller_id` int(11) NOT NULL,
  `seller_name` varchar(120) NOT NULL,
  `state_id` int(11) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `seller`
--

INSERT INTO `seller` (`seller_id`, `seller_name`, `state_id`, `created_at`) VALUES
(1, 'WSRetail', 25, '2016-04-07 22:59:18'),
(2, 'TamilNaduRetail', 31, '2016-04-07 23:01:03'),
(3, 'eKart', 16, '2016-04-07 23:01:17');

-- --------------------------------------------------------

--
-- Table structure for table `selling`
--

CREATE TABLE `selling` (
  `selling_id` int(11) NOT NULL,
  `seller_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `selling`
--

INSERT INTO `selling` (`selling_id`, `seller_id`, `product_id`, `price`, `created_at`) VALUES
(1, 1, 1, 80000, '2016-04-07 23:29:59'),
(2, 2, 1, 70000, '2016-04-07 23:30:13'),
(3, 3, 1, 90000, '2016-04-07 23:30:24'),
(4, 2, 3, 90000, '2016-04-07 23:30:35'),
(5, 1, 3, 100000, '2016-04-07 23:30:44'),
(6, 1, 7, 500, '2016-04-07 23:30:53'),
(7, 3, 7, 300, '2016-04-07 23:30:59');

-- --------------------------------------------------------

--
-- Table structure for table `state`
--

CREATE TABLE `state` (
  `state_id` int(11) NOT NULL,
  `state_name` varchar(120) NOT NULL,
  `tax_percent` int(11) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `state`
--

INSERT INTO `state` (`state_id`, `state_name`, `tax_percent`, `created_at`) VALUES
(1, 'Andaman and Nicobar', 10, '2016-04-07 21:34:33'),
(2, 'Andhra Pradesh', 5, '2016-04-07 21:37:10'),
(3, 'Arunachal Pradesh', 3, '2016-04-07 21:37:26'),
(4, 'Assam', 5, '2016-04-07 21:37:42'),
(5, 'Bihar', 12, '2016-04-07 21:38:10'),
(6, 'Chandigarh', 5, '2016-04-07 21:38:32'),
(7, 'Chhattisgarh', 4, '2016-04-07 21:39:19'),
(8, 'Dadra and Nagar Haveli', 6, '2016-04-07 21:39:19'),
(9, 'Daman and Diu', 6, '2016-04-07 21:40:35'),
(10, 'Goa', 7, '2016-04-07 21:40:35'),
(11, 'Gujarat', 4, '2016-04-07 21:40:58'),
(12, 'Haryana', 6, '2016-04-07 21:41:15'),
(13, 'Himachal Pradesh', 15, '2016-04-07 21:41:34'),
(14, 'Jammu and Kashmir', 10, '2016-04-07 21:41:47'),
(15, 'Jharkhand', 6, '2016-04-07 21:41:56'),
(16, 'Karnataka', 4, '2016-04-07 21:42:06'),
(17, 'Kerala', 6, '2016-04-07 21:42:17'),
(18, 'Lakshadweep', 9, '2016-04-07 21:42:39'),
(19, 'Madhya Pradesh', 9, '2016-04-07 21:42:49'),
(20, 'Maharashtra', 11, '2016-04-07 21:43:01'),
(21, 'Manipur', 11, '2016-04-07 21:43:08'),
(22, 'Meghalaya', 13, '2016-04-07 21:43:23'),
(23, 'Mizoram', 13, '2016-04-07 21:45:16'),
(24, 'Nagaland', 13, '2016-04-07 21:45:34'),
(25, 'New Delhi', 8, '2016-04-07 21:46:03'),
(26, 'Odisha', 3, '2016-04-07 21:46:13'),
(27, 'Puducherry', 4, '2016-04-07 21:46:20'),
(28, 'Punjab', 9, '2016-04-07 21:46:35'),
(29, 'Rajasthan', 5, '2016-04-07 21:46:42'),
(30, 'Sikkim', 3, '2016-04-07 21:46:59'),
(31, 'Tamil Nadu', 3, '2016-04-07 21:47:07'),
(32, 'Telangana', 7, '2016-04-07 21:47:17'),
(33, 'Tripura', 15, '2016-04-07 21:47:31'),
(34, 'Uttarakhand', 20, '2016-04-07 21:47:43'),
(35, 'Uttar Pradesh', 7, '2016-04-07 21:47:54'),
(36, 'West Bengal', 7, '2016-04-07 21:50:05');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `buyer`
--
ALTER TABLE `buyer`
  ADD PRIMARY KEY (`buyer_id`),
  ADD UNIQUE KEY `buyer_name` (`buyer_name`),
  ADD KEY `ix_buyer_state_id` (`state_id`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`product_id`),
  ADD UNIQUE KEY `product_name` (`product_name`);

--
-- Indexes for table `seller`
--
ALTER TABLE `seller`
  ADD PRIMARY KEY (`seller_id`),
  ADD UNIQUE KEY `seller_name` (`seller_name`),
  ADD KEY `ix_seller_state_id` (`state_id`);

--
-- Indexes for table `selling`
--
ALTER TABLE `selling`
  ADD PRIMARY KEY (`selling_id`),
  ADD KEY `ix_selling_product_id` (`product_id`),
  ADD KEY `ix_selling_seller_id` (`seller_id`);

--
-- Indexes for table `state`
--
ALTER TABLE `state`
  ADD PRIMARY KEY (`state_id`),
  ADD UNIQUE KEY `state_name` (`state_name`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `buyer`
--
ALTER TABLE `buyer`
  MODIFY `buyer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `seller`
--
ALTER TABLE `seller`
  MODIFY `seller_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `selling`
--
ALTER TABLE `selling`
  MODIFY `selling_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `state`
--
ALTER TABLE `state`
  MODIFY `state_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `buyer`
--
ALTER TABLE `buyer`
  ADD CONSTRAINT `buyer_ibfk_1` FOREIGN KEY (`state_id`) REFERENCES `state` (`state_id`);

--
-- Constraints for table `seller`
--
ALTER TABLE `seller`
  ADD CONSTRAINT `seller_ibfk_1` FOREIGN KEY (`state_id`) REFERENCES `state` (`state_id`);

--
-- Constraints for table `selling`
--
ALTER TABLE `selling`
  ADD CONSTRAINT `selling_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`),
  ADD CONSTRAINT `selling_ibfk_2` FOREIGN KEY (`seller_id`) REFERENCES `seller` (`seller_id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
