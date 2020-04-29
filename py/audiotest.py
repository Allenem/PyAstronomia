import winsound

# 音阶频率对应表
scale_frequency_dic = {
    'l1': 262,  'l2': 294,  'l3': 330,  'l4': 349,  'l5': 392,  'l6': 440,  'l7': 494,
    'm0': 37, 'm1': 523,  'm2': 587,  'm3': 659,  'm4': 698,  'm5': 784,  'm6': 880,  'm7': 988,
    'h1': 1046,  'h2': 1175,  'h3': 1318,  'h4': 1397,  'h5': 1568,  'h6': 1760,  'h7': 1967
}

# astronomia乐谱
notation_astronomia = [
    'm4', 'm4', 'm4', 'm4', 'm6', 'm6', 'm6', 'm6', 'm5', 'm5', 'm5', 'm5', 'h1', 'h1', 'h1', 'h1',
    'h2', 'h2', 'h2', 'h2', 'h2', 'h2', 'h2', 'h2', 'm5', 'm4', 'm3', 'm1', 'm2', 'm0', 'm2', 'm6',
    'm5', 'm0', 'm4', 'm0', 'm3', 'm0', 'm3', 'm3', 'm5', 'm0', 'm4', 'm3', 'm2', 'm0', 'm2', 'h4',
    'h3', 'h4', 'h3', 'h4', 'm2', 'm0', 'm2', 'h4', 'h3', 'h4', 'h3', 'h4', 'm2', 'm0', 'm2', 'm6',
    'm5', 'm0', 'm4', 'm0', 'm3', 'm0', 'm3', 'm3', 'm5', 'm0', 'm4', 'm3', 'm2', 'm0', 'm2', 'h4',
    'h3', 'h4', 'h3', 'h4', 'm2', 'm0', 'm2', 'h4', 'h3', 'h4', 'h3', 'h4',
    'm4', 'm4', 'm4', 'm4', 'm6', 'm6', 'm6', 'm6', 'm5', 'm5', 'm5', 'm5', 'h1', 'h1', 'h1', 'h1',
    'h2', 'h2', 'h2', 'h2', 'h2', 'h2', 'h2', 'h2', 'm5', 'm4', 'm3', 'm1', 'm2', 'm0', 'm2', 'm6',
    'm5', 'm0', 'm4', 'm0', 'm3', 'm0', 'm3', 'm3', 'm5', 'm0', 'm4', 'm3', 'm2', 'm0', 'm2', 'h4',
    'h3', 'h4', 'h3', 'h4', 'm2', 'm0', 'm2', 'h4', 'h3', 'h4', 'h3', 'h4', 'm2', 'm0', 'm2', 'm6',
    'm5', 'm0', 'm4', 'm0', 'm3', 'm0', 'm3', 'm3', 'm5', 'm0', 'm4', 'm3', 'm2', 'm0', 'm2', 'h4',
    'h3', 'h4', 'h3', 'h4', 'm2', 'm0', 'm2', 'h4', 'h3', 'h4', 'h3', 'h4', 'm2', 'm0', 'm2', 'm6'
]

# 生日快乐乐谱
notation_happybirthday = [
    'l5', 'l5', 'l6', 'l6', 'l5', 'l5', 'm1', 'm1', 'l7', 'l7', 'm0', 'm0',
    'l5', 'l5', 'l6', 'l6', 'l5', 'l5', 'm2', 'm2', 'm1', 'm1', 'm0', 'm0',
    'l5', 'l5', 'm5', 'm5', 'm3', 'm3', 'm1', 'm1', 'l7', 'l7', 'm6', 'm6',
    'm4', 'm4', 'm3', 'm3', 'm1', 'm1', 'm2', 'm2', 'm3', 'm3', 'm0', 'm0',

    'm5', 'm5', 'm6', 'm6', 'm5', 'm5', 'h1', 'h1', 'm7', 'm7', 'm0', 'm0',
    'm5', 'm5', 'm6', 'm6', 'm5', 'm5', 'h2', 'h2', 'h1', 'h1', 'm0', 'm0',
    'm5', 'm5', 'h5', 'h5', 'h3', 'h3', 'm1', 'm1', 'm7', 'm7', 'm6', 'm6',
    'h4', 'h4', 'h3', 'h3', 'h1', 'h1', 'h2', 'h2', 'h1', 'h1', 'm0', 'm0',
]

# 频率谱
frequency_list = []


# 乐谱转频率谱
def number2frequency(notation):
    for name in notation:
        if name in scale_frequency_dic.keys():
            frequency_list.append(scale_frequency_dic[name])
    # print(frequency_list)


if __name__ == '__main__':
    number2frequency(notation_astronomia)
    for frequency in frequency_list:
        # 播放频率frequency固定时间（单位ms），frequency must be in 37 thru 32767
        winsound.Beep(frequency, 500)
    frequency_list = []

    number2frequency(notation_happybirthday)
    for frequency in frequency_list:
        winsound.Beep(frequency, 500)
    frequency_list = []
