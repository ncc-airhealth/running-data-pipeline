# Running Data Pipeline

데이터 파이프라인 운영 정책을 관리하는 저장소입니다.

## 지리공간 데이터 파이프라인 프로젝트 소개

- 보건의료, 사회, 환경 등 다양한 분야의 연구에서 공간 데이터가 필요합니다.
- 하지만 공공기관이 제공하는 공간 데이터는 **분석에 바로 사용하기 어렵거나, 도메인 지식이 필요한 경우**가 많습니다.
- **공간지리정보 데이터 파이프라인**는 이런 문제를 해결하기 위해 공간 데이터를 수집·검토·처리하여 **분석 가능한 데이터**를 구축하는 프로젝트입니다.

## 프로젝트 참여 요건

이 프로젝트에 참여하려면 다음 개념과 도구를 이해하고 활용할 수 있어야 합니다.

| 대상 | 용도 |
| --- | --- |
| [SpatioTemporal Asset Catalog](https://stacspec.org/en) | 공간 데이터와 메타데이터를 표준화된 방식으로 관리 |
| [STAC Static Catalog](https://github.com/radiantearth/stac-best-practices/blob/main/best-practices-catalog-and-collection.md#static-catalogs) | 데이터/메타데이터 구축·배포 |
| [Git](https://git-scm.com/) | 코드/문서/데이터 파일의 변경 이력을 관리 |
| [GitHub](https://github.com/about) | Git 기반 코드 협업 |
| [Hugging Face Hub Datasets](https://huggingface.co/docs/hub/datasets) | Git 기반 데이터 협업 |
| [Python](https://www.python.org/) | 데이터 수집·검토·처리 코드 작성 |
| [Astral uv](https://docs.astral.sh/uv/) | Python 실행 환경과 의존성을 관리 |

## 시작하기

이 프로젝트의 참여자라면 [`ncca-data-manual`의 개발 환경 설정 지침](skills/ncca-data-manual/reference/0-set-dev-env.md)에 따라 개발 환경부터 설정합시다.

AI 에이전트에게 다음과 같이 요청해도 좋습니다.

```text
skills/ncca-data-manual/reference/0-set-dev-env.md의 지침에 따라 개발 환경을 설정해 줘.
```

## 관리 구조

본 프로젝트의 문서와 데이터는 GitHub와 Hugging Face Hub를 통해 관리하고 있습니다.

| 위치 | 관리 대상 |
| --- | --- |
| GitHub `ncc-airhealth/running-data-pipeline` | 운영 방법과 Agent Skills |
| GitHub `ncc-airhealth/geovars` | 지리변수 연산 Python 라이브러리 |
| Hugging Face `ncca-pipeline` | 데이터, 처리 코드, 메타데이터 관리 |
| Hugging Face `husgbb` | 데이터, 처리 코드, 메타데이터 시험 운영 |

Hugging Face 데이터셋은 현재 개인 계정(`husgbb`)에서 시험 운영하며, 팀 도입 시 `ncca-pipeline` Organization으로 이전할 예정입니다.

## 세부 매뉴얼 목록

세부 작업 매뉴얼은 [Agent Skills](https://agentskills.io/home) 형식으로 `skills/` 경로에 정리해 두었습니다.

| 이름 | 설명 |
| --- | --- |
| `ncca-skills-manual` | 작업 매뉴얼과 Agent Skill 작성 지침 |
| `ncca-data-manual` | Hugging Face Hub 데이터·메타데이터 처리 및 저장 매뉴얼 |
| `ncca-geovariable-manual` | 지리변수 라이브러리 관리 매뉴얼 |
| `ncca-modeling-manual` | 대기오염 관측값 예측 모델링 매뉴얼 |
