# 6. 검토 및 배포

최종적으로 데이터를 배포합니다.

## 완료 조건

- [ ] 배포 대상 Hugging Face 저장소와 공개 범위를 확인했다.
- [ ] 로컬 `HEAD`가 추적 대상 원격 브랜치보다 뒤처져 있지 않다.
- [ ] Xet/LFS로 추적할 대용량·바이너리 데이터 파일들이 `.gitattributes`에 지정되어 있다.
- [ ] 작업 트리와 staged diff에 배포하면 안 되는 파일이나 정보가 없다.

## 방법

1. 작업 범위와 파일의 용도를 기준으로 변경사항을 검토하고, 사용자가 배포할 파일만 stage합니다.
2. 다음 명령어로 stage된 파일과 변경 내용을 확인합니다.

   ```bash
   git status --short
   git diff --cached --name-status
   git diff --cached
   ```

3. 사용자가 stage된 변경사항을 commit합니다.
4. 사용자의 명시적 승인 후 commit을 Hugging Face Dataset Repository에 push합니다.

# AI 추가 지침

- Git을 기본으로 사용하며 다른 업로드 방식은 사용자와 협의
- `git add`, `git stage`, `git commit`, `git push`는 실행하지 않고 사용자(사람)가 직접 수행하도록 요청
