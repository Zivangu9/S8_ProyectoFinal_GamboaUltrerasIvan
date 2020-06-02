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
INSERT INTO libro VALUES(null,"Throne of Glass","Sarah J. Maas",1,"United States","Ingles","Bloomsbury Publishing",2012,"Throne of Glass",406,null,"After a year of slavery, an infamous teenage assassin named Celaena is given the chance to become the tyrannical king's personal assassin/King's Champion by representing Prince Dorian in a competition against the most gifted thieves and assassins in the land. She must survive every test and trial in order to proceed to the final, in which she has to fight her remaining opponents to the death. As candidates are found dead in the castle, their bodies ruptured, Celaena finds herself delving deep into mysteries concerning not only her, but her very own ancestors and the creatures of darkness that dwell deep beneath the castle.");
INSERT INTO libro VALUES(null,"Crown of Midnight","Sarah J. Maas",1,"United States","Ingles","Bloomsbury Publishing",2013,"Throne of Glass",420,null,"Celaena, the King's Champion, must win her freedom by butchering every person the king asks her to, but she cannot bear to kill for the crown. With every death she fakes, she puts her close friends at risk. Celaena must choose between a captain and a prince, and battle forces more threatening than the king. She also reunites with an old colleague, becomes obsessed with a rebel movement, and learns more about the king's source of power.");
INSERT INTO libro VALUES(null,"Heir of Fire","Sarah J. Maas",1,"United States","Ingles","Bloomsbury Publishing",2014,"Throne of Glass",569,null,"Celaena travels to Wendlyn, where magic is still free, where she must train as a Fae with the powerful, cold immortal warrior Rowan Whitethorn. Tensions high between them, the pair have to work together to stop evil forces from rising, as well as learning to accept herself as the Queen of Terrasen. Meanwhile, in Adarlan, Chaol teams with General Aedion Ashryver to rebel against the king. Manon Blackbeak, an immortal, Ironteeth witch, competes in a competition against other witches in order to become the Wing leader of the clan.");
INSERT INTO libro VALUES(null,"Queen of Shadows","Sarah J. Maas",1,"United States","Ingles","Bloomsbury Publishing",2015,"Throne of Glass",648,null,"Stronger than ever, Aelin Galathynius (AKA Celaena Sardothien) returns to Adarlan, but this time she is free. She teams up with Chaol and the King of Assassins, Arobynn Hamel, determined to get her revenge for over ten years of pain. Manon is forced to use her witches to produce evil monsters as weapons. She befriends Elide Lochan, a servant girl who is the rightful lady of Perranth, and daughter of Aelin's nursemaid as a child.");
INSERT INTO libro VALUES(null,"Empire of Storms","Sarah J. Maas",1,"United States","Ingles","Bloomsbury Publishing",2016,"Throne of Glass",689,null,"Aelin is determined to never turn her back on her kingdom again. Cashing in debts to raise an army, Aelin and her court travel around Erilea in an attempt to stop Lord Erawan of the Valg from destroying the world, but with so many sworn enemies in want of revenge, including Queen Maeve of the Fae, survival seems unlikely. Aelin begins to realise that there are events in her life which may not have happened by coincidence; in fact, many have been pulling strings in the background long before she was born, and that she was destined for something far greater than she thought.");
INSERT INTO libro VALUES(null,"Tower of Dawn","Sarah J. Maas",1,"United States","Ingles","Bloomsbury Publishing",2017,"Throne of Glass",660,null,"Taking place around the same time as Empire of Storms, Chaol Westfall travels to the Southern Continent with Nesryn Faliq to receive treatment from the gifted healers there, and to raise a powerful army against the Valg. Yrene Towers' attempts of healing him lead to her becoming entangled in Chaol's past. Meanwhile, Nesryn improves relations with her family during her stay, and befriends Prince Sartaq.");
INSERT INTO libro VALUES(null,"Kingdom of Ash","Sarah J. Maas",1,"United States","Ingles","Bloomsbury Publishing",2018,"Throne of Glass",984,null,"After being locked in an iron coffin for months by Maeve, Aelin resists torture in hopes to return to her kingdom. Rowan searches with his cadre and Elide to find Aelin, his mate and wife, while Aedion and Lysandra continue to defend Terrasen with the armies that Aelin gathered before she was captured, from forces that would seek to destroy it: Erawan. Chaol, Manon, and Dorian travel their own paths and missions to rescue Aelin and help her on her mission to become Queen again. Threads draw every character closer as they move towards a final battle of freedom for the lands of Adarlan and Terrasen.");