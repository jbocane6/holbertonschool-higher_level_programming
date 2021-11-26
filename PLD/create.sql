-- Script that creates low range insurance DB
CREATE DATABASE IF NOT EXISTS low_range_insurance;
USE low_range_insurance;

-- Script that creates table of employee
CREATE TABLE IF NOT EXISTS tb_employee
(id INT PRIMARY KEY,
name VARCHAR(256) NOT NULL);

-- Script that creates client table
CREATE TABLE IF NOT EXISTS tb_customer
(id INT PRIMARY KEY,
name VARCHAR(256) NOT NULL,
id_employee INT NOT NULL,
city VARCHAR(256) NOT NULL,
FOREIGN KEY (id_employee) REFERENCES tb_employee(id));

-- Script that creates car table
CREATE TABLE IF NOT EXISTS tb_car
(plate_id CHAR(6) PRIMARY KEY,
id_customer INT NOT NULL,
status ENUM('Used', 'New') NOT NULL,
FOREIGN KEY (id_customer) REFERENCES tb_customer(id));

-- Script that creates insurance table
CREATE TABLE IF NOT EXISTS tb_insurance
(insurance_id INT PRIMARY KEY,
id_customer INT NOT NULL,
plate_car CHAR(6) NOT NULL,
id_employee INT NOT NULL,
date_start DATE NOT NULL,
date_end DATE NOT NULL,
FOREIGN KEY (id_employee) REFERENCES tb_employee(id),
FOREIGN KEY (id_customer) REFERENCES tb_customer(id),
FOREIGN KEY (plate_car) REFERENCES tb_car(plate_id));

-- Queries
-- Insert Values
INSERT INTO tb_employee VALUES
    (10125326, "ANDRES ALVAREZ"),
    (10268551, "JOSE FLORES"),
    (10654351, "CARLOS CARDENAS"),
    (16541357, "DAVID MARQUEZ");

INSERT INTO tb_customer VALUES
    (68215675, "MARCELA RUIZ", 10125326, "Bogotá"),
    (68253468, "MARIA GARCIA", 10268551, "Cali"),
    (69413416, "MONICA DIAZ", 10654351, "Medellin"),
    (63216841, "LUISA LOPEZ", 16541357, "Bogotá");

INSERT INTO tb_car VALUES
    ("WMF958", 68215675, 'Used'),
    ("OIJ651", 68253468, 'New'),
    ("FOS023", 69413416, 'New'),
    ("XGP745", 63216841, 'Used');

INSERT INTO tb_insurance VALUES
    (001, 68215675, "WMF958", 10125326, "2021-12-05", "2022-12-05"),
    (002, 68253468, "OIJ651", 10268551, "2021-06-20", "2021-12-20"),
    (003, 69413416, "FOS023", 10654351, "2021-03-31", "2022-03-31"),
    (004, 63216841, "XGP745", 16541357, "2021-01-06", "2022-01-12");

-- Update Values
UPDATE tb_employee SET name="ANDRES ROJAS" WHERE id = 10125326;
UPDATE tb_employee SET name="JOSE MARTINEZ" WHERE id = 10268551;
UPDATE tb_employee SET name="CARLOS OSORIO" WHERE id = 10654351;
UPDATE tb_employee SET name="DAVID LOPEZ" WHERE id = 16541357;

UPDATE tb_customer SET name="CAROLINA RUIZ" WHERE id = 68215675;
UPDATE tb_customer SET name="MARIA ALVAREZ" WHERE id = 68253468;
UPDATE tb_customer SET name="ANGELY DIAZ" WHERE id = 69413416;
UPDATE tb_customer SET name="LUISA CASTIBLANCO" WHERE id = 63216841;

UPDATE tb_car SET status='New' WHERE plate_id = "WMF958";
UPDATE tb_car SET status='Used' WHERE plate_id = "OIJ651";
UPDATE tb_car SET status='Used' WHERE plate_id = "FOS023";
UPDATE tb_car SET status='New' WHERE plate_id = "XGP745";

UPDATE tb_insurance SET date_end="12-05-2023" WHERE insurance_id = "001";
UPDATE tb_insurance SET date_end="20-06-2023" WHERE insurance_id = "002";
UPDATE tb_insurance SET date_end="31-03-2023" WHERE insurance_id = "003";
UPDATE tb_insurance SET date_end="01-06-2023" WHERE insurance_id = "004";

-- Delete Values
DELETE FROM tb_insurance WHERE insurance_id = 004;
DELETE FROM tb_car WHERE plate_id = 'XGP745';
DELETE FROM tb_customer WHERE ID = 63216841;
DELETE FROM tb_employee WHERE ID = 16541357;

-- Show all
SELECT * FROM tb_employee;

SELECT tb_customer.id, tb_customer.name, tb_customer.city, tb_employee.name AS seller
FROM tb_customer
INNER JOIN tb_employee ON tb_customer.id_employee = tb_employee.id;

SELECT tb_car.plate_id, tb_car.status, tb_customer.name AS owner FROM tb_car
INNER JOIN tb_customer ON tb_car.id_customer = tb_customer.id;

SELECT tb_insurance.insurance_id, tb_customer.id AS owner, tb_car.plate_id AS plate, tb_insurance.date_start, tb_insurance.date_end, tb_employee.id AS seller FROM tb_insurance
INNER JOIN tb_customer ON tb_insurance.id_customer = tb_customer.id,
INNER JOIN tb_car ON tb_insurance.plate_car = tb_car.plate_id,
INNER JOIN tb_employee ON tb_insurance.id_employee = tb_employee.id;

-- Show unique
SELECT * FROM tb_employee WHERE id = 10268551;

SELECT tb_customer.id, tb_customer.name, tb_customer.city, tb_employee.name AS seller
FROM tb_customer
INNER JOIN tb_employee ON tb_customer.id_employee = tb_employee.id
WHERE tb_customer.name = "MONICA DIAZ";

SELECT tb_car.plate_id, tb_car.status, tb_customer.name AS owner FROM tb_car
INNER JOIN tb_customer ON tb_car.id_customer = tb_customer.id
WHERE tb_car.plate_id="FOS023";