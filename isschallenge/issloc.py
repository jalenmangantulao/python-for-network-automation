#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime
import reverse_geocoder as rg

URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp = requests.get(URL).json()
    
    # part 02
    isspos = resp.get('iss_position')
    # print(f"CURRENT LOCATION OF THE ISS:\nLon: {isspos.get('longitude')}\nLat: {isspos.get('latitude')}")

    # part 03
    # print(resp.get('timestamp'))
    epoch = resp.get('timestamp')
    timestamp = datetime.datetime.fromtimestamp(epoch)
    # print(f"CURRENT LOCATION OF THE ISS:\nLon: {isspos.get('longitude')}\nLat: {isspos.get('latitude')}\nTimestamp: {timestamp}")


    # part 04
    lat = isspos.get('latitude')
    lon = isspos.get('longitude')
    coords_tuple = (lat, lon)
    exactloc = rg.search(coords_tuple)
    # print(exactloc)
    locdict = exactloc[0]
    city = locdict['name']
    print(f"CURRENT LOCATION OF THE ISS:\nLon: {isspos.get('longitude')}\nLat: {isspos.get('latitude')}\nTimestamp: {timestamp}\nCity or Country: {city}")

if __name__ == "__main__":
    main()
