from tkinter import *

Calculadora = Tk()
Calculadora.title('Calculadora')
Calculadora.maxsize(width=335, height=415)
Calculadora.minsize(width=335, height=415)
Calculadora['bg'] = "#252729"
Calculadora.geometry('-600+200')
conta = ''

InputArea = Frame(Calculadora, bg='#252729')
InputArea.place(relx=0.08, rely=0.02, relwidth=0.80, relheight=0.13)

lb_input = Label(InputArea, text='0', font='Arial 20 bold')
lb_input['bg'] = '#252729'
lb_input['fg'] = 'white'
lb_input.place(relx=0.02, rely=0.02, relwidth=0.95, relheight=0.82)

BotoesArea = Frame(Calculadora, bg='#252729')
BotoesArea.place(relx=0.02, rely=0.16, relwidth=0.95, relheight=0.82)

# funcoes
def calculo(valores):
    global conta
    conta = (f'{conta}{valores}')
    lb_input = Label(InputArea, text=conta, font='Arial 20 bold')
    lb_input['bg'] = '#252729'
    lb_input['fg'] = 'white'
    lb_input.place(relx=0.02, rely=0.16, relwidth=0.95, relheight=0.82)

def resultado():
    global conta
    lb_input = Label(InputArea, text=(eval(conta)), font='Arial 20 bold')
    lb_input['bg'] = '#252729'
    lb_input['fg'] = 'white'
    lb_input.place(relx=0.02, rely=0.16, relwidth=0.95, relheight=0.82)
    conta = ''

def limpar():
    global conta
    lb_input = Label(InputArea, text='', font='Arial 20 bold')
    lb_input['bg'] = '#252729'
    lb_input['fg'] = 'white'
    lb_input.place(relx=0.02, rely=0.02, relwidth=0.95, relheight=0.95)
    conta = ''

#linha 1
BT_LIMPAR = Button(BotoesArea, text='C', font='Arial 20 bold', command=limpar)
BT_LIMPAR['bg'] = '#0e0f0f'
BT_LIMPAR['fg'] = 'white'
BT_LIMPAR.place(relx=0.07, rely=0.01, relwidth=0.2, relheight=0.15)

BT_DIVISAO = Button(BotoesArea, text='/', font='Arial 20 bold', command=lambda: calculo (valores = '/'))
BT_DIVISAO['bg'] = '#0e0f0f'
BT_DIVISAO['fg'] = 'white'
BT_DIVISAO.place(relx=0.29, rely=0.01, relwidth=0.2, relheight=0.15)

BT_MULT = Button(BotoesArea, text='X', font='Arial 20 bold', command=lambda: calculo (valores = '*'))
BT_MULT['bg'] = '#0e0f0f'
BT_MULT['fg'] = 'white'
BT_MULT.place(relx=0.50, rely=0.01, relwidth=0.2, relheight=0.15)

BT_PORC = Button(BotoesArea, text='%', font='Arial 20 bold', command=lambda: calculo (valores = '/100'))
BT_PORC['bg'] = '#0e0f0f'
BT_PORC['fg'] = 'white'
BT_PORC.place(relx=0.71, rely=0.01, relwidth=0.2, relheight=0.15)

#linha 2
BT_NUM_7 = Button(BotoesArea, text='7', font='Arial 20 bold', command=lambda: calculo (valores = '7'))
BT_NUM_7['bg'] = '#000000'
BT_NUM_7['fg'] = 'white'
BT_NUM_7.place(relx=0.07, rely=0.17, relwidth=0.2, relheight=0.15)

BT_NUM_8 = Button(BotoesArea, text='8', font='Arial 20 bold', command=lambda: calculo (valores = '8'))
BT_NUM_8['bg'] = '#000000'
BT_NUM_8['fg'] = 'white'
BT_NUM_8.place(relx=0.29, rely=0.17, relwidth=0.2, relheight=0.15)

BT_NUM_9 = Button(BotoesArea, text='9', font='Arial 20 bold', command=lambda: calculo (valores = '9'))
BT_NUM_9['bg'] = '#000000'
BT_NUM_9['fg'] = 'white'
BT_NUM_9.place(relx=0.50, rely=0.17, relwidth=0.2, relheight=0.15)

BT_SUB = Button(BotoesArea, text='-', font='Arial 20 bold', command=lambda: calculo (valores = '-'))
BT_SUB['bg'] = '#000000'
BT_SUB['fg'] = 'white'
BT_SUB.place(relx=0.71, rely=0.17, relwidth=0.2, relheight=0.15)

#linha 3
BT_NUM_4 = Button(BotoesArea, text='4', font='Arial 20 bold', command=lambda: calculo (valores = '4'))
BT_NUM_4['bg'] = '#000000'
BT_NUM_4['fg'] = 'white'
BT_NUM_4.place(relx=0.07, rely=0.33, relwidth=0.2, relheight=0.15)

BT_NUM_5 = Button(BotoesArea, text='5', font='Arial 20 bold', command=lambda: calculo (valores = '5'))
BT_NUM_5['bg'] = '#000000'
BT_NUM_5['fg'] = 'white'
BT_NUM_5.place(relx=0.29, rely=0.33, relwidth=0.2, relheight=0.15)

BT_NUM_6 = Button(BotoesArea, text='6', font='Arial 20 bold', command=lambda: calculo (valores = '6'))
BT_NUM_6['bg'] = '#000000'
BT_NUM_6['fg'] = 'white'
BT_NUM_6.place(relx=0.50, rely=0.33, relwidth=0.2, relheight=0.15)

BT_ADIC = Button(BotoesArea, text='+', font='Arial 20 bold', command=lambda: calculo (valores = '+'))
BT_ADIC['bg'] = '#000000'
BT_ADIC['fg'] = 'white'
BT_ADIC.place(relx=0.71, rely=0.33, relwidth=0.2, relheight=0.15)

#linha 4
BT_NUM_0 = Button(BotoesArea, text='0', font='Arial 20 bold', command=lambda: calculo (valores = '0'))
BT_NUM_0['bg'] = '#000000'
BT_NUM_0['fg'] = 'white'
BT_NUM_0.place(relx=0.07, rely=0.49, relwidth=0.2, relheight=0.15)

BT_NUM_1 = Button(BotoesArea, text='1', font='Arial 20 bold', command=lambda: calculo (valores = '1'))
BT_NUM_1['bg'] = '#000000'
BT_NUM_1['fg'] = 'white'
# BT_NUM_1.command=teste1
BT_NUM_1.place(relx=0.29, rely=0.49, relwidth=0.2, relheight=0.15)

BT_NUM_2 = Button(BotoesArea, text='2', font='Arial 20 bold', command=lambda: calculo (valores = '2'))
BT_NUM_2['bg'] = '#000000'
BT_NUM_2['fg'] = 'white'
BT_NUM_2.place(relx=0.50, rely=0.49, relwidth=0.2, relheight=0.15)

BT_NUM_3 = Button(BotoesArea, text='3', font='Arial 20 bold', command=lambda: calculo (valores = '3'))
BT_NUM_3['bg'] = '#000000'
BT_NUM_3['fg'] = 'white'
BT_NUM_3.place(relx=0.71, rely=0.49, relwidth=0.2, relheight=0.15)

#linha 5
BT_PONTO = Button(BotoesArea, text='.', font='Arial 20 bold', command=lambda: calculo (valores = '.'))
BT_PONTO['bg'] = '#000000'
BT_PONTO['fg'] = 'white'
BT_PONTO.place(relx=0.07, rely=0.65, relwidth=0.2, relheight=0.15)

#linha 6
BT_IGUAL = Button(BotoesArea, text='=', font='Arial 20 bold', command=resultado)
BT_IGUAL['bg'] = '#000000'
BT_IGUAL['fg'] = 'white'
BT_IGUAL.place(relx=0.07, rely=0.81, relwidth=0.85, relheight=0.15)


# BT_NUM_0['fg'] = '2d3436'
# self._BTN_NUM_0 = tk.Button(master, text=0, cnf=self.theme['BTN_NUMERICO'])

mainloop()
