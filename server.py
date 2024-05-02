from proto_moduli.trougao_pb2_grpc import RacunanjeTrouglaServicer, add_RacunanjeTrouglaServicer_to_server
from proto_moduli.trougao_pb2 import Tacka, Trougao, ParametriTrougla
from grpc import server as grpc_server, Server
from concurrent.futures import ThreadPoolExecutor
from overrides import override

class ServiserZaRacunanje(RacunanjeTrouglaServicer):
    @override
    def IzracunajTrougao(self, request: Trougao, context) -> ParametriTrougla:
        print("Racuna se trougao: " + self.__ispisi_trougao(request))
        parametri_trougla: ParametriTrougla = ParametriTrougla()
        parametri_trougla.povrsina = self.__izracunaj_povrsinu(request)
        parametri_trougla.obim = self.__izracunaj_obim(request)
        return parametri_trougla

    @staticmethod
    def __ispisi_trougao(trougao: Trougao) -> str:
        return f"A({trougao.A.x},{trougao.A.y}), B({trougao.B.x},{trougao.B.y}), C({trougao.C.x},{trougao.C.y})"

    @staticmethod
    def __izracunaj_povrsinu(trougao: Trougao) -> float:
        (x1, y1) = (trougao.A.x, trougao.A.y)
        (x2, y2) = (trougao.B.x, trougao.B.y)
        (x3, y3) = (trougao.C.x, trougao.C.y)
        return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0

    @staticmethod
    def __izracunaj_obim(trougao: Trougao) -> float:
        (x1, y1) = (trougao.A.x, trougao.A.y)
        (x2, y2) = (trougao.B.x, trougao.B.y)
        (x3, y3) = (trougao.C.x, trougao.C.y)
        prva_strana: float = (x2 - x1) * (x2 - x1) - (y2 - y1) * (y2 - y1)
        druga_strana: float = (x3 - x1) * (x3 - x1) - (y3 - y1) * (y3 - y1)
        treca_strana: float = (x3 - x2) * (x3 - x2) - (y3 - y2) * (y3 - y2)
        print(f"Duzine stranica: {prva_strana}, {druga_strana}, {treca_strana}")
        return prva_strana + druga_strana + treca_strana


def startuj_server():
    server: Server = grpc_server(ThreadPoolExecutor(max_workers=3))
    add_RacunanjeTrouglaServicer_to_server(ServiserZaRacunanje(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    try:
        startuj_server()
        print("Server startovan")
    except Exception as e:
        print(f"Greska: {e}")
