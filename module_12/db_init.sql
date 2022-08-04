drop database if exists whatabook;

create database whatabook;

use whatabook;

drop table if exists whishlist;
drop table if exists user;
drop table if exists book;
drop table if exists store;


CREATE TABLE  store  (
   Store_id  int NOT NULL,
   locale  varchar(500) NOT NULL,
  PRIMARY KEY ( Store_id )
) ;



CREATE TABLE  book  (
   book_id  int NOT NULL AUTO_INCREMENT,
   book_name  varchar(200) NOT NULL,
   details  varchar(500),
   Author varchar(200) not null ,
  PRIMARY KEY ( book_id )
) ;



CREATE TABLE  user  (
   User_id  int NOT NULL AUTO_INCREMENT,
   first_name  varchar(75) NOT NULL,
   last_name  varchar(75) NOT NULL,
  PRIMARY KEY ( User_id )
);

CREATE TABLE  wishlist  (
   wishlist_id  int NOT NULL AUTO_INCREMENT,
   user_id  int NOT NULL,
   book_id  int NOT NULL,
  PRIMARY KEY ( wishlist_id ),
  CONSTRAINT  wishlist_ibfk_1  FOREIGN KEY ( user_id ) REFERENCES  user  ( User_id ),
  CONSTRAINT  wishlist_ibfk_2  FOREIGN KEY ( book_id ) REFERENCES  book  ( book_id )
) ;

Insert into store(Store_id, locale) values(1, '125 Ashley Ave, NYC, NY, 23456');


Insert into Book (Book_name, author) values('Introduction to Database', 'Rama Krishnan');
Insert into Book(Book_name,  details, author) values('The Dogman Unleashed', 'Second Book of Dogman','Dav Picker');
Insert into Book(Book_name, author) values('Sams Teach Yourself SQL', 'Ben Forta');
Insert into Book(Book_name, details, author) values ('The complete Reference Java', 'Second Edition' ,'Herbert  Schildt');
Insert into Book(book_name, details, author) values ('NoSQL Distilled', 'A Brief Guide to the Emerging World of Polyglot Persistence','Martin Fowler');
Insert into Book(book_name, author) values ('Successful Project Management', 'Jack Gido');
Insert into Book(book_name, details, author) values('The Data warehouse Took kit','The definitive Guide to Dimensional Modeling','Ralph kimball');
Insert into Book(book_name, author) values ('Introduction to Networking',' Charles R.Severance');
Insert into Book(book_name, details, author) values ('Data Analytics','A Deconstructed Guide to Data Literacy','Oliver Theohald');




Insert into User(first_name, last_name) values ('John','Blake');
Insert into User(first_name, last_name) values ('Mary','Lee');
Insert into User(first_name, last_name) values ('Sandra','Ade');




Insert into wishlist (user_id, book_id) values ((select user_id from user where first_name = 'John' and last_name = 'Blake'),(select book_id from book where book_name = 'Introduction to Database'));
Insert into wishlist (user_id, book_id) values ((select user_id from user where first_name = 'Mary' and last_name = 'Lee'),(select book_id from book where book_name = 'NoSQL Distilled'));
Insert into wishlist (user_id, book_id) values ((select user_id from user where first_name = 'Sandra' and last_name = 'Ade'),(select book_id from book where book_name = 'Successful Project Management'));
