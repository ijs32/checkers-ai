CREATE TABLE `piece_training_data` (
        data_id INT NOT NULL AUTO_INCREMENT,
        before_turn BIGINT NOT NULL,
        after_turn BIGINT NOT NULL,
        points SMALLINT,
        PRIMARY KEY ( data_id )
    );

ALTER TABLE `piece_training_data`
    ADD COLUMN team VARCHAR(1) NOT NULL AFTER after_turn