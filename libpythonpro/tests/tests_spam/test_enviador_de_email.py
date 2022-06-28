from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido
import pytest


def test_create_email_sender():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'jukinha@gmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
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
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            destinatario,
            'zezinho@gmail.com',
            'Breja Artesanal',
            'Melhores IPAs da face da terra.'
        )
