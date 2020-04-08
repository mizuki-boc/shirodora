import json

class shirodora_info():
    def __init__(self):
        with open("shirodora_data.json") as f:
            self.char_data = json.load(f)
        self.char_list = list(self.char_data.keys())

    def search_d1_getable_char(self, search_chars):
        d1_getable_char = []
        for ch_d1 in search_chars:
            if not self.char_data[ch_d1]["トロフィー"].keys():
                continue
            need_char = []
            for ch_d2 in list(self.char_data[ch_d1]["トロフィー"].keys()):
                for ch_d3 in self.char_data[ch_d1]["トロフィー"][ch_d2]:
                    need_char.append(ch_d3)
            if set(search_chars) >= set(need_char):
                d1_getable_char.append(ch_d1)
        return d1_getable_char

    def search_gbadge_getable_char(self, search_chars):
        gb_getable_char = []
        for ch_gb in search_chars:
            if not self.char_data[ch_gb]["金バッジ"].keys():
                continue
            need_char = []
            for ch_sb in list(self.char_data[ch_gb]["金バッジ"].keys()):
                for ch_bb in self.char_data[ch_gb]["金バッジ"][ch_sb]:
                    need_char.append(ch_bb)
            if set(search_chars) >= set(need_char):
                gb_getable_char.append(ch_gb)
        return gb_getable_char

    def search_rbadge_getable_char(self, search_chars):
        rb_getable_char = []
        for ch_rb in search_chars:
            if not self.char_data[ch_rb]["虹バッジ"].keys():
                continue
            need_gb = list(self.char_data[ch_rb]["虹バッジ"].keys())
            #print(need_gb)
            if set(self.search_gbadge_getable_char(search_chars)) >= set(need_gb):
                rb_getable_char.append(ch_rb)
        return rb_getable_char

if __name__ == "__main__":
    test = shirodora_info()
    #test.search_d1_getable_char("剣士")
    print(test.search_d1_getable_char(["バルーンガール"]))
