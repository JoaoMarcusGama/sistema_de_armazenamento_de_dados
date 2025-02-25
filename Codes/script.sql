-- SCRIPT PARA A CRIAÇÃO DO BANCO DE DADOS 'chapada_imperial' E DA TABELA 'multimedidor' CONTENDO AS COLUNAS PARA ARMAZENAR AS MEDIÇÕES DO MULTIMEDIDOR --

-- Criando o banco de dados chamado 'chapada_imperial'
CREATE DATABASE chapada_imperial;

-- Selecionando o banco de dados para uso
USE chapada_imperial;

-- Criando a tabela 'multimedidor' para armazenar medições elétricas
CREATE TABLE multimedidor (
    -- Coluna para registrar a data e hora da medição, sendo chave primária
    datahora DATETIME NOT NULL PRIMARY KEY,
    
    -- Colunas para armazenar as tensões entre fases e neutro (em Volts)
    tensao_L1_N DECIMAL(6,2) NOT NULL,
    tensao_L2_N DECIMAL(6,2) NOT NULL,
    tensao_L3_N DECIMAL(6,2) NOT NULL,
    tensao_L1_L2 DECIMAL(6,2) NOT NULL,
    tensao_L2_L3 DECIMAL(6,2) NOT NULL,
    tensao_L3_L1 DECIMAL(6,2) NOT NULL,
    
    -- Colunas para armazenar as correntes por fase (em Amperes)
    corrente_L1 DECIMAL(6,2) NOT NULL,
    corrente_L2 DECIMAL(6,2) NOT NULL,
    corrente_L3 DECIMAL(6,2) NOT NULL,
    
    -- Colunas para armazenar a potência aparente por fase (em Volt-Ampere)
    potencia_aparente_L1 DECIMAL(6,2) NOT NULL,
    potencia_aparente_L2 DECIMAL(6,2) NOT NULL,
    potencia_aparente_L3 DECIMAL(6,2) NOT NULL,
    
    -- Colunas para armazenar a potência ativa por fase (em Watts)
    potencia_ativa_L1 DECIMAL(6,2) NOT NULL,
    potencia_ativa_L2 DECIMAL(6,2) NOT NULL,
    potencia_ativa_L3 DECIMAL(6,2) NOT NULL,
    
    -- Colunas para armazenar a potência reativa por fase (em Volt-Ampere Reativo)
    potencia_reativa_L1 DECIMAL(6,2) NOT NULL,
    potencia_reativa_L2 DECIMAL(6,2) NOT NULL,
    potencia_reativa_L3 DECIMAL(6,2) NOT NULL,
    
    -- Coluna para armazenar a corrente do condutor neutro (em Amperes)
    corrente_condutor_neutro DECIMAL(6,2) NOT NULL,
    
    -- Coluna para armazenar a frequência do sistema elétrico (em Hertz)
    frequencia DECIMAL(6,2) NOT NULL
);
