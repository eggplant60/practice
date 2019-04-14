-- 準備
DROP TABLE IF EXISTS cfgdsp;

CREATE TABLE IF NOT EXISTS cfgdsp (
    mailid integer,
    date timestamp,
    serial varchar,
    plu varchar,
    var varchar
);
 
\COPY cfgdsp FROM './csv/cfgdsp.csv' CSV HEADER;


-- カーソルの宣言
DROP FUNCTION IF EXISTS func;

CREATE FUNCTION func() RETURNS void AS $$
DECLARE
    disk CURSOR FOR (
        SELECT date, serial, plu FROM cfgdsp
    );
    date_i timestamp;
    serial_i varchar;
    plu_i varchar;
BEGIN
    OPEN disk;
    LOOP
        FETCH disk INTO date_i, serial_i, plu_i;
	EXIT WHEN NOT FOUND;
	RAISE INFO '%, %, %', date_i, serial_i, plu_i;

-- -- ループ内の処理
-- 	-- INSERT INTO event_4w
-- 	--        SELECT * FROM event e
-- 	--        WHERE e.date > :date_i
-- 	--        	       AND e.serial_number = :serial_number_i
-- 	--        	       AND e.plu = :plu_i

    END LOOP;	
    CLOSE disk;

END;
$$ LANGUAGE plpgsql;


-- BEGIN WORK;
SELECT func();
-- COMMIT WORK;


