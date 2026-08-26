# 6. 검토 및 배포

최종적으로 데이터를 배포합니다.

## 완료 조건

- [ ] 배포 대상 Hugging Face 저장소와 공개 범위를 확인했다.
- [ ] 로컬 `HEAD`가 추적 대상 원격 브랜치보다 뒤처져 있지 않다.
- [ ] Xet/LFS로 추적할 대용량·바이너리 데이터 파일들이 `.gitattributes`에 지정되어 있다.
- [ ] 작업 트리와 staged diff에 배포하면 안 되는 파일이나 정보가 없다.

## 방법

1. 변경사항을 검토하고 배포할 파일만 stage합니다.
2. stage된 변경사항을 commit합니다.
3. commit을 Hugging Face Dataset Repository에 push합니다.

# AI 추가 지침

- 사용자가 stage·commit을 마치면 commit 내용과 배포 대상을 검토한다.
