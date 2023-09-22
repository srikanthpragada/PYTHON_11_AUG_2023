CREATE TABLE employees (
    Id       INTEGER      PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR (30) NOT NULL,
    job      VARCHAR (10),
    salary   INTEGER (10) CHECK(salary > 100000)
);

insert into employees(fullname,job,salary) values('Andy Roberts','SP',1500000);
insert into employees(fullname,job,salary)  values('Larry Ellison','PL',3500000);
insert into employees(fullname,job,salary)  values('James Gosling','TL',2500000);