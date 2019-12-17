execute deptree_fill('table', 'system', 'humorously_joke');
select * from deptree;
execute deptree_fill('table', 'system', 'humorously_act');
select * from deptree;
execute deptree_fill('table', 'system', 'humorously_category');
select * from deptree;
execute deptree_fill('table', 'system', 'humorously_club'); 
select * from deptree;
execute deptree_fill('table', 'system', 'humorously_jokester'); 
select * from deptree;
execute deptree_fill('table', 'system', 'humorously_review');
select * from deptree;
execute deptree_fill('table', 'system', 'humorously_set'); 
select * from deptree;
 
 select *
 From user_objects
 where lower(object_name) like '%humorously%';