from bancos_de_dados import USER_DB

class UsuariosDados:
    @staticmethod
    def listar_usuarios():
        return USER_DB

    @staticmethod
    def buscar_por_id(user_id: int):
        return next((u for u in USER_DB if u["id"] == int(user_id)), None)
