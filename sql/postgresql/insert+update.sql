-- name must be unique 
-- if the name exists in the  customers table, just ignore it (do nothing)

INSERT INTO customers (name, email)
VALUES('Microsoft','hotline@microsoft.com') 
ON CONFLICT (name) 
DO NOTHING;

-- when inserting a customer that already exists, in this case, you use the UPDATE clause as the action of the INSERT statement as follows:

-- newly inserted value: excluded / existing value: customer(table name)
-- for example, "Microsoft" has "contact@microsoft.com" , and it want to add "hotline@microsoft.com"
-- email will be "hotline@microsoft.com;contact@microsoft.com"

INSERT INTO customers (name, email)
VALUES('Microsoft','hotline@microsoft.com') 
ON CONFLICT (name) 
DO 
   UPDATE SET email = EXCLUDED.email || ';' || customers.email;
   
