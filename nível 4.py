import shutil
import time
import threading

if __name__ == '__main__':
    # Versão sequencial
    print("Cópia sequencial de ficheiros")
    inicio = time.time()
    for k in range(10):
        fileName1 = "fich" + str(k + 1) + ".dat"
        fileName2 = "outFich" + str(k + 1) + ".dat"
        shutil.copy(fileName1, fileName2)
    print(f"\tTempo utilizado na cópia sequencial de ficheiros = {time.time()-inicio}")


    # Versão com threads
    print("Cópia multi-threading de ficheiros")
    inicio = time.time()
    threads = []
    for k in range(10):
        fileName1 = "fich" + str(k + 1) + ".dat"
        fileName2 = "outFich" + str(k + 1) + ".dat"
        t = threading.Thread(target=shutil.copy, args=[fileName1, fileName2])
        threads.append(t)
        t.start()
    for i in range(10):
        threads[i].join()
    print(f"\tTempo utilizado na cópia multi-threading de ficheiros = {time.time() - inicio}")


# Pergunta 4.1 - Numa primeira fase, este algoritmo é apresentado na sua versão sequencial, onde é efetuada uma
# cópia sequencial de 10 arquivos, sendo que para cada arquivo de origem "fichX.dat"
# é criado um arquivo de destino "outFichX.dat". Em seguida é escrito o tempo total de execução.
#
# Já numa segunda fase, é executada a versão multi-thread, onde são criadas 10 threads.
# Para cada thread criada, é atribuída a tarefa de copiar o ficheiro de origem "fichX.dat" para o ficheiro de
# destino outFichX.dat. Após a criação das threads, o programa aguarda a conclusão de todas as threads usando o método "join()".
# Por fim é escrito o tempo total da execução.


# Pergunta 4.2 - Enquanto a versão sequencial é executada de forma cada ficheiro seja copiado apenas depois
# do anterior ser copiado, na versão multi-thread as threads executam a cópia dos ficheiros em paralelo (uma thread para cada ficheiro),
# e aguarda a conclusão de todas as threads utilizando o método join(). Nesta versão podemos ver ganhos de performance pois
# embora haja uma adição de overhead extra ao programa, pois há um custo adicional associado à criação, execução e gestão das threads,
# este é compensado no processamento de ficheiros grandes em relação ao processamento sequencial.

# Pergunta 5 -
# Execução de programas em CPU-Bound - Neste caso, o uso de uma única thread pode ser benéfica pois não é necessário gerir
# múltiplas threads, o que pode fazer com que o tempo de execução aumente. Embora isso possa acontecer, quanto maior for a quantidade
# de dados/ ficheiros a serrem processados, maior será o tempo de execução, por isso é altamente provável que tempos de execução em processamento multi-thread
# seja menor para muitos dados/ficheiros, mesmo que seja necessário gerir o ciclo de vida das threads.

# Em programas de I/O bound, o processamento multi-thread leva a ganhos bastante relevantes de tempo de execução pois
# o programa pode continuar a processar outros dados enquanto espera pela conclusão de operações I/O, algo que não é possível
# no processamento com uma única thread.
