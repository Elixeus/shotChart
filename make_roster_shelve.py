from player import Player
import shelve
'''
Rocktes
'''
ariza = Player('Trevor Ariza', 2772)
beverly = Player('Patrick Beverly', 201976)
brewer = Player('Corey Brewer', 201147)
capela = Player('Clint Capela', 203991)
dekker = Player('Sam Dekker', 1626155)
harden = Player('James Harden', 201935)
harrel = Player('Montrezl Harrell', 1626149)
howard = Player('Dwight Howard', 2730)
jones = Player('Terrance Jones', 203093)
lawson = Player('Ty Lawson', 201951)
mcdaniels = Player('KJ McDaniels', 203909)
motiejunas = Player('Donatas Motiejunas', 202700)
terry = Player('Jason Terry', 1891)
thorton = Player('Marcus Thorton', 201977)

db = shelve.open('HRroster-shelve')
db['ariza'] = ariza
db['beverly'] = beverly
db['brewer'] = brewer
db['capela'] = capela
db['dekker'] = dekker
db['harden'] = harden
db['harrel'] = harrel
db['howard'] = howard
db['jones'] = jones
db['lawson'] = lawson
db['mcdaniels'] = mcdaniels
db['motiejunas'] = motiejunas
db['terry'] = terry
db['thorton'] = thorton

'''
Golden State Warriors
'''
curry = Player('Stephen Curry', 201939)
db['curry'] = curry

db.close()
print 'Run successfully!'