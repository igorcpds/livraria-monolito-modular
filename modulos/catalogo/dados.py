from bancos_de_dados import ITENS_DB

class CatalogoDados:
    @staticmethod
    def listar_todos():
        return ITENS_DB

    @staticmethod
    def buscar_por_id(livro_id: int):
        return next((l for l in ITENS_DB if l["id"] == int(livro_id)), None)

    @staticmethod
    def buscar_por_isbn(isbn: str):
        return next((l for l in ITENS_DB if l["isbn"] == isbn.strip()), None)
