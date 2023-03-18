with open('timecode.txt', 'r', encoding='utf-8') as timecode_file:
    timecodes = timecode_file.read().splitlines()

with open('subtitles.txt', 'r', encoding='utf-8') as subtitle_file:
    subtitles = subtitle_file.read().split('\n\n')

with open('merged.txt', 'w', encoding='utf-8') as merged_file:
    for index, (timecode, subtitle) in enumerate(zip(timecodes, subtitles), start=1):
        merged_file.write(str(index) + "\n" + timecode + "\n" + subtitle + "\n\n")
