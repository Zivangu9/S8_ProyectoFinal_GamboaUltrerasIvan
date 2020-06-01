CREATE USER 'usuario'@'%' IDENTIFIED WITH mysql_native_password BY 'CjxR9g4QLSxeSps7';
GRANT SELECT, INSERT, UPDATE, DELETE ON book_collection.* TO 'usuario'@'%';

use book_collection;
INSERT INTO usuario VALUES(null,"Ivan","Gamboa","Ultreras","zivan",SHA1('12345'));

INSERT INTO libro VALUES(null,"Harry Potter y la piedra filosofal","J. K. Rowling",null,"Barcelona, España","Español","Salamandra",1998,"Harry Potter",255,null,null);
INSERT INTO libro VALUES(null,"Harry Potter y la cámara secreta","J. K. Rowling",null,"Barcelona, España","Español","Salamandra",1999,"Harry Potter",286,null,null);
INSERT INTO libro VALUES(null,"Harry Potter y el prisionero de Azkaban","J. K. Rowling",null,"Barcelona, España","Español","Salamandra",2000,"Harry Potter",359,null,null);
INSERT INTO libro VALUES(null,"Harry Potter y el cáliz de fuego","J. K. Rowling",null,"Barcelona, España","Español","Salamandra",2001,"Harry Potter",636,null,null);
INSERT INTO libro VALUES(null,"Harry Potter y la Orden del Fénix","J. K. Rowling",null,"Barcelona, España","Español","Salamandra",2004,"Harry Potter",893,null,null);
INSERT INTO libro VALUES(null,"Harry Potter y el misterio del príncipe","J. K. Rowling",null,"Barcelona, España","Español","Salamandra",2006,"Harry Potter",602,null,null);
INSERT INTO libro VALUES(null,"Harry Potter y las reliquias de la Muerte","J. K. Rowling",null,"Barcelona, España","Español","Salamandra",2008,"Harry Potter",638,null,null);

INSERT INTO libro_leido VALUES(null,1,1,now());
INSERT INTO libro_obtenido VALUES(null,1,1,now());
INSERT INTO libro_obtenido VALUES(null,1,3,now());
INSERT INTO libro_obtenido VALUES(null,1,4,now());
INSERT INTO libro_deseado VALUES(null,1,2,now());
INSERT INTO libro_deseado VALUES(null,1,5,now());

