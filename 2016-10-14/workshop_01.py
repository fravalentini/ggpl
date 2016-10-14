""" Primo esercizio in aula di creazione di una struttura"""
from pyplasm import *
def structure(x):
	horizontal =  CUBOID ([5,2,1])
	vertical  = CUBOID ([1,2,3])
	verticalStructure = STRUCT([vertical,T(3)(3),vertical]*x)
 	verticalStructure = STRUCT([verticalStructure,T(1)(4.0),verticalStructure]*(x+1))
    	horizontalStructure = STRUCT([horizontal,T(1)(4),horizontal]*x)
    	horizontalStructure = STRUCT([horizontalStructure,T(3)(3),horizontalStructure]*(x+1))
	structure = STRUCT([verticalStructure,T(0)(0),horizontalStructure]*x)
	VIEW(structure)

structure(5)