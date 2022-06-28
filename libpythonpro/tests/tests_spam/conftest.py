import pytest
# todas estas fixtures de conftest ficarao disponiveis para os modulos de test_spam
from libpythonpro.spam.db import Conexao

# usado este escopo para a fixture ser usada apenas uma vez, mesmo que varios modulos a usem
@pytest.fixture(scope='session')
def conexao():
    # setup
    conexao_obj = Conexao()
    yield conexao_obj
    # tear down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield  sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()
