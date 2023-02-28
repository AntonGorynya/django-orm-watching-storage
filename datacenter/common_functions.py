from django.utils.timezone import localtime, now
from datetime import timedelta


def format_duration(duration):
    hours = duration.total_seconds()//3600
    minutes = duration.seconds//60 % 60
    return f'{hours}ч  {minutes}мин'


def get_duration(entered_at, leaved_at=None):
    if leaved_at:
        duration = leaved_at - entered_at
    else:
        duration = now() - localtime(entered_at)
    return duration


def is_visit_long(visit, minutes=60):
    entered_at = visit.entered_at
    leaved_at = visit.leaved_at
    time_limit = timedelta(minutes=minutes)
    duration = get_duration(entered_at, leaved_at)
    return duration > time_limit
