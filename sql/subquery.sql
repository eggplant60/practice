-- CREATE TABLE IF NOT EXISTS test
--        (date timestamp,
--         id int);
-- \COPY test FROM './data.csv' CSV HEADER;
-- INSERT INTO test
--        VALUES ('2019-02-22 00:00:00', 3);

SELECT * FROM test;


-- CREATE VIEW v_test AS SELECT * FROM test WHERE id >=2;
-- SELECT * FROM v_test;

-- 相関副問合せ
CREATE OR REPLACE VIEW v_test AS
       SELECT * FROM test t1
       WHERE NOT EXISTS (
       	     SELECT * FROM test t2
       	     WHERE
		t1.id < t2.id AND
		t1.date >= t2.date);


SELECT * FROM v_test;
