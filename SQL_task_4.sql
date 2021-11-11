-- Какой(ие) кабинет(ы) пользуются самым большим спросом?

SELECT classroom 
FROM Schedule
GROUP BY classroom
HAVING COUNT(classroom) = 
(SELECT COUNT(classroom) 
FROM Schedule 
GROUP BY classroom
ORDER BY COUNT(classroom) DESC 
LIMIT 1)
     
