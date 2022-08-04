const Sequelize = require('sequelize');
const sequelize = new Sequelize('tabelateste', 'root', '123456', {
    host: "localhost",
    dialect: 'mysql'
})

sequelize.authenticate().then(() => {
    console.log('Conectado com sucesso!')
}).catch((erro) => {
    console.log('Houve um erro a se conectar ' + erro)
})