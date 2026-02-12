distance = float(input("Enter the distance in miles "))
speedlimit = float(input("What is the speed limit in miles per hour? "))
speed = float(input("What is your average speed, in miles per hour? "))
time = distance/speedlimit
speedtime = distance/speed
hour = 60
speedtimein = speedtime*hour
timein = time*hour
if speed>speedlimit:
    savedtime = timein - speedtimein
else:
    print("No time saved")
print(f'Time at speed limit is {timein:.2f} minutes')
print(f'Time at average speed is {speedtimein:.2f} minutes')
print(f'Time saved would be {savedtime:.2f} minutes')
