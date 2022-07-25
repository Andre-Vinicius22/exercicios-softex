// função tradicional com a palavra reservada "function"
function primeiraFunction() {
    return console.log('primeira function sem parametros')
}

//  função tradicional com parâmetros e um retorno de valor
function segundaFunction(nome) {
    return console.log(`Bem Vindo ${nome}`);
}

// arrow function com parâmetros e que retorne um valor

let arrow = (direction) => {
    console.log(`a flecha aponta para, ${direction}`);
}

primeiraFunction() // resultado: primeira function sem parametros

segundaFunction('Andre') // resultado: Bem Vindo Andre

arrow('direita') // resultado: a flecha aponta para, direita