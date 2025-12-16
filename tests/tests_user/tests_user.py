import pytest
from django.contrib.auth import get_user_model
from django.test import Client

User = get_user_model()


@pytest.mark.django_db
def test_create_user() -> None:
    user = User.objects.create_user(
        username="user1", email="test@example.com", password="testpassword123"
    )
    assert user.username == "user1"
    assert user.email == "test@example.com"
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser


@pytest.mark.django_db
def test_create_superuser() -> None:
    admin_user = User.objects.create_superuser(
        username="admin1", email="admin@example.com", password="adminpassword123"
    )
    assert admin_user.username == "admin1"
    assert admin_user.email == "admin@example.com"
    assert admin_user.is_active
    assert admin_user.is_staff
    assert admin_user.is_superuser


@pytest.mark.django_db
def test_user_authentication(client: Client) -> None:
    User.objects.create_user(
        username="authuser1", email="authuser@example.com", password="mypassword123"
    )
    login_successful = client.login(
        email="authuser@example.com", password="mypassword123"
    )
    assert login_successful
