# ファイル名: firstPython.py
# 作成者: 櫻井正樹
# 作成日: 2024年12月2日
#
# 説明:
# このPythonファイルは、基本的な挨拶を表示するプログラムです。
#
# テスト項目:
# 1. 挨拶メッセージが正しく表示されるか確認

from datetime import datetime
import pytz

def greet():
    jst = pytz.timezone('Asia/Tokyo')
    current_time = datetime.now(jst)
    print("こんにちは。Pythonです。")
    print(f"現在の日時: {current_time.strftime('%Y年%m月%d日 %H:%M:%S JST')}")

greet()