def find_s_algorithm(data):
    print("\n--- Find-S Algorithm ---")
    hypothesis = ['0'] * len(data[0][0])

    for attributes, label in data:
        if label == 'Yes':
            for i in range(len(hypothesis)):
                if hypothesis[i] == '0':
                    hypothesis[i] = attributes[i]
                elif hypothesis[i] != attributes[i]:
                    hypothesis[i] = '?'

    print("Final Hypothesis (Find-S):", hypothesis)
    return hypothesis


def more_general(h1, h2):
    return all(x == '?' or x == y for x, y in zip(h1, h2))


def candidate_elimination_algorithm(data):
    print("\n--- Candidate Elimination Algorithm ---")
    num_attributes = len(data[0][0])

    S = ['0'] * num_attributes
    G = [['?' for _ in range(num_attributes)]]

    for attributes, label in data:
        if label == 'Yes':
            G = [g for g in G if more_general(g, attributes)]
            for i in range(num_attributes):
                if S[i] == '0':
                    S[i] = attributes[i]
                elif S[i] != attributes[i]:
                    S[i] = '?'
        else:
            G_new = []
            for g in G:
                if more_general(g, attributes):
                    for i in range(num_attributes):
                        if g[i] == '?':
                            if S[i] != attributes[i] and S[i] != '?':
                                new_hypothesis = g[:]
                                new_hypothesis[i] = S[i]
                                if new_hypothesis not in G_new:
                                    G_new.append(new_hypothesis)
            G = G_new

    print("Final S (Specific Hypothesis):", S)
    print("Final G (General Hypotheses):", G)
    return S, G



dataset = [
    (['Young', 'High', 'No', 'Fair'], 'No'),
    (['Young', 'High', 'No', 'Excellent'], 'No'),
    (['Middle-aged', 'High', 'No', 'Fair'], 'Yes'),
    (['Senior', 'Medium', 'No', 'Fair'], 'Yes'),
    (['Senior', 'Low', 'Yes', 'Fair'], 'Yes'),
    (['Senior', 'Low', 'Yes', 'Excellent'], 'No'),
    (['Middle-aged', 'Low', 'Yes', 'Excellent'], 'Yes'),
    (['Young', 'Medium', 'No', 'Fair'], 'No'),
    (['Young', 'Low', 'Yes', 'Fair'], 'Yes'),
    (['Senior', 'Medium', 'Yes', 'Fair'], 'Yes'),
]


find_s_algorithm(dataset)
candidate_elimination_algorithm(dataset)
