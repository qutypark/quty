set @number:=21;
select repeat('* ', @number:=@number-1)
from information_schema.tables
where @number>0;


select repeat('* ', @number:=@number-1)
from information_schema.tables, (select @number:=21) as tm1
where @number>0;
