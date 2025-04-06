from django.utils import timezone
from datetime import timedelta


SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = SECONDS_IN_MINUTE * 60
SECONDS_IN_DAY = SECONDS_IN_HOUR * 24


def get_duration(visit):
    start_time = timezone.localtime(visit.entered_at)
    end_time = timezone.localtime(visit.leaved_at) if visit.leaved_at else timezone.localtime(timezone.now())
    duration = end_time - start_time
    return duration


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    remaining_seconds = total_seconds % SECONDS_IN_DAY
    hours = remaining_seconds // SECONDS_IN_HOUR
    minutes = (remaining_seconds % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE
    return f"{hours} ч. {minutes} мин."
