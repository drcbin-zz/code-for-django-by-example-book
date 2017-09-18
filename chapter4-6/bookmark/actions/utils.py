from django.contrib.contenttypes.models import ContentType
import datetime
from django.utils import timezone
from .models import Action


def create_action(user, verb, target=None):
    # check fir aby similar action made in the last minute
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)

    # find all actions in the pase one minute with same verb an user
    similar_actions = Action.objects.filter(user_id=user.id, verb=verb, timestamp__gte=last_minute)

    # if the similar actions is refer to any target, we check if them is same
    if target:
        target_type = ContentType.objects.get_for_model(target)
        similar_actions = similar_actions.filter(target_type=target_type, target_id=target.id)

    if not similar_actions:
        # no exist similar actions
        action = Action(user=user, verb=verb, target=target)
        action.save()
        return True
    return False
