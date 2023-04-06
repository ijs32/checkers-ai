CREATE TABLE `predicted_categories` (
  `prediction_id` BIGINT(20) NOT NULL AUTO_INCREMENT,
	`member_id` BIGINT(20) NOT NULL,
  `category_id` BIGINT(20) NOT NULL,
	`VendorPartNumber` VARCHAR(50) NOT NULL,
  `Description` VARCHAR(120) NOT NULL,
  PRIMARY KEY (`prediction_id`)
)
COLLATE='latin1_swedish_ci'
ENGINE=InnoDB
;