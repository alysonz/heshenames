heshenames
==========
Purpose: Produce a good guess at the gender of each employee of the state of Arizona
and compare the wages of men and women with the same job title in the same department.

First name gender data is drawn from here:
http://www.census.gov/genealogy/www/data/1990surnames/dist.male.first  for male

and here:
http://www.census.gov/genealogy/www/data/1990surnames/dist.female.first for female

Methodology for name gender data is here:
http://www.census.gov/genealogy/www/data/1990surnames/nam_meth.txt

The above lists of names were copy and pasted into female.txt and male.txt.
Those files were reformatted with heshe.py into femnames.txt and malenames.txt for loading into a mysql table.

doa.txt is the copy and paste product of the Arizona Deparment of Administration
employee database. It is a snapshot of employment in the state from 7-29-2013.
doa.txt was reformatted by doa.py into doanames.txt, which is just the first names
of employees, for loading into mysql. I removed apostrophes from names because I didn't
understand how to escape special characters yet. Similarly, I used currency.py to remove
apostrophes and $ from doa.txt to get doafull.txt for loading into mysql. This was dumb,
and I wouldn't do it again now that I know how to work around it, but I don't think it effected my results.

sql.py matches each name in doanames.txt with gender information from femnames.txt
and malenames.txt and combines full employee information from doafull.txt with the
matching gender information into a new table.

gender.py calculates the %maleness and %femaleness of each employee 
name where gender information is available and creates a new table with
all previous information plus those added indexes called doagender. (Each name from the
census database has information about how many people in the sample population own that 
name. The sample population included about 6 million people, about 3 million men and
about 3.2 million women. For example, .328 percent of the male sample population has the name Ryan.
About .006 percent of the female sample population has the name Ryan.
.328 percent of 3 million is 9,840 male Ryans. .006 percent of 3.2 million is 192 female Ryans.
Out of a total of 10,032 Ryans, 1.91 percent are female (192/10,032) and 98.1 percent are male (9,840/10,032).)

salary.py queries doagender for unique job title's within each state department
and flags titles/departments when the disparity between average male and average
female salaries exceeds $.50 per hour. This flags instances where, on average, men
make more than women and when women make more than men within the same job title and
the same department. It also produces mitigating information like how many employees
the average salaries are derived from and how many employees with that title in that
department have names that have less than a 70 percent gender certainty. It also lists
counts the number and lists the employees for whom gender data was not available, aka people with unusual names.

I wouldn't use this process to draw any hard conclusions. There is way too much error involved.
37 percent of the employees in doa database had names for which there was no gender information.
But, I intend to use this as a good starting place for asking questions about cases where there
appears to be a clear disparity in wage.
