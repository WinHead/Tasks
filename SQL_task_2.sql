--Сколько времени обучающийся будет находиться в школе, учась со 2-го по 4-ый уч. предмет ?

SELECT TIMEDIFF((SELECT end_pair FROM Timepair WHERE id = 4), (SELECT start_pair FROM Timepair WHERE id = 2)) AS time
FROM Timepair
LIMIT 1
