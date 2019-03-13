import requests


def get_live_data(city):
    r = requests.get('https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key=579b464db66ec23bdd000001c12b17afa71643da48365c5735fdc91d&format=json&offset=0&limit=800')
    r.json()
    data = r.json()
    station_list = ["Sanjay Palace, Agra - UPPCB",
                    "Maninagar, Ahmedabad - GPCB",
                    "Moti Doongri, Alwar, Rajasthan - RSPCB",
                    "Secretariat, Amaravati - APPCB",
                    "Golden Temple, Amritsar - PPCB",
                    "Asansol Court Area, Asansol - WBPCB",
                    "Hardev Nagar, Bathinda - PPCB",
                    "BTM Layout, Bengaluru - CPCB",
                    "Chandrapur, Chandrapur - MPCB",
                    "Mundaka, Delhi - DPCC",
                    "Bhopal Chauraha, Dewas - MPPCB"
                    "Sidhu Kanhu Indoor Stadium, Durgapur - WBPCB",
                    "Sector- 16A, Faridabad, Haryana - HSPCB",
                    "Vasundhara, Ghaziabad, UP - UPPCB",
                    "Haldia, Haldia - WBPCB",
                    "Ghusuri, Howrah - WBPCB",
                    "Bollaram Industrial Area, Hyderabad - TSPCB",
                    "Adarsh Nagar, Jaipur - RSPCB",
                    "Civil Line, Jalandhar - PPCB",
                    "Collectorate, Jodhpur - RSPCB",
                    "Nehru Nagar, Kanpur - UPPCB",
                    "Victoria, Kolkata - WBPCB",
                    "Shrinath Puram, Kota - RSPCB",
                    "Lalbagh, Lucknow - CPCB",
                    "Punjab Agricultural University, Ludhiana - PPCB",
                    "Opp GPO Civil Lines, Nagpur - MPCB",
                    "Gangapur Road, Nashik - MPCB",
                    "Airoli, Navi Mumbai - MPCB",
                    "Sector - 125, Noida, UP - UPPCB",
                    "IGSC Planetarium Complex, Patna - BSPCB",
                    "Karve Road Pune, Pune - MPCB",
                    "Bandhavgar Colony, Satna - MPPCB",
                    "Vindhyachal STPS, Singrauli - MPPCB",
                    "Tirumala, Tirupati - APPCB",
                    "Ashok Nagar, Udaipur - RSPCB",
                    "Mahakaleshwar Temple, Ujjain - MPPCB",
                    "Ardhali Bazar, Varanasi - UPPCB",
                    "PWD Grounds, Vijayawada - APPCB",
                    "GVM Corporation, Visakhapatnam - APPCB"
                    ]
    NO2 = "NA"
    SO2 = "NA"
    PM2_5 = "NA"
    PM10 = "NA"
    AQI = "NA"
    for ele in data['records']:
        if ele['city'] == city:
            if ele["station"] in station_list and ele["pollutant_id"] == "NO2":
                NO2 = ele["pollutant_avg"]
                if NO2 != "NA":
                    NO2 = int(ele["pollutant_avg"])
            elif ele["station"] in station_list and ele["pollutant_id"] == "SO2":
                SO2 = ele["pollutant_avg"]
                if SO2 != "NA":
                    SO2 = int(ele["pollutant_avg"])
            elif ele["station"] in station_list and ele["pollutant_id"] == "PM2.5":
                PM2_5 = ele["pollutant_avg"]
                if PM2_5 != "NA":
                    PM2_5 = int(ele["pollutant_avg"])
            elif ele["station"] in station_list and ele["pollutant_id"] == "PM10":
                PM10 = ele["pollutant_avg"]
                if PM10 != "NA":
                    PM10 = int(ele["pollutant_avg"])
    # print({"no2": NO2, "so2": SO2, "pm2_5": PM2_5, "pm10": PM10})
    if PM2_5 != "NA" and PM10 != "NA":
        AQI = calAqi(PM2_5, PM10)
    elif PM2_5 == "NA" and PM10 != "NA":
        AQI = calAqi(0, PM10)
    elif PM2_5 != "NA" and PM10 == "NA":
        AQI = calAqi(PM2_5, 0)
    else:
        AQI = calAqi(0, 0)
    return {"aqi": AQI, "no2": NO2, "so2": SO2, "pm2_5": PM2_5, "pm10": PM10}


def calAqi(pm2, pm10):
    aqi = 0
    ccaa = []
    # ccaa = [conc_low, conc_hi, aqi_low, aqi_hi]

    if pm2 != 0:
        if pm2 <= 12.0:
            ccaa = [0, 12.0, 0, 50]
        elif pm2 > 12.0 and pm2 <= 35.4:
            ccaa = [12.1, 35.4, 51, 100]
        elif pm2 > 35.4 and pm2 <= 55.4:
            ccaa = [35.5, 55.4, 101, 150]
        elif pm2 > 55.4 and pm2 <= 150.4:
            ccaa = [55.5, 150.4, 151, 200]
        elif pm2 > 150.4 and pm2 <= 250.4:
            ccaa = [150.5, 250.4, 201, 300]
        else:
            ccaa = [250.5, 500.4, 301, 500]

        aqi = int(((ccaa[3] - ccaa[2]) / (ccaa[1] - ccaa[0])) * (pm2 - ccaa[0]) + ccaa[2])

    elif pm10 != 0:
        if pm10 <= 54:
            ccaa = [0, 54, 0, 50]
        elif pm10 > 54 and pm10 <= 154:
            ccaa = [55, 154, 51, 100]
        elif pm10 > 154 and pm10 <= 254:
            ccaa = [155, 254, 101, 150]
        elif pm10 > 254 and pm10 <= 354:
            ccaa = [255, 354, 151, 200]
        elif pm10 > 354 and pm10 <= 424:
            ccaa = [355, 424, 201, 300]
        else:
            ccaa = [425, 604, 301, 500]

        aqi = int(((ccaa[3] - ccaa[2]) / (ccaa[1] - ccaa[0])) * (pm10 - ccaa[0]) + ccaa[2])


    return aqi
