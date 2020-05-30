-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema book_collection
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema book_collection
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `book_collection` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `book_collection` ;

-- -----------------------------------------------------
-- Table `book_collection`.`libro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `book_collection`.`libro` (
  `id_libro` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(120) NOT NULL,
  `autor` VARCHAR(50) NOT NULL,
  `edicion` TINYINT NULL DEFAULT NULL,
  `publicacion` VARCHAR(25) NULL DEFAULT NULL,
  `idioma` VARCHAR(20) NOT NULL,
  `editorial` VARCHAR(40) NOT NULL,
  `año` TINYINT NOT NULL,
  `saga` VARCHAR(50) NULL DEFAULT NULL,
  `paginas` SMALLINT NULL DEFAULT NULL,
  `capitulos` TINYINT NULL DEFAULT NULL,
  `sinopsis` VARCHAR(1500) NULL DEFAULT NULL,
  PRIMARY KEY (`id_libro`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `book_collection`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `book_collection`.`usuario` (
  `id_usuario` INT NOT NULL AUTO_INCREMENT,
  `nombe` VARCHAR(30) NOT NULL,
  `primer_apellido` VARCHAR(30) NOT NULL,
  `segundo_apellido` VARCHAR(30) NOT NULL,
  `usuario` VARCHAR(30) NOT NULL,
  `clave` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id_usuario`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `book_collection`.`libro_deseado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `book_collection`.`libro_deseado` (
  `id_deseado` INT NOT NULL AUTO_INCREMENT,
  `id_usuario` INT NOT NULL,
  `id_libro` INT NOT NULL,
  `fecha` DATE NOT NULL,
  PRIMARY KEY (`id_deseado`),
  INDEX `libro_deseado_usuario_id_fk_idx` (`id_usuario` ASC) VISIBLE,
  INDEX `libro_deseado_libro_id_fk_idx` (`id_libro` ASC) VISIBLE,
  CONSTRAINT `libro_deseado_usuario_id_fk`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `book_collection`.`usuario` (`id_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `libro_deseado_libro_id_fk`
    FOREIGN KEY (`id_libro`)
    REFERENCES `book_collection`.`libro` (`id_libro`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `book_collection`.`libro_leido`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `book_collection`.`libro_leido` (
  `id_leido` INT NOT NULL AUTO_INCREMENT,
  `id_usuario` INT NOT NULL,
  `id_libro` INT NOT NULL,
  `fecha` DATE NOT NULL,
  PRIMARY KEY (`id_leido`),
  INDEX `libro_leido_usuario_id_fk_idx` (`id_usuario` ASC) VISIBLE,
  INDEX `libro_leido_libro_id_fk_idx` (`id_libro` ASC) VISIBLE,
  CONSTRAINT `libro_leido_usuario_id_fk`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `book_collection`.`usuario` (`id_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `libro_leido_libro_id_fk`
    FOREIGN KEY (`id_libro`)
    REFERENCES `book_collection`.`libro` (`id_libro`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `book_collection`.`libro_obtenido`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `book_collection`.`libro_obtenido` (
  `id_obtenido` INT NOT NULL AUTO_INCREMENT,
  `id_usuario` INT NOT NULL,
  `id_libro` INT NOT NULL,
  `fecha` DATE NOT NULL,
  PRIMARY KEY (`id_obtenido`),
  INDEX `libro_obtenido_usuario_id_fk_idx` (`id_usuario` ASC) VISIBLE,
  INDEX `libro_obtenido_usuario_id_fk_idx1` (`id_libro` ASC) VISIBLE,
  CONSTRAINT `libro_obtenido_usuario_id_fk`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `book_collection`.`usuario` (`id_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `libro_obtenido_libro_id_fk`
    FOREIGN KEY (`id_libro`)
    REFERENCES `book_collection`.`libro` (`id_libro`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
