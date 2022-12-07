from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
# CRIANDO JANELA

janela = Tk()
janela.title('Calculadora de IMC')
janela.geometry('450x450')
janela.iconbitmap('Calculadora-IMC-1.ico')
janela.resizable(False,False)

# CORES

cor1='#FDF5F2' #off white
cor2='#02693D' #verde 

# FUNÇÃO CALCULAR

def resultado():
    peso = float(en_peso.get())
    altura = float(en_altura.get())
    
    imc = peso / altura**2
    resultado = imc
    
    if resultado <18.5:
        l_result_text['text']= 'O resultado do seu IMC é:'
        l_result_text2['text']= 'Magreza'
    elif resultado >=18.5 and resultado <=24.9:
         l_result_text['text']= 'O resultado do seu IMC é:'
         l_result_text2['text']= 'Peso Normal'
    elif resultado >=25 and resultado <=29.9:
         l_result_text['text']= 'O resultado do seu IMC é:'
         l_result_text2['text']= 'Sobrepeso'
    elif resultado >=30 and resultado <=34.9:
         l_result_text['text']= 'O resultado do seu IMC é:'
         l_result_text2['text']= 'Obesidade grau I'
    elif resultado >=35 and resultado <=40:
         l_result_text['text']= 'O resultado do seu IMC é:'
         l_result_text2['text']= 'Obesidade grau II'
    elif resultado >40:
        l_result_text['text']= 'O resultado do seu IMC é:'
        l_result_text2['text']= 'Obesidade grau III'
        
    l_result['text']="{:.{}f}".format(resultado,2)
    

# IMPORTANDO IMAGEM

img_fundo = PhotoImage(file='3.1.png')
l_fundo = Label(janela, image=img_fundo)
l_fundo.pack()

botao = PhotoImage(file='enter 2.png')
bt_enter = Button(janela, bd=0, image=botao, command=resultado)
bt_enter.place(width=100, height=40, x=173, y=395)

# ENTRADA DE INFORMAÇÕES 

en_peso = Entry(bd=1, font=("Arial",12), justify=LEFT, bg=cor1)
en_peso.place(width=96 ,height=34 ,x=104, y=31.5)

en_altura = Entry(bd=1, font=("Arial",12), justify=LEFT, bg=cor1)
en_altura.place(width=97, height=34, x=130, y=90)

# EXIBIÇÃO DO RESULTADO

l_result = Label(bd=0, text='---', font=("Arial Black",16), justify=RIGHT, bg=cor1)
l_result.place(width=130, height=95, x=242, y=200)

l_result_text = Label(bd=0, text='', font=('Arial',11), justify=RIGHT, bg=cor1)
l_result_text.place(width=175, height=35, x=220, y=275)

l_result_text2 = Label(bd=0, text='', font=('Arial',11), justify=RIGHT, bg=cor1)
l_result_text2.place(width=130, height=30, x=243, y=305)
        

janela.mainloop()