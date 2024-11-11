# DATMAP-VS-Linux

A web service to plot the course of DJI Phantom Series Drones on the map. Version for Mac and Linux.

# Prerequisites

To run this program in your system, the following software and libraries are required:

Software:
1. [Python version 3.12.2](https://www.python.org/downloads/)
2. A code editor. Providing [VSCode](https://code.visualstudio.com/download) as an example. VSCode requires `Python` Extension to read and edit Python files.

Python Libraries:

1. Django
2. Folium
3. Pandas

# Installing Libraries

1. After installing Python, open a terminal/powershell at the `..\Website` folder and enter the command `pipenv install django`. Wait for the installlation to finish.
2. Next, enter `pipenv install folium`. Wait for the installlation to finish.
3. Finally, enter `pipenv install pandas`. Wait for the installlation to finish.

If the procedure says `new version of ___ available`, you many ignore them.

# Opening the Application

1. Open the terminal in the `..\Website` folder and enter the command `python manage.py runserver`.

2. Use the provided Address in the form of `x.x.x.x` and open the URL in a browser to access the Website.

3. Open a `FLYXXX.csv` file from your system to plot its course on the map. Alternatively, use the provided `MapSample - Copy.csv` file as input instead.

4. If the flight log you have is in the form of a `FLYXXX.DAT` file, use dedicated DJI file parsers like DROP (DRone Open source Parser) from the following link: https://github.com/unhcfreg/DROP. Follow the instructions given in the page and convert any FLYXXX.DAT file into it's corresponding .csv file. 

5. If the map is emtpy, or some of the points are skipped. It is because the points have empty latitude and longitude values. The flight log system does not update geolocation values unless a significant change in values is recorded. Therefore, if a point is skipped over and/or the map is empty, it is because the Drone did not move too far from the last co-ordinate/ did not move at all.

6. You can save the Map as a `map.html` file by right-clicking on the map. 
