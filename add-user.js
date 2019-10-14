const process = require('process');
const argv = process.argv;

process.on('exit', function(code) {
    return console.log(`About to exit with code ${code}`);
});
console.log(argv);

if (argv.length < 5) {
    const msg = "Invalid number of arguments. Three expected (username, email, password)";
    console.log(msg);
    return msg;
}



const mysql = require('mysql');
const conection = mysql.createConnection({
    host: 'localhost',
    user: 'admin',
    password: 'admin',
    database: 'jpp-sql'
});



conection.connect((err) => {
    if (err) {
        console.log('Error connecting to Db');
        return;
    }
    console.log('Connection established');
});

const user = {
    username: argv[2],
    email: argv[3],
    password: argv[4]
};
conection.query('INSERT INTO users SET ?', user, (err, res) => {
    if (err) throw err;

    console.log('Last insert ID:', res.insertId);
});
