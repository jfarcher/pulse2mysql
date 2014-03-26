pulse2mysql
===========

Converts the pulse mqtt message from my energy monitor into a counter stored in a mysql table.

The script requires python-mosquitto and python-MySQL

you will need to create a database for this to be used, you can use the included sql file

mysql -p < enmon.sql

I recommend manually running the commands though for sanity sake.
