CREATE TABLE `turns` (
    game_id INT NOT NULL,
    turn_id INT NOT NULL AUTO_INCREMENT,
    before_rp_board BIGINT NOT NULL,
    before_rk_board BIGINT NOT NULL,
    before_bp_board BIGINT NOT NULL,
    before_bk_board BIGINT NOT NULL,
    after_rp_board BIGINT NOT NULL,
    after_rk_board BIGINT NOT NULL,
    after_bp_board BIGINT NOT NULL,
    after_bk_board BIGINT NOT NULL,
    PRIMARY KEY ( turn_id, game_id )
);

ALTER TABLE `turns`
    ADD COLUMN round_num INT NOT NULL AFTER turn_id -- need a non auto-incrementing value