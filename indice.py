from mila import priceChegusanARS
from glassdoor import salaryArgentinaARS

def indice(debug=False):
    ratioMes = salaryArgentinaARS(debug=debug) / priceChegusanARS(debug=debug)
    print (f"Indice Mila : {ratioMes:.2f} sandwiches de milanga por mes")
    ratioDia = ratioMes * 12 / 365
    print (f"Indice Mila : {ratioDia:.2f} sandwiches de milanga por día")
    

if __name__ == "__main__": 
    indice(debug=True)
