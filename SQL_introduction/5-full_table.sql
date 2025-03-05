SELECT CONCAT('Table   ', table_name, '     ', table_schema, '.', table_name, '     ', 
       CREATE_TABLE_STATEMENT) AS CreateTable
FROM information_schema.tables
WHERE table_schema = DATABASE() AND table_name = 'first_table';
