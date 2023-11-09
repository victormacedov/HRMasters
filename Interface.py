import tkinter as tk
from tkinter import simpledialog, messagebox


class Funcionario:
    def __init__(self, idFuncionario, nome, cargo, informacoesContato, salario):
        self.idFuncionario = idFuncionario
        self.nome = nome
        self.cargo = cargo
        self.informacoesContato = informacoesContato
        self.salario = salario

    def obterDetalhes(self):
        return f"\nID: {self.idFuncionario}\nNome: {self.nome}\nCargo: {self.cargo}\nContato: {self.informacoesContato}\nSalário: {self.salario}\n"


class HRMasters:
    def __init__(self):
        self.listaFuncionarios = []
        self.contador_id = 0

    def cadastrarFuncionario(self):
        while True:
            self.contador_id += 1
            print(f"\nID: {self.contador_id}")
            nome = simpledialog.askstring("Cadastro de Funcionário", "Digite o nome do funcionário:")
            while True:
                cargo = simpledialog.askstring("Cadastro de Funcionário", "Digite o cargo do funcionário (A, B, C):").upper()
                if cargo in ["A", "B", "C"]:
                    break
                else:
                    messagebox.showinfo("Cargo inválido", "O cargo inserido não é válido. Por favor, insira um cargo válido.")
            if cargo == "A":
                salario = 2500
            elif cargo == "B":
                salario = 5000
            elif cargo == "C":
                salario = 6500
            informacoesContato = simpledialog.askinteger("Cadastro de Funcionário", "Digite o número para contato:")

            funcionario = Funcionario(self.contador_id, nome, cargo, informacoesContato, salario)
            self.listaFuncionarios.append(funcionario)

            opcao = simpledialog.askstring("Cadastro de Funcionário", "Deseja cadastrar mais algum funcionário? (S/N)")
            if opcao.lower() != "s":
                break

    def listarFuncionarios(self):
        list_window = tk.Tk()
        list_window.title("Lista de Funcionários")
        list_text = tk.Text(list_window)
        list_text.pack()

        for funcionario in self.listaFuncionarios:
            list_text.insert(tk.END, funcionario.obterDetalhes())

        screen_width = list_window.winfo_screenwidth()
        screen_height = list_window.winfo_screenheight()
        window_width = 600
        window_height = 400
        x_coordinate = (screen_width / 2) - (window_width / 2)
        y_coordinate = (screen_height / 2) - (window_height / 2)
        list_window.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

    def excluirFuncionarios(self):
        while True:
            id_funcionario = simpledialog.askinteger("Excluir Funcionário", "Digite o ID do funcionário que deseja excluir:")
            encontrado = False
            for funcionario in self.listaFuncionarios:
                if id_funcionario == funcionario.idFuncionario:
                    self.listaFuncionarios.remove(funcionario)
                    print("Usuário removido.")
                    encontrado = True
                    break
            if not encontrado:
                messagebox.showinfo("Funcionário não encontrado", "Esse funcionário não foi cadastrado.")
            opcao = simpledialog.askstring("Excluir Funcionário", "Deseja excluir mais algum funcionário? (S/N)")
            if opcao.lower() != "s":
                break

    def modificarFuncionarios(self):
        while True:
            id_funcionario = simpledialog.askinteger("Modificar Funcionário",
                                                     "Digite o ID do funcionário que deseja modificar:")
            encontrado = False
            for funcionario in self.listaFuncionarios:
                if id_funcionario == funcionario.idFuncionario:
                    print("Funcionário cadastrado.")
                    while True:
                        novoCargo = simpledialog.askstring("Modificar Funcionário", "Digite o novo cargo:").upper()
                        if novoCargo in ["A", "B", "C"]:
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
                        else:
                            messagebox.showinfo("Cargo inválido",
                                                "O cargo inserido não é válido. Por favor, insira um cargo válido.")
                            continue
                    break
            if not encontrado:
                messagebox.showinfo("Funcionário não encontrado", "Esse funcionário não foi cadastrado.")
                break
            select = simpledialog.askstring("Modificar Funcionário",
                                            "Deseja modificar mais algum funcionário? (S/N)").lower()
            if select == "n":
                break


class InterfaceGrafica:
    def __init__(self, master):
        self.master = master
        self.master.title("HRMasters Interface")
        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()
        self.window_width = 600
        self.window_height = 400
        self.x_coordinate = (self.screen_width / 2) - (self.window_width / 2)
        self.y_coordinate = (self.screen_height / 2) - (self.window_height / 2)
        self.master.geometry(f"{self.window_width}x{self.window_height}+{int(self.x_coordinate)}+{int(self.y_coordinate)}")

        self.hrmasters = HRMasters()

        self.title_label = tk.Label(self.master, text="Gerenciamento de Funcionários - HRMasters", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        self.cadastrar_button = tk.Button(self.master, text="Cadastrar Funcionário", command=self.hrmasters.cadastrarFuncionario)
        self.cadastrar_button.pack(pady=10)

        self.listar_button = tk.Button(self.master, text="Listar Funcionários", command=self.hrmasters.listarFuncionarios)
        self.listar_button.pack(pady=10)

        self.excluir_button = tk.Button(self.master, text="Excluir Funcionário", command=self.hrmasters.excluirFuncionarios)
        self.excluir_button.pack(pady=10)

        self.modificar_button = tk.Button(self.master, text="Modificar Funcionário", command=self.hrmasters.modificarFuncionarios)
        self.modificar_button.pack(pady=10)


if __name__ == '__main__':
    root = tk.Tk()
    app = InterfaceGrafica(root)
    root.mainloop()
