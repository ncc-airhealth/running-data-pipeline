---
name: ncca-set-dev-env
description: ncca 데이터 파이프라인 개발 환경 설정 메뉴얼
---

# 데이터 파이프라인 개발 환경 설정 메뉴얼

다음 순서에 따라 현재 상태를 확인하고 **누락된 항목**만 설정해주세요.

### 1. 환경 확인

현재 사용중인 PC의 사양과 OS를 파악해주세요

예시) Macbook M4 Pro (2024) / MacOS 15.x	Sequoia

### 2. uv 설치

Python 의존성을 관리하기 위해 `uv`를 설치합니다.

[공식 문서](https://docs.astral.sh/uv/getting-started/installation/)에 따라 설치하고, `uv --version`으로 검증해주세요.

### 3. Git, Git LFS, Git Xet

문서·코드·데이터의 버전 관리와 대용량 데이터 전송을 위해 Git, Git LFS, Git Xet을 설치합니다. 다음의 공식 문서를 참고해주세요.

a. [Git](https://git-scm.com/downloads) 설치
b. [Git LFS](https://git-lfs.com/) 설치
c. [Git Xet](https://huggingface.co/docs/hub/xet/using-xet-storage) 설치
d. 다음 명령어로 설정과 설치 결과를 검증해주세요.

```bash
git --version
git lfs version
git xet --version
```

### 4. GitHub CLI

문서·코드의 버전 관리를 위해 `gh`를 설치합니다. 다음의 공식 문서를 참고해주세요.

a. [설치 문서](https://github.com/cli/cli#installation)에 따라 설치
b. [인증 문서](https://cli.github.com/manual/gh_auth_login)에 따라 설정
c. `gh auth status`로 검증

### 5. Hugging Face CLI

데이터의 버전 관리를 위해 `hf`를 설치합니다.

a. [공식 문서](https://huggingface.co/docs/huggingface_hub/en/guides/cli)에 따라 설치 및 로그인
b. `hf auth whoami`로 검증

### 6. 환경변수

운영체제와 셸에 맞게 다음의 환경변수를 영구 설정해주세요.
| 변수명 | 값 |
| --- | --- |
| NCCA_HF_NAMESPACE | husgbb |

(데이터 안정화 이후, ncca-pipeline으로 이전 예정입니다.)

> [!IMPORTANT]
> Hugging Face 계정에 `<NCCA_HF_NAMESPACE>`의 데이터셋을 생성·수정할 권한이 있는지 확인해주세요.

### 7. Agent Skills 설치

파이프라인 작업에는 [Claude Code](https://claude.com/ko/product/claude-code), [Codex](https://openai.com/ko-KR/index/introducing-codex/) 등 코딩 에이전트 툴을 사용하는 것을 권장드립니다.

다음의 스킬을 현재 사용하는 툴에 맞게 설치해주세요.
(에이전트에게 설치를 요청하세요)

- `skills/ncca-data-manual`
- `skills/ncca-geovariable-manual`

# 에이전트를 위한 추가 지침

- 각 단계를 시작하기 전에 현재 상태를 확인하고 이미 완료된 항목은 건너뜁니다.
- 기존 Git 설정, 로그인 계정, 셸 설정을 변경하려면 먼저 사람의 확인을 받습니다.
- 로그인과 인증 정보 입력이 필요하면 사람에게 직접 진행하도록 요청합니다. 인증 정보를 대신 입력하거나 출력하지 않습니다.
- 설치 방법은 운영체제와 셸에 맞게 선택하고 본문에 제시된 명령어로 결과를 검증합니다.
- `gh auth status`와 `hf auth whoami` 결과만으로 저장소나 namespace의 쓰기 권한까지 확인했다고 판단하지 않습니다.
- Agent Skills는 현재 사용하는 코딩 에이전트에 필요한 두 스킬만 설치하고 설치 위치를 확인합니다.
- 작업을 마치면 설치한 도구의 버전, 로그인 계정, 환경변수, 설치한 스킬, 남은 작업을 정리해 보고합니다.
