from modulos.pagamento.negocio import PagamentoNegocio
from modulos.pagamento.dados import PagamentoDados

class PagamentoAplicacao:
    @staticmethod
    def finalizar_pedido(user_id: int, itens_carrinho: list[dict]):
        return PagamentoNegocio.processar_compra_pix(user_id, itens_carrinho)

    @staticmethod
    def historico_pagamentos():
        return PagamentoDados.listar_transacoes()
