class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def exibir_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano: {self.ano}")
        print("-" * 20)


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"O livro '{livro.titulo}' foi adicionado com sucesso!")

    def mostrar_livros(self):
        if not self.livros:
            print("A biblioteca está vazia!")
        else:
            print("\n📚 Livros na biblioteca:")
            for livro in self.livros:
                livro.exibir_info()


# Usando as classes
livro1 = Livro("1984", "George Orwell", 1949)
livro2 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)

biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

biblioteca.mostrar_livros()
