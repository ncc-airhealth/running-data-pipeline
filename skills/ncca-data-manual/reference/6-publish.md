# 6. 데이터셋 검토·배포

데이터, STAC 메타데이터, Dataset Card를 함께 검토하고 Hugging Face Dataset Repository에 배포해요.

## 완료 조건

- [ ] 배포 대상 Hugging Face 저장소와 공개 범위를 확인함
- [ ] 로컬 `HEAD`가 추적 대상 원격 브랜치보다 뒤처져 있지 않음
- [ ] Xet/LFS로 추적할 대용량·바이너리 데이터 파일이 `.gitattributes`에 지정됨
- [ ] 작업 트리와 staged diff에 배포하면 안 되는 파일이나 정보가 없음
- [ ] 데이터, `data/collection.json`, README가 서로 일치하고 각 단계의 검증을 통과함
- [ ] 배포할 commit이 Hugging Face의 대상 원격 브랜치에 반영됨

## 방법

1. [로컬 데이터셋 저장소 준비](2-clone-repo.md)의 명령어로 원격 동기화 상태를 다시 확인하세요.
2. 데이터 획득·처리, STAC 메타데이터, Dataset Card의 완료 조건을 다시 확인하세요.
3. 사용자는 배포할 파일만 stage하세요.
4. 다음 명령어로 작업 트리와 stage된 변경 내용을 확인하세요.

   ```bash
   git status --short
   git diff --check
   git diff --cached --check
   git diff --cached --name-status
   git diff --cached
   ```

5. 비밀정보, 캐시, 임시 파일, 원본 이용 조건에 어긋나는 파일이 없는지 확인하세요.
6. 사용자는 검토한 변경사항을 commit하세요.
7. 원격 저장소와 공개 범위를 다시 확인하세요.
8. 사용자의 명시적 승인 후 commit을 Hugging Face Dataset Repository에 push하세요.
9. Hugging Face에서 commit, 파일, Dataset Card, 공개 범위를 확인하세요.

# AI 추가 지침

- Git을 기본 배포 방법으로 사용하세요.
- 다른 업로드 방법이 필요하면 사용자와 먼저 협의하세요.
- `git add`, `git stage`, `git commit`, `git push`는 실행하지 말고 사용자가 직접 수행하도록 요청하세요.
- 배포 후 원격 commit을 확인하기 전에는 완료로 판단하지 마세요.
