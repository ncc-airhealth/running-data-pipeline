---
name: ncca-data-manual
description: NCCA Hugging Face 데이터셋 저장소를 새로 구축하거나 데이터, STAC 메타데이터, Dataset Card를 수정·검토·배포할 때 사용한다.
---

# Hugging Face 데이터셋 구축·관리

NCCA 데이터 파이프라인 프로젝트는 데이터와 변경 이력을 버전별로 관리하기 위해 Hugging Face Hub의 Dataset Repository를 사용하고 있어요.
이 문서는 NCCA Hugging Face 데이터셋을 새로 구축하거나 기존 데이터셋을 업데이트하기 위한 지침이에요.

> [!NOTE] Hugging Face Hub의 Dataset Repository를 사용하는 이유
> - Dataset Repository는 [Git 저장소](https://huggingface.co/docs/hub/repositories)이므로 커밋으로 파일의 변경 이력을 관리할 수 있어요.
> - [Xet 프로토콜](https://huggingface.co/docs/hub/xet) 기반으로 대용량 데이터 파일을 효율적으로 저장할 수 있어요.

## 작업 전 준비

필요한 명령어나 계정 인증이 준비되지 않았다면 먼저 [NCCA 데이터 파이프라인 개발 환경 설정](../ncca-set-dev-env/SKILL.md)을 완료해 주세요.

## 작업 순서

데이터셋을 새로 구축할 때는 다음 순서대로 진행해요.
기존 데이터셋을 업데이트할 때는 변경이 필요한 가장 이른 단계부터 6단계까지 순서대로 진행해요.

1. [Hugging Face 데이터셋 저장소 생성](reference/1-create-repo.md)
2. [로컬 데이터셋 저장소 준비](reference/2-clone-repo.md)
3. [데이터 획득·처리](reference/3-etl.md)
4. [STAC 메타데이터 작성·개선](reference/4-write-metadata.md)
5. [Dataset Card 작성·개선](reference/5-write-dataset-card.md)
6. [데이터셋 검토·배포](reference/6-publish.md)

> [!NOTE]
> - 작업을 시작하는 단계보다 앞선 단계는 완료 조건을 이미 만족하면 생략하세요.
> - 작업을 시작한 단계부터 6단계까지는 각 단계의 문서를 확인하고 완료 조건을 검토하세요.

# AI 추가 지침

- 작업 범위와 기존 산출물을 먼저 확인하세요.
- `README.md`와 메타데이터만 수정할 때는 기존 로컬 데이터를 재사용하고 `scripts/process.py`를 다시 실행하지 마세요.
- 공식 출처의 의미를 유지하면서 짧고 자연스러운 한국어를 사용하세요.
- 뜻이 모호한 용어는 원문을 함께 표기하세요.
- GIS 배경지식이 있는 사람을 대상으로 설명하세요.
