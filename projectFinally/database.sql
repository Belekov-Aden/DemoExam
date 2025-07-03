create database demo;


use demo;

create table categories
(
    id   integer primary key auto_increment,
    name varchar(255) not null unique
);


create table products
(
    id         integer primary key auto_increment,
    name       varchar(255) not null unique,
    categories integer      not null,
    price      float        not null,
    count      integer      not null,
    constraint fk_products_categroies foreign key (categories) references categories (id)
        ON DELETE CASCADE
);


INSERT INTO demo.categories (name)
VALUES ('Спортивные');
INSERT INTO demo.categories (name)
VALUES ('Техника');
INSERT INTO demo.categories (name)
VALUES ('Для дома');

