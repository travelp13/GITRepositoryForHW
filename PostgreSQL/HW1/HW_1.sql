CREATE TABLE IF NOT EXISTS USERS (
	ID SERIAL PRIMARY KEY,
	NAME TEXT NOT NULL,
	AGE INT NOT NULL,
	GENDER TEXT NOT NULL,
	NATIONALITY TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS EMAILS (
	ID SERIAL PRIMARY KEY,
	USER_ID INT NOT NULL,
	EMAIL TEXT,
	FOREIGN KEY (USER_ID) REFERENCES USERS (ID)
);

CREATE TABLE IF NOT EXISTS POSTS (
	ID SERIAL PRIMARY KEY,
	USER_ID INT NOT NULL,
	TITLE TEXT NOT NULL,
	DESCRIPTION TEXT NOT NULL,
	FOREIGN KEY (USER_ID) REFERENCES USERS (ID)
);

CREATE TABLE IF NOT EXISTS LIKES (
	ID SERIAL PRIMARY KEY,
	USER_ID INT NOT NULL,
	POST_ID INT NOT NULL,
	FOREIGN KEY (USER_ID) REFERENCES USERS (ID),
	FOREIGN KEY (POST_ID) REFERENCES POSTS (ID)
);

CREATE TABLE IF NOT EXISTS COMMENTS (
	ID SERIAL PRIMARY KEY,
	USER_ID INT NOT NULL,
	POST_ID INT NOT NULL,
	TEXT TEXT,
	FOREIGN KEY (USER_ID) REFERENCES USERS (ID),
	FOREIGN KEY (POST_ID) REFERENCES POSTS (ID)
);
-----------------------------------------------------------------------------------------------------
INSERT INTO USERS (NAME, AGE, GENDER, NATIONALITY)
VALUES 
    ('Олександр', 30, 'Чоловіча', 'Українська'),
    ('Марія', 25, 'Жіноча', 'Українська'),
    ('Віталій', 40, 'Чоловіча', 'Українська'),
    ('Ірина', 35, 'Жіноча', 'Українська');

INSERT INTO EMAILS (USER_ID, EMAIL)
VALUES
    (1, 'oleksandr@gmail.com'),
    (2, 'maria@gmail.com'),
    (3, 'vitaliy@gmail.com'),
    (4, 'iryna@gmail.com'),
	(1, 'oleksandr_new@gmail.com');

INSERT INTO POSTS (USER_ID, TITLE, DESCRIPTION)
VALUES
    (1, 'Перший пост Олександра', 'Це мій перший пост!'),
    (1, 'Другий пост Олександра', 'Це мій другий пост!'),
    (1, 'Третій пост Олександра', 'Це мій третій пост!');

INSERT INTO POSTS (USER_ID, TITLE, DESCRIPTION)
VALUES
    (2, 'Перший пост Марії', 'Це мій перший пост!'),
    (2, 'Другий пост Марії', 'Це мій другий пост!'),
    (2, 'Третій пост Марії', 'Це мій третій пост!');
	
INSERT INTO POSTS (USER_ID, TITLE, DESCRIPTION)
VALUES
    (3, 'Перший пост Віталія', 'Це мій перший пост!'),
    (3, 'Другий пост Віталія', 'Це мій другий пост!'),
    (3, 'Третій пост Віталія', 'Це мій третій пост!');

INSERT INTO POSTS (USER_ID, TITLE, DESCRIPTION)
VALUES
    (4, 'Перший пост Ірини', 'Це мій перший пост!'),
    (4, 'Другий пост Ірини', 'Це мій другий пост!'),
    (4, 'Третій пост Ірини', 'Це мій третій пост!');

INSERT INTO LIKES (USER_ID, POST_ID)
VALUES
    (1, 4),
    (1, 7),
	(3, 10),
	(1, 10),
    (2, 1);

INSERT INTO COMMENTS (USER_ID, POST_ID, TEXT)
VALUES
    (1, 4, 'Цікаво!');

INSERT INTO COMMENTS (USER_ID, POST_ID, TEXT)
VALUES
    (2, 1, 'Цікаво!');

INSERT INTO COMMENTS (USER_ID, POST_ID, TEXT)
VALUES
    (3, 10, 'Цікаво!');
	
-----------------------------------------------------------------------------------------------------
SELECT
	U.ID,
	U.NAME,
	U.AGE,
	U.GENDER,
	U.NATIONALITY,
	E.EMAIL,
	P.TITLE,
	P.DESCRIPTION,
	COALESCE(L.CNT, 0) AS COUNT_LIKES,
	COALESCE(C.CNT, 0) AS COUNT_COMMENTS
FROM
	USERS U
	LEFT JOIN (
		SELECT
			USER_ID,
			EMAIL
		FROM
			(
				SELECT
					USER_ID,
					EMAIL,
					ROW_NUMBER() OVER (
						PARTITION BY
							USER_ID
						ORDER BY
							ID DESC
					) AS RN
				FROM
					EMAILS
			)
		WHERE
			RN = 1
	) E ON E.USER_ID = U.ID
	LEFT JOIN POSTS P ON P.USER_ID = U.ID
	LEFT JOIN (
		SELECT
			COUNT(*) AS CNT,
			POST_ID
		FROM
			LIKES
		GROUP BY
			POST_ID
	) L ON L.POST_ID = P.ID
	LEFT JOIN (
		SELECT
			COUNT(*) AS CNT,
			POST_ID
		FROM
			COMMENTS
		GROUP BY
			POST_ID
	) C ON C.POST_ID =P.ID;