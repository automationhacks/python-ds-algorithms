from data_structures.graph.graph import Graph


def build_word_ladder_graph(words_file):
    buckets = {}
    word_graph = Graph()

    with open(words_file) as file:
        for line in file:
            # Remove CRLF chars
            word = line[:-1]

            # For every word, construct a bucket, if bucket exists, then
            # add word to list
            for i in range(len(word)):
                bucket = f'{word[:i]}_{word[i + 1:]}'
                if bucket in buckets:
                    buckets[bucket].append(word)
                else:
                    buckets[bucket] = [word]

    # For every bucket, make edges between all words in each bucket
    for bucket in buckets.keys():
        for word in buckets[bucket]:
            for other_word in buckets[bucket]:
                if word != other_word:
                    word_graph.add_edge(word, other_word)

    return word_graph
