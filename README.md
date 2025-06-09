# Todoデスクトップアプリ

このプロジェクトは、Flaskをバックエンド、Electronをフロントエンドとして使用するシンプルなToDoアプリケーションを、Windows向けのデスクトップアプリケーションとして実装しています。

## 内容

- **base.py**: ToDoアプリケーションの機能を処理するFlaskバックエンドサーバーです。
- **requirements.txt**: Flaskバックエンド用のPython依存パッケージを記載しています。
- **package.json**: Electron用のNodeプロジェクトの設定ファイルです。
- **main.js**: Electronのメインプロセスファイルで、Flaskバックエンド（base.py）を起動し、デスクトップウィンドウを作成します。

## 依存パッケージ

### Python依存

- Flask
- flask-cors

これらは `requirements.txt` に記載されています。

### Node依存

- Electron (バージョン ^23.0.0)

これらは、`package.json` の `devDependencies` に記載されています。

## インストール方法

### Python環境のセットアップ

1. （任意）仮想環境の作成:
   ```bash
   python -m venv venv
   ```
2. 仮想環境の有効化:
   - Windowsの場合:
     ```bash
     venv\\Scripts\\activate
     ```
   - Unix/Macの場合:
     ```bash
     source venv/bin/activate
     ```
3. Python依存パッケージのインストール:
   ```bash
   pip install -r requirements.txt
   ```

### Node環境のセットアップ

1. [Node.js](https://nodejs.org/) をインストールしてください（未インストールの場合）。
2. Node依存パッケージのインストール:
   ```bash
   npm install
   ```

## アプリケーションの起動方法

### Electronを用いたデスクトップアプリとしての起動

1. Python依存パッケージがインストールされていることを確認してください（上記のPython環境のセットアップを参照）。
2. 以下のコマンドでElectronアプリケーションを起動します:
   ```bash
   npm start
   ```
   これにより、Flaskサーバー（`base.py`を経由）が起動し、ElectronウィンドウによりToDoアプリが [http://127.0.0.1:51140](http://127.0.0.1:51140) で表示されます。

### Flaskのみを使用してウェブサーバーとしての起動

Flaskサーバーのみを起動する場合は、以下のコマンドを実行してください:
   ```bash
   python base.py
   ```
その後、ブラウザで [http://127.0.0.1:51140](http://127.0.0.1:51140) にアクセスします。

## トラブルシューティング

- すべてのPython依存パッケージが正しくインストールされていることを確認してください。
- `python base.py` を実行して、ブラウザでサーバーにアクセスできるか確認してください。

## 配布用パッケージの作成

Windows向けのデスクトップ実行可能ファイルを作成する場合は、以下のツールを検討してください:
- [Electron Packager](https://github.com/electron/electron-packager)
- [Electron Builder](https://www.electron.build/)

これらのツールを利用することで、Pythonバックエンドを含むアプリケーション全体をスタンドアロンの実行可能ファイルにパッケージ化できます。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。
