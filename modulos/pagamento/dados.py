from bancos_de_dados import PAGAMENTO_DB

class PagamentoDados:
    @staticmethod
    def registar_transacao(transacao: dict):
        PAGAMENTO_DB.append(transacao)
        return transacao

    @staticmethod
    def listar_transacoes():
        return PAGAMENTO_DB
