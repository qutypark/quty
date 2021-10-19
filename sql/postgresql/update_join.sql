-- you have to calculate the net price of every product based on the discount of the product segment

UPDATE product
SET net_price = price - price * discount
FROM product_segment
WHERE product.segment_id = product_segment.id;
