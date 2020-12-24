import requests

headers = {
    "User-Agent":"Mozilla/5.0 (Linux; Android 10; SM-J400F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36",
    "Referer":"https://www.zee5.com",
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.9",
    "Origin":"https://www.zee5.com",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-site",
}

token_url1 = "https://useraction.zee5.com/tokennd"
search_api_endpoint = "https://gwapi.zee5.com/content/details/"
platform_token = "https://useraction.zee5.com/token/platform_tokens.php?platform_name=web_app"
token_url2 = "https://useraction.zee5.com/token"
stream_baseurl = "https://zee5vodnd.akamaized.net"


# link = "https://www.zee5.com/movies/details/khaali-peeli/0-0-260877"
link = input("Enter the Zee5 link: ")
w = link.split('/')[-1]

req1 = requests.get(token_url1, headers=headers).json()
req2 = requests.get(platform_token).json()["token"]
headers["X-Access-Token"] = req2
req3 = requests.get(token_url2, headers=headers).json()
r1 = requests.get(search_api_endpoint+w,headers=headers, params={"translation":"en", "country":"IN"}).json()
g1 = (r1["hls"][0].replace("drm", "hls") + req1["video_token"])
stream = stream_baseurl+g1

print("\nLINK TO STREAM: \n\n"+stream+"\n\n")