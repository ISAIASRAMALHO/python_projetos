"""
 OBJETIVO DESTE PROGRAMA É POSSIBILITAR A EXPORTAÇÃO DE TABELAS dBASE (*DBF) PARA ARQUIVOS CSV.
 PROGRAMA: cria_csv.py
 LINGUAGEM: PYTHON
 PROGRAMADOR: ISAIAS RAMALHO
 """
import sys, csv
import glob
from dbfread import DBF
from datetime import date, datetime



# FUNÇÃO PARA CONVERTER ARQUIVOS DBF EM ARQUIVOS CSV

def Converta_DBF_em_CSV( c_dbf ):
    for item in c_dbf:
        tabela = DBF(item, encoding='latin1')
        so_nome = item.replace( '.dbf'.upper(), '') + '.csv'
        f = open(so_nome, 'w', encoding='utf-8')

        b_progress  = 0
        c = 1 

        try:
            wrt = csv.writer(f)
            wrt.writerow( tabela.field_names )
            for record in tabela:
                wrt.writerow( record.values() )
                b_progress = int( ( c /  len(tabela) ) * 100 )
                print('#'*b_progress, str(b_progress)+'%')
                c += 1
        finally:
            f.close()


lista_f = glob.glob( '*.dbf')

if lista_f:
    print('Existem {} arquivos nesta pasta.'.format( len(lista_f)))
    s_n = input( 'Deseja fazer a conversão? S=CONTINUA N=SAI : ')
    if s_n == 's'.upper():
        Converta_DBF_em_CSV( lista_f)

