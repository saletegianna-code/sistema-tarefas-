import json

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    try:
        with open(ARQUIVO, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w") as file:
        json.dump(tarefas, file, indent=4)

def listar_tarefas(tarefas):
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.\n")
        return

    print("\nTarefas:")
    for i, tarefa in enumerate(tarefas):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{i+1}. {tarefa['titulo']} - {status}")
    print()

def adicionar_tarefa(tarefas):
    titulo = input("Digite o título da tarefa: ")
    tarefas.append({"titulo": titulo, "concluida": False})
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!\n")

def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    escolha = int(input("Digite o número da tarefa que deseja concluir: ")) - 1

    if 0 <= escolha < len(tarefas):
        tarefas[escolha]["concluida"] = True
        salvar_tarefas(tarefas)
        print("Tarefa concluída!\n")
    else:
        print("Tarefa inválida.\n")

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    escolha = int(input("Digite o número da tarefa que deseja remover: ")) - 1

    if 0 <= escolha < len(tarefas):
        tarefas.pop(escolha)
        salvar_tarefas(tarefas)
        print("Tarefa removida!\n")
    else:
        print("Tarefa inválida.\n")

def menu():
    tarefas = carregar_tarefas()

    while True:
        print("=== Sistema de Tarefas ===")
        print("1 - Listar tarefas")
        print("2 - Adicionar tarefa")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "0":
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu()
