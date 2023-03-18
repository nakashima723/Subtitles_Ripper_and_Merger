# Subtitles_Ripper_and_Merger
SRTファイルを、翻訳しやすいように分割・結合するツールです。

<strong>使い方：</strong>

１．srtファイルの内容を、同じフォルダ内に「input.txt」として保存します。

２．コマンドプロンプトで作業フォルダをこのフォルダに設定し、「python subtitles_ripper.py」 を実行します。

３．input.txtの内容が、「timecode.txt」と「subtitle.txt」に分けて出力されます。

４．subtitle.txtのほうを自由に翻訳などしてください。段落（２連続改行）の数を変えないように注意してください。

５．「python subtitles_merger.py」 を実行します。出力された「merged.txt」が、統合された翻訳ずみファイルです。
