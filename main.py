import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x180")
window.title("Simulatore esami")
window.resizable(False, False)
window.grid_columnconfigure(0, weight=1)

welcome_label = tk.Label(window,
                         text='Seleziona la tipologia di esame da creare:',
                         font=('Selawik', 8))
welcome_label.grid(row=0, column=0, sticky="N", padx=20, pady=10)

tipologia = tk.StringVar()
tipo_combobox = ttk.Combobox(window, textvariable=tipologia)
tipo_combobox['values'] = ["Esame completo su carta 5/D", "Esame completo su carta 42/D",
                           "Quattro esercizi tipologia \"carburante\"",
                           "Quattro esercizi tipologia \"corrente\"", "Quattro esercizi tipologia \"scarroccio\"",
                           "Quattro esercizi tipologia \"navigazione costiera\""]
tipo_combobox['state'] = 'readonly'
tipo_combobox.grid(row=1, column=0, sticky='WE', padx=10)

quantita_label = tk.Label(window,
                         text='Seleziona il numero di esami da creare:',
                         font=('Selawik', 8))
quantita_label.grid(row=2, column=0, sticky="N", padx=20, pady=10)

quantita = tk.IntVar()
quantita_combobox = ttk.Combobox(window, textvariable=quantita)
quantita_combobox['values'] = [i for i in range(1, 21)]
quantita_combobox['state'] = 'readonly'
quantita_combobox.grid(row=3, column=0, sticky='WE', padx=10)


def crea_esame():
    if tipologia.get() == "Esame completo su carta 5/D":
        from cinque_d import CinqueD
        CinqueD(quantita.get())
    elif tipologia.get() == "Esame completo su carta 42/D":
        from quarantadue_d import QuarantadueD
        QuarantadueD(quantita.get())
    elif tipologia.get() == "Quattro esercizi tipologia \"carburante\"":
        from carburante import Carburante
        Carburante(quantita.get())
    elif tipologia.get() == "Quattro esercizi tipologia \"corrente\"":
        from corrente import Corrente
        Corrente(quantita.get())
    elif tipologia.get() == "Quattro esercizi tipologia \"scarroccio\"":
        from scarroccio import Scarroccio
        Scarroccio(quantita.get())
    elif tipologia.get() == "Quattro esercizi tipologia \"navigazione costiera\"":
        from navigazione_costiera import NavigazioneCostiera
        NavigazioneCostiera(quantita.get())
    elif tipologia.get() == "Ho degli esercizi da stampare":
        from stampa_esami import StampaEsami
        StampaEsami(carta.get(), esercizi.get())


creator_button = tk.Button(text="Crea", command=crea_esame)
creator_button.grid(row=8, column=0, pady=20)

if __name__ == "__main__":
    window.mainloop()
'''

else:
    carta_label = tk.Label(window,
                             text='Seleziona la carta che vuoi utilizzare:',
                             font=('Selawik', 8))
    carta_label.grid(row=2, column=0, sticky="N", padx=20, pady=10)

    carta = tk.StringVar()
    carta_combobox = ttk.Combobox(window, textvariable=carta)
    carta_combobox['values'] = ['5/D', '42/D']
    carta_combobox['state'] = 'readonly'
    carta_combobox.grid(row=3, column=0, padx=10)

    esercizi_label = tk.Label(window,
                              text='Inserisci gli esercizi che vuoi selezionare nella forma #.#.# - # separati da ", ":',
                              font=('Selawik', 8))
    esercizi_label.grid(row=4, column=0, sticky="N", padx=20, pady=10)

    esercizi = tk.Entry(width=50)
    esercizi.grid(row=5, column=0, padx=10)

'''
