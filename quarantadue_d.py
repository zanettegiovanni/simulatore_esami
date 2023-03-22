class QuarantadueD:
    def __init__(self, n):

        import numpy as np
        from stampante import Stampante

        for j in range(n):
            tipo = []
            sett = [5, 6, 7, 8]
            estr = []

            while len(tipo) < 3:
                n = np.random.randint(1, 5)
                if n not in tipo and n != 2:
                    tipo.append(n)

            while len(tipo) <4:
                p = np.random.randint(1, 5)
                if p != 2:
                    tipo.append(p)

            estr.append(sett)
            estr.append(tipo)

            exe = []

            if estr[1][0] == 1:
                m = np.random.randint(1, 4)
                exe.append(m)
            elif estr[1][0] == 3:
                m = np.random.randint(1, 3)
                exe.append(m)
            elif estr[1][0] == 4:
                m = np.random.randint(1, 2)
                exe.append(m)

            if estr[1][1] == 1:
                m = np.random.randint(1, 3)
                exe.append(m)
            elif estr[1][1] == 3:
                m = np.random.randint(1, 4)
                exe.append(m)
            elif estr[1][1] == 4:
                m = np.random.randint(1, 2)
                exe.append(m)

            if estr[1][2] == 1:
                m = np.random.randint(1, 3)
                exe.append(m)
            elif estr[1][2] == 3:
                m = np.random.randint(1, 3)
                exe.append(m)
            elif estr[1][2] == 4:
                m = np.random.randint(1, 2)
                exe.append(m)

            if estr[1][3] == 1:
                m = np.random.randint(1, 7)
                exe.append(m)
            elif estr[1][3] == 3:
                m = np.random.randint(1, 4)
                exe.append(m)
            elif estr[1][3] == 4:
                m = np.random.randint(1, 2)
                exe.append(m)

            estr.append(exe)

            exam = []

            for i in range(0, 4):
                exam.append(str(5) + "." + str(estr[0][i]) + "." + str(estr[1][i]) + " - " + str(estr[2][i]))

            Stampante('42_D', exam, j, '42/D')