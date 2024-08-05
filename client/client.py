import requests

# URL du serveur à contacter
server_url = 'http://server-container:5000'

# Envoi d'une requête GET au serveur et affichage de la réponse
response = requests.get(server_url)
print(f"Response from server: {response.text}")
