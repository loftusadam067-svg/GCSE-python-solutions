-- Year: 2023 | Question: Q6(d) | Marks: 3
-- Description: Return SensorID from events where SensorType is Door and Length exceeds 20.

SELECT SensorID FROM TblEvents WHERE SensorType = "Door" AND Length > 20;
