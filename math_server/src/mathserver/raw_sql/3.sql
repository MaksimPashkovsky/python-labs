select 
	operator, 
	count(*) as op_count
from history
group by operator