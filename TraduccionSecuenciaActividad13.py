# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re 



def leer_secuencia(inputfile):
    '''Función que nos permite leer y cargar la secuencia desde el txt.
    '''
    with open(inputfile, "r") as f:
        secuencia = f.read()
        
    return secuencia 

def traduccion(secuencia):
    """
    Función que se encarga de llevar a cabo la traducción de una cadena
    de nucleótidos a una cadena de aminoácidos. 
    """
    tabla = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
    
    proteina = " "  #Inicializamos la variable proteina como una cadena vacía.

    pattern = re.compile('((?:A|C|T|G){3})', re.IGNORECASE ) 
    '''Se trata de un patrón que nos permite reconocer dichos caracteres 
en la secuencia y agruparlos en grupos de 3.
'''
    for codon in pattern.findall(secuencia):
        print(codon.upper())
        
        proteina += tabla[codon]

    return proteina 