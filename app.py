from flask import Flask, render_template, request, redirect, url_for, flash
from modulos.catalogo.aplicacao import CatalogoAplicacao
from modulos.usuarios.aplicacao import UsuariosAplicacao
from modulos.pagamento.aplicacao import PagamentoAplicacao

app = Flask(__name__)
app.secret_key = "chave_monolito_modular_livraria"

# Regista as rotas REST do módulo de Catálogo
app.register_blueprint(CatalogoAplicacao.blueprint)

# Estado da sessão do módulo de Carrinho
CARRINHO_ATUAL = []
ULTIMO_RECIBO = None

@app.route("/", methods=["GET"])
def gateway_home():
    termo = request.args.get("q", "")
    livros = CatalogoAplicacao.obter_livros(termo)
    usuarios = UsuariosAplicacao.listar_todos()
    pagamentos = PagamentoAplicacao.historico_pagamentos()
    subtotal = sum(i["preco"] for i in CARRINHO_ATUAL)

    return render_template(
        "index.html",
        livros=livros,
        usuarios=usuarios,
        carrinho=CARRINHO_ATUAL,
        subtotal=subtotal,
        ultimo_recibo=ULTIMO_RECIBO,
        pagamentos=pagamentos,
        termo_atual=termo
    )

@app.route("/gateway/carrinho/adicionar/<int:livro_id>", methods=["POST"])
def gateway_adicionar_id(livro_id):
    livro = CatalogoAplicacao.buscar_item_disponivel(livro_id=livro_id)
    if livro:
        CARRINHO_ATUAL.append(livro)
        flash(f"'{livro['titulo']}' adicionado ao módulo Carrinho!", "sucesso")
    else:
        flash("Livro indisponível no Estoque.", "erro")
    return redirect(url_for("gateway_home"))

@app.route("/gateway/carrinho/scan", methods=["POST"])
def gateway_scan_isbn():
    isbn = request.form.get("isbn", "")
    livro = CatalogoAplicacao.buscar_item_disponivel(isbn=isbn)
    if livro:
        CARRINHO_ATUAL.append(livro)
        flash(f"Scan & Go: '{livro['titulo']}' adicionado ao Carrinho!", "sucesso")
    else:
        flash(f"ISBN '{isbn}' não encontrado ou sem estoque.", "erro")
    return redirect(url_for("gateway_home"))

@app.route("/gateway/carrinho/remover/<int:indice>", methods=["POST"])
def gateway_remover(indice):
    if 0 <= indice < len(CARRINHO_ATUAL):
        CARRINHO_ATUAL.pop(indice)
    return redirect(url_for("gateway_home"))

@app.route("/gateway/compra/finalizar", methods=["POST"])
def gateway_comprar():
    global ULTIMO_RECIBO
    user_id = int(request.form.get("user_id", 1))
    try:
        ULTIMO_RECIBO = PagamentoAplicacao.finalizar_pedido(user_id, CARRINHO_ATUAL)
        CARRINHO_ATUAL.clear()
        flash("Compra processada entre Usuários, Pagamento e Estoque com sucesso!", "sucesso")
    except ValueError as e:
        flash(str(e), "erro")
    return redirect(url_for("gateway_home"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
