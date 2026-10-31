from flask import Blueprint, jsonify, request
from modulos.catalogo.negocio import CatalogoNegocio

catalogo_rotas_bp = Blueprint("catalogo_rotas", __name__)

@catalogo_rotas_bp.route("/api/catalogo", methods=["GET"])
def api_listar():
    termo = request.args.get("q", "")
    return jsonify(CatalogoNegocio.listar_catalogo_com_estoque(termo)), 200
