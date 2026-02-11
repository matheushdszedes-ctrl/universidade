# Projeto Universidade

Modelagem em Orientação à Objetos das Entidades Alunos, Cursos e Turmas.

## Caso de Uso
```mermaid
flowchart LR
    Usuario([Secretaria])

    UC1((Cadrastra Alunos))
    UC2((Editar Alunos))
    UC3((Trasferir Alunos))

    Usuario --> UC1
    Usuario --> UC2
    Usuario --> UC3
```

## Diagrama de Classes


```mermaid
classDiagram
    class aluno{
        - nome
        - email
        - cpf
        - telefone
        - endereço
        - matrícula
        - cadrastra()
        + editar()
        + trasferir()

    }
```

## Dependências
- **VSCode**: IDE(interface de Desenvolvimento)

- **Mermaind**: Linguagem para confecção de Diagramas em Documentos MD (Mark Down)

- **Matherial**: Tema para colorir as pastas.

- **Git lens**: Interface gráfica pra o versionamento .git intergrada ao VSCode.