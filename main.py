from pyscript import document
import random

#for _ in range(5):
 #   szam=random.randint(1,10)
   # document.querySelector("#kimenet").innerText+=str(szam)+"\n"
    
#def beolvas(event):
 #   felhasznalo = document.querySelector("#beviteli-mezo").value
  #  document.querySelector("#kimenet1").innerText = felhasznalo


def kivonas(event):
    eredmeny=document.getElementById("beviteli-mezo1").value - document.getElementById("beviteli-mezi2").value
