patterns = {1: ['#', '#', '#', '#', '#'], 2: ['###', '  #', '###', '#  ', '###'],
            3: ['###', '  #', '###', '  #', '###'], 4: ['# #', '# #', '###', '  #', '  #'], \
            5: ['###', '#  ', '###', '  #', '###'], 6: ['###', '#  ', '###', '# #', '###'],
            7: ['###', '  #', '  #', '  #', '  #'], 8: ['###', '# #', '###', '# #', '###'], \
            9: ['###', '# #', '###', '  #', '###'], 0: ['###', '# #', '# #', '# #', '###']}

x = input("Please input the number you want to display: ")

ref_list = []
try:
    for strel in x:
        y = int(strel)
        ref_list.append(y)
except ValueError:
    print("You did not input a valid number.")

printlist = []

for i in range(5):
    del printlist[:]
    for element in ref_list:
        printlist.append(patterns[element][i])
    for symbol in printlist:
        print(symbol, end=" ")
    print()
