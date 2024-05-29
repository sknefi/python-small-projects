import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_prime():
    while True:
        num = random.randint(100, 1000)
        if is_prime(num):
            return num


def generate_keypair():
    p = generate_prime()
    q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    # Brute force hladania klúča e
    e = 3
    while gcd(e, phi) != 1:
        e += 2

    # Výpočet súkromného klúča d pomocou Eulerovej vetzy
    d = pow(e, -1, phi)

    return ((e, n), (d, n))


def encrypt(public_key, plaintext):
    e, n = public_key
    return [pow(ord(char), e, n) for char in plaintext]


def decrypt(private_key, ciphertext):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])


def brute_force_attack(public_key, encrypted_message):
    e, n = public_key
    for possible_key in range(2, n):
        if n % possible_key == 0:
            p = possible_key
            q = n // possible_key
            phi = (p - 1) * (q - 1)
            d = pow(e, -1, phi)
            try:
                decrypted_message = decrypt((d, n), encrypted_message)
                return decrypted_message
            except:
                pass


# Testovanie
public_key, private_key = generate_keypair()
message = "Toto je RSA šifra - Kryptografia"
print("Pôvodna správa:", message)

encrypted_msg = encrypt(public_key, message)
print("Zakodovana správa:", encrypted_msg)

decrypted_msg = decrypt(private_key, encrypted_msg)
print("Dekodovana správa:", decrypted_msg)

# Testovanie prelomenia
print("Prelomená správa:", brute_force_attack(public_key, encrypted_msg))

print(ord('4'))