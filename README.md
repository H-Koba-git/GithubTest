# Python掛け算プログラム

シンプルな掛け算機能を持つPythonアプリケーション

## 🐍 プログラムの概要

このプロジェクトは、2つの数値を入力して掛け算を行うシンプルなPythonプログラムです。

### 機能
- 2つの数値の掛け算
- エラーハンドリング（不正な入力の検出）
- 小数対応
- 自動テスト

## 🚀 使用方法

### ローカルでの実行

```bash
# プログラムの実行
python multiply.py

# テストの実行
python test_multiply.py
```

### 実行例

```
=== 掛け算プログラム ===

1つ目の数を入力してください: 5
2つ目の数を入力してください: 3

計算結果: 5.0 × 3.0 = 15.0
```

## 🧪 テスト

プログラムには包括的なテストスイートが含まれています：

```bash
python test_multiply.py
```

### テスト内容
- 正の数の掛け算
- 負の数の掛け算
- ゼロとの掛け算
- 小数の掛け算

## 🔧 CI/CD パイプライン

このプロジェクトは GitHub Actions を使用した CI/CD パイプラインを実装しています。

### パイプラインの流れ

1. **テスト (Test)**
   - Python環境のセットアップ
   - 依存関係のインストール
   - ユニットテストの実行
   - コードの構文チェック

2. **ビルド (Build)**
   - 実行可能ファイルの準備
   - ビルド成果物の保存

3. **デプロイ (Deploy)**
   - GitHub Pages への自動デプロイ

### トリガー条件

- `main` ブランチへのプッシュ
- `develop` ブランチへのプッシュ
- `main` ブランチへのプルリクエスト

## 📁 ファイル構成

```
GithubTest/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # CI/CD ワークフロー
├── multiply.py                # メインプログラム
├── test_multiply.py           # テストファイル
├── requirements.txt           # 依存関係
└── README.md                  # このファイル
```

## 🛠️ 開発環境

### 必要な環境
- Python 3.9以上
- 標準ライブラリのみ使用（追加の依存関係なし）

### セットアップ

```bash
# リポジトリのクローン
git clone <repository-url>
cd GithubTest

# 依存関係のインストール（現在は不要）
# pip install -r requirements.txt

# プログラムの実行
python multiply.py
```

## 📝 ライセンス

MIT License

## 🤝 貢献

プルリクエストやイシューの報告を歓迎します！

