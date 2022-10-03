SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema museum
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `museum` DEFAULT CHARACTER SET utf8 ;
USE `museum` ;

-- -----------------------------------------------------
-- Table `museum`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `museum`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `firstName` VARCHAR(12) NOT NULL,
  `lastName` VARCHAR(12) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `username` VARCHAR(16) NOT NULL,
  `password` VARCHAR(102) NOT NULL,
  `securityKey` VARCHAR(102) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC));


-- -----------------------------------------------------
-- Table `museum`.`employee`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `museum`.`employee` (
  `userId` INT NOT NULL,
  `status` VARCHAR(6) NOT NULL,
  PRIMARY KEY (`userId`),
  CONSTRAINT `fk_employee_user`
    FOREIGN KEY (`userId`)
    REFERENCES `museum`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table `museum`.`client`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `museum`.`client` (
  `userId` INT NOT NULL,
  `bibliography` VARCHAR(255) NOT NULL,
  `birthDate` DATE NOT NULL,
  `nationality` VARCHAR(3) NOT NULL,
  `photography` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`userId`),
  INDEX `fk_client_user1_idx` (`userId` ASC),
  CONSTRAINT `fk_client_user1`
    FOREIGN KEY (`userId`)
    REFERENCES `museum`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table `museum`.`artwork`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `museum`.`artwork` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `clientId` INT NOT NULL,
  `title` VARCHAR(20) NOT NULL,
  `image` VARCHAR(25) NOT NULL,
  `price` FLOAT NOT NULL,
  `createTime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_artwork_client1_idx` (`clientId` ASC),
  UNIQUE INDEX `title_UNIQUE` (`title` ASC),
  CONSTRAINT `fk_artwork_client1`
    FOREIGN KEY (`clientId`)
    REFERENCES `museum`.`client` (`userId`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table `museum`.`ceramic`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `museum`.`ceramic` (
  `artworkId` INT NOT NULL,
  `color` VARCHAR(45) NOT NULL,
  `composition` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`artworkId`),
  CONSTRAINT `fk_ceramic_artwork1`
    FOREIGN KEY (`artworkId`)
    REFERENCES `museum`.`artwork` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table `museum`.`photography`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `museum`.`photography` (
  `artworkId` INT NOT NULL,
  `dimensions` VARCHAR(45) NOT NULL,
  `resolution` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`artworkId`),
  CONSTRAINT `fk_photography_artwork1`
    FOREIGN KEY (`artworkId`)
    REFERENCES `museum`.`artwork` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table `museum`.`painting`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `museum`.`painting` (
  `artworkId` INT NOT NULL,
  `dimensions` VARCHAR(45) NOT NULL,
  `gender` VARCHAR(45) NOT NULL,
  `technique` VARCHAR(45) NOT NULL,
  `stream` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`artworkId`),
  CONSTRAINT `fk_painting_artwork1`
    FOREIGN KEY (`artworkId`)
    REFERENCES `museum`.`artwork` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table `museum`.`goldsmith`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `museum`.`goldsmith` (
  `artworkId` INT NOT NULL,
  `materials` VARCHAR(45) NOT NULL,
  `technique` VARCHAR(45) NOT NULL,
  `appearance` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`artworkId`),
  CONSTRAINT `fk_goldsmith_artwork1`
    FOREIGN KEY (`artworkId`)
    REFERENCES `museum`.`artwork` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table `museum`.`sculpture`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `museum`.`sculpture` (
  `artworkId` INT NOT NULL,
  `description` VARCHAR(45) NOT NULL,
  `materials` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`artworkId`),
  CONSTRAINT `fk_sculpture_artwork1`
    FOREIGN KEY (`artworkId`)
    REFERENCES `museum`.`artwork` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table `museum`.`bill`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `museum`.`bill` (
  `artworkId` INT NOT NULL,
  `clientId` INT NOT NULL,
  `date` DATE NOT NULL,
  `amount` VARCHAR(45) NOT NULL,
  `createTime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`artworkId`),
  INDEX `fk_bill_client1_idx` (`clientId` ASC),
  CONSTRAINT `fk_bill_artwork1`
    FOREIGN KEY (`artworkId`)
    REFERENCES `museum`.`artwork` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_bill_client1`
    FOREIGN KEY (`clientId`)
    REFERENCES `museum`.`client` (`userId`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table `museum`.`userHasClient`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `museum`.`userHasClient` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `userId` INT NOT NULL,
  `clientId` INT NOT NULL,
  INDEX `fk_user_has_client_client1_idx` (`clientId` ASC),
  INDEX `fk_user_has_client_user1_idx` (`userId` ASC),
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_user_has_client_user1`
    FOREIGN KEY (`userId`)
    REFERENCES `museum`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_user_has_client_client1`
    FOREIGN KEY (`clientId`)
    REFERENCES `museum`.`client` (`userId`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;