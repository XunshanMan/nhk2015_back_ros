NHK2015 ROS programs for back players
=================

# ロボットの動かし方

##PCの接続
グラナイトにG-Tune、Jr.にAlienwareを搭載する。
搭載後、各USBをPCに接続する。

- KinectとCANUSBはハブを介さず直接PCに接続する
- KinectはUSB3.0のコネクタにさす

## DualShock3の接続
ターミナルで

```Bash
sixad -start
```
として、コントローラのPSボタンを押す。

* BluetoothのドングルをUSBポートにあらかじめさしておくこと
* 赤いコントローラはグラナイト用、白いコントローラはJr.用

## ROSの起動
新しいターミナルで

```Bash
roscore
```

## プログラムの実行

1. センサーの電源(12V)を入れる
2. グラナイトのラケットを、中央上向きになるように手で合わせる(電源投入時、それがホームポジションとなる)
3. ロボットをフィールドにおいて、マイコンの電源を入れる
4. 以下のコマンドを使用し、プログラム実行

### グラナイトの場合

```Bash
roslaunch robominton robominton.launch
```

### Jr.の場合

```Bash
roslaunch robominton third.launch
```

コマンド実行時、赤いログが流れたら何らかのエラーが起きている。
Ctrl+Cでプログラムを停止し、エラー内容に従って各デバイスがコンピュータに正常に接続されていることを確認すること。

## プログラム実行後
緊急停止を解除し、駆動部に電源を供給する。 

* グラナイトのラケットが引き絞られ、自動で下向きに回転するはず。
* 引き絞られた後に下向きに回転しない時は、ラケット付近に付いているメイン基板のリセットスイッチを押す。

# トラブルシューティング
## 画面が固まった
1. Ctrl + Alt + F3
2. Ctrl + Alt + F7

これで直らなかったら強制再起動