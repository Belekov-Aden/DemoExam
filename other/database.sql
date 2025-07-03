create table type_products
(
    id          int  not null
        constraint type_products_pk
            primary key autoincrement,
    type        TEXT not null,
    coefficient real not null
);

create table products
(
    id integer primary key autoincrement,
    type integer not null,
    name text not null,
    article text not null,
    price real not null,
    foreign key (type) references type_products(id)
);


create table partners
(
    id integer primary key autoincrement,
    type_partner varchar not null,
    name varchar not null,
    director varchar not null,
    email varchar not null,
    phone varchar not null,
    address varchar not null,
    inn integer not null,
    raiting integer not null
);

create table sales
(
    id integer primary key autoincrement,
    product integer not null,
    partner integer not null,
    count_product integer not null,
    date_sale date not null,
    foreign key (product) references products(id),
    foreign key (partner) references partners(id)
);

INSERT INTO type_products (id, type, coefficient) VALUES (null, 'Ламинат', 2)
INSERT INTO type_products (id, type, coefficient) VALUES (null, 'Массивная доска', 5)
INSERT INTO type_products (id, type, coefficient) VALUES (null, 'Паркетная доска', 4)
INSERT INTO type_products (id, type, coefficient) VALUES (null, 'Пробковое покрытие', 1)

INSERT INTO products (type, name, article, price)
VALUES (3, 'Паркетная доска Ясень темный однополосная 14 мм', '8758385', 4456);
INSERT INTO products (type, name, article, price)
VALUES (3, 'Инженерная доска Дуб Французская елка однополосная 12 мм', '8858958', 7330);
INSERT INTO products (type, name, article, price)
VALUES (1, 'Ламинат Дуб дымчато-белый 33 класс 12 мм', '7750282', 1799);
INSERT INTO products (type, name, article, price)
VALUES (1, 'Ламинат Дуб серый 32 класс 8 мм с фаской', '7028748', 3890);
INSERT INTO products (type, name, article, price)
VALUES (4, 'Пробковое напольное клеевое покрытие 32 класс 4 мм', '5012543', 5450);



INSERT INTO partners (type_partner, name, director, email, phone, address, inn, raiting)
VALUES ('ЗАО', 'База Строитель', 'Иванова Александра Ивановна', 'aleksandraivanova@ml.ru', '493 123 45 67',
        '652050, Кемеровская область, город Юрга, ул. Лесная, 15', 2222455179, 7);

INSERT INTO partners (type_partner, name, director, email, phone, address, inn, raiting)
VALUES ('ООО', 'Паркет 29', 'Петров Василий Петрович', 'vppetrov@vl.ru', '987 123 56 78',
        '164500, Архангельская область, город Северодвинск, ул. Строителей, 18', 3333888520, 7);

INSERT INTO partners (type_partner, name, director, email, phone, address, inn, raiting)
VALUES ('ПАО', 'Стройсервис', 'Соловьев Андрей Николаевич', 'ansolovev@st.ru', '812 223 32 00',
        '188910, Ленинградская область, город Приморск, ул. Парковая, 21', 4440391035, 7);

INSERT INTO partners (type_partner, name, director, email, phone, address, inn, raiting)
VALUES ('ОАО', 'Ремонт и отделка', 'Воробьева Екатерина Валерьевна', 'ekaterina.vorobeva@ml.ru', '444 222 33 11', '143960, Московская область, город Реутов, ул. Свободы, 51
', 1111520857, 5);

INSERT INTO partners (type_partner, name, director, email, phone, address, inn, raiting)
VALUES ('ЗАО', 'МонтажПро', 'Степанов Степан Сергеевич', 'stepanov@stepan.ru', '912 888 33 33',
        '309500, Белгородская область, город Старый Оскол, ул. Рабочая, 122', 5552431140, 10);

INSERT INTO sales (product, partner, count_product, date_sale)
VALUES (3, 1, 15500, '23.03.2023');

INSERT INTO sales (product, partner, count_product, date_sale)
VALUES (3, 1, 12350, '18.12.2023');

INSERT INTO sales (product, partner, count_product, date_sale)
VALUES (4, 1, 37400, '07.06.2024');

INSERT INTO sales (product, partner, count_product, date_sale)
VALUES (2, 2, 35000, '02.12.2022');

INSERT INTO sales (product, partner, count_product, date_sale)
VALUES (5, 2, 1250, '17.05.2023');

INSERT INTO sales (product, partner, count_product, date_sale)
VALUES (3, 2, 1000, '07.06.2024');

INSERT INTO sales (product, partner, count_product, date_sale)
VALUES (1, 2, 7550, '01.07.2024');

INSERT INTO sales (product, partner, count_product, date_sale)
VALUES (1, 3, 7250, '22.01.2023');

INSERT INTO sales (product, partner, count_product, date_sale)
VALUES (2, 3, 2500, '05.07.2024');

INSERT INTO sales (product, partner, count_product, date_sale)
VALUES (4, 4, 59050, '20.03.2023');

INSERT INTO sales (product, partner, count_product, date_sale)
VALUES (3, 4, 37200, '12.03.2024');

INSERT INTO sales (product, partner, count_product, date_sale)
VALUES (5, 4, 4500, '14.05.2024');

INSERT INTO sales (product, partner, count_product, date_sale)
VALUES (3, 5, 50000, '19.09.2023');

INSERT INTO sales (product, partner, count_product, date_sale)
VALUES (4, 5, 670000, '10.11.2023');

INSERT INTO sales (product, partner, count_product, date_sale)
VALUES (1, 5, 35000, '15.04.2024');

INSERT INTO sales (product, partner, count_product, date_sale)
VALUES (2, 5, 25000, '12.06.2024');

