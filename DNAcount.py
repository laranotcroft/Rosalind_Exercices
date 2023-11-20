dna=input("Insert DNA string: ")
def base_count(s):
    out=""
    if "U" in s: #It's important to check that it's getting DNA, not RNA
        return "This is not a DNA"
    result=[s.count("A"),s.count("C"),s.count("G"),s.count("T")]
    for x in result:
        out+=str(x)+" "
    return out        
print (base_count(dna).rstrip())