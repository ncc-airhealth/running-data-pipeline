# 2. 로컬 데이터셋 저장소 준비

Hugging Face Dataset Repository를 복제하거나 기존 로컬 저장소의 원격 상태를 확인해요.

## 완료 조건

- [ ] `origin`이 작업할 Hugging Face Dataset Repository를 가리킴
- [ ] 현재 브랜치와 추적 대상 원격 브랜치를 확인했거나, 빈 원격 저장소에서 사용할 기본 브랜치를 확인함
- [ ] 로컬 브랜치가 추적 대상 원격 브랜치보다 뒤처져 있지 않음

## 저장소 준비

로컬 저장소가 없으면 저장할 경로와 여유 공간을 확인한 뒤 복제하세요.

```bash
DATASET_NAME="<dataset-name>"
git clone "https://huggingface.co/datasets/${NCCA_HF_NAMESPACE}/${DATASET_NAME}"
cd "${DATASET_NAME}"
```

복제한 저장소나 기존 로컬 저장소의 루트에서 다음 명령어를 실행하세요.

```bash
git remote get-url origin
git branch --show-current
git ls-remote --heads origin
git fetch origin
git status --short --branch
git rev-list --left-right --count HEAD...@{upstream}
```

`@{upstream}`은 현재 브랜치가 추적하는 원격 브랜치를 뜻해요.
`git rev-list` 결과의 오른쪽 값이 `0`이면 원격에만 있는 커밋이 없어요.
원격 저장소가 비어 있어 추적 대상이 없다면 `git ls-remote --heads origin` 결과와 Hugging Face의 기본 브랜치를 확인하세요.

## 권장 저장소 구조

데이터셋 저장소는 다음 구조로 구성하는 것을 권장해요.

```text
<NCCA_HF_NAMESPACE>/<dataset-name>/
├── data/           # 데이터와 메타데이터 저장
├── scripts/        # 데이터 처리 코드와 의존성 관리
├── .gitattributes  # Xet/LFS로 추적할 파일 패턴
└── README.md       # 데이터 설명 문서
```

# AI 추가 지침

- 로컬 저장소의 예상 위치와 여유 공간을 확인하세요.
- 사용자의 명시적 승인을 받은 뒤 `git clone`을 실행하세요.
- `git rev-list` 결과의 오른쪽 값이 `0`이 아니면 이후 작업을 중단하고 사용자에게 보고하세요.
- 원격 URL이나 추적 대상 원격 브랜치가 예상과 다르면 변경하지 말고 사용자에게 확인하세요.
