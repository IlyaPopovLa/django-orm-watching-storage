from django.shortcuts import render
from datacenter.models import Visit
from datacenter.duration import get_duration, format_duration
from datetime import datetime, timedelta


def storage_information_view(request):
    non_leaved_visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visit in non_leaved_visits:
        duration = get_duration(visit)
        formatted_duration = format_duration(duration)
        entered_at_utc = visit.entered_at
        entered_at_local = entered_at_utc + timedelta(hours=3)

        entered_at_formatted = entered_at_local.strftime('%d-%m-%Y %H:%M')

        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': entered_at_formatted,
            'duration': formatted_duration,
        })

    context = {
        'non_closed_visits': non_closed_visits
    }

    return render(request, 'storage_information.html', context)