## User Stories

## Implemented
* As a riding school teacher I want to create lessons so that customers can apply for them.

```sql
INSERT INTO Lesson (id, day, start_time, end_time, price, skill_level, type_of_lesson) 
VALUES (1, "01-01-2020", "11:00", "12:00", "40", "easy", "Dressage");
```

* As a riding shool teacher I want to see people that have applied to lesson so that name of the rider and name of the horse is visible.

```sql
SELECT Lesson.id, Lesson.day, Account.name, Horse.name FROM Lesson
LEFT OUTER JOIN horse_rider_lesson ON Lesson.id = horse_rider_lesson.lesson_id
LEFT OUTER JOIN account ON horse_rider_lesson.account_id = Account.id
LEFT OUTER JOIN horse ON horse_rider_lesson.horse_id = Horse.id
ORDER BY Lesson.id;
```

* As a riding school teacher I want to give horses to lesson applicants so that level of horse, lesson and rider is compatible.

```sql
INSERT INTO horse_rider_lesson (rider_id, lesson_id) VALUES (2, 2);
UPDATE horse_rider_lesson SET horse_id=1 WHERE rider_id=2;
```

* As a riding school customer I want to apply for riding lesson so that I see when the riding lesson is.
```sql
INSERT INTO horse_rider_lesson (rider_id, lesson_id) VALUES (1, 2);
SELECT Lesson.day, Lesson.start_time, Lesson.end_time FROM Lesson
LEFT OUTER JOIN horse_rider_lesson ON Lesson.id = horse_rider_lesson.lesson_id
LEFT OUTER JOIN account ON horse_rider_lesson.account_id = Account.id
WHERE Account.id=1;
```

* As a riding school customer I want to see statistics of my riding lessons so that they are accurate.

```sql
SELECT Horse.id, Horse.name, Horse.breed, Horse.gender, COUNT(Account.id) FROM Horse
LEFT OUTER JOIN horse_rider_lesson ON Horse.id = horse_rider_lesson.horse_id
LEFT OUTER JOIN account ON horse_rider_lesson.account_id = account.id
WHERE Account.id = 1"
GROUP BY Horse.id;
```



