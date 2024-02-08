from typing import Dict # faz com que cada elemento seja em formato de dicionário

# As requisições HTTP serão colocadas nesta classe para deixar em um formato padrão na aplicação
class HttpRequest:
    def __init__(
            self,
            header: Dict = None,
            body: Dict = None,
            query_params: Dict = None
        ) -> None: # caso estes elementos não sejam especificados eles receberão None como valor
        self.header = header
        self.body = body
        self.query_params = query_params # salvando todos os elementos q entrarem no método construtor

# Padroniza o uso do HTTP, retirando dele tudo que precisa e colocando nos parametros de entrada
