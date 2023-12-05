import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains

from webdev.tarefas.models import Tarefa


@pytest.fixture
def response(client, db):
    return client.get(reverse('tarefas:home'))


def test_status_code(response):
    assert response.status_code == 200


def test_form_present(response):
    assertContains(response, '<form')


def test_form_present_button(response):
    assertContains(response, '<button type="submit"')


@pytest.fixture
def lista_de_tarefas_pendentes(db):
    tarefas = [
        Tarefa(nome='Tarefa 1', feita=False),
        Tarefa(nome='Tarefa 2', feita=False),
    ]
    Tarefa.objects.bulk_create(tarefas)
    return tarefas

@pytest.fixture
def lista_de_tarefas_feitas(db):
    tarefas = [
        Tarefa(nome='Tarefa 3', feita=True),
        Tarefa(nome='Tarefa 4', feita=True),
    ]
    Tarefa.objects.bulk_create(tarefas)
    return tarefas

@pytest.fixture
def resposta_com_lista_de_tarefas(client, lista_de_tarefas_pendentes, lista_de_tarefas_feitas):
    return client.get(reverse('tarefas:home'))


def test_lista_de_tarefas_pendentes_presentes(resposta_com_lista_de_tarefas, lista_de_tarefas_pendentes):
    print(resposta_com_lista_de_tarefas.content.decode())
    for tarefa in lista_de_tarefas_pendentes:
        assertContains(resposta_com_lista_de_tarefas, tarefa.nome)

def test_lista_de_tarefas_feitas_presentes(resposta_com_lista_de_tarefas, lista_de_tarefas_feitas):
    print(resposta_com_lista_de_tarefas.content.decode())
    for tarefa in lista_de_tarefas_feitas:
        assertContains(resposta_com_lista_de_tarefas, tarefa.nome)
