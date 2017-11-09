## 0x0F Python Object Relational Mapping

<img src="https://image.slidesharecdn.com/sqlaintro-130921142257-phpapp02/95/michael-bayer-introduction-to-sqlalchemy-postgres-open-6-638.jpg?cb=1379773451">

### Overview of Object-relational mappers

An object-relational mapper (ORM) is a code library that automates the transfer of data stored in relational databases tables in objects that are more commonly used in application code.

The database storage abstraction most commonly used in Python web development is sets of relational tables. Relational databases store data in a series of tables. Interconnections between the tables are specified as foreign keys. A foreign key is a unique reference from one row in a relational table to another row in a table, which can be the same table but is most commonly a different table.

ORMs provide a high-level abstraction upon a relational database that allows a developer to write Python code instead of SQL to create, read, update and delete data and schemas in their database. The advantage is allowing developers to use the programming language that they are most comfortable working with to access a database instead of writing SQL statements or stored procedures.

The ability to write Python code instead of SQL can speed up web application development, especially at the beginning of a project since it's typically easier to knock out a prototype or start a web application using a single programming language.

### Disadvantages of using an ORM

There are a number of downsides of using ORMs, including:
```
1. Impedance mismatch
2. Potential for reduced performance
3. Shifting complexity from the database into the application code
```

#### Impedance Mismatch

Impedance mismatch is a catch-all term for the difficulties that occur when moving data between relational tables and application objects. The way a developer uses objects is different from how data is stored and joined in relational tables.

#### Potential for Reduced Performance

One of the concerns that is associated with higher-level abstraction or framework is potential for reduced performance. With ORMs, the performance problem comes from the translation of application code into a corresponding SQL statement which may not be turned properly.

There's a lot of "potential for" and "may or may not" guess work when using ORMs. In large projects, at least 10-20% of a project's database interactions can have a major performance improvement by having a knowledgeable database administrator write tuned SQL statements to replace the ORM's generated SQL code.

#### Shifting Complexity

The code for working with an application's data has to live somewhere. With an ORM, the data manipulation code instead lives within the application's Python codebase. The addition of data handling logic in the codebase generally isn't an issue with a sound application design, but it does increase the total amount of Python code instead of splitting code between the application and the database stored procedures.
