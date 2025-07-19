#!/usr/bin/env python3
"""
簡単な掛け算プログラム
"""

def multiply(a, b):
    """2つの数を掛け算する関数"""
    return a * b

def main():
    print("=== 掛け算プログラム ===")
    print()
    
    try:
        # ユーザーから入力を受け取る
        num1 = float(input("1つ目の数を入力してください: "))
        num2 = float(input("2つ目の数を入力してください: "))
        
        # 掛け算を実行
        result = multiply(num1, num2)
        
        # 結果を表示
        print()
        print(f"計算結果: {num1} × {num2} = {result}")
        
    except ValueError:
        print("エラー: 正しい数値を入力してください。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main() 