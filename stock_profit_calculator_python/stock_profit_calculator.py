#Submitted by: Rucha Apte

#This is a file to calculate stock profit for a particular symbol.
#Prerequisites: Python3 should be installed


while True:
    print("Compute Your Profit:")
    print("")
    symbol= input("Please enter the stock symbol?")
    #allotment is number of shares
    allotment= float(input("Please enter Allotment/ number of shares?"))
    #buy price
    finalSharePrice= float(input("Please enter the Final Share Price?"))
    #selling commission
    commission= float(input("Please enter the Sell commission ?"))
    #sell price
    initialSharePrice= float(input("Please enter the Initial Share Price ?"))
    #buying commission
    buycommission= float(input("Please enter the Buy commission ?"))
    #tax rate
    capitalGain= float( input("Please enter the capital Gain in % ?"))
    print(" ")

    print("PROFIT REPORT: ")
    #Proceeds (Allotment x Final share price)
    proceeds= allotment*finalSharePrice
    print ("Proceeds")
    print ("$"+ str( proceeds))

    #capitalGain1 = ( ( Selling Price × Number of Shares ) - Selling Commission ) - ( ( Buying Price × Number of Shares ) + Buying Commission)
    capitalGain1 = ((finalSharePrice * allotment) - commission) - ((initialSharePrice * allotment) + buycommission)
    #print (capitalGain1)
    print(" ")

    #Cost (Allotment x Initial Share Price + commissions + Tax on Capital Gain)
    cost= (allotment*initialSharePrice+(commission+buycommission)+(capitalGain/100 )*capitalGain1)
    print ("Cost")
    print ("$"+ str( cost))
    print("")

    print ("Cost details: ")
    print("Total Purchase Price")
    print(allotment * initialSharePrice)
    print("Buy Commission=", buycommission)
    print("Sell Commission=", commission)
    print ("Tax on Capital Gain = " , ((capitalGain/100) *capitalGain1))



    print("")

    #Net Profit (in dollars)
    net = proceeds - cost
    print ("Net Profit")
    print ("$"+ str( net))
    print(" ")

    #Return on investment (in %), Net Profit / Total Investment * 100.
    roi = (net / cost *100)
    print("Return on Investment:")
    print (str(roi )+ "%")
    print(" ")

    #Break even price (in dollars) 2500+10+15/100
    breakeven= ((allotment *initialSharePrice) + buycommission +  commission )/100
    print("To break even, you should have a final share price of")
    print ( "$"+ str(breakeven))
    print(" ")

    print("***************************************************************************")
