const mysql = require('think-model-mysql');

module.exports = {
    handle: mysql,
    database: '你的数据库名',
    prefix: 'hiolabs_',
    encoding: 'utf8mb4',
    host: '127.0.0.1',
    port: '3306',
    user: 'root',
    password: '密码',
    dateStrings: true
};
