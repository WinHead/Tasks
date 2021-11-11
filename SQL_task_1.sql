-- Вывести отсортированный по количеству перелетов (по убыванию) и имени (по возрастанию) список пассажиров, совершивших хотя бы 1 полет.

SELECT name, COUNT(Pass_in_trip.trip) as count
FROM Passenger INNER JOIN Pass_in_trip
ON Passenger.id = Pass_in_trip.passenger
GROUP BY Passenger.name
ORDER BY count DESC, name
