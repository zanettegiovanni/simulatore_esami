class StampaEsami:
    def __init__(self, exam, carta):
        from stampante import Stampante
        Stampante('prova_esame', exam, 99999, carta)

"""
        exam = []

        for j in range(4):
            exe = input("Inserire il progressivo nella forma #.#.# - #: ")
            exam.append(exe)
"""

