from TOKENS.tokens import tokens
import requests
amount = 0
for token in tokens:
    token = token.replace('http://kavkev.kg/', '')
    
    data = {
            "token": token,
            "slug": token
            }
    siteURL = 'http://api-kavkev.kg:8080/api/token/'
    response = requests.post(siteURL, data)
    amount += 1

    print(f"{token}   ---   {amount}")