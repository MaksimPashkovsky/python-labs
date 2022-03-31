select
	distinct h.operator,
	(round(100.0 * count(*) / (select count(*) from history), 2)) as percents
from 
	history as h
group by h.operator