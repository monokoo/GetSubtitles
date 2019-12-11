import os
import chardet
import codecs

def WriteFile(filePath, lines, encoding="utf-8"):
    with codecs.open(filePath, "w", encoding) as f:
        actionR = '' #定位到[Events]区域的标记
        for sline in lines:
            if '[Events]' in sline:
                actionR = 'ok'
                f.write(sline)
                continue
            if actionR == 'ok':
                f.write(sline.replace(
                    'Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding',\
                    'Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text'))
                actionR = ''
                print("├  已为Emby改善字幕兼容性")
            else:
                f.write(sline)


def CONV_UTF8(src, dst):
    # 检测编码，coding可能检测不到编码，有异常
    f = open(src, "rb")
    coding = chardet.detect(f.read())["encoding"]
    f.close()
    # if coding != "utf-8":
    with codecs.open(src, "r", coding) as f:
        try:
            WriteFile(dst, f.readlines(), encoding="utf-8")
        except Exception:
            print(src + "  " + coding + "  read error")

if __name__ == "__main__":
    filename="the.walking.dead.s10e05.1080p.web.h264-xlf.zh.ass"
    CONV_UTF8(filename,filename)
