from django.utils.timezone import localtime
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.common_functions import get_duration, format_duration, is_visit_long


def storage_information_view(request):
    non_closed_visits = []
    for visit in Visit.objects.filter(leaved_at=None):
        entered_at = localtime(visit.entered_at)
        duration = get_duration(entered_at)
        non_closed_visits.append({
            'who_entered': visit.passcard,
            'entered_at': entered_at,
            'duration': format_duration(duration),
            'is_strange': is_visit_long(visit)
        })
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
