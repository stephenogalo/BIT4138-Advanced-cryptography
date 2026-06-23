"""
Diffie-Hellman Key Exchange Implementation
==========================================
A demonstration of the Diffie-Hellman key exchange protocol where two parties
(Alice and Bob) can establish a shared secret over an insecure channel.
"""

import random


# ── Helpers ────────────────────────────────────────────────────────────────────

def is_prime(n: int) -> bool:
    """Miller-Rabin primality test (deterministic for n < 3,317,044,064,679,887,385,961,981)."""
    if n < 2:
        return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    if n in small_primes:
        return True
    if any(n % p == 0 for p in small_primes):
        return False

    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for a in small_primes:
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def validate_inputs(p: int, g: int) -> None:
    """Validate that p is prime and g is a valid primitive root candidate."""
    if p < 2:
        raise ValueError(f"p={p} must be ≥ 2.")
    if not is_prime(p):
        raise ValueError(f"p={p} is not prime. Please choose a prime number.")
    if g < 2 or g >= p:
        raise ValueError(f"g={g} must satisfy 2 ≤ g < p (p={p}).")


def generate_private_key(p: int) -> int:
    """Return a random private key in [2, p-2]."""
    return random.randint(2, p - 2)


# ── Core DH functions ──────────────────────────────────────────────────────────

def generate_public_key(g: int, private_key: int, p: int) -> int:
    """Compute public key: g^private_key mod p."""
    return pow(g, private_key, p)


def compute_shared_secret(other_public_key: int, private_key: int, p: int) -> int:
    """Compute shared secret: other_public_key^private_key mod p."""
    return pow(other_public_key, private_key, p)


# ── Display helpers ────────────────────────────────────────────────────────────

def separator(char: str = "─", width: int = 60) -> str:
    return char * width


def header(title: str) -> None:
    print(f"\n{'═' * 60}")
    print(f"  {title}")
    print(f"{'═' * 60}")


def section(title: str) -> None:
    print(f"\n  {separator()}")
    print(f"  {title}")
    print(f"  {separator()}")


# ── Main exchange ──────────────────────────────────────────────────────────────

def run_key_exchange(
    p: int,
    g: int,
    alice_private: int | None = None,
    bob_private: int | None = None,
) -> dict:
    """
    Execute a full Diffie-Hellman key exchange.

    Parameters
    ----------
    p             : Prime modulus (public).
    g             : Generator / primitive root (public).
    alice_private : Alice's private key (auto-generated if None).
    bob_private   : Bob's private key (auto-generated if None).

    Returns
    -------
    dict with all exchange values.
    """
    validate_inputs(p, g)

    # Private keys
    a = alice_private if alice_private is not None else generate_private_key(p)
    b = bob_private   if bob_private   is not None else generate_private_key(p)

    # Public keys
    A = generate_public_key(g, a, p)   # Alice's public key
    B = generate_public_key(g, b, p)   # Bob's public key

    # Shared secrets
    secret_alice = compute_shared_secret(B, a, p)
    secret_bob   = compute_shared_secret(A, b, p)

    return {
        "p": p, "g": g,
        "alice_private": a, "bob_private": b,
        "alice_public":  A, "bob_public":  B,
        "secret_alice":  secret_alice,
        "secret_bob":    secret_bob,
        "match":         secret_alice == secret_bob,
    }


def display_exchange(result: dict) -> None:
    """Pretty-print the full key exchange."""
    header("Diffie-Hellman Key Exchange")

    section("① Public Parameters  (shared openly)")
    print(f"     Prime modulus  p = {result['p']}")
    print(f"     Generator      g = {result['g']}")

    section("② Private Keys  (kept secret)")
    print(f"     Alice's private key  a = {result['alice_private']}")
    print(f"     Bob's   private key  b = {result['bob_private']}")

    section("③ Public Keys  (exchanged openly)")
    print(f"     Alice sends  A = g^a mod p = {result['alice_public']}")
    print(f"     Bob   sends  B = g^b mod p = {result['bob_public']}")

    section("④ Shared Secret Computation")
    print(f"     Alice computes  s = B^a mod p = {result['secret_alice']}")
    print(f"     Bob   computes  s = A^b mod p = {result['secret_bob']}")

    section("⑤ Verification")
    if result["match"]:
        print("     ✅  Both parties derived the SAME shared secret!")
        print(f"         Shared secret = {result['secret_alice']}")
    else:
        print("     ❌  ERROR: Secrets do not match — check your inputs.")

    print(f"\n{'═' * 60}\n")


# ── Interactive mode ───────────────────────────────────────────────────────────

def prompt_int(prompt: str, min_val: int | None = None) -> int:
    while True:
        try:
            val = int(input(prompt))
            if min_val is not None and val < min_val:
                print(f"    Value must be ≥ {min_val}. Try again.")
                continue
            return val
        except ValueError:
            print("    Please enter a valid integer.")


def interactive_mode() -> None:
    print("\n╔══════════════════════════════════════════════════════════╗")
    print("║      Diffie-Hellman Key Exchange — Interactive Mode      ║")
    print("╚══════════════════════════════════════════════════════════╝\n")

    print("  Enter the shared public parameters:")
    while True:
        p = prompt_int("    Prime modulus p : ", min_val=2)
        if is_prime(p):
            break
        print(f"    {p} is not prime. Please choose a prime number.")

    g = prompt_int(f"    Generator g (2 ≤ g < {p}) : ", min_val=2)

    print("\n  Enter private keys (or press Enter to auto-generate):")

    def optional_private(name: str) -> int | None:
        raw = input(f"    {name}'s private key (blank = random) : ").strip()
        if not raw:
            return None
        try:
            val = int(raw)
            if 2 <= val <= p - 2:
                return val
            print(f"    Key must be in [2, {p-2}]. Generating randomly.")
        except ValueError:
            print("    Invalid input. Generating randomly.")
        return None

    alice_priv = optional_private("Alice")
    bob_priv   = optional_private("Bob")

    try:
        result = run_key_exchange(p, g, alice_priv, bob_priv)
        display_exchange(result)
    except ValueError as e:
        print(f"\n  ❌  Input error: {e}\n")


# ── Demo ───────────────────────────────────────────────────────────────────────

def demo() -> None:
    """Run three preset examples."""
    examples = [
        {"label": "Small / textbook example",
         "p": 23,  "g": 5,  "a": 6,  "b": 15},
        {"label": "Medium example",
         "p": 997, "g": 7,  "a": 123, "b": 456},
        {"label": "Large example (2048-bit-style prime truncated for demo)",
         "p": 7919, "g": 2, "a": None, "b": None},
    ]

    for ex in examples:
        print(f"\n  ── Demo: {ex['label']} ──")
        result = run_key_exchange(ex["p"], ex["g"], ex.get("a"), ex.get("b"))
        display_exchange(result)


# ── Entry point ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        demo()
    else:
        interactive_mode()