
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE IF NOT EXISTS buyer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    mail VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    password VARCHAR(255) NOT NULL,
    acc ENUM('yes', 'no') NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Create seller table
CREATE TABLE IF NOT EXISTS seller (
`id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `mail` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `accno` varchar(255) NOT NULL,
  `branch` varchar(255) NOT NULL,
  `bal` decimal(10,2) NOT NULL,
  `role` varchar(255) NOT NULL,  
  PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Create products table
CREATE TABLE `products` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `seller` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `hash` varchar(255) NOT NULL,
  `img` varchar(255) NOT NULL,
  `q_score` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `desc` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Create purchase table
CREATE TABLE IF NOT EXISTS purchase (
    id INT AUTO_INCREMENT PRIMARY KEY,
    seller VARCHAR(255) NOT NULL,
    buyer VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    rate DECIMAL(10, 2) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Create account table
CREATE TABLE IF NOT EXISTS account (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    acc VARCHAR(20) NOT NULL,
    branch VARCHAR(255) NOT NULL,
    amount INT NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;