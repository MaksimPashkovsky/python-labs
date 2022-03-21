select (
		select count(*) from (
			select operator, number1, number2 from history
			except all
			select distinct operator, number1, number2 from history
		) as fff
	) as duplicated_count,
	(
		select count(*) from (
			select distinct operator, number1, number2 from history
			except all (
				select operator, number1, number2 from history
				except all
				select distinct operator, number1, number2 from history
			)
		) as ggg
	) as unique_count
from history
group by unique_count