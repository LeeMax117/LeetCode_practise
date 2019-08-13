# Write your MySQL query statement below
select 
    Department.Name as 'Department',
    Employee.Name as 'Employee',
    Salary
from
    Employee join Department on Department.Id = Employee.DepartmentId
where
    (Employee.DepartmentId, Salary) in 
    (select
        DepartmentId, Max(Salary)
    from 
        Employee
    group by
        DepartmentId)
