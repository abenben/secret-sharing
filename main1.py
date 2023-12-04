import tss

# 秘密をファイルから読み込む
with open('./input/memo.txt', 'r') as file:
    secret_data = file.read()

# 秘密を分割
shares = tss.share_secret(2, 2, secret_data, 'secretid42', tss.Hash.SHA256)

# 分割された秘密を個別のファイルに保存（バイナリモードで開く）
for i, share in enumerate(shares):
    with open(f'./middle/share_{i}.bin', 'wb') as file:  # 'wb' を使用してバイナリモードで開く
        file.write(share)

# 分割された秘密をファイルから読み込む（バイナリモードで読み込む）
loaded_shares = []
for i in range(2):  # 2つの分割ファイルを読み込む
    with open(f'./middle/share_{i}.bin', 'rb') as file:  # 'rb' を使用してバイナリモードで読み込む
        loaded_shares.append(file.read())

# 秘密を回復
try:
    recovered_secret = tss.reconstruct_secret(loaded_shares)
    with open(f'./output/memo.txt', 'wb') as file:  # 'wb' を使用してバイナリモードで開く
        file.write(recovered_secret)
except tss.TSSError:
    pass  # エラー処理
