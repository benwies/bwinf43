import ListeAktionen as la
import ListeBloecke as lb 

liste = la.ListeAktionen()
blöcke = lb.ListBlocks()
blöcke.addBlock(1)
blöcke.addBlock(1)
blöcke.addBlock(1)
blöcke.addBlock(1)
blöcke.printList()

blöcke.checkStatusFromTo(0,3,1)