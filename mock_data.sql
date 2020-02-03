insert into cbk_user (balance, telegram_id) values 
    (13, 1),
    (42, 2),
    (18, 3),
    (38, 4),
    (13, 5),
    (0, 6),
    (47, 7),
    (15, 8),
    (0, 9),
    (0, 10),
    (5, 11),
    (35, 12),
    (9, 13),
    (16, 14),
    (31, 15),
    (6, 16),
    (31, 17),
    (43, 18),
    (3, 19),
    (12, 20);

insert into product (name, category, price, active) values 
    ('Event photography', 'Reward', 50, false),
    ('A1', 'Print', -13, false),
    ('A2', 'Print', -9, false),
    ('A3', 'Print', -16, true),
    ('A4', 'Print', -15, true),
    ('A5', 'Print', -7, false),
    ('A6', 'Print', -5, false),
    ('C-41 Kehitys', 'Chemistry & Film', -18, true),
    ('ID-11 Kehitys', 'Chemistry & Film', -8, false),
    ('ColorPlus 200', 'Chemistry & Film', -16, true),
    ('Hp5+ 400', 'Chemistry & Film', -6, true),
    ('Tupla', 'Food & Drinks', -19, false),
    ('Twix', 'Food & Drinks', -4, true),
    ('Freeway Soda', 'Food & Drinks', -7, true),
    ('Banana', 'Food & Drinks', -5, false);

insert into transaction (product_id, cbk_user_id, date) VALUES 
    ((SELECT id from product limit 1 offset 0),(SELECT id from cbk_user limit 1 offset 1),NOW()),
    ((SELECT id from product limit 1 offset 2),(SELECT id from cbk_user limit 1 offset 2),NOW()),
    ((SELECT id from product limit 1 offset 3),(SELECT id from cbk_user limit 1 offset 3),NOW()),
    ((SELECT id from product limit 1 offset 4),(SELECT id from cbk_user limit 1 offset 4),NOW()),
    ((SELECT id from product limit 1 offset 5),(SELECT id from cbk_user limit 1 offset 5),NOW()),
    ((SELECT id from product limit 1 offset 6),(SELECT id from cbk_user limit 1 offset 6),NOW()),
    ((SELECT id from product limit 1 offset 7),(SELECT id from cbk_user limit 1 offset 7),NOW()),
    ((SELECT id from product limit 1 offset 8),(SELECT id from cbk_user limit 1 offset 8),NOW()),
    ((SELECT id from product limit 1 offset 9),(SELECT id from cbk_user limit 1 offset 9),NOW());


select * from balances;
select * from products;