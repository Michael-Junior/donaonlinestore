import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains


@pytest.fixture
def response(client):
    return client.get(reverse('tarefas:home'))


def test_status_code(response):
    assert response.status_code == 200


def test_form_present(response):
    assertContains(response, '<form')


def test_form_present_button(response):
    assertContains(response, '<button type="submit"')
