# ICDS6-2023-Projeto-Dataset-

```
https://storage.googleapis.com/kaggle-data-sets/3590545/6248227/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20231016%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20231016T124555Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=9359b03021c86b8d61f3fdf7226f5b03c3a3f6dac4736ef395d2091ff17b166fd9d025c53dd2a2c93c5f3e1f3cd1b7785fcade5423f9e0de53ec3731c3a23dbe6d51916b4519c0011876f8954d805a584948d389b2cc456a6c400c20a1c1c6a9808eb9304c208c5a6636d285e81b626f537f6d83bee52eedab4b9cb4e0deefcf92254e3b910d816e943a6157c44281dcac9ed38437b8995cb4e0fa2d140e6d536195903312ec84e44eea313190a4e9a56508f9e2812ebf42224be562f7c1b9f3b19237f97ba1ac8f55c939d8600a6267ae7d63fe871230602abd641f6d85953cbc55f2b90f469702cce1bd6b05150ebb2f820c98d92f976056b2963fe1dc804a
```
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


# data
# horario
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

# tipo_de_ocorrencia
sem vitima = 0 <br>
com vitima = 1 <br>

# km
Mantém

# trecho
Qualquer que tenha MG = 0 <br>
Qualquer que tenha SP = 1 <br>

# sentido
Norte = 0 <br>
Sul = 1 <br>

# tipo_de_acidente
Mantém
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
