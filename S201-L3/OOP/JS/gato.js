class Gato extends Animal{
    constructor(nome, idade, especie, cores){
        super(nome, idade, especie)
        this.nome = nome
        this.idade = idade
        this.especie = especie
        this.cores = cores
    }
    mostraInfo(){
        console.log(`Nome: ${nome}. Idade: ${idade}. Especie: ${especie}. Cores: ${}`)
    }
}