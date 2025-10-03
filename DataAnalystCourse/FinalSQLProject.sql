--Hiba Abidelkarem Final Project

--01 
/*We will need an overview of our main KPIs performance, such as gross revenue,
total discount, net revenue, orders, quantity of products and unique products,
divided by years and quarters.*/

select year(o.OrderDate) as Year, datepart(QUARTER, o.OrderDate) as Quarter,
sum(UnitPrice * Quantity) as Gross_Revenue, sum(UnitPrice * Discount * Quantity) as Total_discount, 
(sum(UnitPrice *Quantity) - sum(UnitPrice * Discount * Quantity) ) as Net_revenue, count( distinct od.OrderID) as Orders, 
sum(Quantity) as Quantity_of_products, count(DISTINCT ProductID) as UniqueProducts
from [Order Details] od 
join Orders o on od.OrderID=o.OrderID
group by year(o.OrderDate), datepart(QUARTER,o.OrderDate)
order by YEAR, Quarter

--02
/*We want to see out shipment performance by product name. Please separate
counts of orders by each product and show the amount of days to ship higher
than 200 only in 1997. Order it by days to ship descending.*/

select p.productname, sum(datediff(day, o.orderdate, o.shippeddate)) as total_days_to_ship,
    count(distinct od.orderid) as orders
from [Order Details] od
join orders o on od.orderid = o.orderid
join products p on od.productid = p.productid
where year(o.orderdate) = 1997
  and o.shippeddate is not null
group by p.productname
having sum(datediff(day, o.orderdate, o.shippeddate)) > 200
order by total_days_to_ship desc;

--03
/*Please provide per ship country the gross revenue, discount, net revenue, orders,
quantity and the amount of products only for ship countries – Germany, USA, Brazil
and Austria.*/

select o.shipcountry,
    sum(od.unitprice * od.quantity) as gross_revenue,
    sum(od.unitprice * od.discount * od.quantity) as total_discount,
    sum(od.unitprice * od.quantity) - sum(od.unitprice * od.discount * od.quantity) as net_revenue,
    count(distinct od.orderid) as orders,
    sum(od.quantity) as quantity_of_products,
    count(distinct od.productid) as unique_products
from [Order Details] od
join orders o on od.orderid = o.orderid
where o.shipcountry in ('Germany', 'USA', 'Brazil', 'Austria')
group by o.shipcountry

--04
/*We need to break down the gross revenue and orders by months names in 1997.
Please order it by months numbers*/

select month(o.orderdate) as month_number,
    datename(month, o.orderdate) as month_name,
    sum(od.unitprice * od.quantity) as gross_revenue,
    count(distinct od.orderid) as orders
from [Order Details] od
join orders o on od.orderid = o.orderid
where year(o.orderdate) = 1997
group by month(o.orderdate), datename(month, o.orderdate)
order by month_number;

--05
/*We are interested in how the shipping companies are performing. Please provide the days
to ship and the amount of orders in 1997 per ship company name.*/

select s.companyname as ship_company,
    sum(datediff(day, o.orderdate, o.shippeddate)) as total_days_to_ship,
    count(o.orderid) as orders
from orders o
join shippers s on o.shipvia = s.shipperid
where year(o.orderdate) = 1997
  and o.shippeddate is not null
group by s.companyname
order by total_days_to_ship asc;



--06
/*We would like to understand the top and bottom products we have in our store in
1997. Please show the top and bottom 5 products names by the their amount of sales.*/

select ProductName, orders
from (
	select  ProductName, orders,
	DENSE_RANK() over (order by orders) as randasc,
	DENSE_RANK() over (order by orders desc) as randdesc
	from (
		select ProductName, count(od.OrderID) as orders
		from [Order Details] od 
		join Products p on od.ProductID=p.ProductID
		join Orders o on od.OrderID=o.OrderID
		where OrderDate between '1997-01-01' and '1997-12-31'
		group by ProductName
		) a
		) a
where randasc <= 5 or randdesc <=5

--07
/*We are interested in knowing better how main categories and products performing.
Please provide the orders, quantity, gross revenue, discount and net revenue for
the top 10 percent orders of each category name and product name in 1997.*/

select top 10 percent CategoryName,ProductName, count(o.OrderID) as orders, sum(Quantity) as quantity, 
sum(od.UnitPrice * Quantity) as Gross_Revenue, 
sum(od.UnitPrice * Discount * Quantity) as Total_discount, 
(sum(od.UnitPrice *Quantity) - sum(od.UnitPrice * Discount * Quantity) ) as Net_revenue
from Products p 
join [Order Details] od on p.ProductID=od.ProductID
join Categories c on p.CategoryID=c.CategoryID
join Orders o on od.OrderID=o.OrderID
where year(OrderDate) = 1997
group by CategoryName,ProductName
order by CategoryName,ProductName asc

select
    c.categoryname,
    p.productname,
    count(distinct od.orderid) as orders,
    sum(od.quantity) as quantity,
    sum(od.unitprice * od.quantity) as gross_revenue,
    sum(od.unitprice * od.discount * od.quantity) as total_discount,
    sum(od.unitprice * od.quantity) - sum(od.unitprice * od.discount * od.quantity) as net_revenue
from products p
join categories c on p.categoryid = c.categoryid
join [Order Details] od on p.productid = od.productid
join orders o on od.orderid = o.orderid
where year(o.orderdate) = 1997
and od.orderid in (
    select top 10 percent od2.orderid
    from [Order Details] od2
    join products p2 on od2.productid = p2.productid
    join categories c2 on p2.categoryid = c2.categoryid
    join orders o2 on od2.orderid = o2.orderid
    where year(o2.orderdate) = 1997
      and c2.categoryid = c.categoryid
      and p2.productid = p.productid
    group by od2.orderid
    order by sum(od2.unitprice * od2.quantity) desc
)
group by c.categoryname, p.productname
order by c.categoryname, net_revenue desc;

--09
/*We would like to know the performance of our employees. Please provide a list of
employees names with top 5 orders and bottom 5 orders in 1997. Add new column
and name it performance for the top 5 and bottom 5 for each employee.*/

select *
from (
	select top 5 FirstName, 'top 5' as performance,  count(OrderID) as orders 
	from Orders o 
	join Employees e on o.EmployeeId = e.EmployeeID
	where o.OrderDate between '1997-01-01' and '1997-12-31'
	group by FirstName
	order by orders desc
	union all
	select top 5 FirstName, 'bottom 5' as performance,  count(OrderID) as orders 
	from Orders o 
	join Employees e on o.EmployeeId = e.EmployeeID
	where o.OrderDate between '1997-01-01' and '1997-12-31'
	group by FirstName
	order by orders asc
	) a

--10
/*We need more data also about the titles of the employees. Please pull the orders,
quantity, gross revenue, discount and net revenue per each employee in 1997.*/

select Title, FirstName, orders,quantity, gross_revenue,Discount, net_revenue,
sum(orders) over (partition by Title) as ordertotal,
sum(quantity) over (partition by Title) as quantitytotal,
sum(gross_revenue) over (partition by Title) as gross_revenuetotal,
sum(Discount) over (partition by Title) as Discounttotal,
sum(net_revenue) over (partition by Title) as net_revenuetotal
from
(
select Title, FirstName, count(distinct od.OrderID) as orders,
sum(Quantity) as quantity, sum(od.UnitPrice*Quantity) as gross_revenue,
sum(od.UnitPrice*Quantity*Discount) as Discount,
sum(od.UnitPrice*Quantity)-sum(od.UnitPrice*Quantity*Discount) as net_revenue
from Orders o
join [Order Details] od on o.OrderID=od.OrderID
join Employees e on o.EmployeeID=e.EmployeeID
where o.OrderDate between '1997-01-01' and '1997-12-31'
group by Title, FirstName
) a

--11
/*We would like to know per each of region description the orders and revenue made,
and the revenue per order. Please order it by revenue per order descending.*/

select RegionDescription, sum(orders) as orders, sum(revenue) as revenue, 
sum(orders) over (partition by Title) as ordertotal,
sum(revenue)/sum(orders) as revenue_per_order
from (
	select EmployeeID, RegionDescription, count(*) as cnt
	from EmployeeTerritories et
	left join Territories t on et.TerritoryID=t.TerritoryID
	left join Region r on r.RegionID=t.RegionID
	group by EmployeeID, RegionDescription
	) a
left join 
(
	select EmployeeID, count(distinct o.OrderID) as orders,
	sum(UnitPrice*Quantity) as revenue
	from Orders o 
	left join [Order Details] od on o.OrderID= od.OrderID
	group by EmployeeID
	) b 
on a.EmployeeID= b.EmployeeID
group by RegionDescription


--12
/*We need a dashboard to monitor our main KPIs through time. Please prepper the data
we need (create all KPIs with one query): OrderDate, Month, Quarter, CustomerID,
Country, City, ShipperID, ShippingCompany, EmployeeID, Title, FirstName, ProductName,
CategoryName, gross_revenue, Discount, Quantity, days_to_ship, products, orders*/

select o.OrderDate, datepart(month, o.OrderDate) as Month,
   datepart(quarter, o.OrderDate) as Quarter, c.CustomerID,
    c.Country, c.City, s.ShipperID, s.CompanyName as ShippingCompany,
    e.EmployeeID, e.Title, e.FirstName, p.ProductName, cat.CategoryName,
    sum(od.UnitPrice * od.Quantity) as Gross_Revenue,
    sum(od.UnitPrice * od.Quantity * od.Discount) as Discount,
    sum(od.Quantity) as Quantity,
    datediff(day, o.OrderDate, o.ShippedDate) as Days_to_Ship,
    count(distinct p.ProductID) as Products,
    count(distinct o.OrderID) as Orders
from [Order Details] od
join Orders o on od.OrderID = o.OrderID
join Products p on od.ProductID = p.ProductID
join Categories cat on p.CategoryID = cat.CategoryID
join Customers c on o.CustomerID = c.CustomerID
join Shippers s on o.ShipVia = s.ShipperID
join Employees e on o.EmployeeID = e.EmployeeID
group by o.OrderDate, c.CustomerID,c.Country,c.City,s.ShipperID,s.CompanyName,e.EmployeeID,e.Title,
 e.FirstName,p.ProductName,cat.CategoryName,datediff(day, o.OrderDate, o.ShippedDate)
order by o.OrderDate;
