---
name: ncca-data-manual
description: NCCA Hugging Face 데이터셋 저장소를 새로 구축하거나 데이터, STAC 메타데이터, Dataset Card를 수정·검토·배포할 때 사용한다.
---

# Hugging Face 데이터셋 구축·관리

NCCA Hugging Face 데이터셋을 새로 구축하거나 기존 데이터셋을 관리하기 위한 지침이에요.
NCCA 데이터 파이프라인 프로젝트는 데이터와 변경 이력을 버전별로 관리하기 위해 Hugging Face Hub의 Dataset Repository를 사용해요.

## 작업 전 준비

필요한 명령어나 계정 인증이 준비되지 않았다면 먼저 [NCCA 데이터 파이프라인 개발 환경 설정](../ncca-set-dev-env/SKILL.md)을 완료해 주세요.
다음으로 작업할 데이터셋 저장소, 작업 범위, 기존 산출물을 확인하세요.

## 작업 순서

데이터셋을 새로 구축할 때는 다음 순서대로 진행해요.

1. [Hugging Face 데이터셋 저장소 생성](reference/1-create-repo.md)
2. [로컬 데이터셋 저장소 준비](reference/2-clone-repo.md)
3. [데이터 획득·처리](reference/3-etl.md)
4. [STAC 메타데이터 작성·개선](reference/4-write-metadata.md)
5. [Dataset Card 작성·개선](reference/5-write-dataset-card.md)
6. [데이터셋 검토·배포](reference/6-publish.md)

> [!NOTE]
> - 각 단계의 완료 조건을 이미 만족하면 해당 단계를 생략하세요.
> - 기존 데이터셋의 일부만 수정할 때는 해당 단계의 문서만 확인하세요.
> - 수정 결과가 이후 단계의 산출물과 일치해야 한다면 영향을 받는 이후 단계도 다시 확인하세요.

# AI 추가 지침

- 작업 범위와 기존 산출물을 먼저 확인하세요.
- README와 메타데이터만 수정할 때는 기존 로컬 데이터와 검증 결과를 재사용하세요.
- 공식 출처의 의미를 유지하면서 짧고 자연스러운 한국어를 사용하세요.
- 뜻이 모호한 용어는 원문을 함께 표기하세요.
- GIS 배경지식이 있는 사람을 대상으로 설명하세요.
