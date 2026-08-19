# Running Data Pipeline

데이터 파이프라인 운영 정책

## 공간지리정보 데이터 파이프라인 소개

- 보건의료, 사회, 환경 등 다양한 분야의 연구에서 공간 데이터가 필요합니다.
- 하지만 공공기관이 제공하는 공간 데이터는 **분석에 바로 사용하기 어렵거나**, **도메인 지식이 필요한** 경우가 많습니다.
- 이 프로젝트는 이런 문제를 해결하기 위해 공간 데이터를 수집·처리·적재하여 **분석 가능한 데이터**로 제공합니다.

## 알아야 할 개념들

파이프라인 프로젝트 운영에 필요한 기본 개념입니다.

- [SpatioTemporal Asset Catalog](https://stacspec.org/en)
- [STAC Static Catalog](https://github.com/radiantearth/stac-best-practices/blob/main/best-practices-catalog-and-collection.md#static-catalogs)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/about)
- [Hugging Face Hub Datasets](https://huggingface.co/docs/hub/datasets)
- [Python](https://www.python.org/)
- [Astral uv](https://docs.astral.sh/uv/)

## 시작하기

이 프로젝트의 참여자라면 [`ncca-set-dev-env`](.agents/skills/ncca-set-dev-env/SKILL.md)에 따라 개발 환경부터 설정합시다.

1. 환경 변수 설정
2. uv 설치
3. Git 설치
4. GitHub CLI 설치
5. Hugging Face CLI 설치

## 관리 구조

| 위치 | 관리 대상 |
| --- | --- |
| GitHub `ncc-airhealth/running-data-pipeline` | 운영 방법과 Agent Skills |
| GitHub `ncc-airhealth/geovars` | 지리변수 연산 Python 라이브러리 |
| Hugging Face `<namespace>/<dataset-id>` | 데이터, 처리 코드, 메타데이터 관리 |

*STAC Collection 하나를 Hugging Face Dataset Repository 하나로 관리합니다.

## 세부 매뉴얼 목록

세부 작업 메뉴얼은 [Agent Skills](https://agentskills.io/home) 형식으로 `.agents/skills/` 경로에 정리해 두었습니다.

| 이름 | 설명 |
| --- | --- |
| `ncca-set-dev-env` | 개발 환경 설정 매뉴얼 |
| `ncca-data-manual` | Hugging Face Hub 데이터·메타데이터 처리 및 저장 매뉴얼 |
| `ncca-geovariable-manual` | 지리변수 라이브러리 관리 매뉴얼 |
