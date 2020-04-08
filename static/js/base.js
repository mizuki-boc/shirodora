
function check_all(tf) {
  // var ElementsCount = document.char_c1.elements.length; // チェックボックスの数
  // すべてチェックされている場合 または いくつかチェックされている場合，全てチェックを外す
  // 全てチェックされていない場合，全てチェックする
  check_c1(tf)
  check_c2(tf)
  check_c3(tf)
  check_c4(tf)
  check_c5(tf)
  check_c7(tf)
}
function check_c1(tf) {
  for( i=0 ; i<document.all.char1.length ; i++ ) {
    document.all.char1[i].checked = tf; // ON・OFFを切り替え
  }
}
function check_c2(tf) {
  for( i=0 ; i<document.all.char2.length ; i++ ) {
    document.all.char2[i].checked = tf; // ON・OFFを切り替え
  }
}
function check_c3(tf) {
  for( i=0 ; i<document.all.char3.length ; i++ ) {
    document.all.char3[i].checked = tf; // ON・OFFを切り替え
  }
}
function check_c4(tf) {
  for( i=0 ; i<document.all.char4.length ; i++ ) {
    document.all.char4[i].checked = tf; // ON・OFFを切り替え
  }
}
function check_c5(tf) {
  for( i=0 ; i<document.all.char5.length ; i++ ) {
    document.all.char5[i].checked = tf; // ON・OFFを切り替え
  }
}
function check_c7(tf) {
  for( i=0 ; i<document.all.char7.length ; i++ ) {
    document.all.char7[i].checked = tf; // ON・OFFを切り替え
  }
}
