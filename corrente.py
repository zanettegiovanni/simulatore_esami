class Corrente:
    def __init__(self, n):

        import numpy as np
        from stampante import Stampante

        for j in range(n):
            sett = []
            tipo = [1, 1, 1, 1]
            estr = []

            while len(sett) < 4:
                n = np.random.randint(1, 5)
                if n not in sett:
                    sett.append(n)

            estr.append(sett)
            estr.append(tipo)

            exe = []
            for i in range(0,4):
                if estr[0][i] == 1:
                    m = np.random.randint(1, 7)
                    exe.append(m)
                elif estr[0][i] == 2:
                    m = np.random.randint(1, 6)
                    exe.append(m)
                elif estr[0][i] == 3:
                    m = np.random.randint(1, 11)
                    exe.append(m)
                elif estr[0][i] == 4:
                    m = np.random.randint(1, 19)
                    exe.append(m)

            estr.append(exe)

            exam = []

            for i in range(0, 4):
                exam.append(str(5) + "." + str(estr[0][i]) + "." + str(estr[1][i]) + " - " + str(estr[2][i]))

            Stampante('corrente', exam, j, '5/D')