from libpythonpro.spam.email_sender import Sender, EmailInvalido
import pytest

def test_create_email_sender():
    sender = Sender()
    assert sender is not None

@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br','jukinha@gmail.com']
)
def test_remetente(destinatario):
    sender = Sender()
    resultado = sender.send(
        destinatario,
        'zezinho@gmail.com',
        'Breja Artesanal',
        'Melhores IPAs da face da terra.'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'destinatario',
    ['','jukinha']
)
def test_remetente_invalido(destinatario):
    sender = Sender()
    with pytest.raises(EmailInvalido):
        sender.send(
        destinatario,
            'zezinho@gmail.com',
            'Breja Artesanal',
            'Melhores IPAs da face da terra.'
        )
