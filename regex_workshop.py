#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: musaddiqlodi

REGEX Workshop


"""

import re 


# Creating your first regular expression

search_string_one = "LeBron James is the greatest basketball player of all time. Leonel Messi is the greatest soccer player of all time"

# Using the search function, finds the first instance of a search pattern within a string
# Find basketball
search_result_one = re.search(r"", INSERTSEARCHSTRINGHERE)


# Find all instances of a pattern within a string 

# Find all the instances of the word time




# Find indexes of all matches of a search string 
'''for match in re.finditer(r"", INSERTSEARCHSTRINGHERE:
    print(match.group() + " found: " + str(match.start()) + "-" + str(match.end()))'''
    
    
    
# Conditional Example... write if statement! # If basketball is in the string...
'''if re.search(r"basketball", search_string_one):
    print("True!")'''




# Find index of all polyA tracts in a gene

search_gene = '''ATGCTCAAGCAATATATTATAAATTTAAATAGAATAGAAGAAGAAGGAAAATTAAATTCTGTAATTATAT
TAAAAAAAGAGATAGAAGATATTATTCAAATTTTTTATAGAAAAACAAAAAATAATCCGATACTTATTGG
AGAAAATGGAATAGGTAAAAAATCTATTGTTTACGGACTCGTAAAAAGAATTATAGATAGGAAAGTCCCA
AAAGAACTAATAAATAAAAAAATTCTTTATATAAAATTAAACGATATACTAAAAGAAATAGAATATTCTA
AAAAACTTTTACATAAAATAAATAGAATTCTCTCAAAGATCAGAGGAAATACAAATGTTATTATTTTTAT
CGAAAATTTACATGAAATATTCTACAAAAAAATTAGTAAAAATTTGAAGATTATAAAAAAATTAAAGAGC
AAAATTGATAAAAGACATGTGTATTGTATAGGTACAACTTCAAAAAGTAAATATATAAGTTATATATTAC
CAGATTCTATATTAGATAGAAGGTTTCAAAAAATATATATAAAAGAACCTACAGAGAAACAAACAGTTTC
CATATTGGAAAATATGAAATATAAATATGAATTATTCTATAATGTTCAAATAACAAGTTCAGCAATTTTA
GCAGCTTACAATTTTTCTAATCGTTTTATTAAGGATAAAGTTTTACCTGGTAAAGCAATAGATTTAATTG
ACAGAGCTAGTGCTATGGTAAAAGTTAAAATAGATTCTAATCCGAAGTTTTTACGTAAAGTAATAAATAA
AATTGAAAAATTAGAAATGAAGAAAGCTTTTCTAGATCACACAAACAATAAAACAAATGAAAATAAAGTA
AAAAATATTATAAAACAAATAATACAAAAAAAAAATGAACTTTTAGATTTAAGAAACAAATTAAAAAAAG
AAAGAGAAATAATTCAATATGTTAAAACCATTAAAAATAAAGTAATAAAACTTAAAAATAAATTGGAGCT
AGCTAAAAGAAACAAAAGTTTCTTTAAAATTTATGAATTACAAAAAAAAATGATTCCTTTATTAAATAAA
AGAATCTCATACATACAAAAAAAAGAAATTAAATGGAAAAAACTATTAAATAATAAGGTAACAAAACTTG
AAATAGCAAAAATTATTTCTAAAGACGAAGGAATACCAATTAATCTAATATTAGAAAATGAAAAAGAAAA
ATTAACTTTCATTGAAAGAGAAATAAGAAAAAATATTATTGGACAAAATAATGCAATTGTTAGAGTTTCG
AATACAATTATTAGAAATCAAACTTTTTCATCAAGTTCGAAGAATAAAATTATTTCATTTTTATTTCTTG
GACCAAAAGGAATTGGAAAAACTAAATTATGTAAAATACTTTCAAGATTTTTGTTTAATAGTGAAGATAC
TTTAGTAGAAATTAACATGTCAAACTACAGTAATGAAAATTCAATATATGACTTTATAGGAAGTAAATCT
AAGTCATTAAATAATAAACGTGGAATTTTAATAAAAAAACTTGAAATATATCCTAGTTGCATAATTCTAT
TAAAAAATATTGAACAAGCTGATAAAAATATTATTAATTTTCTTATGAAAATATTAAAAAATAAAAAATT
TGTTGATCTTGACGATAAGACAATAAATCATTCAAATATAATAATAGTTATGGAATCAAATATTATCTCT
TATATAATAAGAGAAAGATTTAAGCAATCGAAATACGACGAAATTCGGGAAATTTCATTAGACTCTATTC
TTCATATTTTTGATGTAGATTTTATTAAAATAATTGACGATATTGTAATTTTTAATCAACTTAGTAATAA
TCAAATTAAATATATAGTGAAAAATAAGCTTACAAAAATACTTAACAAAACAAAAGAACTTGGTTATAAA
GTTTTACCACTATCTTCTGTAATAACAAAATTGAGTGAAATTGGATTCGATAAAAACTTTGGATTAAAAA
ATTTAGATAAAGTAATACAAGAAAAAATAATGAACTTATTATCCAAAAAAATATTGTCGAAAGAAATTAA
AAAAGATAGAATACTAAAAGTAAGAACAAGAAAAAACAAATTTTTTCTTACATATTAA'''

# Indexes of all polyA Tracts in gene
'''for polyA in re.finditer(r"AAA+?(?=T|G|C)", search_gene):
    print(polyA.group() + " found: " + str(polyA.start()) + "-" + str(polyA.end()))'''

# List of all polyA Tracts in gene

#polyAList = re.findall(r"", search_gene)




# Go Term File 
# Goal: Write goTerms and their genes in tab separated file
'''
go_term_file = open("gotermfileworkshop.txt", "r")

go_term_string = go_term_file.read()






'''

















