CREATE TABLE user (
    email varchar(255),
    username varchar(255),
    rollnumber int,
    password1 varchar(255)
);


INSERT INTO user VALUES ('xyz@gmail.com' ,'gopi', '1923', 'Skagen');
INSERT INTO user VALUES ('x@gmail.com' ,'mani', '192', 'Skaen');
INSERT INTO user VALUES ('xy@gmail.com' ,'pradessh', '19', 'Sagen');



UPDATE user
SET  username = 'pradeeshuuuu'
WHERE email = 'xy@gmail.com';

DELETE FROM user WHERE email='xyz@gmail.com';
