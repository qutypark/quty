select repeat('* ', @number:=@number+1)
from information_schema.tables, (select @number:=0) as tm1
where @number<21;

set @temp:=0;
select repeat('* ', @temp:=@temp+1)
from information_schema.tables
where @temp<20;
