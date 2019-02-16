""" The code consists of several functions that combined together produce and store police crime log obtained from their servers.
    Required input (Post code, start date, end date) is turned into json then formatted by one of the mentioned functions
    and stored.
"""

def getCoords(PostCode):
    try:
        url = "http://api.postcodes.io/postcodes/CV15FB" #+ str(PostCode)
        data = generateJsonUrl(url)
        return data["result"]["latitude"], data["result"]["longitude"]
    except:
        print("Wrong UK address")

def getTimePeriods (startDate, endDate):
    """ Function to output a list with the range of time periods between startDate and endDate """
    #startMonth,startYear, endMonth, endYear

    months = [None, "01","02","03","04","05","06","07","08","09","10","11","12"]
    outputDates = []

    try:
        startYear = startDate[:4]
        startYear = int(startYear)

        endYear = endDate[:4]
        endYear = int(endYear)

        startMonth = startDate[5:]
        startMonth = months.index(startMonth)

        endMonth = endDate[5:]
        endMonth = months.index(endMonth)

    except:
        print("Incorrect Date Format")
        return None

    # Time period enumerator
    for year in range(startYear,endYear + 1):
        for month in range(startMonth,13):

            outputDates.append(str(year) +"-"+str(months[month]))

            if month == endMonth and year == endYear:
                break

        startMonth = 1

    return outputDates

def generateApiUrl(date, coords):
    """Output an url for API"""
    # Coords[0] = latitude; coords[1] = longitude
    try:
        date = str(date)
        lat = str(coords[0])
        lng = str(coords[1])
    except ValueError:
        print("Wrong value")

    return "https://data.police.uk/api/crimes-at-location?date=%s&lat=%s&lng=%s" % (date,lat,lng)

generateApiUrl("2015-02",(52.629729,-1.121592))

def generateJsonUrl(url):
    """This reads the contents of a URL.  Works for json data and Python 3"""
    #####################################################################
    # In this block of code:
    # - Python opens the url
    # - reads the data
    # - stores it as a string
    # - closes the url
    import urllib.request
    try:
        page = urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        print("There was an error opening the URL (description below).")
        print(e)
        print("Ask for help?")
        return(None)
    data_bytes = page.read()
    data_str = data_bytes.decode('utf-8')
    page.close()
    #####################################################################
    # In this block of code
    # - The json string is converted to a Python dictionary.
    # - This is returned
    import json
    try:
        output = json.loads(data_str)
    except:
        print("Error")
        return(None)
    return(output)
    #####################################################################

def formatData(json):
    """In: Json
       Out: Dict {date: [[crime1]...[crimeN]]}"""

    crimeDict = {}
    i = 0

    try:
        crimeDate = str(json[0]["month"])
        for i in range(len(json)):
            print(str(json[i]["month"]))

        crimeDict[crimeDate] = []


        for i in range(len(json)):

            output = ""
            output = "Category: " + json[i]['category']
            output = output + "\nApproximate location: " + str(json[i]['location']["street"]["name"])
            if isinstance(json[i]['outcome_status'],str):
                output = output + "\nCurrent status: " + str(json[i]['outcome_status']["category"]) +' ('+ str(json[i]['outcome_status']["date"]) +')'
            else:
                output = output + "\nCurrent status: Not Available"
            crimeDict[crimeDate].append([output])
        return crimeDict
    except:
        return {"Unavailable Month":[]}

def storeData(data, postCode):
    """Function for storing data in a file"""
    f = open("Crimes.txt", 'a')

    for key, value in data.items(): # Breaks down the input tuple
        date = key
        data = value

    #Create a title for each new peace of appended data ( date at latitude: X longitude: X )
    f.write(date + " at " + postCode )

    for i in range(len(data)): # will enumerate and start each crime in a new line

        content = "".join(data[i]) # Will convert a list to string
        f.write('\n[' +str(i+1) + '] ' + str(content) )

    f.write("\n")

    f.close()

def makeLog (postCode, startDate, endDate):
    dates = getTimePeriods(startDate, endDate)
    coords = postCodeToCoordinates(postCode)

    for i in range(len(dates)):
        url = generateApiUrl(dates[i], coords)
        data = generateJsonUrl(url)
        data = formatData(data)
        storeData(data,postCode)

