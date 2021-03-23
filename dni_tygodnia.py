def dzien_tygodnia(a):
    dni=["poniedzialek","wtorek","sroda","czwartek","piatek","sobota","niedziela"]
    return dni[a-1]
def skroty(b):
    krotkiedni = {'poniedzialek': "pon", 'wtorek': 'wt', 'sroda': 'srd', 'czwartek': 'czw','piatek': 'pt','sobota':'sb','niedziela': 'nd'}
    return (krotkiedni[b])