-- Выведите список комнат, которые были зарезервированы в течение 12 недели 2020 года.

SELECT Rooms.*
FROM Rooms INNER JOIN Reservations
ON Rooms.id = Reservations.room_id
WHERE YEAR(Reservations.start_date) = 2020 AND WEEK(start_date, 1) = 12
