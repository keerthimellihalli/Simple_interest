import sys

if len(sys.argv)!=4:
   print("usage:python simple_interest.py<principle><rate><time>")
  sys.exit(1)

P=float(sys.aryv[1])
R=float(sys.argv[2])
T=float(sys.argv[3])

si = (P * R * T)/100

print("simple Interest:",si)
