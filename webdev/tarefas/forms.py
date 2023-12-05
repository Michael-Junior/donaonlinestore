from django.forms import ModelForm

from webdev.tarefas.models import Tarefa


class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome', 'feita']
