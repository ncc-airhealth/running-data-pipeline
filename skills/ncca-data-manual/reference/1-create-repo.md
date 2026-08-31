# 1. Hugging Face 데이터셋 저장소 생성

새로운 데이터셋을 추가할 때 Hugging Face Dataset Repository를 만들어요.

## 작업 전 준비

- `NCCA_HF_NAMESPACE` 환경 변수와 Hugging Face 인증 상태를 확인하세요.
- 데이터의 내용과 범위를 바탕으로 저장소 이름을 정하세요.
- 가공·재배포 조건을 확인하기 전에는 공개 저장소를 만들지 마세요.

## 완료 조건

다음 조건을 모두 만족하면 저장소 생성이 끝나요.

- [ ] 데이터셋 이름과 저장소 ID가 정해짐
- [ ] `<NCCA_HF_NAMESPACE>/<dataset-name>` Dataset Repository가 존재함
- [ ] 저장소 공개 범위가 데이터의 가공·재배포 조건과 일치함

## 규칙

- 기존 데이터로 새로운 산출물을 만들 때는 별도 저장소를 사용하세요.
- 데이터셋 이름은 [kebab-case](https://developer.mozilla.org/en-US/docs/Glossary/Kebab_case)로 작성하는 것을 권장해요.
- 가공·재배포 조건을 확인하기 전에는 `private` 저장소로 만드세요.

## 저장소 생성

웹이나 CLI 중 한 가지 방법을 선택하세요.

### 웹

1. [New Dataset](https://huggingface.co/new-dataset)에 접속하세요.
2. `Owner`를 `<NCCA_HF_NAMESPACE>`로 지정하세요.
3. `Dataset name`을 입력하세요.
4. `Private` 체크박스를 선택하세요.
5. `Create Dataset`을 선택하세요.

### CLI

```bash
DATASET_NAME="<dataset-name>"
hf repos create "${NCCA_HF_NAMESPACE}/${DATASET_NAME}" --repo-type dataset --private
```

# AI 추가 지침

- 데이터셋 이름의 최종 결정은 사용자에게 요청하세요.
- 저장소 ID와 공개 범위를 제시하고 사용자의 명시적 승인을 받은 뒤 저장소를 생성하세요.
- 근거 없이 기존 저장소의 공개 범위를 변경하지 마세요.
