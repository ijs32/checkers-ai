CREATE TABLE `Turns` (
    game_id INT NOT NULL,
    turn_id INT NOT NULL AUTO_INCREMENT,
    red_piece_board INT NOT NULL,
    red_king_board INT NOT NULL,
    red_team_points INT NOT NULL,
    black_piece_board INT NOT NULL,
    black_king_board INT NOT NULL,
    black_team_points INT NOT NULL,
    TURN_DATE DATE,
    PRIMARY KEY ( turn_id, game_id )
);