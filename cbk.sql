-- PostrgreSQL schema for Clubroom Balance Keeper database

CREATE TABLE IF NOT EXISTS product (
    name            VARCHAR(50)     NOT NULL PRIMARY KEY,
    category        VARCHAR(50)     NOT NULL,
    price           INT             NOT NULL,
);

CREATE TABLE IF NOT EXISTS user (
    id              BIGINT          NOT NULL PRIMARY KEY,
    balance         INT             NOT NULL,
);

CREATE TABLE IF NOT EXISTS transaction (
    id              BIGINT          NOT NULL PRIMARY KEY,
    description     VARCHAR(255)    NOT NULL,
    amount          INT             NOT NULL,
    date            DATE            NOT NULL,
);
