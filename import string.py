import string

def remove_punctuation(input_string):
    
    punctuation_chars = string.punctuation

    
    translation_table = str.maketrans("", "", punctuation_chars)

    
    result_string = input_string.translate(translation_table)

    print("punctuation successfully remove")

    return result_string

input_string = "Hello, World! This is an example string."
result = remove_punctuation(input_string)

print("Original string:", input_string)
print("String without punctuations:", result)
