def pattern_count(text, pattern):
    count = 0

    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            count = count + 1
    return count


def frequency_map(text, k):
    freq_map = {}
    n = len(text)

    for i in range(n-k+1):
        key = text[i:i+k]
        freq_map[key] = 0
    for i in range(n-k+1):
        key = text[i:i+k]
        freq_map[key] = freq_map[key]+1
    return freq_map


def frequent_words(text, k):
    freq_words = []
    freq_map = frequency_map(text, k)
    maximum = max(freq_map.values())

    for key in freq_map:
        if freq_map[key] == maximum:
            freq_words.append(key)
    return freq_words


def reverse(pattern):
    rev = ""

    for character in pattern:
        rev = character + rev
    return rev


def complement(pattern):
    comp = ""

    for character in pattern:
        if character == "A":
            comp += "T"
        if character == "T":
            comp += "A"
        if character == "G":
            comp += "C"
        if character == "C":
            comp += "G"
    return comp


def reverse_complement(pattern):
    return reverse(complement(pattern))


def pattern_matching(pattern, genome):
    starting_positions = []

    for i in range(len(genome)-len(pattern)+1):
        if genome[i:i+len(pattern)] == pattern:
            starting_positions.append(i)
    return starting_positions


def symbol_array(genome, symbol):
    array = {}
    n = len(genome)
    extended_genome = genome+genome[0:(n//2)]

    for i in range(n):
        array[i] = pattern_count(extended_genome[i:i+(n//2)], symbol)
    return array


def faster_symbol_array(genome, symbol):
    n = len(genome)
    extended_genome = genome+genome[0:(n//2)]
    array = {0: pattern_count(extended_genome[0:(n//2)], symbol)}

    for i in range(1, n):
        array[i] = array[i-1]

        if extended_genome[i-1] == symbol:
            array[i] -= 1
        if extended_genome[i+(n//2)-1] == symbol:
            array[i] += 1
    return array


def skew_array(genome):
    skew = [0]

    for i in range(len(genome)):
        if genome[i] == "G":
            skew.append(skew[i]+1)
        elif genome[i] == "C":
            skew.append(skew[i]-1)
        else:
            skew.append(skew[i])
    return skew


def minimum_skew(genome):
    positions = []
    skew = skew_array(genome)

    for i in range(1, len(skew)):
        if i == 1:
            minimum = skew[i]
        else:
            minimum = min(minimum, skew[i])
    for i in range(1, len(skew)):
        if minimum == skew[i]:
            positions.append(i)
    return positions


def hamming_distance(str1, str2):
    mismatch = 0

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            mismatch += 1
    return mismatch


def approximate_pattern_matching(text, pattern, d):
    starting_positions = []

    for i in range(len(text)-len(pattern)+1):
        if hamming_distance(pattern, text[i:i+len(pattern)]) <= d:
            starting_positions.append(i)
    return starting_positions


def approximate_pattern_count(pattern, text, d):
    count = 0

    for i in range(len(text)-len(pattern)+1):
        if hamming_distance(pattern, text[i:i+len(pattern)]) <= d:
            count += 1
    return count

