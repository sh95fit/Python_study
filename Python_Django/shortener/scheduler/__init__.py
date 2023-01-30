from shortener.scheduler.cron import *  # pip install apscheduler
from apscheduler.schedulers.background import BackgroundScheduler

# 1회성 실행이 필요!


def cron_jobs():
    # 파이썬 장고와 다른 쓰레드에서 사용
    sched = BackgroundScheduler()
    sched.add_job(visitor_collector, "interval", seconds=60)
    sched.add_job(telegram_command_handler, "interval", seconds=5)
    sched.add_job(db_job_handler, "interval", seconds=10)
    # sched.add_job(XXXX, "cron", hour=1, minute=1)
    sched.start()


# https://apscheduler.readthedocs.io/en/3.x/
