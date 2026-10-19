import re,html,sys
s=open('site/index.html',encoding='utf-8').read()
body=re.sub(r'<style>.*?</style>','',s,flags=re.S)
txt=html.unescape(re.sub(r'<[^>]+>',' ',body))
# 입력란 안내 글자·대체 텍스트처럼 속성 안에 있는 글자도 화면에 나온다
txt+=html.unescape(' '.join(re.findall(r'(?:placeholder|alt|aria-label|title)="([^"]*)"',body)))
# 스크립트 안 문자열(문의 메시지 등)도 포함
chars=set(txt)|set(''.join(map(chr,range(0x20,0x7f))))|set('·—–…“”‘’→←−■①②③④⑤')
ks=set()
for hi in range(0xB0,0xC9):
    for lo in range(0xA1,0xFF):
        try: ks.add(bytes([hi,lo]).decode('euc-kr'))
        except: pass
open(sys.argv[1]+'/page.txt','w',encoding='utf-8').write(''.join(sorted(chars)))
open(sys.argv[1]+'/full.txt','w',encoding='utf-8').write(''.join(sorted(chars|ks)))
heads=re.findall(r'<(?:h1|h2|h3|b|dd|strong)[^>]*>(.*?)</(?:h1|h2|h3|b|dd|strong)>',body,flags=re.S)
h=set(html.unescape(re.sub(r'<[^>]+>','',''.join(heads))))|set(''.join(map(chr,range(0x20,0x7f))))|set('·~')
open(sys.argv[1]+'/head.txt','w',encoding='utf-8').write(''.join(sorted(h)))
print(len(chars),len(chars|ks),len(h))
