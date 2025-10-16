-- Create the database
CREATE DATABASE IF NOT EXISTS car_details;
USE car_details;

-- Create the table
CREATE TABLE car_details (
    Client_Name VARCHAR(20),
    Client_Number_plate VARCHAR(20),
    Client_Car_Company VARCHAR(20),
    Service_Date DATE,
    Delivery_Date_After_Service DATE
);