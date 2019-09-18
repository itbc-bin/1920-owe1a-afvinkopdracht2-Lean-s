#Weektaak script 2.1 , door Lean Schoonveld
print("Om het aantal nucleotiden te tellen, moet je een sequentie invoeren:")
sequentie = input('voer nu het mRNA (zonder enters) in -> ')

aantal_A = sequentie.count("A")
aantal_T = sequentie.count("T")
aantal_C = sequentie.count("C")
aantal_G = sequentie.count("G")
#Hier worden de nucleotiden apart geteld.

print(" ")
cg_mRNA = (aantal_C + aantal_G)
print("Van cytosine en guanine zijn er in totaal " + str(cg_mRNA))

totaal_nuc_mRNA = (aantal_A + aantal_T + aantal_C + aantal_G)
print("Het totaal aantal nucleotiden is " + str(totaal_nuc_mRNA))
#Hier worden de nucleotiden bij elkaar opgeteld, het kan sneller met len, maar toen had ik dit al:0

print("Het GC% is " + str(float(float(cg_mRNA) / float(totaal_nuc_mRNA)) * 100) + "%")

#We gaan nu kijken bij het GENOOM
print(" ")
print("We gaan nu kijken bij het genoom: ")
sequentie_genoom = input("vul hier nu het genoom (zonder enters) in -> ")


aantal_Aa = sequentie_genoom.count("A")
aantal_Tt = sequentie_genoom.count("T")
aantal_Cc = sequentie_genoom.count("C")
aantal_Gg = sequentie_genoom.count("G")

totaal_nuc_genoom = int(aantal_Aa + aantal_Tt + aantal_Cc + aantal_Gg)
#Het totaal aantal aan nucleotiden in het genoom
print(" ")
print("Het totaal aantal aan nucleotiden in het genoom is " + str(totaal_nuc_genoom) + ".")

cg_genoom = int(aantal_Cc + aantal_Gg)
print("Van cytosine en guanine zijn er in totaal " + str(cg_genoom) + ".")
print("Het GC% van het genoom is " + str(float(cg_genoom) / float(totaal_nuc_genoom) * 100) + "%")



