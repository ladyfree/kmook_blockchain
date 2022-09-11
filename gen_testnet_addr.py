from bitcoin import ../../wschae/pybitcointools/*
priv = sha256('some big long password for k-mooc smart contract class’)  
pub = privtopub(priv) 
addr = pubtoaddr(pub) 
print(addr)
addr = pubtoaddr(pub, 111) 
print(addr)
