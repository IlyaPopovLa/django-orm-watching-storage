from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from  datetime import timedelta



def format_duration(duration):
    hours, remainder = divmod(duration.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return f'{hours:02}:{minutes:02}'


def passcard_info_view(request, passcode):
    # Программируем здесь
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        duration = visit.leaved_at - visit.entered_at
        formatted_duration = format_duration(duration)
        is_strange = duration > timedelta(minutes=60)
        this_passcard_visits.append({
            'entered_at': visit.entered_at,
            'duration': formatted_duration,
            'is_strange': is_strange
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
