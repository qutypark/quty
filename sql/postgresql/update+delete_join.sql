-- you have to calculate the net price of every product based on the discount of the product segment

UPDATE product
SET net_price = price - price * discount
FROM product_segment
WHERE product.segment_id = product_segment.id;


-- delete the contacts in the contacts table with the phone number exists in the blacklist table:

DELETE FROM contacts 
USING blacklist
WHERE contacts.phone = blacklist.phone;
