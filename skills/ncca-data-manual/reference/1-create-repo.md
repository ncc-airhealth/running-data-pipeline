# 1. 저장소 생성

새로운 데이터셋을 추가하는 경우, Hugging Face Dataset Repository를 만들어야 합니다.

## 완료 조건

다음 조건을 모두 만족하면 이 단계를 완료하고 `SKILL.md`의 다음 미완료 단계로 넘어갑니다.

- [ ] 현재 다루는 데이터셋의 이름이 결정됨
- [ ] 현재 다루는 데이터셋이 Hugging Face에 존재

## 규칙

- 기존 데이터로 새 데이터셋을 만들 때는 별도 저장소 사용
- 데이터셋 이름은 [kebab-case](https://developer.mozilla.org/en-US/docs/Glossary/Kebab_case)에 따라 명명 (권장)
- 기본적으로 `private` 레포지토리로 설정 (가공 및 재배포 정책이 확인된 경우 `public`으로 전환)

## 저장소 생성 방법 1: 웹에서 저장소를 만드는 경우

다음 순서로 저장소를 생성해주세요.

1. [New Dataset](https://huggingface.co/new-dataset)에 접속
2. `Owner`를 `<NCCA_HF_NAMESPACE>`로 지정
3. `Dataset name` 입력
4. `Private` 체크박스 선택
5. `Create Dataset` 선택하여 저장소 생성

## 저장소 생성 방법 2: CLI에서 저장소를 만드는 경우

```bash
DATASET_NAME="<dataset-name>"
hf repos create "${NCCA_HF_NAMESPACE}/${DATASET_NAME}" --repo-type dataset --private
```

# AI 추가 지침

- 데이터셋 이름은 사용자(사람)가 결정한다.
- 사용자(사람)의 명시적 승인 후, 저장소를 생성한다.
