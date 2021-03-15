skroty = {"Jajka": "sztuki",
"Mleko": "sztuki",
"Kielbasa": "kilogramy",
"pomidor" : "kilogramy",
"butelka wody 2L": "sztuki"}
newlist = [x for x in skroty.items() if "sztuki" in x]
print (newlist)
print(skroty)