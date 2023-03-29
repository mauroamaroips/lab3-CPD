import threading
import time


def conecta():  # simula uma ligação remota a um servidor
    print("\tligado")
    time.sleep(2)
    print("\tdesligado")


if __name__ == '__main__':
    numero_de_ligacoes = 20
    inicio = time.time()

    # Processamento
    print("Início do processamento sequencial")
    for i in range(numero_de_ligacoes):
        print(f'{i+1}ª ligação')
        conecta()
    fim = time.time()
    print(f'Tempo gasto para realizar {numero_de_ligacoes}ª ligações sequenciais: {fim-inicio}s')

    # Processamento multi-thread
    print("Início do processamento multi-threading")
    # multi-threaded
    threads = []
    inicio = time.time()
    for i in range(numero_de_ligacoes):
        t = threading.Thread(target=conecta)
        threads.append(t)
        t.start()
    for i in range(numero_de_ligacoes):
        threads[i].join()
    fim = time.time()
    print(f'Tempo gasto para realizar {numero_de_ligacoes} ligações multi-threading: {fim - inicio}s')

    # Pergunta 1.1 - O processamento sequencial apresentado neste algoritmo simula a ligação sequencial a um servidor.
    # A 2º ligação só é executada depois da 1º ligação ser desligada (a espera ocorre com o time.sleep(2));
    # No processamento multi-threading, as threads são criadas, adicionadas a uma queue e inicializadas.
    # As threads enviam todas o sinal de inicialização quase ao mesmo tempo, são esperados
    # 2 segundos e por fim todas as threads executam o respetivo join().
    # A instrução time.sleep(2) é executada apenas uma vez.

    # Pergunta 1.2 - Mudando o número de ligações para 20, é possível visualizar que o processo sequencial
    # demorará muito mais tempo, visto que cada ligação terá que inicializar, esperar 2 segundos e só depois
    # é inicializada a próxima ligação.
    # No caso do processamento multi-threading, acontece exatamente o descrito na pergunta 1.1, embora haja
    # um pequeno incremento no tempo de execução, devido ao join() das threads.