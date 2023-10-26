# Fungsi untuk mengenkripsi teks menggunakan Vigenere Cipher
def vigenere_encrypt(text, key):
    encrypted_text = []
    key_len = len(key)
    key_index = 0
    for char in text:
        if char.isalpha():
            key_char = key[key_index % key_len]
            key_shift = ord(key_char) - ord('A')
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + key_shift) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
            key_index += 1
        else:
            encrypted_char = char
        encrypted_text.append(encrypted_char)

    # Teks dalam bentuk Vigenere Cipher
    vigenere_cipher_text = ''.join(encrypted_text)

    return vigenere_cipher_text, encrypted_text

# Fungsi untuk mendekripsi teks menggunakan Columnar Cipher dengan panjang kunci yang diinputkan
def columnar_decrypt(text, columnar_key_length):
    num_rows = len(text) // columnar_key_length
    if len(text) % columnar_key_length != 0:
        num_rows += 1
    num_columns = columnar_key_length
    matrix = [[''] * num_columns for _ in range(num_rows)]

    char_index = 0
    for row in range(num_rows):
        for col in range(num_columns):
            if char_index < len(text):
                matrix[row][col] = text[char_index]
                char_index += 1

    # Membuat kunci urutan kolom
    sorted_columns = sorted(range(num_columns))

    decrypted_text = ''
    for col in sorted_columns:
        for row in range(num_rows):
            decrypted_text += matrix[row][col]

    return decrypted_text, matrix

# Meminta pengguna memasukkan plaintext
original_text = input("Masukkan plaintext: ")

# Meminta pengguna memasukkan kunci Vigenere
vigenere_key = input("Masukkan kunci Vigenere: ")

# Hilangkan spasi dalam plain teks
original_text = original_text.replace(" ", "")

# Proses enkripsi menggunakan Vigenere Cipher
vigenere_cipher_text, _ = vigenere_encrypt(original_text, vigenere_key)

# Menampilkan hasil enkripsi dalam bentuk Vigenere Cipher
print("\nTeks Asli:", original_text)
print("Teks Terenkripsi (Vigenere Cipher):", vigenere_cipher_text)

# Panjang kunci Columnar Cipher adalah panjang kunci Vigenere
columnar_key_length = len(vigenere_key)

# Proses dekripsi menggunakan Columnar Cipher
columnar_decrypted_text, columnar_matrix = columnar_decrypt(vigenere_cipher_text, columnar_key_length)

# Menampilkan hasil dekripsi dan hasil matriks transposisi
print("Teks Terdekripsi (Columnar Cipher):", columnar_decrypted_text)
