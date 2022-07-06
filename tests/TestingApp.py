from MyScheduleApp.Contact import Contact
from MyScheduleApp.Timeline import Timeline
from MyScheduleApp.MyDay import MyDay
from MyScheduleApp.subs.Hour import Hour


hour = Hour(22, 62)
newhour = hour.get_hour()
print(newhour)
