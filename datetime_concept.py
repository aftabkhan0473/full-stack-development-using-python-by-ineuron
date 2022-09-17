#Note:- import module not work accurately if there exist a file which name is equal to that module name! It's ilterally very important
import datetime
today = datetime.datetime.now()
print(today)
osm_date = today.strftime("%d-%b-%Y %I:%M %p %A")
print(osm_date)
