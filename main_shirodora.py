# coding: utf-8
from flask import Flask, render_template, request, session, url_for, redirect
import json

import func_shirodora
import key

app = Flask(__name__)
app.secret_key = key.SECRET_KEY

info = func_shirodora.shirodora_info()

@app.route("/")
def index():
    #all_chars = info.char_list
    #print(session["checked_chars"])
    if "checked_chars" in session:
        checked_chars = session["checked_chars"]
    else:
        checked_chars = []
    #return render_template("index.html")
    return render_template("index.html",
                            chars_info=info.char_data,
                            checked_chars=checked_chars,)

@app.route("/result", methods=["POST"])
def result():
    #session["checked_chars"] = request.form.getlist("char")
    form_char_list = []
    for ch in ["char1", "char2", "char3", "char4", "char5", "char7"]:
        form_char_list = form_char_list + request.form.getlist(ch)
    session["checked_chars"] = form_char_list
    print(session["checked_chars"])
    #print(info.search_rbadge_getable_char(session["checked_chars"]))
    #print(info.search_gbadge_getable_char(session["checked_chars"]))
    max_len = max(len(info.search_d1_getable_char(session["checked_chars"])),
                len(info.search_rbadge_getable_char(session["checked_chars"])),
                len(info.search_gbadge_getable_char(session["checked_chars"])))
    return render_template("trophy_result.html",
                            chars_info=info.char_data,
                            d1_getable_chars=info.search_d1_getable_char(session["checked_chars"]),
                            rb_getable_chars=info.search_rbadge_getable_char(session["checked_chars"]),
                            gb_getable_chars=info.search_gbadge_getable_char(session["checked_chars"]),
                            max_len=max_len)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8888, threaded=True)
