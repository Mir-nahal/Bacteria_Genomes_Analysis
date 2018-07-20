from Bio import SeqIO
import os
from hash import hash

prime = 2147483647 #16 bit
count = [0 for i in range(prime)]


def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))


def process(sequence, seg_size, h):
    segs = list(chunkstring(sequence, seg_size))
    print(len(segs))
    for seg in segs:
        # print(seg)
        count[h.calc(seg)] += 1
    return


if __name__ == '__main__':
    counter = 0
    values = {'A': 0, 'a': 0, 'C': 1, 'c': 1, 'G': 2, 'g': 2, 'T': 3, 't': 3}
    h = hash(values, prime)
    directory = '../Bacteria_whole_genome_db/GbBac'
    # filename = '../Bacteria_whole_genome_db/GbBac/GCF_000005825.2_ASM582v2_genomic.fna'

    for filename in os.listdir(directory):
        counter += 1
        print(filename)
        if filename.endswith(".fna"):
            fasta_sequences = SeqIO.parse(open(os.path.join(directory, filename)), 'fasta')

            for fasta in fasta_sequences:
                name, sequence = fasta.id, str(fasta.seq)
                print(name)
                process(sequence, 100, h)
        if counter > 0:
            break

    s = set(count)
    s_l = {i: 0 for i in s}

    f = open("raw_result.txt", "w+")
    for number in count:
        f.write(str(number))
        f.write('\n')
        s_l[number] = s_l.get(number) + 1
    f.close()

    f = open("result.txt", "w+")
    for number in s_l.keys():
        f.write(str(number) + " " + str(s_l.get(number)))
        f.write('\n')

    f.close()

