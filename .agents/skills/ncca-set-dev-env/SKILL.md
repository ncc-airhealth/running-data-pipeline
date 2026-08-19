---
name: ncca-set-dev-env
description: ncca 데이터 파이프라인 개발 환경 설정 메뉴얼
---

# ncca 데이터 파이프라인 개발 환경 설정 메뉴얼

## 규칙

- 현재 상태를 확인하고 **누락된 항목**만 설정한다.
- 기존 Git 설정과 로그인 계정을 바꿔야 한다면 **인간**의 검토를 거쳐야 한다.

## 설정 순서

### 1. 환경 확인

운영체제와 셸, `NCCA_HF_NAMESPACE`, Git 사용자 정보, `git`, `uv`, `gh`, `hf`의 설치·인증 상태를 확인한다. Windows Subsystem for Linux는 Linux 환경으로 취급한다.

### 2. uv

[공식 문서](https://docs.astral.sh/uv/getting-started/installation/)에 따라 설치하고 `uv --version`으로 확인한다.

### 3. Git

[공식 문서](https://git-scm.com/downloads)에 따라 설치한다. `git --version`과 Git 사용자 이름·이메일을 확인하고 비어 있으면 사용자에게 값을 묻는다.

### 4. GitHub CLI

[설치 문서](https://github.com/cli/cli#installation)와 [인증 문서](https://cli.github.com/manual/gh_auth_login)에 따라 설정하고 `gh auth status`로 확인한다.

### 5. Hugging Face CLI

`hf`가 없으면 `uv tool install huggingface_hub`로 설치한다. [공식 문서](https://huggingface.co/docs/huggingface_hub/en/guides/cli)에 따라 Git credential을 포함해 로그인하고 `hf auth whoami`로 확인한다.

### 6. 환경변수

운영체제와 셸에 맞게 다음의 환경변수를 영구 설정한다. 
| 변수명 | 값 |
| --- | --- |
| NCCA_HF_NAMESPACE | husgbb |

### 7. 접근 확인

GitHub `ncc-airhealth/running-data-pipeline`과 Hugging Face `<NCCA_HF_NAMESPACE>`의 데이터셋 하나를 조회한다. 조회 결과로 쓰기 권한까지 검증했다고 판단하지 않는다.

## 완료 보고

운영체제와 셸, 도구 버전, 로그인 계정, namespace, 접근 결과와 남은 작업을 짧게 정리한다.
