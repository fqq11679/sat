class CNF:
    def __init__(self, n_variables, clauses, occur_list, comments, weights, top_val):
        self.n_variables = n_variables
        self.clauses = clauses
        self.occur_list = occur_list
        self.comments = comments
        self.weights = weights
        self.top_val = top_val

    def __str__(self):
        return f"""Number of variables: {self.n_variables}
Clauses: {str(self.clauses)}
Comments: {str(self.comments)}
Weights: {str(self.weights)}
Top: {str(top_val)}"""

    def to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(self.to_string())

    def to_string(self):
        string = f'p wcnf {self.n_variables} {len(self.clauses)} {str(top_val)}\n'
        #for clause in self.clauses:
        for i in range(len(self.clauses)):
            string += self.weights[i] + ' ' + ' '.join(str(literal) for literal in self.clauses[i]) + ' 0\n'
        return string

    @classmethod
    def from_file(cls, filename):
        with open(filename) as f:
            return cls.from_string(f.read())

    @classmethod
    def from_string(cls, string):
        n_variables, clauses, occur_list, comments, weights, top_val  = CNF.parse_dimacs(string)
        return cls(n_variables, clauses, occur_list, comments, weights, top_val)

    @staticmethod
    def parse_dimacs(string):
        n_variables = 0
        top_val = 0
        clauses = []
        weights = []
        comments = []
        for line in string.splitlines():
            line = line.strip()
            if not line:
                continue
            elif line[0] == 'c':
                comments.append(line)
            elif line.startswith('p wcnf'):
                tokens = line.split()
                n_variables, n_remaining_clauses, top_val = int(tokens[2]), int(tokens[3]), int(tokens[4])
                occur_list = [[] for _ in range(n_variables * 2 + 1)]
            elif n_remaining_clauses > 0:
                weights.append(line.split()[0])
                clause = []
                clause_index = len(clauses)
                for literal in line.split()[1:-1]:
                    literal = int(literal)
                    clause.append(literal)
                    occur_list[literal].append(clause_index)
                clauses.append(clause)
                n_remaining_clauses -= 1
            else:
                break
        return n_variables, clauses, occur_list, comments, weights, top_val
