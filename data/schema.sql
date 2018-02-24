CREATE DATABASE unid;

USE unid;

CREATE TABLE users(
    username varchar(20) NOT NULL PRIMARY KEY,
    password varchar(32) NOT NULL,
    privilege integer NOT NULL DEFAULT -1,
    status integer NOT NULL DEFAULT 1,
    name varchar(150) NOT NULL,
    email varchar(100) NOT NULL,
    other_data varchar(50) NOT NULL,
    user_hash varchar(32) NOT NULL,
    change_pwd integer NOT NULL DEFAULT 1,
    created timestamp NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE sessions(
    session_id char(128) UNIQUE NOT NULL,
    atime timestamp NOT NULL default current_timestamp,
    data text
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE logs( 
    id_log integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username varchar(20) NOT NULL,
    ip varchar(16) NOT NULL,
    access timestamp NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE productos( 
    id_productos integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    producto varchar(50) NOT NULL,
    existencias integer NOT NULL,
    precio float NOT NULL
    )ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE impresoras( 
    id_impresora integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    modelo varchar(50) NOT NULL,
    existencias integer NOT NULL,
    precio float NOT NULL
    )ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO users (username, password, privilege, status, name, email, other_data, user_hash, change_pwd)
VALUES ('admin',MD5(concat('admin', 'kuorra_key')), 0, 1, 'Admin', 'admin@gmail.com','TIC:SI', MD5(concat('admin', 'kuorra_key', '2016/06/04')), 0),
('guess',MD5(concat('guess', 'kuorra_key')), 1, 1, 'Guess', 'guess@gmail.com','TIC:SI', MD5(concat('guess', 'kuorra_key','2016/06/04')), 0);

INSERT INTO productos(producto , existencias, precio ) VALUES ("magenta",3,50);
INSERT INTO productos(producto , existencias, precio ) VALUES ("cyan",3,50);
INSERT INTO productos(producto , existencias, precio ) VALUES ("yellow",3,50);
INSERT INTO productos(producto , existencias, precio ) VALUES ("black",3,50);
INSERT INTO impresoras(modelo , existencias, precio ) VALUES ("xerox",3,3500);

CREATE USER 'uniduser'@'localhost' IDENTIFIED BY 'unid.2018';
GRANT ALL PRIVILEGES ON unid.* TO 'uniduser'@'localhost';
FLUSH PRIVILEGES;
