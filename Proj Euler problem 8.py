a = ("73167176531330624919225"
"119674426574742355349194934969835203"
"1277450632623957831801698480186947885"
"1843858615607891129494954595017379583"
"3195285320880551112540698747158523863"
"0507156932909632952274430435576689664"
"8950445244523161731856403098711121722"
"3831136222989342338030813533627661428"
"2806444486645238749303589072962904915"
"6044077239071381051585930796086670172"
"4271218839987979087922749219016997208"
"8809377665727333001053367881220235421"
"8097512545405947522435258490771167055"
"6013604839586446706324415722155397536"
"9781797784617406495514929086256932197"
"8468622482839722413756570560574902614"
"0797296865241453510047482166370484403"
"1998900088952434506585412275886668811"
"6427171479924442928230863465674813919"
"1231628245861786645835912456652947654"
"5682848912883142607690042242190226710"
"5562632111110937054421750694165896040"
"8071984038509624554443629812309878799"
"2724428490918884580156166097919133875"
"4992005240636899125607176060588611646"
"7109405077541002256983155200055935729"
"7257163626956188267042825248360082325"
"7530420752963450")




product = 1
save = 0
list1 = []
list2 = []

for ab in range(0, len(a)-13):
    start = ab
    stop = ab+13
    check = a[start:stop]
    list1.append(check)

for c in list1:
    for b in c:
        product = product*int(b)
    list2.append(product)
    if product > save:
        save = product
        print('This is currently the largest product: ', product)
        product = 1
    else:
        product = 1

print(max(list2))