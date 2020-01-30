-- PostrgreSQL schema for Clubroom Balance Keeper database

-- UUID generator module
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS product (
    id              UUID            NOT NULL PRIMARY KEY,
    name            VARCHAR(50)     NOT NULL,
    category        VARCHAR(50)     NOT NULL,
    price           INT             NOT NULL,
    active          BOOLEAN         NOT NULL DEFAULT TRUE,

    UNIQUE(id),
);

CREATE TABLE IF NOT EXISTS user (
    id              UUID            NOT NULL PRIMARY KEY,
    balance         INT             NOT NULL DEFAULT 0 CHECK balance >= 0,
    telegram_id     BIGINT,

    UNIQUE(id),
);

CREATE TABLE IF NOT EXISTS transaction (
    id              UUID            NOT NULL PRIMARY KEY,
    amount          INT             NOT NULL,
    date            DATE            NOT NULL,
    product_id      UUID            NOT NULL,
    user_id         UUID            NOT NULL,
    description     VARCHAR(255),

    FOREIGN KEY (product_id) REFERENCES Product (id),
    FOREIGN KEY (user_id) REFERENCES User (id),
    UNIQUE(id),
);
