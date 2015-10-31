
m_en = {}
for line in open("../data/Mention_Entity_Count.dat"):
    m,e = line.strip("\n").strip("\r").split(":::")[:2]
    m_en[m] = m_en.get(m, [])+[e]

print "All:",len(m_en)
am = dict((k,v) for k,v in m_en.items() if len(v) > 1)
print "Has Ambiguation:",len(am)
print "Has 2 Ambiguation:",len([k for k,v in m_en.items() if len(v) == 2])
print "Has 3 Ambiguation:",len([k for k,v in m_en.items() if len(v) == 3])
print "Has 4 Ambiguation:",len([k for k,v in m_en.items() if len(v) == 4])
print "Has 5 Ambiguation:",len([k for k,v in m_en.items() if len(v) == 5])
print "Has more than 5 Ambiguation:",len([k for k,v in m_en.items() if len(v) > 5])

with open("../data/Mention_Entity_Ambi.dat","w") as f:
    for k,v in am.items():
        f.write(k)
        for vv in v:
            f.write(":::"+vv)
        f.write("\n")


    
        
