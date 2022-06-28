from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Rob', email='rob@fakemail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Rob', email='rob@fakemail.com'),
        Usuario(nome='Zezinho', email='zezinho@gmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
