files = ["seq1", "seq2", "seq3", "seq4"]
data = ("_09_12_26")
for name in files:

   new_name = name + data + ".fasta"

   print(f"{new_name}")