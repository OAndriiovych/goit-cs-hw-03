--1
SELECT * FROM tasks WHERE user_id = 1;
--2
SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new');
--3
UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = 1;
--4
SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);
--4
INSERT INTO tasks (title, description, status_id, user_id) VALUES ('New Task', 'Task Description', (SELECT id FROM status WHERE name = 'new'), 1);
--5
SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed');
--6
DELETE FROM tasks WHERE id = 1;
--7
SELECT * FROM users WHERE email LIKE '%@gmail.com';
--8
UPDATE users SET fullname = 'New Name' WHERE id = 1;
--9
SELECT s.name, COUNT(t.id) AS task_count
FROM status s
LEFT JOIN tasks t ON s.id = t.status_id
GROUP BY s.name;
--10
SELECT t.*
FROM tasks t
JOIN users u ON t.user_id = u.id
WHERE u.email LIKE '%@example.com';
--11
SELECT * FROM tasks WHERE description IS NULL OR description = '';
--12
SELECT u.fullname, t.*
FROM users u
INNER JOIN tasks t ON u.id = t.user_id
WHERE t.status_id = (SELECT id FROM status WHERE name = 'in progress');
--13
SELECT u.fullname, COUNT(t.id) AS task_count
FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.fullname;
