CREATE TABLE `Game` (
        game_id INT NOT NULL AUTO_INCREMENT,
        winning_team ENUM('RED', 'BLACK') NOT NULL,
        CREATE_DATE DATE,
        PRIMARY KEY ( game_id )
    );

ALTER TABLE Game