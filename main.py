import sqlite3
import tkinter as Tk
from tkinter import *



def __init__(self, root, academia):
        self.root = root
        self.root.title("academia.db")
        self.db = academia

        



class Academia:
    
    def __init__(self):
        self.conn = sqlite3.connect('academia.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS membros
                                    (id TEXT PRIMARY KEY, nome TEXT, idade INTEGER, altura REAL)''')

def cadastra_membro(self, membro):
        self.cursor.execute("INSERT INTO membros VALUES (?, ?, ?, ?)",
                             (membro['id'], membro['nome'], membro['idade'], membro['altura']))
        self.conn.commit()

def exibe_membros(self):
        self.cursor.execute("SELECT * FROM membros")
        membros = self.cursor.fetchall()
        for membro in membros:
            print(f"ID: {membro[0]}, Nome: {membro[1]}, Idade: {membro[2]}, Altura: {membro[3]}")

def atualiza_membro(self, id, membro):
        self.cursor.execute("UPDATE membros SET nome = ?, idade = ?, altura = ? WHERE id = ?",
                             (membro['nome'], membro['idade'], membro['altura'], id))
        self.conn.commit()

def exclui_membro(self, id):
        self.cursor.execute("DELETE FROM membros WHERE id = ?", (id,))
        self.conn.commit()

academia = Academia()
while True:
    print("\nEscolha uma opção:")
    print("1. Cadastrar membro")
    print("2. Exibir membros")
    print("3. Atualizar membro")
    print("4. Excluir membro")
    print("5. Sair")

    opcao = input("Digite o número da opção: ")

    if opcao == '1':
        membro = {}
        membro['id'] = input("Digite o ID do membro: ")
        membro['nome'] = input("Digite o nome do membro: ")
        membro['idade'] = int(input("Digite a idade do membro: "))
        membro['altura'] = float(input("Digite a altura do membro: "))
        academia.cadastra_membro(membro)

    elif opcao == '2':
        academia.exibe_membros()

    elif opcao == '3':
        id = input("Digite o ID do membro que deseja atualizar: ")
        membro = {}
        membro['id'] = id
        membro['nome'] = input("Digite o novo nome do membro: ")
        membro['idade'] = int(input("Digite a nova idade do membro: "))
        membro['altura'] = float(input("Digite a nova altura do membro: "))
        academia.atualiza_membro(id, membro)

    elif opcao == '4':
        id = input("Digite o ID do membro que deseja excluir: ")
        academia.exclui_membro(id)

    elif opcao == '5':
        break

    else:
        print("Opção inválida.")






