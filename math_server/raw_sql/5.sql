select (
		select count(distinct (operator, number1, number2))
		from history
	) as unique_count,
	(
		select count(*) from (
			select operator, number1, number2
			from history
			except all
			select distinct operator, number1, number2
			from history
		) as fff
	) as duplicated_count
from history
group by unique_count