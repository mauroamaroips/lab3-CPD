import time

inicio = time.time()
for k in range(10):
    fileName = "fich"+str(k+1)+".dat"
    with open(fileName, 'wb') as file:
        for i in range((k+1)*1000000):
            file.write(i.to_bytes(4, byteorder='big', signed=False))
print(f"Tempo escrita = {time.time()-inicio}")

# Pergunta 3.1 - Este algoritmo cria múltiplos ficheiros onde a numeração difere em k+1 (eg. fich1, fich2, etc;
# Os valores escritos nos ficheiros são inicializados no byte mais significativo (to_bytes='bit') os números presentes
# em cada ficheiro vão aumentando (eg. fich1 -> 1 milhão de números, fich 2 -> 2 milhões de números).
# Isto faz com que os bytes vão aumentado em n * 4 (eg. 1000000 * 4 = 4000000 bytes, 2000000 * 4 = 8000000).

