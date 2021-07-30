from .decorators import Decorators


decs = Decorators()


class Validation:
    def __init__(self, url: str) -> None:
        self.url = url

        self.check_url(self.url)

    @staticmethod
    @decs.check_http
    def check_url(url: str) -> bool:
        assert url.endswith('freelance.habr.com/tasks'), 'parser supports only website freelance.habr.com'
