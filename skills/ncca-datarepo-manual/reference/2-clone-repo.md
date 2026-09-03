# 2. 로컬 작업 공간 준비

원격 저장소를 로컬 컴퓨터로 내려받고, 데이터와 스크립트를 둘 폴더를 만들어요.

## 세부 절차

1. 저장소를 내려받으세요.
   - 저장소를 처음 내려받을 때는 작업할 위치에서 `git clone`을 실행하세요.
     ```bash
     git clone "https://huggingface.co/datasets/${NCCA_HF_NAMESPACE}/${DATASET_NAME}"
     cd "${DATASET_NAME}"
     ```
   - 이미 내려받은 저장소가 있다면 해당 폴더로 이동해 최신 상태인지 확인하세요.
     ```bash
     git remote get-url origin
     git fetch origin
     git status --short --branch
     ```

2. 필수 폴더를 만드세요.
   - [데이터 저장소 운영 및 구성 규칙](./knowledge/repo-rules.md)에 맞춰 `data/`와 `scripts/` 폴더를 만드세요.
     ```bash
     mkdir -p data scripts
     ```
   - 저장소 폴더 구조는 다음과 같이 구성해요.
     ```text
     <dataset-name>/
     ├── data/           # 최종 데이터 파일과 STAC 메타데이터
     ├── scripts/        # 데이터 수집·가공 스크립트
     ├── .gitattributes  # 대용량 파일 추적 설정
     └── README.md       # 데이터셋 안내 문서
     ```

## 완료 조건

다음 조건을 모두 만족하면 로컬 작업 공간 준비가 끝나요.

- [ ] 로컬에 저장소 폴더가 있고, `origin` 원격 주소가 올바름
- [ ] 현재 브랜치가 원격 브랜치보다 뒤처져 있지 않음 (`behind` 없음)
- [ ] `data/`, `scripts/` 폴더가 생성됨

> **AI 추가 지침**
>
> - 저장소를 내려받을 로컬 경로와 디스크 남은 용량을 확인하고, 사용자 승인을 받은 뒤 `git clone`을 실행할 것
> - `git status` 결과에 `behind`가 있거나 원격 저장소 주소가 예상과 다르면 작업을 멈추고 사용자에게 알릴 것

---
다음 작업: [3. 데이터 수집·처리 파이프라인 구성](./3-etl.md)
