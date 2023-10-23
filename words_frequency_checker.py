# Parse text, count the number of occurences of each word, put them as list of tuples

input_text = """
It is a long established fact that a
 reader will be distracted by the
 readable content of a page when
 looking at its layout. The point of
 using Lorem Ipsum is that it has a more-or-less normal distribution of letters,
 as opposed to using 'Content here, content here', making it look like readable English.
 Many desktop publishing packages and web page editors now use Lorem Ipsum as their default
 model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy.
  Various versions have evolved over the years, sometimes by accident, sometimes on purpose
  (injected humour and the like).
"""
# output - [('The', 20), ('to', 10)] or {'The': 20, 'it': 10}

words_frequency_counter = {}
for each_word in input_text.split(' '):
    clean_key = each_word.strip().replace("\n", "")
    if clean_key in words_frequency_counter.keys():
        words_frequency_counter[clean_key] += 1
    else:
        words_frequency_counter[clean_key] = 1
print(f"frequency counter : {words_frequency_counter}")
