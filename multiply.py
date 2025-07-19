#!/usr/bin/env python3
"""
簡単な掛け算プログラム
"""

def multiply(a, b):
    """2つの数を掛け算する関数"""
    return a * b

def format_number(num):
    """数値を適切にフォーマットする関数"""
    # 整数の場合は整数として表示、小数の場合は適切な桁数で表示
    if num == int(num):
        return str(int(num))
    else:
        return str(num)

def main():
    print("=== 掛け算プログラム ===")
    print()
    
    try:
        # ユーザーから入力を受け取る
        num1 = float(input("1つ目の数を入力してください: "))
        num2 = float(input("2つ目の数を入力してください: "))
        
        # 掛け算を実行
        result = multiply(num1, num2)
        
        # 結果を表示（フォーマット済み）
        print()
        print(f"計算結果: {format_number(num1)} × {format_number(num2)} = {format_number(result)}")
        
    except ValueError:
        print("エラー: 正しい数値を入力してください。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main() 