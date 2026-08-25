---
name: ncca-data-manual
description: NCCA Hugging Face 데이터셋 저장소를 생성·복제하고, 데이터를 처리하거나 STAC 메타데이터와 Dataset Card를 작성·검토할 때 사용하는 작업 매뉴얼
---

# Hugging Face 데이터셋 관리 매뉴얼

데이터 파이프라인 프로젝트에서는 데이터를 [Hugging Face](https://huggingface.co/)의 [데이터셋 저장소](https://huggingface.co/datasets)에 저장하고 관리합니다.

데이터셋 저장소는 아래 구조로 구성하는 것을 권장합니다. (static stac catalog)

```text
<NCCA_HF_NAMESPACE>/<dataset-name>/
├── assets/                           # 공통 데이터
│   └── <asset-name>.<extension>
├── items/
│   └── <item-id>/                    # 시공간 단위별 STAC Item
│       ├── <item-id>.json            # STAC Item 메타데이터
│       └── <asset-name>.<extension>
├── .gitattributes                    # Xet/LFS로 추적할 파일 패턴
├── collection.json                   # STAC Collection 메타데이터
├── process.py                        # 데이터 처리 스크립트
├── process.py.lock                   # 데이터 처리 스크립트의 의존성 잠금 파일
└── README.md                         # Dataset Card
```

[개발 환경 설정 매뉴얼](../ncca-set-dev-env/SKILL.md)에 따라 개발 환경 세팅 후, 아래 순서로 작업해주세요. (이미 끝난 단계는 건너뜀)

1. [저장소 생성](#1-저장소-생성)
2. [로컬 저장소 복제](#2-로컬-저장소-복제)
3. [데이터 획득과 처리](#3-데이터-획득과-처리)
4. [STAC 메타데이터 작성·개선](#4-stac-메타데이터-작성개선)
5. [Dataset Card 작성·개선](#5-dataset-card-작성개선)
6. [검토와 배포](#6-검토와-배포)

## 1. 저장소 생성

> [!IMPORTANT]
> - 기존 데이터로 새 데이터셋을 만들 때는 별도 저장소 사용
> - 저장소 하나에는 STAC Collection 하나만 구성
> - 데이터셋 이름은 [kebab-case](https://developer.mozilla.org/en-US/docs/Glossary/Kebab_case)를 강하게 권장됨  
> - 데이터 가공 및 재배포 정책이 확인된 경우만 `public` 저장소 지정 (이외의 모든 경우는 `private`으로 지정)  

> ### 웹에서 저장소를 만드는 경우
> 아래 순서로 진행합니다. ([공식 문서](https://huggingface.co/docs/hub/repositories-getting-started) 참고)
> 1. [New Dataset](https://huggingface.co/new-dataset)에 접속
> 2. `Owner`를 `<NCCA_HF_NAMESPACE>`로 지정
> 3. `Dataset name` 입력
> 4. `Private` 체크박스 선택
> 5. `Create Dataset` 선택하여 저장소 생성

> ### CLI에서 저장소를 만드는 경우
> `DATASET_NAME`에 데이터셋 이름을 지정한 다음 저장소를 생성합니다.
> 
> ```bash
> DATASET_NAME="dataset-name"
> hf repos create "${NCCA_HF_NAMESPACE}/${DATASET_NAME}" --repo-type dataset --private
> ```

## 2. 로컬 저장소 복제

아래 명령어로 저장소를 복제하고 해당 디렉터리로 이동합니다.

```bash
DATASET_NAME="dataset-name"
git clone "https://huggingface.co/datasets/${NCCA_HF_NAMESPACE}/${DATASET_NAME}"
cd "${DATASET_NAME}"
```

## 3. 데이터 획득과 처리

- 데이터를 수동으로 수집·처리했다면 다른 사람이 작업을 재현할 수 있도록 데이터 출처와 처리 과정을 `README.md`에 기록해주세요.
- 데이터를 코드로 수집·처리한다면 `process.py`를 작성하고 실행합니다.
- `process.py`를 작성하거나 실행할 때는 [데이터 처리 지침](reference/process-best-practice.md)을 참고합니다.

## 4. STAC 메타데이터 작성·개선

[STAC Static Catalog 지침](reference/stac-static-catalog-best-practice.md)을 참고하여 STAC 메타데이터를 작성하거나 개선해주세요.

## 5. Dataset Card 작성·개선

[Dataset Card 지침](reference/readme-best-practice.md)을 참고하여 `README.md`에 Dataset Card를 작성 또는 개선해주세요.

## 6. 검토와 배포

a. `process.py`를 실행했다면 스크립트가 오류 없이 끝나고 필요한 데이터 파일이 생성되는지 확인
b. 실제 데이터 파일, Dataset Card, STAC Collection과 Item의 내용 및 경로가 모두 일치하는지 확인
c. Xet/LFS로 추적할 대용량·바이너리 데이터 파일의 패턴을 `.gitattributes`에 지정
d. 추가·수정·삭제된 파일과 검증 결과를 검토 (AI 에이전트 위임 금지)
e. 검토가 끝나면 사람이 커밋 메시지를 정하고 `git add`, `git commit`, `git push`를 수행

# AI 추가 지침

- 작업 전 기존 저장소 상태를 조사하고 누락된 단계만 수행
- 원격 저장소 생성 전 `namespace`, `dataset name`, `private 여부`를 검토하고 불분명한 값은 사용자에게 확인 요청
- 인증에는 로컬 인증 저장소를 사용하고 토큰은 문서·코드·채팅·로그에 남기거나 출력하지 않음
- 파일 작성·수정·검증과 `git status`, `git diff` 같은 읽기 전용 Git 명령만 수행
- `git add`, `git commit`, `git push`는 사람이 수행하도록 변경 사항을 정리하여 인계
- STAC의 모든 Link와 Asset 경로가 실제 파일을 가리키고 Dataset Card의 설명이 데이터 및 STAC 메타데이터와 일치하는지 검증
- 배포 전 추가·수정·삭제된 파일, 수행한 검증, 검증하지 못한 항목과 그 이유를 사용자에게 보고하고 검토 요청
