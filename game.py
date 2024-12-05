import socket
import random
from network import Network
opt={"1":"Stone","2":"Paper","3":"Scissor"}
print("Enter 1 for Stone\n2 for Paper\n3 for Scissor")

def main():
    player=0
    opponent=0
    opp=Network()
    print(opp.recv())
    message=opp.recv()
    while message=="Connected":
        
        x=input("Enter: ")
        if(x=="4"):
            opp.close()
            break
        else:
            rand=opp.send(x)
            
            print("Opponent:",opt[rand])
            print("Our:",opt[x])
            if(opt[x]=="Stone" and opt[rand]=="Scissor" or opt[x]=="Paper" and opt[rand]=="Stone" or opt[x]=="Scissor" and opt[rand]=="Paper"):
                player =player+1
            elif(opt[rand]=="Stone" and opt[x]=="Scissor" or opt[rand]=="Paper" and opt[x]=="Stone" or opt[rand]=="Scissor" and opt[x]=="Paper"):
                opponent= opponent+1
        
    print("You:",player)
    print("Opponent:",opponent)
main()
    