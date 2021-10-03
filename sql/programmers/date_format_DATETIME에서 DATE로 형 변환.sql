SELECT animal_id, name, date_format(datetime, "%Y-%m-%d") as date
from animal_ins
order by animal_id;
