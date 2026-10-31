from modulos.usuarios.dados import UsuariosDados

class UsuariosNegocio:
    @staticmethod
    def validar_usuario_ativo(user_id: int):
        usuario = UsuariosDados.buscar_por_id(user_id)
        if usuario and usuario.get("ativo"):
            return usuario
        return None
