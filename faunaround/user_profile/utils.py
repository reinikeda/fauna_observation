from django.contrib.auth import get_user_model
from . models import Profile


def create_missing_profiles():
    users_without_profile = get_user_model().objects.filter(profile__isnull=True)
    if users_without_profile.count() > 0:
        for user in users_without_profile:
            Profile.objects.create(user=user)
            print(f"{user} profile created")