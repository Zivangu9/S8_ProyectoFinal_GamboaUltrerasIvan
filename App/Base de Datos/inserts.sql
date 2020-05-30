CREATE USER 'usuario'@'%' IDENTIFIED WITH mysql_native_password BY 'CjxR9g4QLSxeSps7';
GRANT SELECT, INSERT, UPDATE, DELETE ON book_collection.* TO 'usuario'@'%';

use book_collection;
INSERT INTO usuario VALUES(null,"Ivan","Gamboa","Ultreras","zivan",SHA1('12345'));

