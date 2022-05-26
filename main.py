def main():
    from requests import get
    from json import loads
    #tymczasowa zmienna url, w przyszlosci bedzie modyfikowana
    #url = "https://ckan2.multimediagdansk.pl/departures?stopId=1719"
    url = get('https://ckan2.multimediagdansk.pl/departures?stopId=1719').text
    response = loads(url)
    for data in response['departures']:
        print("=================================================")
        _id = data['id']
        estimated = data['estimatedTime']
        delay = data['delayInSeconds']
        headsign = data['headsign']
        route = data['routeId']
        status = data['status']
        theoretical = data['theoreticalTime']
        komunikat = "Autobus nr: " + str(route) + " " + str(headsign) + "\nPlanowany odjazd: " + str(theoretical)
        print(komunikat)
        print("=================================================")


        
            
        
        


if __name__ == "__main__":
    main()