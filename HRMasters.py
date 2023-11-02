class Funcionario():
    def __init__(self, idFuncionario, nome, cargo, informacoesContato, salario):
        self.idFuncionario = idFuncionario
        self.nome = nome
        self.cargo = cargo
        self.informacoesContato = informacoesContato
        self.salario = salario

    def obterDetalhes(self):
        print(f"\nID: {self.idFuncionario}\nNome: {self.nome}\nCargo: {self.cargo}\nContato: {self.informacoesContato}\nSalário: {self.salario}\n")

class HRMasters:
    def __init__(self):
        self.listaFuncionarios = []
        self.contador_id = 0

    def cadastrarFuncionario(self):
        print("-------------------- Cadastro Funcionario --------------------")
        while True:
            self.contador_id += 1
            print(f"\nID: {self.contador_id}")
            nome = input("Digite o nome do funcionário: ")
            print("A: R$2500\nB: R$5000\nC: R$6500")
            cargo = input("Digite o cargo do funcionário: ").upper()
            if cargo == "A":
                salario = 2500
            elif cargo == "B":
                salario = 5000
            elif cargo == "C":
                salario = 6500
            informacoesContato = int(input("Digite o número para contato: "))


            funcionario = Funcionario(self.contador_id, nome, cargo, informacoesContato, salario)
            self.listaFuncionarios.append(funcionario)

            opcao = input("\nDeseja cadastrar mais algum funcionário? (S/N)")
            if opcao.lower() != "s":
                break

    def listarFuncionarios(self):
        print("-------------------- Lista de Funcionários --------------------")
        for funcionario in self.listaFuncionarios:
            print(funcionario.obterDetalhes())

    def excluirFuncionarios(self):
        print("\n-------------------- Excluir Funcionario --------------------")
        while True:
            id_funcionario = int(input("Digite o ID do funcionário que deseja excluir: "))
            encontrado = False
            for funcionario in self.listaFuncionarios:
                if id_funcionario == funcionario.idFuncionario:
                    self.listaFuncionarios.remove(funcionario)
                    print("Usuário removido.")
                    encontrado = True
                    break
            if not encontrado:
                print("Esse funcionário não foi cadastrado.")

            opcao = input("Deseja excluir mais algum funcionário? (S/N)")
            if opcao.lower() != "s":
                break

    def modificarFuncionarios(self):
        print("\n-------------------- Modificar Funcionario --------------------")
        while True:
            id_funcionario = int(input("Digite o ID do funcionário que deseja modificar: "))
            encontrado = False
            for funcionario in self.listaFuncionarios:
                if id_funcionario == funcionario.idFuncionario:
                    print("Funcionário cadastrado.")
                    novoCargo = input("Digite o novo cargo: ").upper()
                    if novoCargo == "A":
                        funcionario.cargo = 'A'
                        funcionario.salario = 2500
                    elif novoCargo == "B":
                        funcionario.cargo = 'B'
                        funcionario.salario = 5000
                    elif novoCargo == "C":
                        funcionario.cargo = 'C'
                        funcionario.salario = 6500
                    encontrado = True
                    break
            if not encontrado:
                print("Funcionário não cadastrado.")
            select = input("Deseja modificar mais algum funcionário? (S/N)").lower()
            if select == "n":
                break


sistema_RH = HRMasters()
sistema_RH.cadastrarFuncionario()
sistema_RH.listarFuncionarios()
sistema_RH.modificarFuncionarios()
sistema_RH.excluirFuncionarios()
sistema_RH.listarFuncionarios()
