'''
@Link: https://www.hackerrank.com/challenges/bon-appetit/problem?isFullScreen=true
@Difficulty: Easy

Problem:    
Anna and Brian are sharing a meal at a restaurant and they agree to split the bill equally. 
Brian wants to order something that Anna is allergic to though, and they agree to split the 
amount he has to pay.
You are given an array of prices of all items, an index of the item that Anna did not eat, 
and the amount of money that Brian charged Anna for her portion of the bill.
If the bill is fairly split, print "Bon Appetit", otherwise, print the amount of money that Brian needs to refund to Anna.
Example:
Input:
bill = [3, 10, 2, 9]
k = 1
b = 12
Output: 5

'''
def bonAppetit(bill, k, b):
    total: int = sum(bill)
    cost_of_item_anna_did_not_eat: int = bill[k]
    per_person_split = (total - cost_of_item_anna_did_not_eat)/2
    if b != per_person_split:
        print(int(b - per_person_split))
        return
    print("Bon Appetit")

bonAppetit([3, 10, 2, 9], 1, 12) # 5

'''
Solution:
Easy. Calculate the total bill. Remove the item that Anna did not eat and half it. That is the amount each person shopuld pay. 
Now, Anna paid an about <b>. If <b> is equal to the per person split, then simply print Bon Appetit, otherwise get the difference 
between the amount Anna paid (<b>) and the per person split and print it.

Note: The small trick here is to use the int() function to convert the float to an integer.
'''