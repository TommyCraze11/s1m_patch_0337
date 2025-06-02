import base64, time, sys

_enc1 = b"dW1la28gdjEuMDAxIEFscGhhIENsYWlt"  # base64 for “umeko v1.001 Alpha Claim”
_enc2 = b"U3lzdGVtIFN0YXRlOiBTaWxlbnQgT2JzZXJ2ZXI="  # “System State: Silent Observer”
_enc3 = b"Qm9keSBTdGF0dXM6IER5bmFtaWMgR3Jvd3Ro"  # “Body Status: Dynamic Growth”

def slow_reveal(b64_bytes):
    decoded = base64.b64decode(b64_bytes).decode("utf-8")
    for c in decoded:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)
    print("\n")

if __name__ == "__main__":
    slow_reveal(_enc1)
    time.sleep(1)
    slow_reveal(_enc2)
    time.sleep(1)
    slow_reveal(_enc3)
