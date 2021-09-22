/*
Generate the following two result sets:

Query an alphabetically ordered list of all names in OCCUPATIONS, immediately followed by the first letter of each profession as a parenthetical (i.e.: enclosed in parentheses). For example: AnActorName(A), ADoctorName(D), AProfessorName(P), and ASingerName(S).
Query the number of ocurrences of each occupation in OCCUPATIONS. Sort the occurrences in ascending order, and output them in the following format:
*/

select concat(name,'(',left(occupation,1),')') as ocname from occupations order by name;
select concat('There are a total of',' ',count(occupation),' ',lower(occupation),'s.') as occount from occupations group by occupation order by count(occupation),occupation;
