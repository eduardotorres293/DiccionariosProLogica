graph TD
	%% Clases
	Mamifero[Mamifero] -->|es_un| Animal
	Ave -->|es_un| Animal
	Carnivoro[Carnivoro] -->|es_un| Mamifero
	Ungulado -->|es_un| Mamifero
	Herbivoro[Herbivoro] -->|es_un| Mamifero

	%% Instancias
	guepardo(["guepardo"]) -.->|instancia_de| Carnivoro
	tigre(["tigre"]) -.->|instancia_de| Carnivoro
	jirafa(["jirafa"]) -.->|instancia_de| Ungulado
	cebra(["cebra"]) -.->|instancia_de| Ungulado
	caballo(["caballo"]) -.->|instancia_de| Ungulado
	caballo -.->|instancia_de| Herbivoro
	perro(["perro"]) -.->|instancia_de| Carnivoro
	pinguino(["pinguino"]) -.->|instancia_de| Ave
	albatros(["albatros"]) -.->|instancia_de| Ave