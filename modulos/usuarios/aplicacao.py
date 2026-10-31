from modulos.usuarios.dados import UsuariosDados
from modulos.usuarios.negocio import UsuariosNegocio

class UsuariosAplicacao:
    @staticmethod
    def listar_todos():
        return UsuariosDados.listar_usuarios()

    @staticmethod
    def verificar_cliente(user_id: int):
        return UsuariosNegocio.validar_usuario_ativo(user_id)
