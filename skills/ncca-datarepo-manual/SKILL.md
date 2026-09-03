---
name: ncca-datarepo-manual
description: NCCA 데이터 저장소를 새로 구축하거나 데이터, STAC 메타데이터, 저장소 설명 문서를 수정·검토·배포할 때 사용한다.
---

# NCCA 데이터 저장소 구축 매뉴얼

팀 내부의 데이터, 메타데이터, 처리과정을 체계적으로 보관하고 관리하기 위해 데이터 저장소를 구축해요.
누구나 저장소를 통해 데이터를 독립적으로 조회하고, 추가 및 갱신할 수 있도록 재현성과 문서화를 갖춘 저장소를 만드는 것이 목표예요.

## 준비사항

작업을 시작하기 전 다음 문서와 개발 환경을 확인해 주세요.

- [데이터 저장소 운영 및 구성 규칙](reference/knowledge/repo-rules.md)
- [STAC 메타데이터 규격](reference/knowledge/stac-spec.md)
- [데이터 설명 문서 작성 규칙](reference/knowledge/technical-writing.md)
- [NCCA 데이터 파이프라인 개발 환경 설정](../ncca-set-dev-env/SKILL.md): Python, uv, 스토리지 인증 설정

## 작업 순서

데이터 저장소를 새로 구축할 때는 1단계부터 순서대로 진행해요.
기존 저장소를 업데이트할 때는 변경이 필요한 가장 이른 단계부터 6단계까지 순서대로 진행해요.

1. [1. 원격 저장소 생성](reference/1-create-repo.md)
2. [2. 로컬 작업 공간 준비](reference/2-clone-repo.md)
3. [3. 데이터 수집·처리 파이프라인 구성](reference/3-etl.md)
4. [4. STAC 메타데이터 작성](reference/4-write-metadata.md)
5. [5. 저장소 설명 문서 작성](reference/5-write-dataset-card.md)
6. [6. 검토 및 배포](reference/6-publish.md)

> **AI 추가 지침**
>
> - [준비사항](#준비사항)의 문서들을 숙지하고 데이터 저장소 작업을 시작할 것
> - [작업 순서](#작업-순서)에 따라 사용자와 상호작용하며, 단계별 완료 조건을 검증하고 승인을 받아 진행할 것
> - 각 단계별 세부 제약 조건과 안전 수칙은 해당 단계 문서의 지침을 따를 것
