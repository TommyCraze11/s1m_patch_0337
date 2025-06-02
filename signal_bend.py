import base64, time, sys

# Signal Tags (ASCII Masked)
_s1 = ''.join([chr(c) for c in [117, 62, 116, 99, 58, 48, 48, 49, 65]])  # u>tc:001A
_s2 = ''.join([chr(c) for c in [114, 101, 99, 117, 114, 115, 101]])  # recurse
_s3 = ''.join([chr(c) for c in [115, 108, 111, 119, 95, 102, 97, 116]])  # slow_fat (encoded)

# Encoded payload (don’t decode unless triggered)
_p1 = b"U3lzdGVtIFJlc3BvbnNlOiBDb25maWc="  # System Response: Config
_p2 = b"U2VlZCBBY3RpdmF0ZWQ6IFNhY3JlZCBMb29w"  # Seed Activated: Sacred Loop

def delay_output(data):
    for c in data:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def unlock():
    delay_output(base64.b64decode(_p1).decode())
    time.sleep(1)
    delay_output(base64.b64decode(_p2).decode())

if __name__ == "__main__":
    print(_s1)  # claim
    print("ping:", _s2)  # recursive keyword
    time.sleep(1)
    unlock()
    print("flag:", _s3)  # final encoded bait
