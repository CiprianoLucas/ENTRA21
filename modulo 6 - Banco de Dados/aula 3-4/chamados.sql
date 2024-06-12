-- DROP TABLE public.chamados_agencias_terceiros;
-- DROP TABLE public.chamados_agencias;
-- DROP TABLE public.chamados;
-- DROP TABLE public.agencias;
-- DROP TABLE public.colaboradores;
-- DROP TABLE public.terceiros;
-- DROP TYPE status_chamado;

-- Aula 3

CREATE TABLE IF NOT EXISTS public.colaboradores (
	id SERIAL PRIMARY KEY,
	nome VARCHAR(256) NOT NULL,
	email VARCHAR(256) NOT NULL UNIQUE,
	telefone VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS public.agencias(
	id SERIAL PRIMARY KEY,
	razao_social VARCHAR(256) NOT NULL,
	cnpj VARCHAR(14) NOT NULL UNIQUE,
	logradouro VARCHAR(256) NOT NULL,
	cidade VARCHAR(256) NOT NULL,
	estado VARCHAR(2) NOT NULL
);

CREATE TABLE IF NOT EXISTS public.terceiros(
	id SERIAL PRIMARY KEY,
	razao_social VARCHAR(256) NOT NULL,
	cnpj VARCHAR(14) UNIQUE NOT NULL,
	cidade VARCHAR(256) NOT NULL,
	estado VARCHAR(2) NOT NULL,
	tipo_servico VARCHAR(256) NOT NULL
);

CREATE TYPE status_chamado AS ENUM ('NOVO', 'ANDAMENTO', 'AGUARDANDO FORNECEDOR', 'CONCLUIDO');

CREATE TABLE IF NOT EXISTS public.chamados(
	id SERIAL PRIMARY KEY,
	id_colaborador INT NOT NULL,
	descricao TEXT NOT NULL,
	prazo DATE,
	status status_chamado DEFAULT 'NOVO'
);

CREATE TABLE IF NOT EXISTS public.chamados_agencias(
	id SERIAL PRIMARY KEY,
	id_agencia INT NOT NULL,
	id_chamado INT NOT NULL,
	demanda VARCHAR(256) NOT NULL
);

CREATE TABLE IF NOT EXISTS public.chamados_agencias_terceiros(
	id SERIAL PRIMARY KEY,
	id_chamado_agencia INT NOT NULL,
	id_terceiro INT NOT NULL,
	valor MONEY,
	tenico VARCHAR(256),
	nfse VARCHAR(256) UNIQUE,
	nfe VARCHAR(256) UNIQUE
);


ALTER TABLE IF EXISTS public.chamados
ADD FOREIGN KEY (id_colaborador)
REFERENCES public.colaboradores(id)
ON UPDATE CASCADE
ON DELETE CASCADE;

ALTER TABLE IF EXISTS public.chamados_agencias
ADD FOREIGN KEY (id_chamado)
REFERENCES public.chamados(id)
ON UPDATE CASCADE
ON DELETE CASCADE;

ALTER TABLE IF EXISTS public.chamados_agencias
ADD FOREIGN KEY (id_agencia)
REFERENCES public.agencias(id)
ON UPDATE CASCADE
ON DELETE CASCADE;

ALTER TABLE IF EXISTS public.chamados_agencias_terceiros
ADD FOREIGN KEY (id_chamado_agencia)
REFERENCES public.chamados_agencias(id)
ON UPDATE CASCADE
ON DELETE CASCADE;

ALTER TABLE IF EXISTS public.chamados_agencias_terceiros
ADD FOREIGN KEY (id_terceiro)
REFERENCES public.terceiros(id)
ON UPDATE CASCADE
ON DELETE CASCADE;
-- Aula 4

INSERT INTO public.colaboradores (nome, email, telefone)
VALUES ('Carlos', 'carlos@email.com', '(47) 90000-0001');

INSERT INTO public.colaboradores (nome, email, telefone)
VALUES ('Mariana', 'mariana@email.com', '(47) 90000-0002');

INSERT INTO public.colaboradores (nome, email, telefone)
VALUES ('Rafael', 'rafael@email.com', '(47) 90000-0003');

INSERT INTO public.colaboradores (nome, email, telefone)
VALUES ('Julia', 'julia@email.com', '(47) 90000-0004');

INSERT INTO public.colaboradores (nome, email, telefone)
VALUES ('Fernando', 'fernando@email.com', '(47) 90000-0005');

INSERT INTO public.colaboradores (nome, email, telefone)
VALUES ('Patricia', 'patricia@email.com', '(47) 90000-0006');

INSERT INTO public.colaboradores (nome, email, telefone)
VALUES ('Gabriel', 'gabriel@email.com', '(47) 90000-0007');

INSERT INTO public.colaboradores (nome, email, telefone)
VALUES ('Amanda', 'amanda@email.com', '(47) 90000-0008');

INSERT INTO public.colaboradores (nome, email, telefone)
VALUES ('Diego', 'diego@email.com', '(47) 90000-0009');

INSERT INTO public.colaboradores (nome, email, telefone)
VALUES ('Larissa', 'larissa@email.com', '(47) 90000-0010');

INSERT INTO public.colaboradores (nome, email, telefone)
VALUES ('Rodrigo', 'rodrigo@email.com', '(47) 90000-0011');

INSERT INTO public.colaboradores (nome, email, telefone)
VALUES ('Camila', 'camila@email.com', '(47) 90000-0012');

INSERT INTO public.colaboradores (nome, email, telefone)
VALUES ('Lucas', 'lucas@email.com', '(47) 90000-0013');

INSERT INTO public.colaboradores (nome, email, telefone)
VALUES ('Isabela', 'isabela@email.com', '(47) 90000-0014');

INSERT INTO public.colaboradores (nome, email, telefone)
VALUES ('Felipe', 'felipe@email.com', '(47) 90000-0015');

INSERT INTO public.colaboradores (nome, email, telefone)
VALUES ('Leticia', 'leticia@email.com', '(47) 90000-0016');

INSERT INTO public.colaboradores (nome, email, telefone)
VALUES ('Gustavo', 'gustavo@email.com', '(47) 90000-0017');

INSERT INTO public.colaboradores (nome, email, telefone)
VALUES ('Beatriz', 'beatriz@email.com', '(47) 90000-0018');

INSERT INTO public.colaboradores (nome, email, telefone)
VALUES ('Matheus', 'matheus@email.com', '(47) 90000-0019');

INSERT INTO public.colaboradores (nome, email, telefone)
VALUES ('Vanessa', 'vanessa@email.com', '(47) 90000-0020');


INSERT INTO public.terceiros (razao_social, cnpj, cidade, estado, tipo_servico)
VALUES ('Empresa ABC', '00000000000101', 'Joinville', 'SC', 'Consultoria');

INSERT INTO public.terceiros (razao_social, cnpj, cidade, estado, tipo_servico)
VALUES ('Empresa XYZ', '11111111111111', 'Florianópolis', 'SC', 'Tecnologia');

INSERT INTO public.terceiros (razao_social, cnpj, cidade, estado, tipo_servico)
VALUES ('Empresa QWE', '22222222222222', 'Curitiba', 'PR', 'Marketing');

INSERT INTO public.terceiros (razao_social, cnpj, cidade, estado, tipo_servico)
VALUES ('Empresa JKL', '33333333333333', 'São Paulo', 'SP', 'Logística');

INSERT INTO public.terceiros (razao_social, cnpj, cidade, estado, tipo_servico)
VALUES ('Empresa DEF', '44444444444444', 'Rio de Janeiro', 'RJ', 'Engenharia');

INSERT INTO public.terceiros (razao_social, cnpj, cidade, estado, tipo_servico)
VALUES ('Empresa MNO', '55555555555555', 'Porto Alegre', 'RS', 'Saúde');

INSERT INTO public.terceiros (razao_social, cnpj, cidade, estado, tipo_servico)
VALUES ('Empresa GHI', '66666666666666', 'Brasília', 'DF', 'Educação');

INSERT INTO public.terceiros (razao_social, cnpj, cidade, estado, tipo_servico)
VALUES ('Empresa PQR', '77777777777777', 'Belo Horizonte', 'MG', 'Financeiro');

INSERT INTO public.terceiros (razao_social, cnpj, cidade, estado, tipo_servico)
VALUES ('Empresa STU', '88888888888888', 'Recife', 'PE', 'Telecomunicações');

INSERT INTO public.terceiros (razao_social, cnpj, cidade, estado, tipo_servico)
VALUES ('Empresa VWX', '99999999999999', 'Salvador', 'BA', 'Varejo');

INSERT INTO public.terceiros (razao_social, cnpj, cidade, estado, tipo_servico)
VALUES ('Empresa RST', '12345678000100', 'Campinas', 'SP', 'Software');

INSERT INTO public.terceiros (razao_social, cnpj, cidade, estado, tipo_servico)
VALUES ('Empresa UVW', '23456789000111', 'Manaus', 'AM', 'Manufatura');

INSERT INTO public.terceiros (razao_social, cnpj, cidade, estado, tipo_servico)
VALUES ('Empresa XYZ', '34567890000122', 'Fortaleza', 'CE', 'Transporte');

INSERT INTO public.terceiros (razao_social, cnpj, cidade, estado, tipo_servico)
VALUES ('Empresa 123', '45678901000133', 'Vitória', 'ES', 'Alimentício');

INSERT INTO public.terceiros (razao_social, cnpj, cidade, estado, tipo_servico)
VALUES ('Empresa ABC', '56789012000144', 'Goiânia', 'GO', 'E-commerce');

INSERT INTO public.terceiros (razao_social, cnpj, cidade, estado, tipo_servico)
VALUES ('Empresa DEF', '67890123000155', 'Natal', 'RN', 'Turismo');

INSERT INTO public.terceiros (razao_social, cnpj, cidade, estado, tipo_servico)
VALUES ('Empresa GHI', '78901234000166', 'Teresina', 'PI', 'Mídia');

INSERT INTO public.terceiros (razao_social, cnpj, cidade, estado, tipo_servico)
VALUES ('Empresa JKL', '89012345000177', 'Aracaju', 'SE', 'Construção Civil');

INSERT INTO public.terceiros (razao_social, cnpj, cidade, estado, tipo_servico)
VALUES ('Empresa MNO', '90123456000188', 'Cuiabá', 'MT', 'Serviços Automotivos');

INSERT INTO public.terceiros (razao_social, cnpj, cidade, estado, tipo_servico)
VALUES ('Empresa PQR', '01234567000199', 'Palmas', 'TO', 'Serviços de TI');


INSERT INTO public.agencias (razao_social, cnpj, logradouro, cidade, estado)
VALUES ('Agência Sul', '99999999000100', 'Rua das Flores, 123', 'Florianópolis', 'SC');

INSERT INTO public.agencias (razao_social, cnpj, logradouro, cidade, estado)
VALUES ('Agência Norte', '88888888000111', 'Avenida Central, 456', 'Joinville', 'SC');

INSERT INTO public.agencias (razao_social, cnpj, logradouro, cidade, estado)
VALUES ('Agência Oeste', '77777777000122', 'Praça das Árvores, 789', 'Curitiba', 'PR');

INSERT INTO public.agencias (razao_social, cnpj, logradouro, cidade, estado)
VALUES ('Agência Leste', '66666666000133', 'Alameda das Avenidas, 1011', 'São Paulo', 'SP');

INSERT INTO public.agencias (razao_social, cnpj, logradouro, cidade, estado)
VALUES ('Agência Centro', '55555555000144', 'Travessa das Ruas, 1213', 'Rio de Janeiro', 'RJ');

INSERT INTO public.agencias (razao_social, cnpj, logradouro, cidade, estado)
VALUES ('Agência ABC', '44444444000155', 'Praia da Cidade, 1415', 'Porto Alegre', 'RS');

INSERT INTO public.agencias (razao_social, cnpj, logradouro, cidade, estado)
VALUES ('Agência XYZ', '33333333000166', 'Av. das Montanhas, 1617', 'Brasília', 'DF');

INSERT INTO public.agencias (razao_social, cnpj, logradouro, cidade, estado)
VALUES ('Agência QWE', '22222222000177', 'Estrada do Campo, 1819', 'Belo Horizonte', 'MG');

INSERT INTO public.agencias (razao_social, cnpj, logradouro, cidade, estado)
VALUES ('Agência JKL', '11111111000188', 'Rua das Praias, 2021', 'Recife', 'PE');

INSERT INTO public.agencias (razao_social, cnpj, logradouro, cidade, estado)
VALUES ('Agência MNO', '00000000000199', 'Avenida dos Bosques, 2223', 'Salvador', 'BA');

INSERT INTO public.agencias (razao_social, cnpj, logradouro, cidade, estado)
VALUES ('Agência Sul', '98765432000100', 'Rua das Palmeiras, 333', 'Campinas', 'SP');

INSERT INTO public.agencias (razao_social, cnpj, logradouro, cidade, estado)
VALUES ('Agência Norte', '87654321000111', 'Avenida do Parque, 444', 'Manaus', 'AM');

INSERT INTO public.agencias (razao_social, cnpj, logradouro, cidade, estado)
VALUES ('Agência Oeste', '76543210000122', 'Praça da Liberdade, 555', 'Fortaleza', 'CE');

INSERT INTO public.agencias (razao_social, cnpj, logradouro, cidade, estado)
VALUES ('Agência Leste', '65432109000133', 'Alameda das Praças, 666', 'Vitória', 'ES');

INSERT INTO public.agencias (razao_social, cnpj, logradouro, cidade, estado)
VALUES ('Agência ABC', '54321098000144', 'Praia do Sol, 777', 'Goiânia', 'GO');

INSERT INTO public.agencias (razao_social, cnpj, logradouro, cidade, estado)
VALUES ('Agência XYZ', '43210987000155', 'Av. da Lua, 888', 'Natal', 'RN');

INSERT INTO public.agencias (razao_social, cnpj, logradouro, cidade, estado)
VALUES ('Agência QWE', '32109876000166', 'Estrada da Montanha, 999', 'Teresina', 'PI');

INSERT INTO public.agencias (razao_social, cnpj, logradouro, cidade, estado)
VALUES ('Agência JKL', '21098765000177', 'Rua dos Rios, 1010', 'Aracaju', 'SE');

INSERT INTO public.agencias (razao_social, cnpj, logradouro, cidade, estado)
VALUES ('Agência MNO', '10987654000188', 'Avenida das Estrelas, 1111', 'Cuiabá', 'MT');

INSERT INTO public.agencias (razao_social, cnpj, logradouro, cidade, estado)
VALUES ('Agência PQR', '09876543000199', 'Praça das Torres, 1212', 'Palmas', 'TO');




INSERT INTO public.chamados (id_colaborador, descricao, prazo, status)
VALUES (1, 'Problema na rede local', '2023-12-05', 'NOVO');

INSERT INTO public.chamados (id_colaborador, descricao, prazo, status)
VALUES (2, 'Erro na aplicação financeira', '2023-12-10', 'ANDAMENTO');

INSERT INTO public.chamados (id_colaborador, descricao, prazo, status)
VALUES (3, 'Solicitação de upgrade de software', '2023-11-30', 'AGUARDANDO FORNECEDOR');

INSERT INTO public.chamados (id_colaborador, descricao, prazo, status)
VALUES (4, 'Configuração de novo servidor', '2023-12-15', 'CONCLUIDO');

INSERT INTO public.chamados (id_colaborador, descricao, prazo, status)
VALUES (5, 'Problema com impressora', '2023-12-08', 'NOVO');

INSERT INTO public.chamados (id_colaborador, descricao, prazo, status)
VALUES (6, 'Instalação de antivírus', '2023-12-03', 'ANDAMENTO');

INSERT INTO public.chamados (id_colaborador, descricao, prazo, status)
VALUES (7, 'Atualização de sistema operacional', '2023-12-20', 'AGUARDANDO FORNECEDOR');

INSERT INTO public.chamados (id_colaborador, descricao, prazo, status)
VALUES (8, 'Treinamento em software', '2023-12-18', 'CONCLUIDO');

INSERT INTO public.chamados (id_colaborador, descricao, prazo, status)
VALUES (9, 'Problema de acesso à rede externa', '2023-12-12', 'NOVO');

INSERT INTO public.chamados (id_colaborador, descricao, prazo, status)
VALUES (10, 'Configuração de e-mail', '2023-12-07', 'ANDAMENTO');

INSERT INTO public.chamados (id_colaborador, descricao, prazo, status)
VALUES (11, 'Solicitação de novo equipamento', '2023-12-09', 'AGUARDANDO FORNECEDOR');

INSERT INTO public.chamados (id_colaborador, descricao, prazo, status)
VALUES (12, 'Backup de dados', '2023-12-22', 'CONCLUIDO');

INSERT INTO public.chamados (id_colaborador, descricao, prazo, status)
VALUES (13, 'Problema de login', '2023-12-11', 'NOVO');

INSERT INTO public.chamados (id_colaborador, descricao, prazo, status)
VALUES (14, 'Manutenção de hardware', '2023-12-16', 'ANDAMENTO');

INSERT INTO public.chamados (id_colaborador, descricao, prazo, status)
VALUES (15, 'Revisão de segurança', '2023-12-14', 'AGUARDANDO FORNECEDOR');

INSERT INTO public.chamados (id_colaborador, descricao, prazo, status)
VALUES (16, 'Configuração de VPN', '2023-12-23', 'CONCLUIDO');

INSERT INTO public.chamados (id_colaborador, descricao, prazo, status)
VALUES (17, 'Problema de conexão Wi-Fi', '2023-12-06', 'NOVO');

INSERT INTO public.chamados (id_colaborador, descricao, prazo, status)
VALUES (18, 'Atualização de banco de dados', '2023-12-17', 'ANDAMENTO');

INSERT INTO public.chamados (id_colaborador, descricao, prazo, status)
VALUES (19, 'Solicitação de licença de software', '2023-12-19', 'AGUARDANDO FORNECEDOR');

INSERT INTO public.chamados (id_colaborador, descricao, prazo, status)
VALUES (20, 'Implementação de novos recursos', '2023-12-21', 'CONCLUIDO');


INSERT INTO public.chamados_agencias (id_agencia, id_chamado, demanda)
VALUES (1, 1, 'Reparo na rede local da agência');

INSERT INTO public.chamados_agencias (id_agencia, id_chamado, demanda)
VALUES (2, 2, 'Verificação de sistemas financeiros');

INSERT INTO public.chamados_agencias (id_agencia, id_chamado, demanda)
VALUES (3, 3, 'Acompanhamento do status do upgrade de software');

INSERT INTO public.chamados_agencias (id_agencia, id_chamado, demanda)
VALUES (4, 4, 'Configuração do novo servidor da agência');

INSERT INTO public.chamados_agencias (id_agencia, id_chamado, demanda)
VALUES (5, 5, 'Manutenção da impressora da agência');

INSERT INTO public.chamados_agencias (id_agencia, id_chamado, demanda)
VALUES (6, 6, 'Instalação de antivírus nas máquinas da agência');

INSERT INTO public.chamados_agencias (id_agencia, id_chamado, demanda)
VALUES (7, 7, 'Atualização de sistema operacional nos computadores da agência');

INSERT INTO public.chamados_agencias (id_agencia, id_chamado, demanda)
VALUES (8, 8, 'Treinamento em novo software para funcionários da agência');

INSERT INTO public.chamados_agencias (id_agencia, id_chamado, demanda)
VALUES (9, 9, 'Diagnóstico de problema de acesso à rede externa na agência');

INSERT INTO public.chamados_agencias (id_agencia, id_chamado, demanda)
VALUES (10, 10, 'Configuração de e-mail para colaboradores da agência');

INSERT INTO public.chamados_agencias (id_agencia, id_chamado, demanda)
VALUES (11, 11, 'Solicitação e análise de novo equipamento para a agência');

INSERT INTO public.chamados_agencias (id_agencia, id_chamado, demanda)
VALUES (12, 12, 'Execução do backup de dados da agência');

INSERT INTO public.chamados_agencias (id_agencia, id_chamado, demanda)
VALUES (13, 13, 'Auxílio no problema de login dos colaboradores da agência');

INSERT INTO public.chamados_agencias (id_agencia, id_chamado, demanda)
VALUES (14, 14, 'Manutenção de hardware dos equipamentos da agência');

INSERT INTO public.chamados_agencias (id_agencia, id_chamado, demanda)
VALUES (15, 15, 'Revisão de segurança nos sistemas da agência');

INSERT INTO public.chamados_agencias (id_agencia, id_chamado, demanda)
VALUES (16, 16, 'Configuração de VPN para a agência');

INSERT INTO public.chamados_agencias (id_agencia, id_chamado, demanda)
VALUES (17, 17, 'Identificação e resolução de problema de conexão Wi-Fi na agência');

INSERT INTO public.chamados_agencias (id_agencia, id_chamado, demanda)
VALUES (18, 18, 'Atualização do banco de dados da agência');

INSERT INTO public.chamados_agencias (id_agencia, id_chamado, demanda)
VALUES (19, 19, 'Solicitação de licença de software para a agência');

INSERT INTO public.chamados_agencias (id_agencia, id_chamado, demanda)
VALUES (20, 20, 'Implementação de novos recursos nos sistemas da agência');


INSERT INTO public.chamados_agencias_terceiros (id_chamado_agencia, id_terceiro, valor, tenico, nfse, nfe) 
VALUES (1, 1, 150.00, 'Técnico 1', '111111', '111111');

INSERT INTO public.chamados_agencias_terceiros (id_chamado_agencia, id_terceiro, valor, tenico, nfse, nfe) 
VALUES (2, 2, 200.00, 'Técnico 2', '222222', '222222');

INSERT INTO public.chamados_agencias_terceiros (id_chamado_agencia, id_terceiro, valor, tenico, nfse, nfe) 
VALUES (3, 3, 180.00, 'Técnico 3', '333333', '333333');

INSERT INTO public.chamados_agencias_terceiros (id_chamado_agencia, id_terceiro, valor, tenico, nfse, nfe) 
VALUES (4, 4, 210.00, 'Técnico 4', '444444', '444444');

INSERT INTO public.chamados_agencias_terceiros (id_chamado_agencia, id_terceiro, valor, tenico, nfse, nfe) 
VALUES (5, 5, 190.00, 'Técnico 5', '555555', '555555');

INSERT INTO public.chamados_agencias_terceiros (id_chamado_agencia, id_terceiro, valor, tenico, nfse, nfe) 
VALUES (6, 6, 160.00, 'Técnico 6', '666666', '666666');

INSERT INTO public.chamados_agencias_terceiros (id_chamado_agencia, id_terceiro, valor, tenico, nfse, nfe) 
VALUES (7, 7, 170.00, 'Técnico 7', '777777', '777777');

INSERT INTO public.chamados_agencias_terceiros (id_chamado_agencia, id_terceiro, valor, tenico, nfse, nfe) 
VALUES (8, 8, 220.00, 'Técnico 8', '888888', '888888');

INSERT INTO public.chamados_agencias_terceiros (id_chamado_agencia, id_terceiro, valor, tenico, nfse, nfe) 
VALUES (9, 9, 195.00, 'Técnico 9', '999999', '999999');

INSERT INTO public.chamados_agencias_terceiros (id_chamado_agencia, id_terceiro, valor, tenico, nfse, nfe) 
VALUES (10, 10, 185.00, 'Técnico 10', '101010', '101010');

INSERT INTO public.chamados_agencias_terceiros (id_chamado_agencia, id_terceiro, valor, tenico, nfse, nfe) 
VALUES (11, 11, 175.00, 'Técnico 11', '1111110', '1111110');

INSERT INTO public.chamados_agencias_terceiros (id_chamado_agencia, id_terceiro, valor, tenico, nfse, nfe) 
VALUES (12, 12, 205.00, 'Técnico 12', '1212120', '1212120');

INSERT INTO public.chamados_agencias_terceiros (id_chamado_agencia, id_terceiro, valor, tenico, nfse, nfe) 
VALUES (13, 13, 195.00, 'Técnico 13', '1313130', '1313130');

INSERT INTO public.chamados_agencias_terceiros (id_chamado_agencia, id_terceiro, valor, tenico, nfse, nfe) 
VALUES (14, 14, 225.00, 'Técnico 14', '1414140', '1414140');

INSERT INTO public.chamados_agencias_terceiros (id_chamado_agencia, id_terceiro, valor, tenico, nfse, nfe) 
VALUES (15, 15, 190.00, 'Técnico 15', '1515150', '1515150');

INSERT INTO public.chamados_agencias_terceiros (id_chamado_agencia, id_terceiro, valor, tenico, nfse, nfe) 
VALUES (16, 16, 180.00, 'Técnico 16', '1616160', '1616160');

INSERT INTO public.chamados_agencias_terceiros (id_chamado_agencia, id_terceiro, valor, tenico, nfse, nfe) 
VALUES (17, 17, 210.00, 'Técnico 17', '1717170', '1717170');

INSERT INTO public.chamados_agencias_terceiros (id_chamado_agencia, id_terceiro, valor, tenico, nfse, nfe) 
VALUES (18, 18, 190.00, 'Técnico 18', '1818180', '1818180');

INSERT INTO public.chamados_agencias_terceiros (id_chamado_agencia, id_terceiro, valor, tenico, nfse, nfe) 
VALUES (19, 19, 215.00, 'Técnico 19', '1919190', '1919190');

INSERT INTO public.chamados_agencias_terceiros (id_chamado_agencia, id_terceiro, valor, tenico, nfse, nfe) 
VALUES (20, 20, 200.00, 'Técnico 20', '2020200', '2020200');

UPDATE agencias SET razao_social = 'Sudoeste' WHERE id = 2;
UPDATE agencias SET logradouro = 'Rua 15 de novembro' WHERE razao_social = 'Agência Leste';
UPDATE chamados SET status = 'ANDAMENTO' WHERE id = 1;
UPDATE chamados SET descricao = 'Problema na comunicação com a central' WHERE id = 1;
UPDATE chamados_agencias SET id_agencia = 4 WHERE id = 2;
UPDATE chamados_agencias SET demanda = 'Trocar cabos de rede' WHERE id = 1;
UPDATE chamados_agencias_terceiros SET id_terceiro = 9 WHERE id = 7;
UPDATE colaboradores SET telefone = '(47)12345-4321' WHERE nome = 'Julia';
UPDATE terceiros SET razao_social = 'NewTech' WHERE razao_social = 'Empresa XYZ';
UPDATE terceiros SET cidade = 'Blumenau' WHERE razao_social = 'Empresa MNO';

DELETE FROM agencias WHERE id = 3;
DELETE FROM agencias WHERE logradouro = 'Avenida dos Bosques, 2223';
DELETE FROM chamados WHERE status = 'NOVO';
DELETE FROM chamados WHERE id = 9;
DELETE FROM chamados_agencias WHERE id_agencia = 17;
DELETE FROM chamados_agencias WHERE demanda = 'Atualização do banco de dados da agência';
DELETE FROM chamados_agencias_terceiros WHERE id_terceiro = 11;
DELETE FROM colaboradores WHERE nome = 'Felipe';
DELETE FROM terceiros WHERE razao_social = 'Empresa QWE';
DELETE FROM terceiros WHERE cidade = 'Aracaju';


