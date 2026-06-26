def detect_mutations(strand1, strand2):
    return [i for i in range(len(strand1)) if strand1[i] != strand2[i]]


print(detect_mutations("ATCG", "ATGG"))
print(detect_mutations("ATGCGTACGTTAGC", "ATGCATACGATTGC"))
print(detect_mutations("GATCTAGCTAGGCTAGCTAG", "GATCTAGCTAGGCTAGCTAG"))
