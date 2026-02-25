from modules.MySQL import MySQL
from modules.aluno import Aluno

import sys
import re

from PySide6.QtWidgets import (
    QApplication, 
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox
)

class TelaCadastro():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.janela = QWidget()
        self.layout = QVBoxLayout()
        self.banco = MySQL()

        self.campos = {}

        self.configurar_janela()
        self.criar_componentes()

    # ===============================
    # CONFIGURAÇÃO DA JANELA DINÂMICA
    # ===============================
    def configurar_janela(self):
        self.janela.setWindowTitle("Cadastrar Aluno")

        # Pega tamanho da tela automaticamente
        screen = self.app.primaryScreen()
        tamanho_tela = screen.availableGeometry()

        largura = int(tamanho_tela.width() * 0.5)
        altura = int(tamanho_tela.height() * 0.6)

        self.janela.resize(largura, altura)

        # Centraliza a janela
        self.janela.move(
            (tamanho_tela.width() - largura) // 2,
            (tamanho_tela.height() - altura) // 2
        )

        self.janela.setLayout(self.layout)

    # ===============================
    # COMPONENTES DA TELA
    # ===============================
    def criar_componentes(self):
        componentes = {
            "nome": "Digite seu nome:",
            "email": "Digite seu email:",
            "cpf": "Digite seu cpf:",
            "telefone": "Digite seu telefone:",
            "endereco": "Digite seu endereco:"
        }

        for chave, valor in componentes.items():
            label = QLabel(valor)
            campo = QLineEdit()

            self.layout.addWidget(label)
            self.layout.addWidget(campo)

            self.campos[chave] = campo

        botao_cadastro = QPushButton("Cadastrar")
        self.layout.addWidget(botao_cadastro)

        botao_cadastro.clicked.connect(self.cadastrar)

    # ===============================
    # MÉTODO SEPARADO DE VALIDAÇÃO
    # ===============================
    def validar_campos(self):
        nome = self.campos["nome"].text().strip()
        email = self.campos["email"].text().strip()
        cpf = self.campos["cpf"].text().strip()
        telefone = self.campos["telefone"].text().strip()
        endereco = self.campos["endereco"].text().strip()

        # Nome
        if not nome:
            return False, "O nome é obrigatório."

        if len(nome) < 3:
            return False, "O nome deve ter pelo menos 3 caracteres."

   

        # CPF
        if not cpf.isdigit() or len(cpf) != 11:
            return False, "CPF deve conter exatamente 11 números."

        # Telefone
        if not telefone.isdigit():
            return False, "Telefone deve conter apenas números."

        if len(telefone) < 10:
            return False, "Telefone inválido."

        # Endereço
        if not endereco:
            return False, "O endereço é obrigatório."

        return True, ""

    # ===============================
    # CADASTRO
    # ===============================
    def cadastrar(self):

        # Valida antes de inserir
        valido, mensagem = self.validar_campos()

        if not valido:
            QMessageBox.warning(
                self.janela,
                "Erro de Validação",
                mensagem
            )
            return

        aluno = Aluno(
            self.campos["nome"].text(),
            self.campos["email"].text(),
            self.campos["cpf"].text(),
            self.campos["telefone"].text(),
            self.campos["endereco"].text(),
        )

        try:
            self.banco.connect()
            aluno.cadastrar(self.banco)

            QMessageBox.information(
                self.janela,
                "Sucesso",
                "Aluno Cadastrado!"
            )

            self.limpar_campos()

        except Exception as e:
            QMessageBox.critical(
                self.janela,
                "Erro",
                f"Erro ao Cadastrar: {e}"
            )

        finally:
            self.banco.disconnect()

    # ===============================
    # LIMPAR CAMPOS
    # ===============================
    def limpar_campos(self):
        for campo in self.campos.values():
            campo.clear()


if __name__ == "__main__":
    tela = TelaCadastro()
    tela.janela.show()
    sys.exit(tela.app.exec())