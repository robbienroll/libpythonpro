from unittest.mock import Mock

import pytest as pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Rob', email='rob@fakemail.com'),
            Usuario(nome='Zezinho', email='zezinho@gmail.com')
        ],
        [
            Usuario(nome='Rob', email='rob@fakemail.com')
        ]
    ]
)
def test_qtde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'rob@emailfake.com',
        'Curso Python Pro',
        'Confira os modulos fantasticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Rob', email='rob@fakemail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'zezinho@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantasticos'
    )
    enviador.enviar.assert_called_once_with(
        'zezinho@gmail.com',
        'rob@fakemail.com',
        'Curso Python Pro',
        'Confira os modulos fantasticos'
    )

class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtde_emails_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtde_emails_enviados += 1
