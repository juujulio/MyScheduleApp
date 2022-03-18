##creating a file

myFile = open(f"Z:\pycharm\MyScheduleApp\database\myEvents.txt", "r+")
event = "dia 4-14:43-reunião de pais \n"
divisor = '-'


myFile.write(event)
listFile = list(myFile)
element = listFile[0].split("-")
print(element[2])

myFile.close()