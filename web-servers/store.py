import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    #print(r.status_code)
    #print(r.text)

    categories = r.json()
    
    #for category in categories:
        #print(category['name'])

    category = [category['name'] for category in categories]
    category = set(category)
    for i in category:
        print(i)