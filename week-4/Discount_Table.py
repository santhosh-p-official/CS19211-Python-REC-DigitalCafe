""" A particular retailer is having a 60 percent off sale on a variety of discontinued products. The retailer would like to help its customers determine the reduced price of the merchandise by having a printed discount table on the shelf that shows the original prices and the prices after the discount has been applied. Write a program that uses a loop to generate this table, showing the original price, the discount amount, and the new price for purchases of $4.95, $9.95, $14.95, $19.95 and $24.95. Ensure that the discount amounts and the new prices are rounded to 2 decimal places when they are displayed.

Sample Output

Original: $4.95 | Discounted: $1.98 

Original: $9.95 | Discounted: $3.98 

Original: $14.95 | Discounted: $5.98 

Original: $19.95 | Discounted: $7.98 

Original: $24.95 | Discounted: $9.98"""

for i in range(5):
    a=float(input())
    print("Original: ${:.2f}".format(a),"| Discounted: ${:.2f}".format(a-a*0.6))
