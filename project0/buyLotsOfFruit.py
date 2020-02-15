# buyLotsOfFruit.py
# -----------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
To run this script, type

  python buyLotsOfFruit.py
  
Once you have correctly implemented the buyLotsOfFruit function,
the script should produce the output:

Cost of [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)] is 12.25
"""

fruitPrices = {'apples':2.00, 'oranges': 1.50, 'pears': 1.75,
              'limes':0.75, 'strawberries':1.00}

def buyLotsOfFruit(orderList):
    """
        orderList: List of (fruit, numPounds) tuples
            
    Returns cost of order
    """
    totalCost = 0.0

    for fruitPound in orderList :
    	if fruitPound[0] == 'apples' :
		totalCost = totalCost + fruitPound[1] * fruitPrices['apples']
	elif fruitPound[0] == 'oranges' :
                totalCost = totalCost + fruitPound[1] * fruitPrices['oranges']
	elif fruitPound[0] == 'pears' :
                totalCost = totalCost + fruitPound[1] * fruitPrices['pears']
	elif fruitPound[0] == 'limes' :
                totalCost = totalCost + fruitPound[1] * fruitPrices['limes']
	elif fruitPound[0] == 'strawberries' :
                totalCost = totalCost + fruitPound[1] * fruitPrices['strawberries']
	else :
		print "Sorry, we do not have %s" % (fruitPound[0])
		return None
          
    "*** YOUR CODE HERE ***"
    return totalCost
    
# Main Method    
if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    orderList = [ ('apples', 2.0), ('pears', 3.0), ('limes', 4.0) ]
    print 'Cost of', orderList, 'is', buyLotsOfFruit(orderList)
