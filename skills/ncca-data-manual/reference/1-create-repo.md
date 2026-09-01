# 1. Hugging Face 데이터셋 저장소 생성

새로운 데이터셋을 추가할 때 Hugging Face Dataset Repository를 생성해야 해요.

## 완료 조건

다음 조건을 모두 만족하면 저장소 생성이 끝나요.

- [ ] 데이터셋 이름과 저장소 ID가 정해짐
- [ ] `<NCCA_HF_NAMESPACE>/<dataset-name>` Dataset Repository가 존재함
- [ ] 저장소 공개 범위가 `private`임

## 작업 전 준비

- `NCCA_HF_NAMESPACE` 환경 변수와 Hugging Face 인증 상태를 확인하세요.
- 데이터의 내용과 범위를 바탕으로 저장소 이름을 정하세요. ([kebab-case](https://developer.mozilla.org/en-US/docs/Glossary/Kebab_case) 권장)
- 공개 범위는 `private`으로 설정하세요.

> [!IMPORTANT] 데이터셋 내부 처리 의존성 금지
> - 기존 데이터셋을 가공해 새로운 산출물을 만들 때는 별도 저장소를 사용하세요.
> - 같은 저장소 안의 데이터를 입력으로 사용해 다른 데이터를 생성하는 `내부 처리 의존성`은 금지해요.

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
- 저장소 ID와 `private` 공개 범위를 제시하고 사용자의 명시적 승인을 받은 뒤 저장소를 생성하세요.
- 이 단계에서는 공개 범위를 `public`으로 변경하지 마세요.
