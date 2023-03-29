if __name__ == '__main__':
    n = 10000
    with open('outBig.bin', 'wb') as file:
        for i in range(n):
            file.write(i.to_bytes(4, byteorder='big', signed=False))
    with open('outLittle.bin', 'wb') as file:
        for i in range(n):
            file.write(i.to_bytes(4, byteorder='little', signed=False))

# Pergunta 2.1 - A instrução i.to_bytes() retorna um array de bytes.
# No caso da byteorder='big', o bit mais significativo fica na posição inicial do array,
# já no caso byteorder='little', o bit que aparece na posição inicial do array é o bit menos significativo.

# Pergunta 2.2 - Este programa vai escrever em 2 ficheiros (outBig.bin e outLittle.bin) os valores em byte de i.
# Se o parâmetro recebido for byteorder='big', este irá escrever no ficheiro a começar pelo byte mais significativo,
# se o parâmetro for byteorder='little', este irá escrever no ficheiro a começar pelo byte menos significativo.

# Pergunta 2.3 -
# byteorder='big' - 00 00 04 00
# byteorder='little' - 00 04 00 00

