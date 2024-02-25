import pandas as pd

def encryption(key,plaintext):
    df = pd.read_csv('Vigenere_square.csv', index_col=0)
    row_label = str(key)
    column_label = str(plaintext)
    jene = df.loc[row_label, column_label]
    return jene

def main():
    print("鍵を入力してください。")
    input_key = list(input().upper())
    print("平文を入力してください。")
    input_plaintext = list(input().upper())

    key_len = len(input_key)
    plaintext_len = len(input_plaintext)

    n = 0
    result_list = []
    for i in range(plaintext_len):
        arg_key = input_key[n]
        arg_plaintext = input_plaintext[i]
        result_list.append(encryption(arg_key, arg_plaintext))
        n += 1
        if n == key_len:
            n = 0
    result_str = ''.join(result_list)
    print(result_str)

if __name__ == "__main__":
        main()