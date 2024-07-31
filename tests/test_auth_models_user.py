import pytest

# from django.contrib.auth.models import User


@pytest.mark.django_db()
def test_user_create(django_user_model):
    django_user_model.objects.create_user(username="pedroherub", password="1234")

    assert django_user_model.objects.count() == 1
    user = django_user_model.objects.first()
    assert user.username == "pedroherub"
    assert user.is_active is True
    assert user.is_staff is False
