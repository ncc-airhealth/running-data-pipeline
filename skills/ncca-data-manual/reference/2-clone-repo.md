# 2. 로컬 데이터셋 저장소 준비

Hugging Face Dataset Repository를 로컬 경로로 복제하거나 기존 로컬 저장소의 원격 상태를 확인해요.

## 완료 조건

다음 조건을 모두 만족하면 로컬 데이터셋 저장소 준비가 끝나요.

- [ ] `origin`이 작업할 Hugging Face Dataset Repository를 가리킴
- [ ] 현재 브랜치와 `upstream` 상태를 확인함
- [ ] `upstream`이 있다면 로컬 브랜치가 원격 브랜치보다 뒤처져 있지 않음

## 저장소 준비

### 저장소 복제

로컬 저장소가 없으면 저장할 경로와 여유 공간을 확인한 뒤 복제하세요.

```bash
git clone "https://huggingface.co/datasets/<namespace>/<dataset-name>"
```

- `<namespace>`: Hugging Face 네임스페이스
- `<dataset-name>`: Dataset Repository의 이름

기존 로컬 저장소를 사용한다면 해당 저장소의 루트 경로로 이동하세요.

### 원격·브랜치 상태 확인

`git clone`은 원격 저장소를 `origin`이라는 이름으로 등록해요.
`origin`과 현재 브랜치의 원격 동기화 상태를 확인하세요.

```bash
git remote get-url origin
git fetch origin
git status --short --branch
```

출력된 URL이 작업할 저장소와 다르면 작업을 중단하세요.
`git status`에 `behind`가 표시되거나 브랜치 또는 `upstream`이 예상과 다르면 올바른 작업 대상인지 확인하세요.

## 권장 저장소 구조

데이터셋 저장소는 다음 구조로 구성하는 것을 권장해요.

```text
<namespace>/<dataset-name>/
├── data/           # 데이터와 메타데이터 저장
├── scripts/        # 데이터 처리 코드와 의존성 관리
├── .gitattributes  # Xet/LFS로 추적할 파일 패턴
└── README.md       # 데이터 설명 문서 (Dataset Card)
```

# AI 추가 지침

- 로컬 저장소의 예상 위치와 여유 공간을 확인하세요.
- 사용자의 명시적 승인을 받은 뒤 `git clone`을 실행하세요.
- `git status`에 `behind`가 표시되면 이후 작업을 중단하고 사용자에게 보고하세요.
- 원격 URL이나 추적 대상 원격 브랜치가 예상과 다르면 변경하지 말고 사용자에게 확인하세요.
