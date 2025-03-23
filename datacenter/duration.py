from django.utils import timezone
from datetime import timedelta


def get_duration(visit):
    start_time = timezone.localtime(visit.entered_at)
    end_time = timezone.localtime(visit.leaved_at) if visit.leaved_at else timezone.localtime(timezone.now())
    duration = end_time - start_time
    return duration


def format_duration(duration):
    hours = duration.seconds // 3600
    minutes = (duration.seconds // 60) % 60
    return f"{hours} ч. {minutes} мин."
