CREATE TABLE IF NOT EXISTS `produto` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `descricao` VARCHAR(50) NULL DEFAULT NULL,
    `estoque_minimo` INT(11) NULL DEFAULT NULL,
    `estoque_maximo` INT(11) NULL DEFAULT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `entrada_produto` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `id_produto` INT(11) NULL DEFAULT NULL,
    `qtde` INT(11) NULL DEFAULT NULL,
    `valor_unitario` DECIMAL(9,2) NULL DEFAULT '0.00',
    `data_entrada` DATE NULL DEFAULT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE `estoque` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `id_produto` INT(11) NULL DEFAULT NULL,
    `qtde` INT(11) NULL DEFAULT NULL,
    `valor_unitario` DECIMAL(9,2) NULL DEFAULT '0.00',
    PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `saida_produto` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `id_produto` INT(11) NULL DEFAULT NULL,
    `qtde` INT(11) NULL DEFAULT NULL,
    `data_saida` DATE NULL DEFAULT NULL,
    `valor_unitario` DECIMAL(9,2) NULL DEFAULT '0.00',
    PRIMARY KEY (`id`)
);

ALTER TABLE `entrada_produto` ADD FOREIGN KEY (`id_produto`) REFERENCES produto(`id`);
ALTER TABLE `saida_produto` ADD FOREIGN KEY (`id_produto`) REFERENCES produto(`id`);
ALTER TABLE `estoque` ADD FOREIGN KEY (`id_produto`) REFERENCES produto(`id`);

DELIMITER //
  CREATE PROCEDURE `SP_AtualizaEstoque`( `id_prod` int, `qtde_comprada` int, valor_unit decimal(9,2))
BEGIN
    declare contador int(11);

    SELECT count(*) into contador FROM estoque WHERE id_produto = id_prod;

    IF contador > 0 THEN
        UPDATE estoque SET qtde=qtde + qtde_comprada, valor_unitario= valor_unit
        WHERE id_produto = id_prod;
    ELSE
        INSERT INTO estoque (id_produto, qtde, valor_unitario) values (id_prod, qtde_comprada, valor_unit);
    END IF;
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER `TRG_EntradaProduto_AI` AFTER INSERT ON `entrada_produto`
FOR EACH ROW
BEGIN
      CALL SP_AtualizaEstoque (new.id_produto, new.qtde, new.valor_unitario);
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER `TRG_EntradaProduto_AU` AFTER UPDATE ON `entrada_produto`
FOR EACH ROW
BEGIN
      CALL SP_AtualizaEstoque (new.id_produto, new.qtde - old.qtde, new.valor_unitario);
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER `TRG_EntradaProduto_AD` AFTER DELETE ON `entrada_produto`
FOR EACH ROW
BEGIN
      CALL SP_AtualizaEstoque (old.id_produto, old.qtde * -1, old.valor_unitario);
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER `TRG_SaidaProduto_AI` AFTER INSERT ON `saida_produto`
FOR EACH ROW
BEGIN
      CALL SP_AtualizaEstoque (new.id_produto, new.qtde * -1, new.valor_unitario);
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER `TRG_SaidaProduto_AU` AFTER UPDATE ON `saida_produto`
FOR EACH ROW
BEGIN
      CALL SP_AtualizaEstoque (new.id_produto, old.qtde - new.qtde, new.valor_unitario);
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER `TRG_SaidaProduto_AD` AFTER DELETE ON `saida_produto`
FOR EACH ROW
BEGIN
      CALL SP_AtualizaEstoque (old.id_produto, old.qtde, old.valor_unitario);
END //
DELIMITER ;