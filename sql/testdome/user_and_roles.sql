-- https://www.testdome.com/questions/35745

/*
The users_roles table should contain the mapping between each user and their roles. Each user can have many roles, and each role can have many users.

Modify the provided SQLite create table statement so that:

Only users from the users table can exist within users_roles.
Only roles from the roles table can exist within users_roles.
A user can only have a specific role once.

*/

CREATE TABLE users_roles (
  userId INTEGER NOT NULL,
  roleId INTEGER NOT NULL,
  FOREIGN KEY(userId) REFERENCES users(id),
  FOREIGN KEY(roleId) REFERENCES roles(id),
  PRIMARY KEY (userId, roleId)
);

