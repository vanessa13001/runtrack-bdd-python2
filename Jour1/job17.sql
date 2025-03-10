
mysql> UPDATE etudiant SET age = 20 WHERE nom = 'Spaghetti' AND prenom = 'Betty' AND age = 23;
Query OK, 0 rows affected (0.00 sec)
Rows matched: 0  Changed: 0  Warnings: 0

mysql> SELECT * FROM etudiant WHERE nom = 'Spaghetti' AND prenom = 'Betty';
+----+-----------+--------+-----+---------------------------------+
| id | nom       | prenom | age | email                           |
+----+-----------+--------+-----+---------------------------------+
|  1 | Spaghetti | Betty  |  20 | betty.spaghetti@laplateforme.io |
+----+-----------+--------+-----+---------------------------------+
1 row in set (0.00 sec)