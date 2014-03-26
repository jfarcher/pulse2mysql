
CREATE DATABASE enmon;
GRANT ALL PRIVILEGES ON enmon.* to enmon@localhost identified by 'enm0np455';
CREATE TABLE `power_usage` (
  `meter_id` int(11) DEFAULT NULL,
  `counter` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
USE enmon;
INSERT INTO power_usage values("1","0");
