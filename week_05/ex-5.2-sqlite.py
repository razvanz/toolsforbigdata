import sqlite3

print (sqlite3.version)
print (sqlite3.sqlite_version)

conn = sqlite3.connect('/Users/razvanz/Downloads/northwind.db')
conn.text_factory = str
conn.text_factory = bytes
c = conn.cursor()
c.execute("SELECT * FROM "
	"Customers c INNER JOIN Orders o INNER JOIN "
	"\"Order Details\" od INNER JOIN Products p "
	"ON c.customerid = o.customerid AND "
	"o.orderid = od.orderid AND "
	"od.productid = p.productid "
	"WHERE c.customerid = \"ALFKI\";")
print(c.fetchall())
