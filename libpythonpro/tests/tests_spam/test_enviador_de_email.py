from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido
import pytest


def test_create_email_sender():
    sender = Enviador()
    assert sender is not None


@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'jukinha@gmail.com']
)
def test_remetente(destinatario):
    sender = Enviador()
    resultado = sender.send(
        destinatario,
        'zezinho@gmail.com',
        'Breja Artesanal',
        'Melhores IPAs da face da terra.'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'destinatario',
    ['', 'jukinha']
)
def test_remetente_invalido(destinatario):
    sender = Enviador()
    with pytest.raises(EmailInvalido):
        sender.send(
            destinatario,
            'zezinho@gmail.com',
            'Breja Artesanal',
            'Melhores IPAs da face da terra.'
        )
