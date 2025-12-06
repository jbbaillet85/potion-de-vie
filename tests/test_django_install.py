import django


def test_django_installed():
    """
    Vérifie que Django est installé et sa version est récupérable.
    """
    version = django.get_version()
    assert version is not None
    print(f"Django version installed: {version}")
