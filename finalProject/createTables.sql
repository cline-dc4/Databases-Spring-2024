CREATE TABLE dcbcdb.Employee
(
	employee_id int PRIMARY KEY AUTO_INCREMENT,
    manager bool NOT NULL,
    managed_by int,
    position varchar(50),
    employee_lname varchar(30) NOT NULL,
    employee_fname varchar(30) NOT NULL,
    employee_wage float(7,2)
);

CREATE TABLE dcbcdb.EmployeePhoneNum
(
	phone_id int PRIMARY KEY AUTO_INCREMENT,
    employee_id int,
    phone_num varchar(11) NOT NULL,
    phone_type varchar(20),
    is_primary bool NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES Employee(employee_id)
);

CREATE TABLE dcbcdb.Customer
(
	cust_id int PRIMARY KEY AUTO_INCREMENT,
    cust_fname varchar(30) NOT NULL,
    cust_lname varchar(30) NOT NULL,
    cust_reward int(4)
);

CREATE TABLE dcbcdb.CustomerPhoneNum
(
	phone_id int PRIMARY KEY AUTO_INCREMENT,
    cust_id int,
    phone_num varchar(11) NOT NULL,
    phone_type varchar(20),
    is_primary bool NOT NULL,
    FOREIGN KEY(cust_id) REFERENCES Customer(cust_id)
);

CREATE TABLE dcbcdb.CustomerEmail
(
	email_id int PRIMARY KEY AUTO_INCREMENT,
    cust_id int,
    email_address varchar(60) NOT NULL,
    is_primary bool NOT NULL,
    FOREIGN KEY(cust_id) REFERENCES Customer(cust_id)
);

CREATE TABLE dcbcdb.CoffeeDrink
(
	drink_id int PRIMARY KEY AUTO_INCREMENT,
    drink_name varchar(40) NOT NULL,
    price float(5,2) NOT NULL
);

CREATE TABLE dcbcdb.CoffeeIngredient
(
	ingredient_id int PRIMARY KEY AUTO_INCREMENT,
    ingredient_name varchar(40) NOT NULL,
    stock int(3) NOT NULL
);

CREATE TABLE dcbcdb.IngredientList
(
	drink_id int,
    ingredient_id int,
	FOREIGN KEY (drink_id) REFERENCES CoffeeDrink (drink_id),
    FOREIGN KEY (ingredient_id) REFERENCES CoffeeIngredient (ingredient_id)
);

CREATE TABLE dcbcdb.BakedItem 
(
	baked_id int PRIMARY KEY AUTO_INCREMENT,
    baked_name varchar(40) NOT NULL,
    price float(5,2) NOT NULL,
    stock int(3) NOT NULL
);

CREATE TABLE dcbcdb.Book
(
	book_id int PRIMARY KEY AUTO_INCREMENT,
    isbn varchar(13) NOT NULL,
    title varchar(100) NOT NULL,
    author_lname varchar(30) NOT NULL,
    author_fname varchar(30),
    stock int(3) NOT NULL,
    price float(5,2) NOT NULL
);

CREATE TABLE dcbcdb.Purchase
(
	purchase_id int PRIMARY KEY AUTO_INCREMENT,
    cust_id int,
    employee_id int,
    total_cost float(7,2) NOT NULL,
    FOREIGN KEY(cust_id) REFERENCES Customer(cust_id),
    FOREIGN KEY(employee_id) REFERENCES Employee(employee_id)
);

CREATE TABLE dcbcdb.CoffeeDrinkPurchase
(
	drink_id int,
    purchase_id int,
	quantity int(3) NOT NULL,
    FOREIGN KEY(drink_id) REFERENCES CoffeeDrink(drink_id),
    FOREIGN KEY(purchase_id) REFERENCES Purchase(purchase_id)
);

CREATE TABLE dcbcdb.BakedItemPurchase
(
	baked_id int,
    purchase_id int,
	quantity int(3) NOT NULL,
    FOREIGN KEY(baked_id) REFERENCES BakedItem(baked_id),
    FOREIGN KEY(purchase_id) REFERENCES Purchase(purchase_id)
);

CREATE TABLE dcbcdb.BookPurchase
(
	book_id int,
    purchase_id int,
	quantity int(3) NOT NULL,
    FOREIGN KEY(book_id) REFERENCES Book(book_id),
    FOREIGN KEY(purchase_id) REFERENCES Purchase(purchase_id)
);

INSERT INTO dcbcdb.Customer
VALUES
	(0, 'Evan', 'Hedlund', 0)
    (0, 'Crissy', 'Sanders',  20),
    (0, 'Ken', 'Driver', 10),
    (0, 'Noah', 'Gleason', 5);
    
INSERT INTO dcbcdb.CustomerEmail
VALUES
	(0, 1, 'ehedlund@corban.edu', true),
	(0, 2, 'carissasanders@corban.edu', false),
	(0, 3, 'kdriver@corban.edu', true),
	(0, 4, 'noahgleason@corban.edu', false);
        
INSERT INTO dcbcdb.CustomerPhoneNum
VALUES
	(0, 1, '13604961316', 'Mobile', true),
    (0, 2, '15039904856', 'Mobile', true),
    (0, 3, '12345678910', 'Home', false),
    (0, 4, '15037131425', 'Mobile', true);
    
INSERT INTO dcbcdb.Employee
VALUES
	(0, true, NULL, 'Owner', 'Cline', 'DC', 59999.99),
    (0, false, 0, 'Barista', 'Gleason', 'Seth', 32999.99),
    (0, false, 0, 'Teller', 'Nakamura', 'Ailsie', 33999.99),
    (0, false, 0, 'Store Floor Staff', 'James', 'LeAnna', 32999.99);
    

INSERT INTO dcbcdb.EmployeePhoneNum
VALUES
	(0, 1, '15093024997', 'Mobile', true),
    (0, 2, '19713864734', 'Mobile', true),
    (0, 3, '18083084309', 'Mobile', true),
    (0, 4, '12345678910', 'Home', false);

INSERT INTO dcbcdb.CoffeeIngredient
VALUES
(0, 'Coffee beans', 5),
(0, 'Caramel syrup', 2),
(0, 'Milk', 3),
(0, 'Vanilla syrup', 2),
(0, 'Earl Grey tea bags', 14),
(0, 'Chocolate syrup', 3);

INSERT INTO dcbcdb.CoffeeDrink
VALUES
(0, 'Caramel Macchiato', 4.49),
(0, 'Mocha', 4.29),
(0, 'London Fog', 4.19),
(0, 'Caramel Latte', 4.29);

INSERT INTO dcbcdb.IngredientList
VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 1),
(2, 3),
(2, 6),
(3, 3),
(3, 4),
(3, 5),
(4, 1),
(4, 2),
(4, 3);

INSERT INTO dcbcdb.BakedItem
VALUES
(0, 'Chocolate Chip Scone', 3.99, 7),
(0, 'Lemon Scone', 3.99, 6),
(0, 'Peanut Butter Cookie', 3.29, 12),
(0, 'Chocolate Chip Macadamia Cookie', 3.49, 9);

INSERT INTO dcbcdb.Book
VALUES
(0, '9780765326362', 'Words of Radiance', 'Sanderson', 'Brandon', 3, 18.99),
(0, '9783453270381', 'Oathbringer', 'Sanderson', 'Brandon', 2, 18.99),
(0, '9780060652951', 'The Great Divorce', 'Lewis', 'C.S.', 6, 9.99),
(0, '978804397410', 'Murder on the Orient Express', 'Christie', 'Agatha', 3, 8.99);

INSERT INTO dcbcdb.Purchase
VALUES
-- 5: scone, sanderson, macchiato
(0, 1, 2, 27.47),
-- 6: macadamia, lewis
(0, 2, 3, 13.48),
-- 7: mocha
(0, 3, 2, 4.29),
-- 8: christie, london fog
(0, 4, 3, 13.18);

INSERT INTO dcbcdb.CoffeeDrinkPurchase
VALUES
(1, 5, 1),
(2, 7, 1),
(4, 8, 1);

INSERT INTO dcbcdb.BakedItemPurchase
VALUES
(2, 5, 1),
(4, 6, 1);

INSERT INTO dcbcdb.BookPurchase
VALUES
(1, 5, 1),
(3, 7, 1),
(4, 8, 1);