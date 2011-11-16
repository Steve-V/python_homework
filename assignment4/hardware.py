
#!/usr/bin/env python

#import 

def getCommand(whatType):
    '''Find out what the user wants us to do'''
    
    # Set up the question
    if whatType == "shelve":
        ask = "(1) - Add new tool\n(2) - Get inventory cost\n(3) - Tool Lookup\n(4) - Exit\nCommand: "
        valid = ['1','2','3','4']
    else:
        ask = "(1) - Add new tool\n(2) - Display tools as table\n(3) - Exit\nCommand: "
        valid = ['1','2','3']
    
    # Talk to the user
    command = input(ask)
    
    # Validity check
    if command.strip() not in valid:
        return None
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
    '''Calculate total cost of inventory'''
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
    '''Lookup data on a single tool'''
    requestedTool = input("Tool name: ")
    
    toolData = t.getToolData(requestedTool)
    
    if toolData:
        print("Tool name: {}, Quantity: {}, Price: {}".format( toolData["toolname"],toolData["amount"],toolData["price"] ) )
    else:
        print("Tool not found!")
    

def runTests(t,whichTests):
    '''Test each function - now with polymorphism!'''
    
    runAgain = True
    while(runAgain):
        
        # Get input about what to do next
        nextCommand = getCommand(whichTests)
        
        if nextCommand == '1':
            addNewTool(t)
        elif nextCommand == '2':
            if whichTests == 'csv':
                t.showAllTools()
            else:
                getInventoryCost(t)
        elif nextCommand == '3':
            if whichTests == 'csv':
                runAgain = False
            else:
                lookupTool(t)
        else:
            runAgain = False
        

def main():
    
    # Shelve
    from shelvedb import ToolShelf
    t = ToolShelf()
    runTests(t,'shelve')
    
    # CSV
    from filedb import ToolCsv
    c = ToolCsv()
    runTests(c,'csv')
    
    
    
if __name__ == '__main__':
    main()