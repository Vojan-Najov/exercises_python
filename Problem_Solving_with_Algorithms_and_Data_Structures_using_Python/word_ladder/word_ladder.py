# run --> PYTHONPATH=$PYTHONPATH:graph:queue python3 word_ladder/word_ladder.py

from graph import Graph, bfs, traverse
import io

def buildGraph(wordFile):
    d = {}
    g = Graph()

    # create buckets of words that differ by one letter
    for line in wordFile:
        word = line.strip()
        for i in range(len(word)):
            bucket = f'{word[:i]}_{word[i + 1:]}'
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

        # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)

    return g


def main():
    wordfile = io.StringIO("FOOL\nPOOL\nPOLL\nPOLE\nPALE\nSALE\nSAGE\n")
    g = buildGraph(wordfile)
    bfs(g, g.getVertex('FOOL'))
    traverse(g.getVertex('SAGE'))


if __name__ == '__main__':
    main()
