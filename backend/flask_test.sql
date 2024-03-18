/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE TABLE IF NOT EXISTS `user` (
  `uid` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '用户id',
  `name` varchar(20) NOT NULL DEFAULT '' COMMENT '名称',
  `gender` varchar(10) NOT NULL DEFAULT '' COMMENT '性别',
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;

DELETE FROM `user`;
INSERT INTO `user` (`uid`, `name`, `gender`) VALUES
	(1, '123123555', 'male');
INSERT INTO `user` (`uid`, `name`, `gender`) VALUES
	(2, '434', 'male');
INSERT INTO `user` (`uid`, `name`, `gender`) VALUES
	(3, '1231231', 'male');
INSERT INTO `user` (`uid`, `name`, `gender`) VALUES
	(4, '12312313', 'male');
INSERT INTO `user` (`uid`, `name`, `gender`) VALUES
	(5, '333', 'male');
INSERT INTO `user` (`uid`, `name`, `gender`) VALUES
	(6, '123445', 'male');
INSERT INTO `user` (`uid`, `name`, `gender`) VALUES
	(7, '1', 'male');
INSERT INTO `user` (`uid`, `name`, `gender`) VALUES
	(8, '2', 'male');
INSERT INTO `user` (`uid`, `name`, `gender`) VALUES
	(9, '3', 'male');
INSERT INTO `user` (`uid`, `name`, `gender`) VALUES
	(10, '4', 'male');
INSERT INTO `user` (`uid`, `name`, `gender`) VALUES
	(11, '5--', 'male');
INSERT INTO `user` (`uid`, `name`, `gender`) VALUES
	(12, '6', 'male');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
