def main_request():

    import requests, json
    from datetime import date
    import datetime
    import locale
    
    ##import lyricsgenius
    ####genius = lyricsgenius.Genius("F1kUSDfmkThcvLzkgoWc08iZkzklGWhHHb4rRY6S_Kb4f7dnC130VuHvohfSJuPp")

    api_key = "270c91bb046e4c35af0c1666b7d180e4"

    request_url = f"https://newsapi.org/v2/top-headlines?country=fr&category=technology&apiKey={api_key}"
    response = requests.get(request_url)
    x = response.json()
    print(request_url)
    #return x

    #locale.setlocale(
        #category=locale.LC_ALL,
        #locale="French"  
    #)
    dateee = str(datetime.datetime.now())
    year, month, day = dateee.split("-") 
    day, rest = day.split(" ")

    day = int(day)
    month = int(month)
    year = int(year)

    the_date = date(day=day, month=month, year=year).strftime('%d %B %Y').title()

    if "January" in the_date:
        the_date = the_date.replace("january", "janvier")
    elif "February" in the_date:
        the_date = the_date.replace("February", "février")
    elif "March" in the_date:
        the_date = the_date.replace("March", "Mars")
    elif "April" in the_date:
        the_date = the_date.replace("April", "Avril")
    elif "May" in the_date:
        the_date = the_date.replace("May", "Mai")
    elif "June" in the_date:
        the_date = the_date.replace("June", "Juin")
    elif "July" in the_date:
        the_date = the_date.replace("July", "Juillet")
    


    date_o_the_day = f"Aujourd'hui, nous sommes le {the_date}"

    #return date_o_the_day

    #baseUrl = "http://api.genius.com"

    #headers = {'Authorization': 'Bearer F1kUSDfmkThcvLzkgoWc08iZkzklGWhHHb4rRY6S_Kb4f7dnC130VuHvohfSJuPp'}
    #searchUrl = baseUrl + "/search"
    #songTitle = "Shape of you"
    #data = {'q': songTitle}
    #response = requests.get(searchUrl, params=data, headers=headers)
    
    #x = response.json()

    ########song = genius.search_song("Shape of you")
    
    ########print(song.lyrics)


    i = 0
    while True:
        if x["articles"][i]["urlToImage"] == None:
            i = i+1
        else:
            val = x["articles"][i]["urlToImage"]
            break
    
    while True:
        if "http" not in str(x["articles"][i]["urlToImage"]):
            i = i+1
        else:
            val = x["articles"][i]["urlToImage"]
            break

        



    
    #return x["articles"][0]["urlToImage"]
    return val
    
########main_request()

##print(main_request())