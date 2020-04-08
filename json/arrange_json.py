import json
"""
#標準形式
a = {
"char1":{
    "trophy": {
        "char2": ["char3", "char4"],
        "char5": ["char6", "char7"]
    },
    "badge": {
        "ch1": {
            "ch2": ["ch3", "ch4"],
            "ch5": ["ch6"]
        },
        "ch7": {
            "ch8": ["ch9"],
            "ch0": ["ch1"]
        }
    },
    "img": "~~~~.png"
}
}
"""
tmp = {}
with open("shirodora_trophy_2.json") as f:
    trophy = json.load(f)
with open("shirodora_char_info.json") as f2:
    char_img = json.load(f2)
char_list = list(char_img.keys())
#print(char_list[0])
for ch in char_list:
    #tmp[ch]["トロフィー"] = trophy[ch].keys()
    tmp[ch] = {}
    tmp[ch]["img"] = char_img[ch]["img"]
    try:
        for d2 in list(trophy[ch].keys()):
            tmp[ch]["トロフィー"] = trophy[ch]
    except:
        tmp[ch]["トロフィー"] = {}
    #print(trophy[ch])

with open("newfile.json", mode="w") as f3:
    json.dump(tmp, f3, ensure_ascii=False, indent=4, sort_keys=False, separators=(',', ': '))
