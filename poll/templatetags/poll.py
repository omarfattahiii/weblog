from django import template
from poll.models import Polls, PollsOption

register = template.Library()

@register.inclusion_tag("poll/partials/last_poll.html")
def last_poll():
    try:
        poll = Polls.objects.get(id=1)
        poll_option = PollsOption.objects.filter(poll=poll, is_published=True)

        return {'poll_option': poll_option, 'poll': poll}
    except Exception:
        print(Exception)
