# 2. 로컬 저장소 준비

데이터셋 저장소를 복제하거나 기존 로컬 저장소의 원격 동기화 상태를 확인합니다.

## 완료 조건

- [ ] `origin`이 현재 다루는 Hugging Face 데이터셋 저장소를 가리킨다.
- [ ] 현재 로컬 브랜치와 추적 대상 원격 브랜치를 확인했다.
- [ ] 로컬 브랜치가 추적 대상 원격 브랜치보다 뒤처져 있지 않다.

## 방법

로컬 저장소가 없으면 다음 명령어를 현재 OS·셸에 맞게 실행합니다.

```bash
DATASET_NAME="<dataset-name>"
git clone "https://huggingface.co/datasets/${NCCA_HF_NAMESPACE}/${DATASET_NAME}"
cd "${DATASET_NAME}"
```

로컬 저장소가 있으면 다음 명령어로 상태를 확인해 주세요.

```bash
git remote get-url origin
git branch --show-current
git fetch origin
git status --short --branch
git rev-list --left-right --count HEAD...@{upstream}
```

`@{upstream}`은 현재 로컬 브랜치의 추적 대상 원격 브랜치를 의미합니다.

## 권장 저장소 구조

데이터셋 저장소는 아래 구조로 구성하는 것을 권장합니다.

```text
<NCCA_HF_NAMESPACE>/<dataset-name>/
├── data/           # 데이터와 메타데이터 저장
├── scripts/        # 데이터 처리 코드와 의존성 관리
├── .gitattributes  # Xet/LFS로 추적할 파일 패턴
└── README.md       # 데이터 설명 문서
```

# AI 추가 지침

- 로컬 머신의 저장소 여유공간을 확인하고 `git clone` 명령어를 실행한다.
- 사용자(사람)의 명시적 승인 후, `git clone` 명령어를 실행한다.
- `git rev-list` 결과의 오른쪽 값이 `0`이 아니면 작업을 중단하고 사용자에게 보고한다.
- 원격 URL이나 추적 대상 원격 브랜치가 예상과 다르면 변경하지 않고 사용자에게 확인을 요청한다.
