from app import run
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from time import monotonic, sleep, ctime
import os

sched = BlockingScheduler()
hour = int(os.environ.get("SEARCH_HOUR"))
minutes = int(os.environ.get("SEARCH_MINUTES"))

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=hour, minute = minutes)
def scheduled_job():
    print('This job: Search Traffic Fine is run every weekday at ', hour, ':', minutes)        
    car_plate = os.environ.get("CARPLATE_EXAMPLE")    
    type_vehicle = 'P'
    url_webpage = 'http://especiales.muniguate.com/remisiones.htm'
    run(url_webpage,type_vehicle,car_plate)
   
sched.start()