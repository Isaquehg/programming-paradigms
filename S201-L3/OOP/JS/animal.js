class Animal{
    constructor(nome, idade, especie){
        this.nome = nome
        this.idade = idade
        this.especie = especie
    }
    printInfo(){
        console.log(`Nome: ${nome}. Idade: ${idade}. Especie: ${especie}`)
    }
}