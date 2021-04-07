def samogloski(data):
    if isinstance(data,str):
        for x in range(0,len(data),1):
            if data[x] in "aeiouy":
                yield data[x]

x=samogloski("jacekaaee")
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

