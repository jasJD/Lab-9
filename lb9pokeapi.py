import requests

def get_pokemon_info(name):
    print('Getting Pokemon Information...', end='')
    
    if name is None:
        print("Error: Missing name parameter")
        return
    
    name = name.strip().lower()
    if name =='':
        print('Error: Empty name parameter')
        return 
        
    url = 'https://pokeapi.co/api/v2/pokemon/' + name
    response = requests.get(url)
    if response.status_code == 200:
        print('Success')
        return response.json()
    else:
        print('Failed.Response code:', response.status_code)
        return
    
def get_pokemon_image_url(name):
    pokemon_dict = get_pokemon_info(name)
    if pokemon_dict:
        return pokemon_dict['sprites']['other']['official-artwork']['front_default']

def get_pokemon_list(limit=100, offset=0):
    url = 'https://pokeapi.co/api/v2/pokemon'    
    params ={
        'limit':limit,
        'offset':offset
    }
        
    resp_msg=requests.get(url, params=params)
        
    if resp_msg.status_code == 200:
        resp_dict = resp_msg.json()
        return[p['name']for p in resp_dict['results']]
    else:
        print('Failed to get Pokemon list')
        print('Response code:', resp_msg.status_code)
        print(resp_msg.text)   