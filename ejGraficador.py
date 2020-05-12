import networkx as nx
import matplotlib as plt

G=nx.Graph()

G.add_node("A",pos=(1,2))
G.add_node("B",pos=(1,19))
G.add_node("C",pos=(2,5))
G.add_node("D",pos=(3,11))
G.add_node("E",pos=(5,18))
G.add_node("F",pos=(6,4))
G.add_node("G",pos=(7,12))
G.add_node("H",pos=(8,20))
G.add_node("I",pos=(10,16))
G.add_node("J",pos=(10,10))
G.add_node("K",pos=(11,7))
G.add_node("L",pos=(13,5))
G.add_node("M",pos=(13,11))
G.add_node("N",pos=(14,19))
G.add_node("O",pos=(16,16))
G.add_node("P",pos=(17,4))
G.add_node("Q",pos=(17,9))
G.add_node("R",pos=(19,11))
G.add_node("S",pos=(20,1))
G.add_node("T",pos=(20,20))

G.add_edges_from(
    [('A', 'B'), ('A', 'C'), ('A', 'F'), ('A', 'G'),
     ('B', 'C'), ('B', 'E'), ('B', 'G'), ('B', 'H'),
     ('C', 'D'), ('C', 'F'), ('C', 'G'),
     ('D', 'E'), ('D', 'F'), ('D', 'G'), ('D', 'H'), ('D', 'J'), ('D', 'K'),
     ('E', 'G'), ('E', 'H'), ('E', 'I'),
     ('F', 'K'), ('F', 'L'), ('F', 'S'),
     ('G', 'H'), ('G', 'I'),( 'G', 'J'),
     ('H', 'I'),
     ('I', 'M'), ('I', 'N'), ('I', 'O'),
     ('J', 'K'), ('J', 'M'), ('J', 'N'),('J', 'O'), ('J', 'Q'),
     ('K', 'L'), ('K', 'Q'), 
     ('L', 'M'), ('L', 'O'), ('L', 'P'), ('L', 'Q'),
     ('M', 'P'), ('M', 'Q'), ('M', 'R'), 
     ('N', 'O'), ('N', 'R'), 
     ('O', 'Q'), ('O', 'R'),('O', 'T'),
     ('P', 'Q'), ('P', 'S'),
     ('Q', 'S'),
     ('R', 'S'), ('R', 'T'),
     ('S', 'T')])

pos=nx.get_node_attributes(G,"pos")

nx.draw(G,pos,with_labels=True )