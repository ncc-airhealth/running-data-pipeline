# 1. 원격 저장소 생성

팀의 데이터를 보관하고 버전별로 관리하기 위해 원격 데이터 저장소를 생성해요.

## 세부 절차

1. 데이터셋 이름과 네임스페이스를 확인하세요.
   - [데이터 저장소 운영 및 구성 규칙](./knowledge/repo-rules.md)에 따라 소문자와 하이픈(`-`)만 사용하는 kebab-case 이름을 정하세요.
   - 팀 환경 변수 `NCCA_HF_NAMESPACE`와 계정 인증 상태가 올바른지 확인하세요.
2. 비공개(`private`) 설정으로 원격 저장소를 생성하세요.
   - CLI 명령어 또는 웹 인터페이스 중 한 가지를 선택하세요.
   - **CLI 사용 시**:
     ```bash
     DATASET_NAME="<dataset-name>"
     hf repos create "${NCCA_HF_NAMESPACE}/${DATASET_NAME}" --repo-type dataset --private
     ```
   - **웹 사용 시**:
     Hugging Face Hub의 [New Dataset](https://huggingface.co/new-dataset) 페이지에서 Owner를 `${NCCA_HF_NAMESPACE}`로 지정하고, `Private`을 선택한 후 저장소를 생성하세요.

## 완료 조건

다음 조건을 모두 만족하면 원격 저장소 생성이 완료돼요.

- [ ] 데이터셋 이름이 kebab-case 규칙을 준수함
- [ ] 팀 네임스페이스 하위에 원격 데이터셋 저장소가 존재함 (`<NCCA_HF_NAMESPACE>/<dataset-name>`)
- [ ] 저장소 공개 범위가 비공개(`private`)로 설정됨

> **AI 추가 지침**
>
> - 데이터셋 이름 후보를 사용자에게 제안하고 최종 결정은 사용자에게 요청할 것
> - 저장소 ID와 `private` 공개 범위를 제시하고 사용자의 명시적 승인을 받은 뒤 저장소를 생성할 것
> - 이 단계에서는 공개 범위를 `public`으로 변경하지 말 것

---
다음 작업: [2. 로컬 작업 공간 준비](./2-clone-repo.md)
