# Primeiro, perguntamos qual tabuada o usuário quer: a de 1, de 2, de 3 ou qualquer outra, e armazenamos na variável 'tabuada'.
# Em seguida, usamos uma variável count que vai de 1 até 10 dentro do laço FOR e função range, veja:

tabuada = int(input("Tabuada do número: "))

for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)))
