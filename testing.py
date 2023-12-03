import re

s = ["5seveneighteightzzbnzsvdjnkvndsxlttfour", "4five1"]
tr = ["zero", "one","two","three","four","five","six","seven", "eight","nine"]

for st in s:
    for t in tr:
        x = st.replace(t, str(tr.index(t))) if t in st else st
    s.remove(st)
    s.append(x)
    print(t, x)

print(s)
