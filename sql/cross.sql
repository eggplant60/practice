CREATE TABLE IF NOT EXISTS event (
       mailid integer,
       date timestamp,
       serial varchar,
       plu varchar,
       sk varchar);
 
\COPY event FROM './event.csv' CSV HEADER;

SELECT * FROM event;

-- クロス集計(縦持ち→横持ち)
--      日時    | 装置シリアル | PLU | 最新メールID | 合計SK01 | 合計SK03 | 合計SK04
--  ------------+--------------+-----+--------------+----------+----------+----------
--   2019/03/01 | A            | 0   |      1111111 |        2 |        0 |        0
--   2019/03/01 | A            | 1   |      1111111 |        0 |        1 |        0
--   2019/03/02 | B            | 1   |      1111112 |        1 |        0 |        0
--   2019/03/02 | B            | 2   |      1111112 |        0 |        0 |        0
--   2019/03/02 | B            | 3   |      1111112 |        1 |        0 |        1
--   2019/03/08 | A            | 0   |      1111113 |        0 |        1 |        1
--   2019/03/08 | A            | 1   |      1111113 |        0 |        1 |        0
-- あとはCfgdspと紐づけたらフィルタリングも可能に

CREATE TABLE cross_event
AS SELECT
   -- 日時,
   装置シリアル,
   "PLU",
   MAX("メールID") AS "最新メールID",
   SUM(SK01) AS "合計SK01",
   SUM(SK03) AS "合計SK03",
   SUM(SK04) AS "合計SK04"
FROM (SELECT
	mailid AS "メールID",
	to_char(date, 'yyyy/mm/dd') AS 日時,
	serial AS 装置シリアル,
	plu AS "PLU",
   	CASE WHEN sk LIKE '01/%' THEN 1 ELSE 0 END AS SK01,
   	CASE WHEN sk LIKE '03/%' THEN 1 ELSE 0 END AS SK03,
   	CASE WHEN sk LIKE '04/%' THEN 1 ELSE 0 END AS SK04 -- SASsts もここに追加可能
FROM event) T
GROUP BY 装置シリアル, "PLU" -- dashboard では日時もgroupbyの要素に入れる
ORDER BY 装置シリアル, "PLU";

SELECT * FROM cross_event;

-- -- DISKごとの平均値
-- --      日時    |        平均SK01        |        平均SK03        |        平均SK04
-- --  ------------+------------------------+------------------------+------------------------
-- --   2019/03/02 | 0.66666666666666666667 | 0.00000000000000000000 | 0.33333333333333333333
-- --   2019/03/01 | 1.00000000000000000000 | 0.50000000000000000000 | 0.00000000000000000000
-- SELECT
-- 	日時,
-- 	AVG("合計SK01") AS "平均SK01",
-- 	AVG("合計SK03") AS "平均SK03",
-- 	AVG("合計SK04") AS "平均SK04"
-- FROM cross_event
-- GROUP BY 日時
-- ORDER BY 日時;

DROP TABLE cross_event;
DROP TABLE event;
