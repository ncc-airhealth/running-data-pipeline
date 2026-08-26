# 2. 로컬 저장소 복제

아래 명령어를 실행하여 데이터셋 저장소를 로컬 환경으로 복제(clone)합니다.

## 완료 조건

- [ ] 현재 다루는 데이터셋 저장소가 PC에 존재한다.

## 방법

다음의 명령어를 현재 OS/셸에 맞게 실행합니다.

```bash
DATASET_NAME="<dataset-name>"
git clone "https://huggingface.co/datasets/${NCCA_HF_NAMESPACE}/${DATASET_NAME}"
cd "${DATASET_NAME}"
```

# AI 추가 지침

- 로컬 머신의 저장소 여유공간을 확인하고 `git clone` 명령어를 실행한다.
- 사용자(사람)의 명시적 승인 후, `git clone` 명령어를 실행한다.
