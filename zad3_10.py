def ile_produktow(**suma):
	return sum([int(value) for value in suma.values()])

print(ile_produktow(kielbasa=4,jablko=5,mandarynka=8))
def funkcja(**fun):
	menu = {'maslo': 3, 'bulka': 5}
	suma = 0
	for x,y in menu.items():
    	suma = suma + y
	return suma
print(funkcja())
