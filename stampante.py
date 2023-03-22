class Stampante:
    def __init__(self, type, exam, j, map):
        import os, sys
        import pandas as pd
        from datetime import date
        from docxtpl import DocxTemplate
        from docx2pdf import convert

        os.chdir(sys.path[0])

        df = pd.read_csv('eserciziario.csv', index_col=0)

        d = date.today().strftime("%d/%m/%Y")
        t = date.today().strftime("%d_%m_%Y")

        title = []
        body = []
        sol = []
        lvl = []

        if j == 99999:
            from datetime import datetime
            incr = str(datetime.now().strftime("%H_%M_%S"))
        else:
            incr = str(j + 1)

        for i in range(0, 4):
            title.append('(progressivo ' + exam[i] + ', carta: ' + df.loc[exam[i], "CARTA"] + ' sett. '
                         + df.loc[exam[i], "SETTORE"] + ', tipologia ' + df.loc[exam[i], "ARGOMENTO"] + ")")
            body.append(df.loc[exam[i], "TESTO"])
            sol.append(df.loc[exam[i], "RISPOSTA"])
            lvl.append(df.loc[exam[i], "DIFFICOLTA"])

        doc = DocxTemplate('esame_oltre_template.docx')

        context = {
            'incr': ' - ' + incr,
            'Lvl1': lvl[0],
            'Lvl2': lvl[1],
            'Lvl3': lvl[2],
            'Lvl4': lvl[3],
            'map': map,
            'date': str(d),
            'Title1': title[0],
            'Body1': body[0],
            'Sol1': sol[0],
            'Title2': title[1],
            'Body2': body[1],
            'Sol2': sol[1],
            'Title3': title[2],
            'Body3': body[2],
            'Sol3': sol[2],
            'Title4': title[3],
            'Body4': body[3],
            'Sol4': sol[3]
        }

        doc.render(context)

        os.chdir(os.getcwd() + '\\pdf')

        name = 'simulazione_' + type + '_' + t + '_' + incr

        doc.save(name + '.docx')

        convert(name + '.docx', name + '.pdf')

        os.remove(name + '.docx')