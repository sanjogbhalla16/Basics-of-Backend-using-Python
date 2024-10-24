import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    #data was in string we made sure we have converted into json format
    
    if data["success"] and "data" in data:
        user_data =  data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        city = user_data["location"]["city"]
    else:
        print(f'{data}')

