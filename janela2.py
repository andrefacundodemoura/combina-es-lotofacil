from tkinter import *
from itertools import combinations

janela=Tk()
janela.title('COMBINAÇÔES')
janela.configure(background='gray')

lb1=Label(janela,text='Digite as dezenas que você procura ex:(01,02.03..)')
lb1.place(x=60, y=325)

def bt_click():
    dez1=ent1.get()
    dez2=ent2.get()
    dez3=ent3.get()
    dez4=ent4.get()
    dez5=ent5.get()
    dez6=ent6.get()
    dez7=ent7.get()
    dez8=ent8.get()
    dez9=ent9.get()
    dez10=ent10.get()
    cont=0

    n=('01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25')

    for subset in combinations(n,15):
        a=' '.join(subset)
        a1=a+'\n'
        if dez1 in a1:
            if dez2 in a1:
                if dez3 in a1:
                    if dez4 in a1:
                        if dez5 in a1:
                            if dez6 in a1:
                                if dez7 in a1:
                                    if dez8 in a1:
                                        if dez9 in a1:
                                            if dez10 in a1:
                                                cont=cont+1
                                                result.insert(INSERT,a1)
                                                lb1['text']='Foram encontradas {} combinações!'.format(cont)

#entradas

ent1=Entry(janela)
ent1.place(x=60, y=350)

ent2=Entry(janela)
ent2.place(x=60, y=380)

ent3=Entry(janela)
ent3.place(x=60, y=410)

ent4=Entry(janela)
ent4.place(x=60, y=440)

ent5=Entry(janela)
ent5.place(x=60, y=470)

ent6=Entry(janela)
ent6.place(x=200, y=350)

ent7=Entry(janela)
ent7.place(x=200, y=380)

ent8=Entry(janela)
ent8.place(x=200, y=410)

ent9=Entry(janela)
ent9.place(x=200, y=440)

ent10=Entry(janela)
ent10.place(x=200, y=470)

#BOTÂO

bt=Button(janela,text='PROCURAR COMBINAÇÕES',command=bt_click)
bt.place(x=105,y=500)

#RESULTADO

result = Text(janela, height = 20, width = 200)
result.insert(INSERT, '                   resultado: \n')
result.pack()
#credito

cred=Label(janela, text='by Andre Facundo de moura')
cred.place(x=220,y=620)

janela.geometry('400x650')
janela.mainloop()
