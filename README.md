# ICDS6-2023-Projeto-Dataset-

```
https://storage.googleapis.com/kaggle-data-sets/3590545/6248227/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20231016%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20231016T124555Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=9359b03021c86b8d61f3fdf7226f5b03c3a3f6dac4736ef395d2091ff17b166fd9d025c53dd2a2c93c5f3e1f3cd1b7785fcade5423f9e0de53ec3731c3a23dbe6d51916b4519c0011876f8954d805a584948d389b2cc456a6c400c20a1c1c6a9808eb9304c208c5a6636d285e81b626f537f6d83bee52eedab4b9cb4e0deefcf92254e3b910d816e943a6157c44281dcac9ed38437b8995cb4e0fa2d140e6d536195903312ec84e44eea313190a4e9a56508f9e2812ebf42224be562f7c1b9f3b19237f97ba1ac8f55c939d8600a6267ae7d63fe871230602abd641f6d85953cbc55f2b90f469702cce1bd6b05150ebb2f820c98d92f976056b2963fe1dc804a

```
https://spotted-starburst-40a.notion.site/Capture-the-flag-6f2a1f96fd2a4cb9bfedec81f9b653ef

# Instalação
```
pip install plotly
```
ou
```
pip3 install numpy
```

```
pip install pandas
```
```
pip install cufflinks
```

# Execução

```
python PC.py
```

# Graficos a serem feitos

(Fazer)
Gráfico de Segmento ou gráfico de linhas -> Y = Numero de acidentes, X = Horario (00:00 - 00:59 a 23:00 - 23:59) <br>
Gráfico de Segmento ou gráfico de linhas -> Y = Numero de acidentes, X = Data (2010 a 2023) <br>
(Decidindo)<br>
Donut -> Quantidade de( Ilesos, Levemente moderado e gravemente feridos, mortos ) um para o sentido Sul e outro para o Norte <br>
Donut -> Quantidade de( Ilesos, Levemente moderado e gravemente feridos, mortos ) um para MG e outro para SP <br>




# Cordenadas Paralelas

![image](https://github.com/HenriqueHyonemoto/ICDS6-2023-Projeto-Dataset/assets/91375748/81a1737a-6832-4894-ae8a-af17c8be0141)


# Eixo Radial
https://observablehq.com/@bradysheridan/radar-chart-generator

# Comandos do Jupyter Notebook

### Iniciar o Jupyter Notebook
>Entre no seu diretorio

```
jupyter notebook
```

### Iniciar Edição

>Entre no seu diretorio
>New
>Python3(ipykernel)

```
import pandas as pd
```
```
acidentesDF = pd.read_csv('AUTOPISTA_FERNO_DIAS.csv')
```

# Dataset: Acidentes automotivos na Rodovia Fernão Dias.

![image](https://github.com/HenriqueHyonemoto/ICDS6-2023-Projeto-Dataset/assets/91375748/a79895a2-086d-4ead-9f62-b9f8790b0685)

![image](https://github.com/HenriqueHyonemoto/ICDS6-2023-Projeto-Dataset/assets/91375748/ccc21089-f406-4104-903f-e3af9c9dd665)



# data (CP e ER)
Deixar somente o ano
# horario (CP e ER)
00:00 a 00:59 -> 0 <br>
01:00 a 01:59 -> 1 <br>
02:00 a 02:59 -> 2 <br>
03:00 a 03:59 -> 3  <br>
04:00 a 04:59 -> 4 <br>
05:00 a 05:59 -> 5 <br>
06:00 a 06:59 -> 6 <br>
07:00 a 07:59 -> 7 <br>
08:00 a 08:59 -> 8 <br>
09:00 a 09:59 -> 9 <br>
10:00 a 10:59 -> 10 <br>
11:00 a 11:59 -> 11 <br>
12:00 a 12:59 -> 12 <br>
13:00 a 13:59 -> 13 <br>
14:00 a 14:59 -> 14 <br>
15:00 a 15:59 -> 15 <br>
16:00 a 16:59 -> 16 <br>
17:00 a 17:59 -> 17 <br>
18:00 a 18:59 -> 18 <br>
19:00 a 19:59 -> 19 <br>
20:00 a 20:59 -> 20 <br>
21:00 a 21:59 -> 21 <br>
22:00 a 22:59 -> 22 <br>
23:00 a 23:59 -> 23 <br>

# tipo_de_ocorrencia (CP e ER)
sem vitima = 0 <br>
com vitima = 1 <br>

# km (CP e ER)
0 a 100 = 100 <br>
101 a 200 = 200 <br>
201 a 300 = 300 <br>
301 a 400 = 400 <br>
401 a 500 = 500 <br>
501 a 600 = 600 <br>
601 a 700 = 700 <br>
701 a 800 = 800 <br>
801 a 900 = 900 <br>
901 a 1000 = 1000 <br>

# trecho (CP e ER)
Qualquer que tenha MG = 0 <br>
Qualquer que tenha SP = 1 <br>

# sentido (CP e ER)
Norte = 0 <br>
Sul = 1 <br>

# tipo_de_acidente (Somente CP)
Saida de Pista = 0 <br>
Outros - Sequencia = 1 <br>
Choque - Defensa barreira ou ""submarino"" = 2 <br>
Choque - Elemento de Drenagem = 3 <br>
Colisao Traseira = 4 <br>
Atropelamento de Animal = 5 <br>
Engavetamento = 6 <br>
Capotamento = 7 <br>
Queda de Moto = 8 <br>
Colisao Lateral = 9 <br>
Choque - Suporte de Sinalizacao = 10 <br>
Outros = 11 <br>
Tombamento = 12 <br>
Colisao Frontal = 13 <br>
Atropelamento - Morador = 14 <br>
Choque - Talude = 15 <br>
Choque - Objeto sobre a pista = 16 <br>
Atropelamento - Andarilho = 17 <br>
Atropelamento - Ciclista = 18 <br>
Choque - Poste = 19 <br>
Atropelamento - Usuario = 20 <br>
Choque - Veiculo parado no acostamento = 21 <br>
Choque - Cancela de Pedagio = 22 <br>
Choque - Arvore = 23 <br>
Choque - Veiculo parado na pista = 24 <br>
Atropelamento - Ambulante = 25 <br>
Acidentes de outra natureza = 26 <br>
Atropelamento - Funcionario = 27 <br>
Atropelamento de pedestre = 28 <br>
Atropelamento - Sem Informacao = 29 <br>
Objeto lancado contra veiculo = 30 <br>
Colisao Transversal = 31 <br>
Soterramento = 32 <br>
Choque - outros = 33 <br>
Atropelamento - Outros = 34 <br>
Choque - Objeto nao identificado = 35 <br>
Choque = 36 <br>


# automovel 
Mantém
# bicicleta
Mantém
# caminhao
Mantém
# moto
Mantém
# onibus
Mantém
# outros
Mantém
# tracao_animal
Mantém
# transporte_de_cargas_especiais
Mantém
# trator_maquinas
Mantém
# utilitarios
Mantém
# ilesos
Mantém
# levemente_feridos
Mantém
# moderadamente_feridos
Mantém
# gravemente_feridos
Mantém
# mortos
Mantém
