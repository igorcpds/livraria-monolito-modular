from modulos.catalogo.aplicacao import CatalogoAplicacao
from modulos.pagamento.aplicacao import PagamentoAplicacao
from modulos.estoque.adapters import estoque_facade

def test_fluxo_monolito_modular_completo():
    estoque_inicial = estoque_facade.consultar_disponibilidade(1)
    livro = CatalogoAplicacao.buscar_item_disponivel(isbn="9780451524935")
    assert livro is not None

    recibo = PagamentoAplicacao.finalizar_pedido(user_id=1, itens_carrinho=[livro])
    assert recibo["total"] == 45.00
    assert estoque_facade.consultar_disponibilidade(1) == estoque_inicial - 1
