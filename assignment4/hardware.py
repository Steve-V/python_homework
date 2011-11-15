
#!/usr/bin/env python

#import 

def getCommand():
    '''Find out what the user wants us to do'''
    
    command = input("(1) - Add new tool\n(2) - Get inventory cost\n(3) - Tool Lookup\n(4) - Exit\nCommand: ")
    
    # Validity check
    if command.strip() not in ['1','2','3','4']:
        return '4'
    return command


def addNewTool(t):
    '''Given a tool name, quantity, and price, insert that tool into the database'''
    try:
        toolname = input("New Tool Name: ") 
        quantity = int( input("Quantity: ") )
        price = float( input("Cost: ") )
    except ValueError:
        print("Error!")
        return
    t.addTool(toolname,quantity,price)
    return

def getInventoryCost(t):
    grandTotal = 0.0
    for eachItem in t.getAllTools().values():
        
        # Calculate
        grandTotal += eachItem["amount"] * eachItem["price"]
        
        # Pretty print
        import decimal
        newTotal = "$" +  str(decimal.Decimal(str(grandTotal)).quantize(decimal.Decimal('.01'), rounding="ROUND_DOWN") )
    
    # Print
    print("Total inventory cost: {}".format(newTotal) )
    

def lookupTool(t):
    requestedTool = input("Tool name: ")
    
    toolData = t.getToolData(requestedTool)
    
    if toolData:
        print("Tool name: {}, Quantity: {}, Price: {}".format( toolData["toolname"],toolData["amount"],toolData["price"] ) )
    else:
        print("Tool not found!")
    

def runTests(t):
    
    runAgain = True
    while(runAgain):
        
        # Get input about what to do next
        nextCommand = getCommand()
        
        if nextCommand == '1':
            addNewTool(t)
        elif nextCommand == '2':
            getInventoryCost(t)
        elif nextCommand == '3':
            lookupTool(t)
        else:
            runAgain = False
        
    

def main():
    
    from shelvedb import ToolShelf
    t = ToolShelf()
    runTests(t)
    
    
    
    
if __name__ == '__main__':
    main()