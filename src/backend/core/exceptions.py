"""
Excepciones personalizadas para el API.
"""


class BPAEException(Exception):
    """Excepción base para el proyecto"""

    pass


class APIError(BPAEException):
    """Error en llamada a API externa"""

    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class RepositoryError(BPAEException):
    """Error en acceso a base de datos"""

    pass


class ValidationError(BPAEException):
    """Error de validación de datos"""

    pass


class ExternalAPIError(BPAEException):
    """Error en API externa (MiniMax, Tavily)"""

    def __init__(self, service: str, message: str, original_error: Exception = None):
        self.service = service
        self.message = message
        self.original_error = original_error
        super().__init__(f"[{service}] {message}")
