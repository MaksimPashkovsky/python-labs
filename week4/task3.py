"""
FASTA-парсер
"""

from dataclasses import dataclass


@dataclass
class Sequence:

    id: str
    description: str
    sequence_as_string: str


class FastaParser:

    @staticmethod
    def parse_by_parts(file) -> Sequence:
        """
        Parse a .fasta file by parts.
        Useful for big input files.
        """
        string = iden = desc = ""
        is_first_line = True
        row = file.readline()
        while row:
            if row[0] == '>':
                if not is_first_line:
                    yield Sequence(iden, desc, string)
                    string = ""
                is_first_line = False
                iden, desc = row[1:].replace('\n', '').split(' ', 1)
            else:
                string += row.replace('\n', '')
            row = file.readline()
        yield Sequence(iden, desc, string)

    @staticmethod
    def parse_at_once(file) -> list[Sequence]:
        """
        Parse a .fasta file at once.
        Not recommended for big input files.
        """
        sequences = list()
        parts = file.read().split('>')
        for part in parts[1:]:
            name, *desc, seq = part.replace('\n', ' ', 1).split(' ')
            sequences.append(Sequence(name, " ".join(desc), seq.replace('\n', '')))
        return sequences


if __name__ == '__main__':
    with open(r'week4\abcd.fasta') as fasta_file1:
        seqs = FastaParser.parse_at_once(fasta_file1)
    print(seqs[0])

    with open(r'week4\abcd.fasta') as fasta_file2:
        gen = FastaParser.parse_by_parts(fasta_file2)
        a = next(gen)
        print(a)
