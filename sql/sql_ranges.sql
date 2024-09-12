-- Create Ranges Table --
CREATE TABLE ranges(
ID INT AUTO_INCREMENT PRIMARY KEY,
start INT,
end INT,
counter INT)

--- INSERT RANGES INTO THE TABLE --
insert into ranges
values (1, 1000, 1250, 1000),(2,1250,1500,1250),(3,1500,1750,1500),(4,1750,2000,1750)
