import os
from django.conf import settings
import folium
import pandas
import webbrowser
# open the terminal in the 'Website' folder and enter the command 'python manage.py runserver'.
# Open .csv File


def get_coordinates(uploaded_file):
    path_file = os.path.join(settings.BASE_DIR, "media/"+uploaded_file.name)
    print(path_file)
    file = pandas.read_csv(path_file)

    map_path = folium.Map(location=[39, -106], zoom_start=5, max_zoom=200)

    n = 0

    for index, file in file.iterrows():
        if str(file['latitude']) == "nan" or str(file['longitude']) == "nan":
            n = n + 1
            print("Point {} skipped. Empty Point.".format(n))
        else:
            latitude = (file['latitude'])
            longitude = (file['longitude'])
            n = n + 1
            folium.Marker(location=[latitude, longitude],
                          popup=("Travel Point No.{}".format(n)), icon=folium.Icon(color='red')).add_to(map_path)
            print("Point {} added.".format(n))

    map_path.save("map.html")
    print("Map has been created.")
    webbrowser.open("map.html")
