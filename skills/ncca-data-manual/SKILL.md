---
name: ncca-data-manual
description: NCCA Hugging Face 데이터셋을 구축·관리할 때 사용
---

# Hugging Face 데이터셋 관리 매뉴얼

NCCA Hugging Face 데이터셋을 구축·관리할 때 사용하는 매뉴얼입니다.

## 작업 순서

다음 순서로 작업해 주세요. 각 단계의 완료 조건을 확인하고 완료된 단계는 생략합니다.

0. [개발 환경 설정](reference/0-set-dev-env.md)
1. [저장소 생성](reference/1-create-repo.md)
2. [로컬 저장소 준비](reference/2-clone-repo.md)
3. [데이터 획득과 처리](reference/3-etl.md)
4. [메타데이터 작성·개선](reference/4-write-metadata.md)
5. [README 작성·개선](reference/5-write-dataset-card.md)
6. [검토 및 배포](reference/6-publish.md)

## 저장소 구조

데이터셋 저장소는 아래 구조로 구성하는 것을 권장합니다.

```text
<NCCA_HF_NAMESPACE>/<dataset-name>/
├── data/           # 데이터와 메타데이터 저장
├── scripts/        # 데이터 처리 코드와 의존성 관리
├── .gitattributes  # Xet/LFS로 추적할 파일 패턴
└── README.md       # 데이터 설명 문서
```

## Python 스크립트 작성 및 실행 방법

다음의 규칙에 따라 Python 스크립트를 작성해 주세요.

- 주석과 docstring은 한국어로 작성
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)를 따름
- `if __name__ == "__main__":` 블록에서 `main()`을 호출
- [PEP 723](https://peps.python.org/pep-0723/) 스크립트 상단 의존성 메타데이터 작성

스크립트를 실행할 때 `uv`를 사용하여 의존성 잠금 파일(`process.py.lock`)을 생성하고 실행해 주세요. (재현성 확보 목적)

```bash
uv lock --script scripts/process.py
uv lock --check --script scripts/process.py
uv run --frozen --script scripts/process.py
```

# AI 추가 지침

- GIS 배경지식이 있는 사람과의 소통을 가정
- `git add`, `git stage`, `git commit`은 실행하지 않고 사용자(사람)가 직접 수행하도록 요청
- `git push`는 사용자(사람)의 명시적 승인 후 실행
