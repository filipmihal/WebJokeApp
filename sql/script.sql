/*Select the longest joke*/
SELECT *
FROM jokes
ORDER BY joke_length DESC
LIMIT 1;

/*the average rank of each jokes_category*/
SELECT j.jokes_categories_id,
       c.name,
       round(avg(j.rank), 1) AS average_rank
FROM jokes j
JOIN jokes_categories c ON (j.jokes_categories_id = c.id)
GROUP BY j.jokes_categories_id
ORDER BY average_rank DESC;

/*add new column to jokes_categories*/
ALTER TABLE `jokes_categories`
	ADD COLUMN `average_rank` FLOAT NOT NULL AFTER `name`,
	DROP COLUMN `average_rank`;

/*update jokes_categories table. add average rank*/
UPDATE jokes_categories c,
  (SELECT j.jokes_categories_id AS id,
          c.name,
          round(avg(j.rank), 1) AS average_rank
   FROM jokes j
   JOIN jokes_categories c ON (j.jokes_categories_id = c.id)
   GROUP BY j.jokes_categories_id
   ORDER BY average_rank DESC) import
SET c.average_rank = import.average_rank
WHERE c.id = import.id;

/*select valid categories test #1*/
select * from jokes_categories c where c.average_rank > 0 group by c.id;

/*select valid categories test #2*/
select * from jokes_categories c where c.average_rank > 0;

/*add is_valid column*/
ALTER TABLE `jokes_categories`
	ADD COLUMN `is_valid` TINYINT(1) NOT NULL DEFAULT '0' AFTER `average_rank`;


/*CLEANING JOKES*/
/*find duplicates in jokes table */
select * from (
select *, count(*) as duplicates from jokes group by joke, jokes_categories_id
)q where q.duplicates > 1;

ALTER TABLE `jokes`
	ADD COLUMN `is_valid` TINYINT NOT NULL DEFAULT '1' AFTER `jokes_categories_id`;

/*update jokes_categories table. add average rank*/
UPDATE jokes j,
  (select * from (
select *, count(*) as duplicates from jokes group by joke, jokes_categories_id
)q where q.duplicates > 1) import
SET j.is_valid = 0
WHERE j.id = import.id;

/*CREATED MIG TABLES*/

/*MOVE CONTENT TO MIG*/

/*fullfill my migration tables*/
insert into mig_jokes
select id, joke, joke_length, rank, jokes_categories_id as category_id
from jokes
where is_valid = 1;

insert into mig_jokes_categories
select id, name, average_rank
from jokes_categories
where is_valid = 1;

