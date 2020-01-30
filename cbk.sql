-- PostrgreSQL schema for Clubroom Balance Keeper database

-- UUID generator module
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS product (
    id              UUID            NOT NULL PRIMARY KEY DEFAULT uuid_generate_v4(),
    name            VARCHAR(50)     NOT NULL,
    category        VARCHAR(50)     NOT NULL,
    price           INT             NOT NULL,
    active          BOOLEAN         NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS cbk_user (
    id              UUID            NOT NULL PRIMARY KEY DEFAULT uuid_generate_v4(),
    balance         INT             NOT NULL DEFAULT 0 CHECK (balance >= 0),
    telegram_id     BIGINT
);

CREATE TABLE IF NOT EXISTS transaction (
    id              UUID            NOT NULL PRIMARY KEY DEFAULT uuid_generate_v4(),
    product_id      UUID            NOT NULL,
    cbk_user_id     UUID            NOT NULL,
    date            DATE            NOT NULL,
    description     VARCHAR(255),

    FOREIGN KEY (product_id) REFERENCES product (id),
    FOREIGN KEY (user_id) REFERENCES cbk_user (id)
);

CREATE VIEW user_transactions AS
    SELECT cbk_user.id, product.name, product.price
    FROM transaction
    INNER JOIN product ON transaction.product_id = product.id
    INNER JOIN cbk_user ON transaction.cbk_user_id = cbk_user.id;