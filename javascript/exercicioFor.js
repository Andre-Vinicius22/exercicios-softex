let filme = {
    nome: 'inception',
    genero: 'Acao, Aventura, Sci-fi',
    duracao: '2h 28min'
}

let array = [1, 2, 3]

function listaPropriedades() {
    console.log('As propriedades do objeto filme são:')
    for (const e in filme) {
        console.log(e)
    }
}

function listaElementos() {
    console.log('os elementos do array são:')
    for (const i of array) {
        console.log(i)
    }
}

listaPropriedades()
listaElementos()