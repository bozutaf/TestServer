from proto_moduli.trougao_pb2 import Tacka, Trougao, ParametriTrougla
from proto_moduli.trougao_pb2_grpc import RacunanjeTrouglaStub
from grpc import insecure_channel, Channel

try:
    trougao: Trougao = Trougao()

    tacka_A: Tacka = Tacka()
    tacka_A.x = 2
    tacka_A.y = 3

    tacka_B: Tacka = Tacka()
    tacka_B.x = 5
    tacka_B.y = 4

    tacka_C: Tacka = Tacka()
    tacka_C.x = 7
    tacka_C.y = 2

    trougao.A.CopyFrom(tacka_A)
    trougao.B.CopyFrom(tacka_B)
    trougao.C.CopyFrom(tacka_C)

    kanal: Channel = insecure_channel('localhost:50051')
    stub: RacunanjeTrouglaStub = RacunanjeTrouglaStub(kanal)

    parametri: ParametriTrougla = stub.IzracunajTrougao(trougao)
    print(f"Povrsina: {parametri.povrsina}")
    print(f"Obim: {parametri.obim}")
except Exception as e:
    print(f"Greska: {e}")