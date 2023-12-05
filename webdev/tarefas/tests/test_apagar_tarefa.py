

import pytest
from django.urls import reverse

from webdev.tarefas.models import Tarefa


@pytest.fixture
def tarefa(db):
    return Tarefa.objects.create(nome='Tarefa 1', feita=True)


@pytest.fixture
def resposta(client, tarefa):
    return client.post(reverse('tarefas:apagar', kwargs={'tarefa_id': tarefa.id}))

def test_apagar_tarefa(resposta):
    assert not Tarefa.objects.exists()