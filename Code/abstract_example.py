from abc import ABCMeta, abstractmethod


class Singer(metaclass=ABCMeta):
    def sing(self, tune):
        return tune

    @classmethod
    def __subclasshook__(cls, C):
        # This is some good magic... but is not supported on mypy. Any class C
        # implementing sing would satisfy issubclass(C, Singer)
        if cls is Singer:
            if any("sing" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented


class GuitarPlayer(metaclass=ABCMeta):
    @abstractmethod
    def rock(self, tune):
        pass


class Rocker(Singer, GuitarPlayer):
    def sing(self, tune):
        return f"YEAH {tune}"

    def rock(self, tune):
        return f"🎸 {tune} 🎸"


def max_rock(rocker: Rocker, tune: str) -> str:
    return f"{rocker.rock(rocker.sing(tune))}"


def sing_it(singer: Singer, tune: str) -> str:
    return f"{singer.sing(tune)}"


class BadRocker(Singer):
    pass


class MagicSinger(object):
    def sing(self, tune):
        return f"Oww {tune}"


if True:
    gene_simmons = Rocker()
    max_rock(gene_simmons, "I was made for loving you")
else:
    justin_bieber = Singer()
    max_rock(justin_bieber, "Some crap")
    eric_clapton = MagicSinger()
    sing_it(eric_clapton, "Leyla")
