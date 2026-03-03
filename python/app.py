import sys
from PySide6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QLineEdit,
    QTextEdit,
    QMessageBox
)


# ===============================
# TELA CADASTRAR
# ===============================
class Cadastrar(QWidget):
    def __init__(self, alunos):
        super().__init__()

        self.alunos = alunos

        self.setWindowTitle("Cadastrar Aluno")
        self.resize(300, 200)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.nome = QLineEdit()
        self.nome.setPlaceholderText("Nome")

        self.email = QLineEdit()
        self.email.setPlaceholderText("Email")

        self.btn_salvar = QPushButton("Salvar")
        self.btn_salvar.clicked.connect(self.salvar)

        self.layout.addWidget(self.nome)
        self.layout.addWidget(self.email)
        self.layout.addWidget(self.btn_salvar)

    def salvar(self):
        nome = self.nome.text()
        email = self.email.text()

        if nome == "" or email == "":
            QMessageBox.warning(self, "Erro", "Preencha todos os campos!")
            return

        self.alunos.append({
            "nome": nome,
            "email": email
        })

        QMessageBox.information(self, "Sucesso", "Aluno cadastrado!")
        self.nome.clear()
        self.email.clear()


# ===============================
# TELA LISTAR
# ===============================
class Listar(QWidget):
    def __init__(self, alunos):
        super().__init__()

        self.alunos = alunos

        self.setWindowTitle("Lista de Alunos")
        self.resize(300, 300)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.lista = QTextEdit()
        self.lista.setReadOnly(True)

        self.layout.addWidget(self.lista)

        self.atualizar_lista()

    def atualizar_lista(self):
        self.lista.clear()

        if not self.alunos:
            self.lista.setText("Nenhum aluno cadastrado.")
            return

        for aluno in self.alunos:
            self.lista.append(
                f"Nome: {aluno['nome']} | Email: {aluno['email']}"
            )


# ===============================
# APP PRINCIPAL (IGUAL AO SEU PADRÃO)
# ===============================
class App:
    def __init__(self):
        self.app = QApplication(sys.argv)

        # Lista compartilhada
        self.alunos = []

        self.janela = QWidget()
        self.layout = QVBoxLayout()

        self.janela.setWindowTitle("Sistema Universidade")
        self.janela.resize(400, 200)
        self.janela.setLayout(self.layout)

        self.criar_botoes()

        self.janela.show()

    def criar_botoes(self):
        btn_cadastrar = QPushButton("Cadastrar")
        self.layout.addWidget(btn_cadastrar)
        btn_cadastrar.clicked.connect(self.abrir_cadastro)

        btn_listar = QPushButton("Listar")
        self.layout.addWidget(btn_listar)
        btn_listar.clicked.connect(self.abrir_listagem)

    def abrir_cadastro(self):
        self.tela_cadastro = Cadastrar(self.alunos)
        self.tela_cadastro.show()

    def abrir_listagem(self):
        self.tela_listagem = Listar(self.alunos)
        self.tela_listagem.show()


# ===============================
# EXECUÇÃO
# ===============================
if __name__ == "__main__":
    system = App()
    sys.exit(system.app.exec())