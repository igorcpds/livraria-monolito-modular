from datetime import datetime
from modulos.pagamento.dados import PagamentoDados
from modulos.usuarios.aplicacao import UsuariosAplicacao
from modulos.estoque.adapters import estoque_facade

class PagamentoNegocio:
    @staticmethod
    def processar_compra_pix(user_id: int, itens_carrinho: list[dict]):
        if not itens_carrinho:
            raise ValueError("O carrinho está vazio.")

        # 1. Comunicação lateral Pagamento <-> Usuários
        cliente = UsuariosAplicacao.verificar_cliente(user_id)
        if not cliente:
            raise ValueError("Utilizador inválido ou inativo.")

        # 2. Comunicação lateral Pagamento <-> Estoque (Clean)
        for item in itens_carrinho:
            sucesso = estoque_facade.baixar_estoque(item["id"], 1)
            if not sucesso:
                raise ValueError(f"Sem estoque para o livro '{item['titulo']}'.")

        # 3. Gravação em Pagamento-DB
        total = sum(i["preco"] for i in itens_carrinho)
        recibo = {
            "id_transacao": len(PagamentoDados.listar_transacoes()) + 1,
            "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "cliente": cliente["nome"],
            "cpf": cliente["cpf"],
            "itens": ", ".join(i["titulo"] for i in itens_carrinho),
            "total": total,
            "qr_code": f"QR-MONOLITO-MODULAR-{int(datetime.now().timestamp())}"
        }
        return PagamentoDados.registar_transacao(recibo)
