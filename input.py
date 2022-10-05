import pandas as pd
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
# Get Input
df = pd.read_csv ('world_cities_modified.csv')
cities = pd.DataFrame(columns = ["index","city","city_ascii","lat","lng","country","iso2","iso3","admin_name","capital","population","id","gmtOffset"])
n_people = []

print("Enter two zeros (0 0) to end")

while True:
    inp = input("Enter the name of the city: ")
    if inp == "0 0":
        break
    rslt_df = df[df["city_ascii"] == inp]
    id = 1
    if rslt_df.shape[0] > 1:
        for index, row in rslt_df.iterrows():
            print(f"{id}: Did you mean {row['city_ascii']}, {row['admin_name']}, {row['country']}")
            id += 1
        id = int(input("Enter the ID associated with the city: "))

    n_people.append(int(input("Enter the number of people from that city: ")))
    cities.loc[len(cities)] = rslt_df.iloc[id-1]

cities["n_people"] = n_people 


print(cities)