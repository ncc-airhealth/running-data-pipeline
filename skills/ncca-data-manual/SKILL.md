---
name: ncca-data-manual
description: NCCA Hugging Face 데이터셋 저장소의 데이터, STAC 메타데이터, Dataset Card를 구축·관리·배포할 때 사용
---

# Hugging Face 데이터셋 관리 매뉴얼

NCCA Hugging Face 데이터셋을 구축·관리할 때 사용하는 매뉴얼입니다.

## 작업 전 준비

필요한 명령어나 계정 인증이 준비되지 않았다면 먼저 [NCCA 데이터 파이프라인 개발 환경 설정](../ncca-set-dev-env/SKILL.md)을 완료해 주세요.

## 작업 순서

데이터셋 전체를 구축할 때는 다음 순서로 작업해 주세요.
일부 산출물만 작업할 때는 해당 단계의 참고 문서만 읽고 다른 단계의 지침은 적용하지 않습니다.
각 단계의 완료 조건을 확인하고 완료된 단계는 생략합니다.

1. [저장소 생성](reference/1-create-repo.md)
2. [로컬 저장소 준비](reference/2-clone-repo.md)
3. [데이터 획득과 처리](reference/3-etl.md)
4. [메타데이터 작성·개선](reference/4-write-metadata.md)
5. [README 작성·개선](reference/5-write-dataset-card.md)
6. [검토 및 배포](reference/6-publish.md)

# AI 추가 지침

- 작업 범위와 기존 산출물을 먼저 확인하고, README와 메타데이터만 개선할 때는 기존 로컬 데이터 재사용
- 공식 출처의 의미를 유지하면서 짧고 자연스러운 한국어 사용, 뜻이 모호한 용어는 원문 병기
- GIS 배경지식이 있는 사람과의 소통을 가정
