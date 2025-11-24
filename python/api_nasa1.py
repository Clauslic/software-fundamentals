'''
    API: Aplication Progrmming Interface
    Nasa API: https://api.nasa.gov/
    API_KEY_NASA: YOUR
    Developer: Claudia Cifuentes

''' 
import requests
import os

#os.system('cls')
def get_nasa_data(api_key):
    print("::: COMET INFORMATION :::")
    url =f"https://api.nasa.gov/neo/rest/v1/neo/3726709?api_key={api_key}"
    #realizar la solicitud a la api
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print(data)

    API_KEY_NASA = 'PXUCZslBiB58vBfWNFXOVamZ4J3JupDNLICjAC31'
    get_nasa_data(API_KEY_NASA)    