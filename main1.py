import tss
shares = tss.share_secret(2, 2, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'secretid42',
                          tss.Hash.SHA256)

for share in shares:
    print(share)

try:
    # Recover the secret value
    secret = tss.reconstruct_secret(shares)
    print(secret)
except tss.TSSError:
    pass  # Handling error