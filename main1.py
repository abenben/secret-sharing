import tss

print('[開始]')

filename = 'memo.txt'

# バイナリモードでPDFファイルを読み込む
with open(f'./input/' + filename, 'rb') as file:
    secret_data = file.read()

shares = tss.share_secret(2, 2, secret_data, 'secretid42', tss.Hash.SHA256)

for i, share in enumerate(shares):
    with open(f'./middle/share_{i}.bin', 'wb') as file:
        file.write(share)

loaded_shares = []
for i in range(2):
    with open(f'./middle/share_{i}.bin', 'rb') as file:
        loaded_shares.append(file.read())

# 秘密を回復
try:
    recovered_secret = tss.reconstruct_secret(loaded_shares)
    with open(f'./output/' + filename, 'wb') as file:
        file.write(recovered_secret)
    print('[正常終了]')
except tss.TSSError:
    print('秘密の回復に失敗しました')
