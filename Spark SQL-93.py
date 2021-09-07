## 2. Register the DataFrame as a Table ##

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")

df.registerTempTable('census2010')

tables = sqlCtx.tableNames()
print(tables)

## 3. Querying ##

sqlCtx.sql('select age from census2010').show()

## 4. Filtering ##

query = 'select males, females from census2010 where age > 5 and age < 15'
sqlCtx.sql(query).show()

## 5. Mixing Functionality ##

query= 'select males, females from census2010'

sqlCtx.sql(query).describe().show()

## 6. Multiple tables ##

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
df.registerTempTable('census2010')

census1980 = sqlCtx.read.json('census_1980.json')
census1990 = sqlCtx.read.json('census_1990.json')
census2000 = sqlCtx.read.json('census_2000.json')

census1980.registerTempTable('census1980')
census1990.registerTempTable('census1990')
census2000.registerTempTable('census2000')

tables = sqlCtx.tableNames()
print(tables)

## 7. Joins ##

query = 'select a.total, b.total from census2010 a inner join census2000 b on a.age = b.age'

sqlCtx.sql(query).show()

## 8. SQL Functions ##

query = 'select sum(a.total), sum(b.total), sum(c.total) from census2010 a inner join census2000 b on a.age = b.age inner join census1990 c on a.age = c.age'

sqlCtx.sql(query).show()