from bs4 import BeautifulSoup
import json, requests

# https://www.rappi.com.ar/search?query=milanesa&vertical=restaurants&parent_store_type=restaurant
# https://www.rappi.com.ar/search?query=sandwich%20milanesa&vertical=restaurants&parent_store_type=restaurant


html_content = """
<!DOCTYPE html><html lang="es"><head>
...
</html>
"""

def priceChegusanARS(debug=False):

    url = 'https://www.rappi.com.ar/search?query=milanesa&vertical=restaurants&parent_store_type=restaurant'
    html_content = requests.get(url).text
    #html_content = open('mila4.html').read()

    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all script tags with schema data
    schema_scripts = soup.find_all('script', {'type': 'application/ld+json'})

    print (len(schema_scripts))

    prices = []

    for script in schema_scripts:
        schema_data = json.loads(script.string)
        #print(schema_data.keys())
        if schema_data['@type'] == 'ItemList':
            for item in schema_data['itemListElement']:
                product_name = item['item']['name'].lower()
                #print (product_name)
                
                product_name_s = product_name.split()
                #print (product_name_s)
                    #and ('sándwich' in product_name_s or 'sandwich' in product_name_s)  \
                #if ('cuadrada' in product_name_s or 'peceto' in product_name_s or 'milanesa' in product_name_s or 'mila' in product_name_s or 'completo' in product_name_s or 'completa' in product_name_s or 'sandwich' in product_name_s or 'sándwich' in product_name_s) \
                if 'combo' not in product_name_s \
                    and 'soja' not in product_name_s \
                    and 'vegetalex' not in product_name_s \
                    and 'calabaza' not in product_name_s \
                    and 'vegetales' not in product_name_s \
                    and 'vegetal' not in product_name_s \
                    and 'cerdo' not in product_name_s \
                    and 'pollo' not in product_name_s \
                    and 'lomito' not in product_name_s \
                    and 'plantas' not in product_name_s \
                    and '2' not in product_name_s \
                    and 'churrasquito' not in product_name_s \
                    and 'napolitana' not in product_name_s \
                    and 'jamon' not in product_name_s \
                    and 'jamón' not in product_name_s \
                    and 'miga' not in product_name_s \
                    and 'hamburguesa' not in product_name_s \
                    and 'kg' not in product_name_s:
                    offer = item['item']['offers']
                    #print(offer)
                    
                    if '@type' in offer and offer['@type'] == 'AggregateOffer':
                        prices.append(offer['lowPrice'])
                    elif '@type' in offer and offer['@type'] == 'Offer':
                        prices.append(offer['price'])
                    if debug:
                        print(product_name, prices[-1])

    #print("Precios de Sandwich de Milanesa (ARS):")
    #for price in prices:
    #    print(price)

    if debug:
        print('Mean: ', sum(prices)/len(prices))
        print('Median: ', sorted(prices)[len(prices)//2])
    return sum(prices)/len(prices)

if __name__ == "__main__":
    priceChegusanARS(debug=True)
    
