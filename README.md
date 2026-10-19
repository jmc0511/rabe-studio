# 라베 스튜디오 소개 사이트

정적 페이지 (`site/`). GitHub에 push 하면 Netlify 가 자동 배포 (`netlify.toml`: publish = site).

## 글꼴
`site/fonts/`는 페이지에 쓰인 글자만 남긴 파일이다. **문구를 바꾸면 `sh fonts-src/subset.sh`를 다시 실행**해야 새 글자가 제 글꼴로 나온다 (원본은 `fonts-src/`, fonttools·brotli 필요).
