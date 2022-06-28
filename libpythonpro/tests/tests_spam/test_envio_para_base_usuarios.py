from libpythonpro.spam.email_sender import Sender
from libpythonpro.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Sender())
    enviador_de_spam.enviar_emails(
        'rob@emailfake.com',
        'Curso Python Pro',
        'Confira os modulos fantasticos'
    )