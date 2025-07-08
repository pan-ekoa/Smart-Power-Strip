CREATE DATABASE IF NOT EXISTS device_monitoring
    DEFAULT CHARACTER SET = 'utf8mb4';

USE device_monitoring;

CREATE TABLE IF NOT EXISTS device_properties (
    id INT AUTO_INCREMENT PRIMARY KEY,
    device_id INT NOT NULL,
    voltage FLOAT NOT NULL,
    current FLOAT NOT NULL,
    power FLOAT NOT NULL,
    electricity FLOAT NOT NULL,
    control_signal TINYINT(1) NOT NULL,
    event_time DATETIME NOT NULL,
    record_time DATETIME NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX (device_id),
    INDEX (event_time)
);