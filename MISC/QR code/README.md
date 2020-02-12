# QR code
Category: `MISC`

Do you remember something known as QR Code? Simple. Here for you :
 
https://mega.nz/#!eGYlFa5Z!8mbiqg3kosk93qJCP-DBxIilHH2rf7iIVY-kpwyrx-0

## Write-up
透過題目連結，取得QR code
![QR code](https://github.com/Offliners/CTFlearn-writeup/blob/master/MISC/QR%20code/qrcode.39907201.png)

然後使用線上掃QR code的網站 : https://www.toolskk.com/qrcode-scanner

得到 `c3ludCB2ZiA6IGEwX29icWxfczBldHJnX2RlX3BicXI=` 的訊息

看起來是Base64加密，解密後得 `synt vf : a0_obql_s0etrg_de_pbqr=`

冒號後面感覺就是我們要的flag，直覺是凱薩加密，透過python寫一個凱薩解密
```python
def decrypt(key, message):
    message = message.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for letter in message:
        if letter in alpha: 
            letter_index = (alpha.find(letter) - key) % len(alpha)
            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

text = input('Encrypt text : ')
for shift in range(0,26):
    output = decrypt(shift,text)
    print(f'#{shift} : ',output)
```

結果輸出 : 
```
#0 :  a0_obql_s0etrg_de_pbqr
#1 :  z0_napk_r0dsqf_cd_oapq
#2 :  y0_mzoj_q0crpe_bc_nzop
#3 :  x0_lyni_p0bqod_ab_myno
#4 :  w0_kxmh_o0apnc_za_lxmn
#5 :  v0_jwlg_n0zomb_yz_kwlm
#6 :  u0_ivkf_m0ynla_xy_jvkl
#7 :  t0_huje_l0xmkz_wx_iujk
#8 :  s0_gtid_k0wljy_vw_htij
#9 :  r0_fshc_j0vkix_uv_gshi
#10 :  q0_ergb_i0ujhw_tu_frgh
#11 :  p0_dqfa_h0tigv_st_eqfg
#12 :  o0_cpez_g0shfu_rs_dpef
#13 :  n0_body_f0rget_qr_code
#14 :  m0_ancx_e0qfds_pq_bncd
#15 :  l0_zmbw_d0pecr_op_ambc
#16 :  k0_ylav_c0odbq_no_zlab
#17 :  j0_xkzu_b0ncap_mn_ykza
#18 :  i0_wjyt_a0mbzo_lm_xjyz
#19 :  h0_vixs_z0layn_kl_wixy
#20 :  g0_uhwr_y0kzxm_jk_vhwx
#21 :  f0_tgvq_x0jywl_ij_ugvw
#22 :  e0_sfup_w0ixvk_hi_tfuv
#23 :  d0_reto_v0hwuj_gh_setu
#24 :  c0_qdsn_u0gvti_fg_rdst
#25 :  b0_pcrm_t0fush_ef_qcrs
```

發現位移13就是flag~


Flag : `n0_body_f0rget_qr_code`
