#exercicio01

Bmaior= int(input("base maior:"))
Bmenor= int(input("base menor:"))
h= int(input("altura do tronco da pirâmide:"))
volume =h/3*(Bmaior**2 + Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5)
print("volume=", volume)