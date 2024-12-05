/* ================================ Creación y uso de la base de datos ================================ */

CREATE DATABASE db_gobierno;
USE db_gobierno;

/* ================================ Creación de las tablas de la bdb ================================== */

-- Tabla para géneros 
CREATE TABLE `db_gobierno`.`genero` (
    `genero_id` INT AUTO_INCREMENT PRIMARY KEY,
    `nombre_genero` VARCHAR(50) UNIQUE NOT NULL,
    `descripcion` VARCHAR(250) UNIQUE NOT NULL,
    `fecha_creacion` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla para usuarios (login)
CREATE TABLE `db_gobierno`.`usuario` (
    `user_id` INT AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(50) UNIQUE NOT NULL,
    `password_hash` VARCHAR(255) NOT NULL,
    `email` VARCHAR(100) UNIQUE NOT NULL,
    `fecha_creacion` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla para usuarios (clave)
CREATE TABLE `db_gobierno`.`clave` (
    `username` VARCHAR(50) UNIQUE NOT NULL,
    `token` VARCHAR(255) UNIQUE NOT NULL,
    FOREIGN KEY (`username`) REFERENCES `usuario`(`username`) ON DELETE CASCADE
);

-- Tabla para países
CREATE TABLE `db_gobierno`.`pais` (
    `pais_id` INT AUTO_INCREMENT PRIMARY KEY,
    `nombre_pais` VARCHAR(100) NOT NULL DEFAULT 'Colombia', -- Nombre del país (ej. Colombia, México)
    `descripcion` VARCHAR(255) NOT NULL,
    `fecha_creacion` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla para estados o departamentos
CREATE TABLE `db_gobierno`.`estado` (
    `estado_id` INT AUTO_INCREMENT PRIMARY KEY,
    `nombre_estado` VARCHAR(100) NOT NULL, -- Nombre del estado o departamento (ej. Antioquia, California)
    `descripcion` VARCHAR(255) NOT NULL,
    `pais_id` INT, -- ID del país al que pertenece el estado
    `fecha_creacion` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`pais_id`) REFERENCES `pais`(`pais_id`) ON DELETE CASCADE
);

-- Tabla para ciudades o provincias
CREATE TABLE `db_gobierno`.`ciudad` (
    `ciudad_id` INT AUTO_INCREMENT PRIMARY KEY,
    `nombre_ciudad` VARCHAR(100) NOT NULL, -- Nombre de la ciudad (ej. Medellín, Los Ángeles)
    `descripcion` VARCHAR(255) NOT NULL,
    `estado_id` INT,
    `fecha_creacion` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`estado_id`) REFERENCES `estado`(`estado_id`) ON DELETE CASCADE
);

-- Tabla para personas
CREATE TABLE `db_gobierno`.`persona` (
    `persona_id` INT AUTO_INCREMENT PRIMARY KEY,
    `user_id` INT,
    `nombre_persona` VARCHAR(100) NOT NULL,
    `apellido_persona` VARCHAR(100) NOT NULL,
    `documento_identidad` VARCHAR(50) UNIQUE NOT NULL,
    `genero_id` INT,
    `ciudad_id` INT,
    `fecha_nacimiento` DATE NOT NULL,
    `direccion_persona` VARCHAR(255),
    `fecha_creacion` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`user_id`) REFERENCES `usuario`(`user_id`) ON DELETE SET NULL,
    FOREIGN KEY (`genero_id`) REFERENCES `genero`(`genero_id`),
    FOREIGN KEY (`ciudad_id`) REFERENCES `ciudad`(`ciudad_id`)
);

-- Tabla para teléfonos
CREATE TABLE `db_gobierno`.`telefono` (
    `telefono_id` INT AUTO_INCREMENT PRIMARY KEY,
    `persona_id` INT,
    `tipo_telefono` VARCHAR(50) NOT NULL,
    `numero_telefono` VARCHAR(20) NOT NULL,
    `fecha_creacion` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`persona_id`) REFERENCES `persona`(`persona_id`) ON DELETE CASCADE
);

-- Tabla para cargos públicos
CREATE TABLE `db_gobierno`.`cargo` (
    `cargo_id` INT AUTO_INCREMENT PRIMARY KEY,
    `titulo` VARCHAR(100) NOT NULL,
    `descripcion` VARCHAR(255) NOT NULL,
    `fecha_creacion` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla para entidades gubernamentales
CREATE TABLE `db_gobierno`.`entidad` (
    `entidad_id` INT AUTO_INCREMENT PRIMARY KEY,
    `nombre_entidad` VARCHAR(100) NOT NULL, -- Senado, Ministerio, Alcaldía, etc.
    `descripcion` VARCHAR(255) NOT NULL,
    `tipo_entidad` VARCHAR(50) NOT NULL, -- Tipo de entidad: Nacional, Local, Regional, etc.
    `fecha_creacion` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla para asignación de cargos públicos
CREATE TABLE `db_gobierno`.`asignacion_cargo` (
    `asignacion_id` INT AUTO_INCREMENT PRIMARY KEY,
    `persona_id` INT,
    `cargo_id` INT,
    `entidad_id` INT,
    `fecha_inicio` DATE NOT NULL,
    `fecha_fin` DATE, -- Puede ser NULL si la persona sigue en el cargo
    `estado` VARCHAR(50) DEFAULT 'Activo', -- Estado de la asignación: Activo o Finalizado
    `fecha_creacion` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`persona_id`) REFERENCES `persona`(`persona_id`) ON DELETE CASCADE,
    FOREIGN KEY (`cargo_id`) REFERENCES `cargo`(`cargo_id`) ON DELETE CASCADE,
    FOREIGN KEY (`entidad_id`) REFERENCES `entidad`(`entidad_id`) ON DELETE CASCADE
);

/* ============================== Inserción de datos iniciales en la db =============================== */

-- Inserciones en la tabla de géneros
INSERT INTO `db_gobierno`.`genero` (`nombre_genero`, `descripcion`) VALUES 
('Masculino', 'Identidad de género masculino.'),
('Femenino', 'Identidad de género femenino.'),
('No binario', 'Identidad de género que no se clasifica como exclusivamente masculino o femenino.'),
('Transgénero', 'Persona cuya identidad de género difiere del sexo asignado al nacer.'),
('Género fluido', 'Identidad de género que puede cambiar con el tiempo.'),
('Agénero', 'Identidad que no se identifica con ningún género.'),
('Bigénero', 'Identidad de género que comprende dos géneros.'),
('Pangénero', 'Identidad de género que abarca todos los géneros.'),
('Genderqueer', 'Identidad que desafía las normas tradicionales de género.'),
('Cisgénero', 'Persona cuya identidad de género coincide con el sexo asignado al nacer.');

-- Inserciones en la tabla de usuarios
INSERT INTO `db_gobierno`.`usuario` (`username`, `password_hash`, `email`) VALUES 
('user1', 'hashed_password_1', 'user1@example.com'),
('user2', 'hashed_password_2', 'user2@example.com'),
('user3', 'hashed_password_3', 'user3@example.com'),
('user4', 'hashed_password_4', 'user4@example.com'),
('user5', 'hashed_password_5', 'user5@example.com'),
('user6', 'hashed_password_6', 'user6@example.com'),
('user7', 'hashed_password_7', 'user7@example.com'),
('user8', 'hashed_password_8', 'user8@example.com'),
('user9', 'hashed_password_9', 'user9@example.com'),
('user10', 'hashed_password_10', 'user10@example.com');

-- Inserciones en la tabla de países
INSERT INTO `db_gobierno`.`pais` (`nombre_pais`, `descripcion`) VALUES 
('Colombia', 'Un país en América del Sur conocido por su diversidad cultural.'),
('México', 'Famoso por su comida, historia y tradiciones.'),
('Argentina', 'Conocido por su tango y su carne.'),
('Chile', 'Famoso por sus vinos y paisajes.'),
('Perú', 'Conocido por Machu Picchu y su rica gastronomía.'),
('España', 'Famoso por su historia y arquitectura.'),
('Francia', 'Conocido por su arte, moda y gastronomía.'),
('Italia', 'Famoso por su historia, arte y comida.'),
('Alemania', 'Conocido por su tecnología y cultura.'),
('Brasil', 'Famoso por su carnaval y biodiversidad.');

-- Inserciones en la tabla de estados
INSERT INTO `db_gobierno`.`estado` (`nombre_estado`, `descripcion`, `pais_id`) VALUES 
('Antioquia', 'Departamento de Colombia conocido por su café.', 1),
('Cundinamarca', 'Departamento donde se encuentra Bogotá.', 1),
('California', 'Estado famoso por Hollywood y su clima.', 2),
('Buenos Aires', 'Capital y estado de Argentina.', 3),
('Valparaíso', 'Estado costero de Chile.', 4),
('Lima', 'Estado y capital de Perú.', 5),
('Cataluña', 'Conocido por su cultura y lengua propias en España.', 6),
('Occitania', 'Región histórica del sur de Francia.', 7),
('Lazio', 'Región de Italia donde se encuentra Roma.', 8),
('Baviera', 'Estado en el sur de Alemania famoso por su cerveza.', 9);

-- Inserciones en la tabla de ciudades
INSERT INTO `db_gobierno`.`ciudad` (`nombre_ciudad`, `descripcion`, `estado_id`) VALUES 
('Medellín', 'Conocida como la ciudad de la eterna primavera.', 1),
('Bogotá', 'Capital de Colombia y centro político.', 2),
('Los Ángeles', 'Conocida por su industria del entretenimiento.', 3),
('Buenos Aires', 'Famosa por su tango y cultura.', 4),
('Santiago', 'Capital de Chile, rodeada de montañas.', 5),
('Lima', 'Conocida por su gastronomía y arquitectura.', 6),
('Barcelona', 'Famosa por su arquitectura y playas.', 7),
('Niza', 'Ciudad costera en la Riviera Francesa.', 8),
('Roma', 'Capital de Italia y cuna de la civilización.', 9),
('Múnich', 'Conocida por su Oktoberfest y cultura bávara.', 10);

-- Inserciones en la tabla de personas
INSERT INTO `db_gobierno`.`persona` (`user_id`, `nombre_persona`, `apellido_persona`, `documento_identidad`, `genero_id`, `ciudad_id`, `fecha_nacimiento`, `direccion_persona`) VALUES 
(1, 'Juan', 'Pérez', '123456789', 1, 1, '1990-01-01', 'Calle 1 #1-1'),
(2, 'María', 'González', '987654321', 2, 2, '1985-05-05', 'Calle 2 #2-2'),
(3, 'Luis', 'Martínez', '456789123', 1, 3, '1992-10-10', 'Calle 3 #3-3'),
(4, 'Ana', 'Hernández', '321654987', 2, 4, '1988-02-02', 'Calle 4 #4-4'),
(5, 'Carlos', 'López', '159753468', 1, 5, '1995-08-08', 'Calle 5 #5-5'),
(6, 'Sofía', 'Ramírez', '753159486', 2, 6, '1993-12-12', 'Calle 6 #6-6'),
(7, 'Diego', 'Torres', '258963147', 1, 7, '1987-04-04', 'Calle 7 #7-7'),
(8, 'Isabel', 'Jiménez', '369852741', 2, 8, '1991-11-11', 'Calle 8 #8-8'),
(9, 'Andrés', 'Díaz', '147258369', 1, 9, '1994-07-07', 'Calle 9 #9-9'),
(10, 'Laura', 'Gutiérrez', '963258741', 2, 10, '1996-09-09', 'Calle 10 #10-10');

-- Inserciones en la tabla de teléfonos
INSERT INTO `db_gobierno`.`telefono` (`persona_id`, `tipo_telefono`, `numero_telefono`) VALUES 
(1, 'Móvil', '3001112233'),
(2, 'Fijo', '6012233445'),
(3, 'Móvil', '3009876543'),
(4, 'Fijo', '6013344556'),
(5, 'Móvil', '3002233445'),
(6, 'Trabajo', '6015566778'),
(7, 'Móvil', '3004455667'),
(8, 'Fijo', '6017788990'),
(9, 'Móvil', '3005566778'),
(10, 'Fijo', '6018899001');

-- Inserciones en la tabla de cargos
INSERT INTO `db_gobierno`.`cargo` (`titulo`, `descripcion`) VALUES 
('Ministro', 'Responsable de un ministerio.'),
('Senador', 'Miembro del senado de la república.'),
('Gobernador', 'Autoridad del departamento.'),
('Alcalde', 'Autoridad de un municipio.'),
('Director', 'Responsable de una entidad gubernamental.'),
('Asesor', 'Profesional que brinda apoyo a un cargo.'),
('Jefe de oficina', 'Responsable de una oficina gubernamental.'),
('Inspector', 'Encargado de supervisar el cumplimiento de normas.'),
('Coordinador', 'Responsable de coordinar actividades.'),
('Secretario', 'Encargado de llevar la administración de un cargo.');

-- Inserciones en la tabla de entidades
INSERT INTO `db_gobierno`.`entidad` (`nombre_entidad`, `descripcion`, `tipo_entidad`) VALUES 
('Ministerio de Salud', 'Entidad responsable de la salud pública.', 'Nacional'),
('Ministerio de Educación', 'Encargado de la educación en el país.', 'Nacional'),
('Alcaldía de Medellín', 'Gobierno local de Medellín.', 'Local'),
('Gobernación de Antioquia', 'Gobierno departamental de Antioquia.', 'Regional'),
('Senado de la República', 'Cuerpo legislativo del país.', 'Nacional'),
('Cámara de Representantes', 'Cuerpo legislativo del país.', 'Nacional'),
('Ministerio de Transporte', 'Responsable de la infraestructura de transporte.', 'Nacional'),
('Ministerio de Justicia', 'Encargado de la justicia y el orden público.', 'Nacional'),
('Ministerio del Interior', 'Responsable de la seguridad y la convivencia.', 'Nacional'),
('Ministerio de Cultura', 'Encargado de la promoción cultural.', 'Nacional');

-- Inserciones en la tabla de asignación de cargos
INSERT INTO `db_gobierno`.`asignacion_cargo` (`persona_id`, `cargo_id`, `entidad_id`, `fecha_inicio`, `fecha_fin`, `estado`) VALUES 
(1, 1, 1, '2020-01-01', NULL, 'Activo'),
(2, 2, 5, '2019-05-01', '2023-01-01', 'Finalizado'),
(3, 3, 4, '2021-06-01', NULL, 'Activo'),
(4, 4, 2, '2018-04-01', '2023-05-01', 'Finalizado'),
(5, 5, 3, '2022-03-01', NULL, 'Activo'),
(6, 6, 6, '2021-01-01', NULL, 'Activo'),
(7, 7, 7, '2019-02-01', NULL, 'Activo'),
(8, 8, 8, '2020-08-01', NULL, 'Activo'),
(9, 9, 9, '2023-01-01', NULL, 'Activo'),
(10, 10, 10, '2022-06-01', NULL, 'Activo');

/* ================================ Procedimientos almacenados en la db =============================== */

DELIMITER $$

-- Procedimiento para seleccionar todos los registros de la tabla de género
CREATE PROCEDURE `db_gobierno`.`proc_select_genero`()
BEGIN 
    -- Selecciona todos los registros de la tabla `genero`
    SELECT * FROM `genero`;
END$$

-- Procedimiento para seleccionar todos los registros de la tabla de usuario
CREATE PROCEDURE `db_gobierno`.`proc_select_usuario`()
BEGIN 
    -- Selecciona todos los registros de la tabla `usuario`
    SELECT * FROM `usuario`;
END$$

-- Procedimiento para seleccionar todos los registros de la tabla de claves
CREATE PROCEDURE `db_gobierno`.`proc_select_clave`()
BEGIN 
    -- Selecciona todos los registros de la tabla `clave`
    SELECT * FROM `clave`;
END$$

-- Procedimiento para seleccionar todos los registros de la tabla de países
CREATE PROCEDURE `db_gobierno`.`proc_select_pais`()
BEGIN 
    -- Selecciona todos los registros de la tabla `pais`
    SELECT * FROM `pais`;
END$$

-- Procedimiento para seleccionar todos los registros de la tabla de estados
CREATE PROCEDURE `db_gobierno`.`proc_select_estado`()
BEGIN 
    -- Selecciona todos los registros de la tabla `estado`
    SELECT * FROM `estado`;
END$$

-- Procedimiento para seleccionar todos los registros de la tabla de ciudades
CREATE PROCEDURE `db_gobierno`.`proc_select_ciudad`()
BEGIN 
    -- Selecciona todos los registros de la tabla `ciudad`
    SELECT * FROM `ciudad`;
END$$

-- Procedimiento para seleccionar todos los registros de la tabla de personas
CREATE PROCEDURE `db_gobierno`.`proc_select_persona`()
BEGIN 
    -- Selecciona todos los registros de la tabla `persona`
    SELECT * FROM `persona`;
END$$

-- Procedimiento para seleccionar todos los registros de la tabla de teléfonos
CREATE PROCEDURE `db_gobierno`.`proc_select_telefono`()
BEGIN 
    -- Selecciona todos los registros de la tabla `telefono`
    SELECT * FROM `telefono`;
END$$

-- Procedimiento para seleccionar todos los registros de la tabla de cargos
CREATE PROCEDURE `db_gobierno`.`proc_select_cargo`()
BEGIN 
    -- Selecciona todos los registros de la tabla `cargo`
    SELECT * FROM `cargo`;
END$$

-- Procedimiento para seleccionar todos los registros de la tabla de entidades
CREATE PROCEDURE `db_gobierno`.`proc_select_entidad`()
BEGIN 
    -- Selecciona todos los registros de la tabla `entidad`
    SELECT * FROM `entidad`;
END$$

-- Procedimiento para seleccionar todos los registros de la tabla de asignación de cargo
CREATE PROCEDURE `db_gobierno`.`proc_select_asignacion_cargo`()
BEGIN
    SELECT * FROM `asignacion_cargo`;
END$$

CREATE PROCEDURE `db_gobierno`.`proc_update_genero`(
    IN p_genero_id INT,
    IN p_nombre_genero VARCHAR(50),
    IN p_descripcion VARCHAR(250)
)
BEGIN
    UPDATE `genero`
    SET 
        `nombre_genero` = p_nombre_genero,
        `descripcion` = p_descripcion,
        `fecha_creacion` = CURRENT_TIMESTAMP -- Este campo no debe ser actualizado si no se requiere
    WHERE `genero_id` = p_genero_id;
END$$

CREATE PROCEDURE `db_gobierno`.`proc_update_usuario`(
    IN p_user_id INT,
    IN p_username VARCHAR(50),
    IN p_password_hash VARCHAR(255),
    IN p_email VARCHAR(100)
)
BEGIN
    UPDATE `usuario`
    SET 
        `username` = p_username,
        `password_hash` = p_password_hash,
        `email` = p_email,
        `fecha_creacion` = CURRENT_TIMESTAMP -- Este campo no debe ser actualizado si no se requiere
    WHERE `user_id` = p_user_id;
END$$

CREATE PROCEDURE `db_gobierno`.`proc_update_persona`(
    IN p_persona_id INT,
    IN p_nombre_persona VARCHAR(100),
    IN p_apellido_persona VARCHAR(100),
    IN p_documento_identidad VARCHAR(50),
    IN p_genero_id INT,
    IN p_ciudad_id INT,
    IN p_fecha_nacimiento DATE,
    IN p_direccion_persona VARCHAR(255)
)
BEGIN
    UPDATE `persona`
    SET 
        `nombre_persona` = p_nombre_persona,
        `apellido_persona` = p_apellido_persona,
        `documento_identidad` = p_documento_identidad,
        `genero_id` = p_genero_id,
        `ciudad_id` = p_ciudad_id,
        `fecha_nacimiento` = p_fecha_nacimiento,
        `direccion_persona` = p_direccion_persona,
        `fecha_creacion` = CURRENT_TIMESTAMP -- Este campo no debe ser actualizado si no se requiere
    WHERE `persona_id` = p_persona_id;
END$$

CREATE PROCEDURE `db_gobierno`.`proc_update_cargo`(
    IN p_cargo_id INT,
    IN p_titulo VARCHAR(100),
    IN p_descripcion VARCHAR(255)
)
BEGIN
    UPDATE `cargo`
    SET 
        `titulo` = p_titulo,
        `descripcion` = p_descripcion,
        `fecha_creacion` = CURRENT_TIMESTAMP -- Este campo no debe ser actualizado si no se requiere
    WHERE `cargo_id` = p_cargo_id;
END$$

CREATE PROCEDURE `db_gobierno`.`proc_update_telefono`(
    IN p_telefono_id INT,
    IN p_tipo_telefono VARCHAR(50),
    IN p_numero_telefono VARCHAR(20)
)
BEGIN
    UPDATE `telefono`
    SET 
        `tipo_telefono` = p_tipo_telefono,
        `numero_telefono` = p_numero_telefono,
        `fecha_creacion` = CURRENT_TIMESTAMP -- Este campo no debe ser actualizado si no se requiere
    WHERE `telefono_id` = p_telefono_id;
END$$

CREATE PROCEDURE `db_gobierno`.`proc_update_asignacion_cargo`(
    IN p_asignacion_id INT,
    IN p_persona_id INT,
    IN p_cargo_id INT,
    IN p_entidad_id INT,
    IN p_fecha_inicio DATE,
    IN p_fecha_fin DATE,
    IN p_estado VARCHAR(50)
)
BEGIN
    UPDATE `asignacion_cargo`
    SET 
        `persona_id` = p_persona_id,
        `cargo_id` = p_cargo_id,
        `entidad_id` = p_entidad_id,
        `fecha_inicio` = p_fecha_inicio,
        `fecha_fin` = p_fecha_fin,
        `estado` = p_estado,
        `fecha_creacion` = CURRENT_TIMESTAMP -- Este campo no debe ser actualizado si no se requiere
    WHERE `asignacion_id` = p_asignacion_id;
END$$

-- Procedimiento para actualizar la tabla de claves
CREATE PROCEDURE `db_gobierno`.`proc_update_clave`(
    IN p_username VARCHAR(50), 
    IN p_token VARCHAR(255)
)
BEGIN
    UPDATE `db_gobierno`.`clave`
    SET `token` = p_token
    WHERE `username` = p_username;
END$$

-- Procedimiento para actualizar la tabla de países
CREATE PROCEDURE `db_gobierno`.`proc_update_pais`(
    IN p_pais_id INT, 
    IN p_nombre_pais VARCHAR(100), 
    IN p_descripcion VARCHAR(255)
)
BEGIN
    UPDATE `db_gobierno`.`pais`
    SET `nombre_pais` = p_nombre_pais, 
        `descripcion` = p_descripcion
    WHERE `pais_id` = p_pais_id;
END$$

-- Procedimiento para actualizar la tabla de estados
CREATE PROCEDURE `db_gobierno`.`proc_update_estado`(
    IN p_estado_id INT, 
    IN p_nombre_estado VARCHAR(100), 
    IN p_descripcion VARCHAR(255), 
    IN p_pais_id INT
)
BEGIN
    UPDATE `db_gobierno`.`estado`
    SET `nombre_estado` = p_nombre_estado, 
        `descripcion` = p_descripcion, 
        `pais_id` = p_pais_id
    WHERE `estado_id` = p_estado_id;
END$$

-- Procedimiento para actualizar la tabla de ciudades
CREATE PROCEDURE `db_gobierno`.`proc_update_ciudad`(
    IN p_ciudad_id INT, 
    IN p_nombre_ciudad VARCHAR(100), 
    IN p_descripcion VARCHAR(255), 
    IN p_estado_id INT
)
BEGIN
    UPDATE `db_gobierno`.`ciudad`
    SET `nombre_ciudad` = p_nombre_ciudad, 
        `descripcion` = p_descripcion, 
        `estado_id` = p_estado_id
    WHERE `ciudad_id` = p_ciudad_id;
END$$

-- Procedimiento para actualizar la tabla de entidades
CREATE PROCEDURE `db_gobierno`.`proc_update_entidad`(
    IN p_entidad_id INT, 
    IN p_nombre_entidad VARCHAR(100), 
    IN p_descripcion VARCHAR(255), 
    IN p_tipo_entidad VARCHAR(50)
)
BEGIN
    UPDATE `db_gobierno`.`entidad`
    SET `nombre_entidad` = p_nombre_entidad, 
        `descripcion` = p_descripcion, 
        `tipo_entidad` = p_tipo_entidad
    WHERE `entidad_id` = p_entidad_id;
END$$

-- Procedimiento para crear un registro en la tabla de género
CREATE PROCEDURE `db_gobierno`.`proc_insert_genero`(
    IN p_nombre_genero VARCHAR(50),
    IN p_descripcion VARCHAR(250)
)
BEGIN
    INSERT INTO `genero` (`nombre_genero`, `descripcion`, `fecha_creacion`)
    VALUES (p_nombre_genero, p_descripcion, CURRENT_TIMESTAMP);
END$$

-- Procedimiento para crear un registro en la tabla de usuario
CREATE PROCEDURE `db_gobierno`.`proc_insert_usuario`(
    IN p_username VARCHAR(50),
    IN p_password_hash VARCHAR(255),
    IN p_email VARCHAR(100)
)
BEGIN
    INSERT INTO `usuario` (`username`, `password_hash`, `email`, `fecha_creacion`)
    VALUES (p_username, p_password_hash, p_email, CURRENT_TIMESTAMP);
END$$

-- Procedimiento para crear un registro en la tabla de claves
CREATE PROCEDURE `db_gobierno`.`proc_insert_clave`(
    IN p_username VARCHAR(50), 
    IN p_token VARCHAR(255)
)
BEGIN
    INSERT INTO `clave` (`username`, `token`, `fecha_creacion`)
    VALUES (p_username, p_token, CURRENT_TIMESTAMP);
END$$

-- Procedimiento para crear un registro en la tabla de países
CREATE PROCEDURE `db_gobierno`.`proc_insert_pais`(
    IN p_nombre_pais VARCHAR(100), 
    IN p_descripcion VARCHAR(255)
)
BEGIN
    INSERT INTO `pais` (`nombre_pais`, `descripcion`, `fecha_creacion`)
    VALUES (p_nombre_pais, p_descripcion, CURRENT_TIMESTAMP);
END$$

-- Procedimiento para crear un registro en la tabla de estados
CREATE PROCEDURE `db_gobierno`.`proc_insert_estado`(
    IN p_nombre_estado VARCHAR(100), 
    IN p_descripcion VARCHAR(255), 
    IN p_pais_id INT
)
BEGIN
    INSERT INTO `estado` (`nombre_estado`, `descripcion`, `pais_id`, `fecha_creacion`)
    VALUES (p_nombre_estado, p_descripcion, p_pais_id, CURRENT_TIMESTAMP);
END$$

-- Procedimiento para crear un registro en la tabla de ciudades
CREATE PROCEDURE `db_gobierno`.`proc_insert_ciudad`(
    IN p_nombre_ciudad VARCHAR(100), 
    IN p_descripcion VARCHAR(255), 
    IN p_estado_id INT
)
BEGIN
    INSERT INTO `ciudad` (`nombre_ciudad`, `descripcion`, `estado_id`, `fecha_creacion`)
    VALUES (p_nombre_ciudad, p_descripcion, p_estado_id, CURRENT_TIMESTAMP);
END$$

-- Procedimiento para crear un registro en la tabla de personas
CREATE PROCEDURE `db_gobierno`.`proc_insert_persona`(
    IN p_nombre_persona VARCHAR(100),
    IN p_apellido_persona VARCHAR(100),
    IN p_documento_identidad VARCHAR(50),
    IN p_genero_id INT,
    IN p_ciudad_id INT,
    IN p_fecha_nacimiento DATE,
    IN p_direccion_persona VARCHAR(255)
)
BEGIN
    INSERT INTO `persona` 
        (`nombre_persona`, `apellido_persona`, `documento_identidad`, `genero_id`, `ciudad_id`, `fecha_nacimiento`, `direccion_persona`, `fecha_creacion`)
    VALUES 
        (p_nombre_persona, p_apellido_persona, p_documento_identidad, p_genero_id, p_ciudad_id, p_fecha_nacimiento, p_direccion_persona, CURRENT_TIMESTAMP);
END$$

-- Procedimiento para crear un registro en la tabla de teléfonos
CREATE PROCEDURE `db_gobierno`.`proc_insert_telefono`(
    IN p_tipo_telefono VARCHAR(50),
    IN p_numero_telefono VARCHAR(20)
)
BEGIN
    INSERT INTO `telefono` (`tipo_telefono`, `numero_telefono`, `fecha_creacion`)
    VALUES (p_tipo_telefono, p_numero_telefono, CURRENT_TIMESTAMP);
END$$

-- Procedimiento para crear un registro en la tabla de cargos
CREATE PROCEDURE `db_gobierno`.`proc_insert_cargo`(
    IN p_titulo VARCHAR(100),
    IN p_descripcion VARCHAR(255)
)
BEGIN
    INSERT INTO `cargo` (`titulo`, `descripcion`, `fecha_creacion`)
    VALUES (p_titulo, p_descripcion, CURRENT_TIMESTAMP);
END$$

-- Procedimiento para crear un registro en la tabla de entidades
CREATE PROCEDURE `db_gobierno`.`proc_insert_entidad`(
    IN p_nombre_entidad VARCHAR(100),
    IN p_descripcion VARCHAR(255),
    IN p_tipo_entidad VARCHAR(50)
)
BEGIN
    INSERT INTO `entidad` (`nombre_entidad`, `descripcion`, `tipo_entidad`, `fecha_creacion`)
    VALUES (p_nombre_entidad, p_descripcion, p_tipo_entidad, CURRENT_TIMESTAMP);
END$$

-- Procedimiento para crear un registro en la tabla de asignación de cargos
CREATE PROCEDURE `db_gobierno`.`proc_insert_asignacion_cargo`(
    IN p_persona_id INT,
    IN p_cargo_id INT,
    IN p_entidad_id INT,
    IN p_fecha_inicio DATE,
    IN p_fecha_fin DATE,
    IN p_estado VARCHAR(50)
)
BEGIN
    INSERT INTO `asignacion_cargo` 
        (`persona_id`, `cargo_id`, `entidad_id`, `fecha_inicio`, `fecha_fin`, `estado`, `fecha_creacion`)
    VALUES 
        (p_persona_id, p_cargo_id, p_entidad_id, p_fecha_inicio, p_fecha_fin, p_estado, CURRENT_TIMESTAMP);
END$$

-- Procedimiento para eliminar un registro en la tabla de género
CREATE PROCEDURE `db_gobierno`.`proc_delete_genero`(
    IN p_genero_id INT
)
BEGIN
    DELETE FROM `genero`
    WHERE `genero_id` = p_genero_id;
END$$

-- Procedimiento para eliminar un registro en la tabla de usuario
CREATE PROCEDURE `db_gobierno`.`proc_delete_usuario`(
    IN p_user_id INT
)
BEGIN
    DELETE FROM `usuario`
    WHERE `user_id` = p_user_id;
END$$

-- Procedimiento para eliminar un registro en la tabla de claves
CREATE PROCEDURE `db_gobierno`.`proc_delete_clave`(
    IN p_username VARCHAR(50)
)
BEGIN
    DELETE FROM `clave`
    WHERE `username` = p_username;
END$$

-- Procedimiento para eliminar un registro en la tabla de países
CREATE PROCEDURE `db_gobierno`.`proc_delete_pais`(
    IN p_pais_id INT
)
BEGIN
    DELETE FROM `pais`
    WHERE `pais_id` = p_pais_id;
END$$

-- Procedimiento para eliminar un registro en la tabla de estados
CREATE PROCEDURE `db_gobierno`.`proc_delete_estado`(
    IN p_estado_id INT
)
BEGIN
    DELETE FROM `estado`
    WHERE `estado_id` = p_estado_id;
END$$

-- Procedimiento para eliminar un registro en la tabla de ciudades
CREATE PROCEDURE `db_gobierno`.`proc_delete_ciudad`(
    IN p_ciudad_id INT
)
BEGIN
    DELETE FROM `ciudad`
    WHERE `ciudad_id` = p_ciudad_id;
END$$

-- Procedimiento para eliminar un registro en la tabla de personas
CREATE PROCEDURE `db_gobierno`.`proc_delete_persona`(
    IN p_persona_id INT
)
BEGIN
    DELETE FROM `persona`
    WHERE `persona_id` = p_persona_id;
END$$

-- Procedimiento para eliminar un registro en la tabla de teléfonos
CREATE PROCEDURE `db_gobierno`.`proc_delete_telefono`(
    IN p_telefono_id INT
)
BEGIN
    DELETE FROM `telefono`
    WHERE `telefono_id` = p_telefono_id;
END$$

-- Procedimiento para eliminar un registro en la tabla de cargos
CREATE PROCEDURE `db_gobierno`.`proc_delete_cargo`(
    IN p_cargo_id INT
)
BEGIN
    DELETE FROM `cargo`
    WHERE `cargo_id` = p_cargo_id;
END$$

-- Procedimiento para eliminar un registro en la tabla de entidades
CREATE PROCEDURE `db_gobierno`.`proc_delete_entidad`(
    IN p_entidad_id INT
)
BEGIN
    DELETE FROM `entidad`
    WHERE `entidad_id` = p_entidad_id;
END$$

-- Procedimiento para eliminar un registro en la tabla de asignación de cargos
CREATE PROCEDURE `db_gobierno`.`proc_delete_asignacion_cargo`(
    IN p_asignacion_id INT
)
BEGIN
    DELETE FROM `asignacion_cargo`
    WHERE `asignacion_id` = p_asignacion_id;
END$$

DELIMITER ;