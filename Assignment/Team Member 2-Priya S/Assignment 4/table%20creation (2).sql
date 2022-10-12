CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address1 varchar(255),
    City varchar(255)
);

CREATE TABLE Persons1 (
    MemberID int,
    name1 varchar(255),
    district varchar(255),
    Village varchar(255)
);

CREATE TABLE Persons2 (
    phone int,
    about varchar(255),
    firstname varchar(255),
     kuttyname varchar(255),
    City varchar(255)
);

CREATE TABLE Persons3 (
   sno int,
    comment1 varchar(255),
    mothername varchar(255),
    fathername varchar(255) 
);

CREATE TABLE Persons4 (
    
    sistername varchar(255),
    brothername varchar(255),
    grandpaname varchar(255)
    
);


INSERT INTO persons VALUES ('1' ,'Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavange');
INSERT INTO persons VALUES ('2' ,'pradeesh', 'Toper', 'class leader', 'xman');

UPDATE persons
SET Lastname = 'gopinath', FirstName = 'manikandan'
WHERE     PersonID = 1;

DELETE FROM persons WHERE firstname='manikandan';
