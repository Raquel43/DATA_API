# We import the necessary libraries
import requests
import json
import time
import re
from typing import Optional
from pydantic import BaseModel
# define global variable
selection=0

class BikeUpdate(BaseModel):
    id:Optional[int]
    model: Optional[str]
    brand: Optional[str]
    features: Optional[str]
    year: Optional[int]
    size: Optional[int]
    availability: Optional[bool]
    price: Optional[int]
    type_currency: Optional[str]
    latitude: Optional[float]
    length: Optional[float]

    location: Optional[dict]
# Function test. Displays the first element of the document
def test():
    url = "https://data.mongodb-api.com/app/data-ftfni/endpoint/data/v1/action/findOne"
    payload = json.dumps({
            "collection": "bikes",
            "database": "rental",
            "dataSource": "Cluster0",
            "projection": {
                "_id": 1
            }
        })
    headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': 'dQyCe7lvJL2Rtb1JMHPX6kbyZSybvfuzrZA4tOprAqu0I0lMGSitWA8lCh0np2xO'
        }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

# Shows the list of elements of the collection
def test2():
    url = "https://data.mongodb-api.com/app/data-ftfni/endpoint/data/v1/action/find"
    payload = json.dumps({
            "collection": "bikes",
            "database": "rental",
            "dataSource": "Cluster0",
            "filter": {}
        })
    headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': 'dQyCe7lvJL2Rtb1JMHPX6kbyZSybvfuzrZA4tOprAqu0I0lMGSitWA8lCh0np2xO'
        }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

# Make a grouping of characteristics and count how many documents there are of each
def test3():
    url = "https://data.mongodb-api.com/app/data-ftfni/endpoint/data/v1/action/aggregate"
    payload = json.dumps({
            "collection": "bikes",
            "database": "rental",
            "dataSource": "Cluster0",
            "pipeline" : [ { "$group": { "_id" : "$features",
                        "count" : { "$sum" : 1}
                        }}]

        })
    headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': 'dQyCe7lvJL2Rtb1JMHPX6kbyZSybvfuzrZA4tOprAqu0I0lMGSitWA8lCh0np2xO'
        }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

# Search for a document by its id
def test4(id):
    url = "https://data.mongodb-api.com/app/data-ftfni/endpoint/data/v1/action/find"
    payload = json.dumps({
            "collection": "bikes",
            "database": "rental",
            "dataSource": "Cluster0",
            "filter": {
            "_id": id
            }
        })
    headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': 'dQyCe7lvJL2Rtb1JMHPX6kbyZSybvfuzrZA4tOprAqu0I0lMGSitWA8lCh0np2xO'
        }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

# Search for a documents by price
def test5(price):
    url = "https://data.mongodb-api.com/app/data-ftfni/endpoint/data/v1/action/find"
    payload = json.dumps({
            "collection": "bikes",
            "database": "rental",
            "dataSource": "Cluster0",
            "filter": {
            "Price_day": price
            }
        })
    headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': 'dQyCe7lvJL2Rtb1JMHPX6kbyZSybvfuzrZA4tOprAqu0I0lMGSitWA8lCh0np2xO'
        }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

# Group by the element selected by the user
def test6(key):
    url = "https://data.mongodb-api.com/app/data-ftfni/endpoint/data/v1/action/aggregate"
    payload = json.dumps({
            "collection": "bikes",
            "database": "rental",
            "dataSource": "Cluster0",
            "pipeline" : [ { "$group": { "_id" : f"${key}",
                        "count" : { "$sum" : 1}
                        }}]
        })
    headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': 'dQyCe7lvJL2Rtb1JMHPX6kbyZSybvfuzrZA4tOprAqu0I0lMGSitWA8lCh0np2xO'
        }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

# Insert a document
def test7(id, model, brand, features, year, size, availability, price, type_currency, latitude, length):
    url = "https://data.mongodb-api.com/app/data-ftfni/endpoint/data/v1/action/insertOne"
    payload = json.dumps({
            "collection": "bikes",
            "database": "rental",
            "dataSource": "Cluster0",
            "document": {
            "_id": id, "model": model, "brand":brand, "features": features, "year": year, "size": size, "availability": availability, "Price_day":[ price, type_currency], "location":{"latitude":latitude, "length":length}
            }
        })
    headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': 'dQyCe7lvJL2Rtb1JMHPX6kbyZSybvfuzrZA4tOprAqu0I0lMGSitWA8lCh0np2xO'
        }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

# Delete a document
def test8(id):
    url = "https://data.mongodb-api.com/app/data-ftfni/endpoint/data/v1/action/deleteOne"
    payload = json.dumps({
            "collection": "bikes",
            "database": "rental",
            "dataSource": "Cluster0",
            "filter": {
            "_id": id
            }
        })
    headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': 'dQyCe7lvJL2Rtb1JMHPX6kbyZSybvfuzrZA4tOprAqu0I0lMGSitWA8lCh0np2xO'
        }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

def test9(id, model, brand, features, year, size, availability, price, type_currency, latitude, length):
    url = "https://data.mongodb-api.com/app/data-ftfni/endpoint/data/v1/action/updateOne"
    payload = json.dumps({
            "collection": "bikes",
            "database": "rental",
            "dataSource": "Cluster0",
            "filter": {
            "_id": id
            },
            "update" : {"$set":{"model":model, "brand": brand, "features": features, "year": year, "size": size, "availability":availability, "Price_day":[price, type_currency], "location":{"latitude":latitude, "length":length} }}
        })
    headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': 'dQyCe7lvJL2Rtb1JMHPX6kbyZSybvfuzrZA4tOprAqu0I0lMGSitWA8lCh0np2xO'
        }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

def testModel(id):
    url = "https://data.mongodb-api.com/app/data-ftfni/endpoint/data/v1/action/aggregate"
    payload = json.dumps({
            "collection": "bikes",
            "database": "rental",
            "dataSource": "Cluster0",
            "pipeline" : [ { "$match": { "_id" :id}},
                { "$project": { "model": 1, "_id": 0 }}
                        ]
    })
        
    headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': 'dQyCe7lvJL2Rtb1JMHPX6kbyZSybvfuzrZA4tOprAqu0I0lMGSitWA8lCh0np2xO'
        }
    response = requests.request("POST", url, headers=headers, data=payload)
    word = "model"
    position = re.search(word, response.text)
    ini = position.end()+3
    string = response.text[ini:-4]
    return string

def testBrand(id):
    url = "https://data.mongodb-api.com/app/data-ftfni/endpoint/data/v1/action/aggregate"
    payload = json.dumps({
            "collection": "bikes",
            "database": "rental",
            "dataSource": "Cluster0",
            "pipeline" : [ { "$match": { "_id" :id}},
                { "$project": { "brand": 1, "_id": 0 }}
                        ]
    })
        
    headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': 'dQyCe7lvJL2Rtb1JMHPX6kbyZSybvfuzrZA4tOprAqu0I0lMGSitWA8lCh0np2xO'
        }
    response = requests.request("POST", url, headers=headers, data=payload)
    word = "brand"
    position = re.search(word, response.text)
    ini = position.end()+3
    string = response.text[ini:-4]
    return string

def testFeature(id):
    url = "https://data.mongodb-api.com/app/data-ftfni/endpoint/data/v1/action/aggregate"
    payload = json.dumps({
            "collection": "bikes",
            "database": "rental",
            "dataSource": "Cluster0",
            "pipeline" : [ { "$match": { "_id" :id}},
                { "$project": { "features": 1, "_id": 0 }}
                        ]
    })
        
    headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': 'dQyCe7lvJL2Rtb1JMHPX6kbyZSybvfuzrZA4tOprAqu0I0lMGSitWA8lCh0np2xO'
        }
    response = requests.request("POST", url, headers=headers, data=payload)
    word = "features"
    position = re.search(word, response.text)
    ini = position.end()+3
    string = response.text[ini:-4]
    return string

def testYear(id):
    url = "https://data.mongodb-api.com/app/data-ftfni/endpoint/data/v1/action/aggregate"
    payload = json.dumps({
            "collection": "bikes",
            "database": "rental",
            "dataSource": "Cluster0",
            "pipeline" : [ { "$match": { "_id" :id}},
                { "$project": { "year": 1, "_id": 0 }}
                        ]
    })
        
    headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': 'dQyCe7lvJL2Rtb1JMHPX6kbyZSybvfuzrZA4tOprAqu0I0lMGSitWA8lCh0np2xO'
        }
    response = requests.request("POST", url, headers=headers, data=payload)
    word = "year"
    position = re.search(word, response.text)
    ini = position.end()+2
    string = response.text[ini:-3]
    return string

def testSize(id):
    url = "https://data.mongodb-api.com/app/data-ftfni/endpoint/data/v1/action/aggregate"
    payload = json.dumps({
            "collection": "bikes",
            "database": "rental",
            "dataSource": "Cluster0",
            "pipeline" : [ { "$match": { "_id" :id}},
                { "$project": { "size": 1, "_id": 0 }}
                        ]
    })
        
    headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': 'dQyCe7lvJL2Rtb1JMHPX6kbyZSybvfuzrZA4tOprAqu0I0lMGSitWA8lCh0np2xO'
        }
    response = requests.request("POST", url, headers=headers, data=payload)
    word = "size"
    position = re.search(word, response.text)
    ini = position.end()+3
    string = response.text[ini:-4]
    return string

def testAva(id):
    url = "https://data.mongodb-api.com/app/data-ftfni/endpoint/data/v1/action/aggregate"
    payload = json.dumps({
            "collection": "bikes",
            "database": "rental",
            "dataSource": "Cluster0",
            "pipeline" : [ { "$match": { "_id" :id}},
                { "$project": { "availability": 1, "_id": 0 }}
                        ]
    })
        
    headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': 'dQyCe7lvJL2Rtb1JMHPX6kbyZSybvfuzrZA4tOprAqu0I0lMGSitWA8lCh0np2xO'
        }
    response = requests.request("POST", url, headers=headers, data=payload)
    word = "availability"
    position = re.search(word, response.text)
    ini = position.end()+2
    string = response.text[ini:-3]
    return string

def testPrice(id):
    url = "https://data.mongodb-api.com/app/data-ftfni/endpoint/data/v1/action/aggregate"
    payload = json.dumps({
            "collection": "bikes",
            "database": "rental",
            "dataSource": "Cluster0",
            "pipeline" : [ { "$match": { "_id" :id}},
                { "$project": { "Price_day":1, "_id": 0 }}
                        ]
    })
        
    headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': 'dQyCe7lvJL2Rtb1JMHPX6kbyZSybvfuzrZA4tOprAqu0I0lMGSitWA8lCh0np2xO'
        }
    response = requests.request("POST", url, headers=headers, data=payload)
    word = "Price_day"
    position = re.search(word, response.text)
    ini = position.end()+3
    price = response.text[ini:-8]
    return price


def testLatitude(id):
    url = "https://data.mongodb-api.com/app/data-ftfni/endpoint/data/v1/action/aggregate"
    payload = json.dumps({
            "collection": "bikes",
            "database": "rental",
            "dataSource": "Cluster0",
            "pipeline" : [ { "$match": { "_id" :id}},
                { "$project": { "location.latitude":1, "_id": 0 }}
                        ]
    })
        
    headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': 'dQyCe7lvJL2Rtb1JMHPX6kbyZSybvfuzrZA4tOprAqu0I0lMGSitWA8lCh0np2xO'
        }
    response = requests.request("POST", url, headers=headers, data=payload)
    word = "latitude"
    position = re.search(word, response.text)
    ini = position.end()+2
    latitude = response.text[ini:-4]
    return latitude

def testLength(id):
    url = "https://data.mongodb-api.com/app/data-ftfni/endpoint/data/v1/action/aggregate"
    payload = json.dumps({
            "collection": "bikes",
            "database": "rental",
            "dataSource": "Cluster0",
            "pipeline" : [ { "$match": { "_id" :id}},
                { "$project": { "location.length":1, "_id": 0 }}
                        ]
    })
        
    headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': 'dQyCe7lvJL2Rtb1JMHPX6kbyZSybvfuzrZA4tOprAqu0I0lMGSitWA8lCh0np2xO'
        }
    response = requests.request("POST", url, headers=headers, data=payload)
    word = "length"
    position = re.search(word, response.text)
    ini = position.end()+2
    latitude = response.text[ini:-4]
    return latitude
   
# Search for a documents by price
def test5(price):
    url = "https://data.mongodb-api.com/app/data-ftfni/endpoint/data/v1/action/find"
    payload = json.dumps({
            "collection": "bikes",
            "database": "rental",
            "dataSource": "Cluster0",
            "filter": {
            "Price_day": price
            }
        })
    headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': 'dQyCe7lvJL2Rtb1JMHPX6kbyZSybvfuzrZA4tOprAqu0I0lMGSitWA8lCh0np2xO'
        }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

while selection != "0":
    print("******** MENU *********")
    print("1.- Test")
    print("2.- All documents")
    print("3.- Grouped by features")
    print("4.- Find by id")
    print("5.- Find by price")
    print("6.- Try for group")
    print("7.- Insert a document")
    print("8.- Delete a document")
    print("9.- Update a document")

    print("0.- Finish")
    print("***********************")
    selection=input("Try a action: ")
    if selection == "1":
        test()
        time.sleep(3)
        print(" ")
    elif selection == "2":
        test2()
        time.sleep(3)
        print(" ")
    elif selection == "3":
        test3()
        time.sleep(3)
    elif selection == "4":
        identifier=int(input("Select an id: "))
        test4(identifier)
        time.sleep(4)
        print(" ")
    elif selection == "5":
        price=(int(input("Select price: ")))
        test5(price)
        time.sleep(5)
        print(" ")
    elif selection == "6":
        key=input("Choose an item to group: (model, brand, size, features)\n")
        test6(key)
        time.sleep(7)
        print(" ")

    elif selection == "7":
        id=int(input("Choose id: "))
        model=input("Choose model: ")
        brand=input("Choose brand: ")
        features=input("Choose feature: ")
        year=input("Choose year: ")
        size=input("Choose size: ")
        availability=bool(input("Choose availability (true or false): "))
        price=int(input("Choose price: "))
        type_currency=input("Choose type_currency(example €,$): ")
        latitude=float(input("Choose latitude: "))
        length=float(input("Choose length: "))
        test7(id, model, brand, features, year, size, availability, price, type_currency, latitude, length)
        time.sleep(1)
        print("Document created")
        print("----------------")
        test4(id)
        time.sleep(5)
        print(" ")
        
    
    elif selection == "8":
        identifier=int(input("Select an id to delete: "))
        print("The selected document")
        print("----------------------")
        test4(identifier)
        segurity = input("Do you really want to delete the document? Y or N: ")
        if segurity == "N" or segurity == "n":
            print("NO document has been deleted")
            time.sleep(3)
            print(" ")
            continue
        elif segurity == "Y" or segurity == "y":
            test8(identifier)
            print("Deleted document!!!")
            time.sleep(3)
            print(" ")

    elif selection == "9":
            id=int(input("Choose id: "))
            print("The document to update:")
            test4(id)
            model=input("Choose model: ")
            if model == "":
                model=testModel(id)
            brand=input("Choose brand: ")
            if brand == "":
                brand=testBrand(id)
            features=input("Choose feature: ")
            if features == "":
                features=testFeature(id)
            year=input("Choose year: ")
            if year == "":
                year=testYear(id)
            size=input("Choose size: ")
            if size == "":
                size =testSize(id)
            availability=bool(input("Choose availability (true or false): "))
            if availability=="":
                availability=testAva(id)
            price=input("Choose price: ")
            if price=="":
                price=testPrice(id)
            type_currency=input("Choose type_currency(example €,$): ")
            if type_currency=="":
                type_currency="€"
            latitude=input("Choose latitude: ")
            if latitude == "":
                latitude=testLatitude(id)
            length=input("Choose length: ")
            if length=="":
                length=testLength(id)
            test9(id, model, brand, features, year, size, availability, int(price), type_currency, float(latitude), float(length))
            time.sleep(1)
            print("Document updated")
            print("----------------")
            test4(id)
            time.sleep(6)
            print(" ")

        