CREATE TABLE `Turns` (
    game_id INT NOT NULL,
    turn_id INT NOT NULL AUTO_INCREMENT,
    red_piece_board BIGINT NOT NULL,
    red_king_board BIGINT NOT NULL,
    black_piece_board BIGINT NOT NULL,
    black_king_board BIGINT NOT NULL,
    PRIMARY KEY ( turn_id, game_id )
);