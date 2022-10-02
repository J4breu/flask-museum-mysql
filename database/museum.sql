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


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;