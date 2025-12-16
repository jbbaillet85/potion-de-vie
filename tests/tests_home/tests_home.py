import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_home_view_status_code(client: Client) -> None:
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_home_view_template_used(client: Client) -> None:
    url = reverse("home")
    response = client.get(url)
    templates = [t.name for t in response.templates]
    assert "home/home.html" in templates


@pytest.mark.django_db
def test_home_view_contains_text(client: Client) -> None:
    url = reverse("home")
    response = client.get(url)
    assert "Ma potion de vie" in response.content.decode()
