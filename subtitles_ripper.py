with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

timecodes = []
subtitles = []
current_subtitle = []

for line in lines:
    stripped_line = line.strip()

    if stripped_line.isdigit():  # 段落番号
        if current_subtitle:
            subtitles.append(''.join(current_subtitle).strip())
            current_subtitle = []
    elif '-->' in stripped_line:  # タイムコード
        timecodes.append(stripped_line)
    else:  # 字幕
        current_subtitle.append(stripped_line + ' ')

if current_subtitle:  # 最後の字幕を追加
    subtitles.append(''.join(current_subtitle).strip())

with open('timecode.txt', 'w', encoding='utf-8') as timecode_file:
    timecode_file.write('\n'.join(timecodes))

with open('subtitles.txt', 'w', encoding='utf-8') as subtitle_file:
    subtitle_file.write('\n\n'.join(subtitles))
