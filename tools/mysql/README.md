## 导出建库语句
`$ mysqldump -h localhost -P 3306 -uroot -ppassword -d --skip-lock-tables --databases db_name > db_name.sql`

## 导出dbname.test的表结构及数据，并且不锁表
`$ mysqldump -uroot -pdbpasswd dbname test --lock-tables=false > dbname_test.sql`
