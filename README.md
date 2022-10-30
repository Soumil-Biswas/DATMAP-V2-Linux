Open the terminal in the '..\V2\Website' folder and enter the command 'python manage.py runserver'.

Use the provided Address in the form of x.x.x.x and open the URL in a browser to access the Website.

Open a FLYXXX.csv file from your system to plot its course on the map.

If the flight log you have is in the form of a FLYXXX.DAT file, use dedicated DJI file parsers like DROP (DRone Open source Parser) from the following link: https://github.com/unhcfreg/DROP. Follow the instructions given in the page and convert any FLYXXX.DAT file into it's corresponding .csv file. 

 If the map is emtpy, or some of the points are skipped. It is because the points have empty latitude and longitude values. The flight log system does not update geolocation values unless a significant change in values is recorded. Therefore, if a point is skipped over and/or the map is empty, it is because the Drone did not move too far from the last co-ordinate/ did not move at all.

You can save the Map as a "map.html" file by right-clicking on the map. 
