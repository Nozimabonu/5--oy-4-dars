#Misol-1

create schema if not exists update;
set search_path = update;

create table if not exists categories
(
    id     serial primary key,
    title  varchar(120),
    amount int not null
);

insert into categories(title, amount)
values ('Muzlatkich', 2),
       ('Konditsaner', 3),
       ('Naushnik', 4);



create table if not exists products
(
    id          serial primary key,
    madel        varchar(100) not null,
    price       int          not null,
    category_id int references categories (id)

);

insert into products(madel, price, category_id)
values ('Samsung', 150, 1),
       ('Shivaki', 500, 1),
       ('Hoco W35', 200, 3),
       ('Roison', 400, 2),
       ('Loretto', 160, 1),
       ('Artel', 300, 2);

update products
set price = price + price * amount
from categories
where products.category_id = categories.id;

delete
from products
where id = 6;

#Misol-2

create table person
(
    id        serial primary key,
    full_name varchar(100) not null,
    age       int          not null
);

insert into person(full_name, age)
values ('Samandarova Shirin', 14),
       ('Mirzayeva Osiyo', 5),
       ('Hamidova Nozimabonu', 16);

update public.person
set name = 'Sadiya'
where id = 5;


insert into person(id, full_name, age)
values (1, 'Ali Aliyev', 20)
on conflict (id) do update set id = 7;


drop table inventory;

CREATE TABLE inventory
(
    id       INT PRIMARY KEY,
    name     VARCHAR(255)   NOT NULL,
    price    DECIMAL(10, 2) NOT NULL,
    quantity INT            NOT NULL
);

INSERT INTO inventory(id, name, price, quantity)
VALUES (1, 'Ali', 15.99, 100),
       (2, 'Bonu', 25.49, 50),
       (3, 'Sadiya', 19.95, 75);


insert into inventory(id, name, price, quantity)
values (4, 'Ali', 25.99, 245)
on conflict (id) do update set price    = excluded.price,
                               quantity = excluded.quantity;
