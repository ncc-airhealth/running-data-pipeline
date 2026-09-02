# 6. 데이터셋 검토·배포

데이터, STAC 메타데이터, Dataset Card를 함께 검토하고 Hugging Face Dataset Repository에 배포해요.

## 완료 조건

- [ ] 배포 대상 Hugging Face 저장소와 공개 범위를 확인함
- [ ] 로컬 `HEAD`가 추적 대상 원격 브랜치보다 뒤처져 있지 않음
- [ ] Xet/LFS로 추적할 대용량·바이너리 데이터 파일이 `.gitattributes`에 지정됨
- [ ] 작업 트리와 스테이징된 변경 내용에 배포하면 안 되는 파일이나 정보가 없음
- [ ] 데이터, `data/collection.json`, `README.md`가 서로 일치하고 각 단계의 검증을 통과함
- [ ] 배포할 커밋이 Hugging Face의 대상 원격 브랜치에 반영됨
- [ ] 공개 범위를 `public`으로 변경한다면 공개 조건을 모두 충족함

## 방법

### 산출물 검토

1. [로컬 데이터셋 저장소 준비](2-clone-repo.md)의 명령어로 원격 동기화 상태를 다시 확인하세요.
2. 데이터 획득·처리, STAC 메타데이터, Dataset Card의 완료 조건을 다시 확인하세요.

### Xet/LFS 추적

Hugging Face Dataset Repository는 `.gitattributes`의 Git LFS 호환 규칙으로 지정한 파일의 실제 내용을 Xet에 저장해요.
[Hugging Face 저장소 시작 안내](https://huggingface.co/docs/hub/repositories-getting-started)에 따라 10 MB보다 큰 파일과 대용량 바이너리 파일을 Xet으로 추적하세요.

1. `.gitattributes`에 배포할 데이터 파일의 확장자 패턴이 있는지 확인하세요.
2. 패턴이 없다면 `git xet track`으로 해당 확장자만 정확하게 추가하세요.
   작은 텍스트나 메타데이터 파일까지 포함하는 포괄적인 패턴은 사용하지 마세요.
3. `.gitattributes`의 변경 내용과 각 확장자의 대표 파일에 적용된 `filter` 속성을 확인하세요.

```bash
git xet track "*.parquet"
git diff -- .gitattributes
git check-attr filter -- "data/<file>"
```

이미 정확한 패턴이 있다면 `git xet track`을 다시 실행하지 않아도 돼요.
`git check-attr` 결과가 `unspecified`이면 해당 파일은 Xet/LFS로 추적되지 않아요.

### 변경 사항 배포

1. 배포할 파일만 스테이징하세요.
2. 다음 명령어로 작업 트리와 스테이징된 변경 내용을 확인하세요.

   ```bash
   git status --short
   git diff --check
   git diff --cached --check
   git diff --cached --name-status
   git diff --cached
   ```
3. 검토한 변경 사항을 커밋하세요.
4. 원격 저장소와 공개 범위를 다시 확인하세요. 새로 만든 저장소는 `private`이어야 해요.
5. 사용자의 명시적 승인 후 커밋을 Hugging Face Dataset Repository에 푸시하세요.
6. Hugging Face에서 커밋, 파일, Dataset Card, 공개 범위를 확인하세요.

### 공개 범위 변경

새로 만든 저장소는 `private` 상태에서 산출물을 배포하고 검토하세요.
다음 조건을 모두 만족할 때만 공개 범위를 `public`으로 변경하세요.

- 데이터의 라이선스와 가공·재배포 조건을 확인함
- 관련 법률 검토를 완료함
- 팀이 데이터 공개를 결정함
- Hugging Face에서 배포한 산출물을 확인함

조건을 충족하면 Hugging Face 저장소 설정에서 공개 범위를 변경하고 결과를 확인하세요.
조건을 충족하지 않으면 `private`을 유지하세요.

> [!IMPORTANT] 스테이징 전 검토 항목
>
> 다음 항목은 스테이징하지 마세요.
> - 비밀번호, 액세스 토큰, API 키, 개인 키 등 외부에 공개하면 안 되는 정보
> - 임시 파일, 캐시
> - 원본 데이터의 이용 조건에 어긋나는 파일

# AI 추가 지침

- Git을 기본 배포 방법으로 사용하세요.
- 다른 업로드 방법이 필요하면 사용자와 먼저 협의하세요.
- `git add`, `git stage`, `git commit`, `git push`는 실행하지 말고 사용자가 직접 수행하도록 요청하세요.
- 공개 조건을 모두 충족했는지 확인한 뒤 사용자가 직접 공개 범위를 변경하도록 요청하세요.
- 배포 후 원격 커밋을 확인하기 전에는 완료로 판단하지 마세요.
